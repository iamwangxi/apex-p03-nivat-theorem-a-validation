#!/usr/bin/env python3
"""Read-only, standard-library acceptance of all shipped Nivat certificates.

No generator, third-party package, network service, or historical workspace is
needed. Results are printed as one JSON object; this program writes no files.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

CODE = Path(__file__).resolve().parent
FROZEN_SHA256 = "f988d2c2f79c155535cebe9afafb0bd513cea0d8d69f4456ddcfbc89e01dc2f6"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=CODE.parent / "certificates",
                        help="Certificate collection; defaults to the shipped collection")
    args = parser.parse_args()
    results = args.results.resolve()
    started = time.monotonic()
    manifest = results / "boundary/frozen-inputs.json"
    require(digest(manifest) == FROZEN_SHA256, "Frozen input bytes changed")
    cases = json.loads(manifest.read_bytes())["cases"]
    require(len(cases) == 12 and {c["id"] for c in cases} ==
            {f"B{i:02d}" for i in range(1, 13)}, "All twelve frozen inputs are required")
    require((results / "symbolic-gate.json").read_bytes() ==
            (results / "boundary/B09.json").read_bytes(),
            "The symbolic gate and its boundary regression certificate differ")
    jobs = [
        ("symbolic_gate", "check_symbolic_gate.py",
         [str(results / "symbolic-gate.json"), "--self-test"], None),
        ("three_line_baseline", "check_baseline.py",
         ["--results", str(results / "baseline")], None),
        ("periodic_background", "check_periodic_background.py",
         ["--results", str(results / "periodic-background")], None),
    ]
    for case in cases:
        jobs.append((case["id"], "check_boundary.py",
                     [str(results / "boundary" / (case["id"] + ".json")),
                      "--manifest", str(manifest), "--case", case["id"], "--self-test"], case))
    records = []
    for name, filename, arguments, case in jobs:
        script = CODE / filename
        t0 = time.monotonic()
        # Isolated mode excludes user site packages and ignores Python env hooks.
        proc = subprocess.run([sys.executable, "-I", "-B", str(script), *arguments],
                              cwd=CODE.parent, capture_output=True, text=True, check=False)
        summary, error = {}, None
        try:
            require(proc.returncode == 0, "Checker exited unsuccessfully")
            require(not proc.stderr, "Checker stderr is not empty")
            result = json.loads(proc.stdout)
            controls = result.get("negative_controls", [])
            if name in ("three_line_baseline", "periodic_background"):
                require(result.get("all_checks_passed") is True, "Global configuration failed")
                require(result.get("generator_imported") is False and
                        result.get("generator_read") is False, "Generator separation failed")
                require(result.get("external_packages") == [], "Unexpected external package")
                require(len(controls) == 6 and all(c.get("rejected") is True for c in controls),
                        "Global-configuration negative controls failed")
                ranks = result["rank_certificates"]
                require([ranks[k]["exact_rational_rank"] for k in ("linear", "extended")] ==
                        [46, 55], "Unexpected exact rational ranks")
                require(all(ranks[k]["minor_exact_determinant"] == -1 and
                            ranks[k]["kernel_basis_count"] == 9 for k in ("linear", "extended")),
                        "Unexpected exact rank certificate")
                if name == "three_line_baseline":
                    require(result["coverage"]["pattern_count"] == 347 and
                            result["coverage"]["all_coverage_events"] == 483 and
                            result["witness"]["J_support_size"] == 12,
                            "Baseline coverage or full support mismatch")
                    patterns, events, support = 347, 483, 12
                else:
                    require(result["coverage"]["global_patterns"] == 401 and
                            result["coverage"]["all_events"] == 541 and
                            result["witness"]["entire_J_support_size"] == 32 and
                            result["witness"]["A_eta_equals_4_globally"] is True and
                            result["witness"]["D2_eta_equals_0_globally"] is True,
                            "Periodic-background global identity or coverage mismatch")
                    patterns, events, support = 401, 541, 32
                summary = {"negative_controls": 6, "global_patterns": patterns,
                           "coverage_events": events, "entire_J_support_size": support,
                           "rational_ranks": [46, 55], "minor_determinants": [-1, -1],
                           "right_kernel_dimensions": [9, 9]}
            else:
                require(result.get("status") == "PASS", "Algebraic certificate failed")
                count = 29 if case else 8
                require(len(controls) == count and
                        all(c.get("status") == "REJECTED_AS_REQUIRED" for c in controls),
                        "Algebraic negative controls failed")
                m = len(case["vectors"]) if case else 3
                dimension = case["expected_dimension"] if case else 14
                expected = {"unit_identity_count": m + m * m * (m - 1),
                            "E_inverse_identity_count": m * (m - 1),
                            "component_count": m * (m - 1),
                            "spanning_vector_count": dimension,
                            "dimension_from_structure": dimension}
                for key, value in expected.items():
                    require(result.get(key) == value, "Unexpected " + key)
                if case:
                    require(result["manifest_sha256"] == FROZEN_SHA256 and
                            result["manifest_case_count"] == 12,
                            "Checker did not bind the frozen input collection")
                    require(result["all_directions_primitive"] == (name != "B06"),
                            "Primitive-direction scope mismatch")
                summary = dict(expected, negative_controls=count)
                if "support_point_checks" in result:
                    summary["support_point_checks"] = result["support_point_checks"]
        except (ValueError, KeyError, TypeError) as exc:
            error = str(exc)
        records.append({"id": name, "passed": error is None,
                        "checker": "code/" + filename, "checker_sha256": digest(script),
                        "exit_code": proc.returncode, "stderr_empty": not proc.stderr,
                        "elapsed_seconds": round(time.monotonic() - t0, 6),
                        "error": error, **summary})
    boundary = [r for r in records if r["id"].startswith("B")]
    algebraic = [r for r in records if r["id"] == "symbolic_gate" or r in boundary]
    report = {
        "passed": all(r["passed"] for r in records), "python": platform.python_version(),
        "third_party_packages": [], "generator_invoked": False, "network_used": False,
        "writes_files": False, "frozen_input_sha256": digest(manifest),
        "runner_sha256": digest(Path(__file__)), "job_count": len(records),
        "boundary_case_count": len(cases),
        "negative_controls": sum(r.get("negative_controls", 0) for r in records),
        "boundary_unit_identities": sum(r.get("unit_identity_count", 0) for r in boundary),
        "boundary_inverse_identities": sum(r.get("E_inverse_identity_count", 0) for r in boundary),
        "boundary_spanning_vectors": sum(r.get("spanning_vector_count", 0) for r in boundary),
        "boundary_support_point_checks": sum(r.get("support_point_checks", 0) for r in boundary),
        "algebraic_unit_identities_including_gate": sum(r.get("unit_identity_count", 0) for r in algebraic),
        "algebraic_inverse_identities_including_gate": sum(r.get("E_inverse_identity_count", 0) for r in algebraic),
        "algebraic_spanning_vectors_including_gate": sum(r.get("spanning_vector_count", 0) for r in algebraic),
        "elapsed_seconds": round(time.monotonic() - started, 6), "jobs": records,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
