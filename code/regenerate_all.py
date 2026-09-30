#!/usr/bin/env python3
"""Optional regeneration into a fresh directory, separate from shipped evidence.

Requires the pinned generation dependencies. Acceptance does not invoke this
program. Each algebraic input runs in a separate process; no case is replaced.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

CODE = Path(__file__).resolve().parent
FROZEN_SHA256 = "f988d2c2f79c155535cebe9afafb0bd513cea0d8d69f4456ddcfbc89e01dc2f6"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path,
                        help="Fresh output directory; must not already exist")
    parser.add_argument("--timeout", type=float, default=300.0,
                        help="Per-generator timeout in seconds")
    args = parser.parse_args()
    if args.timeout <= 0:
        raise ValueError("Timeout must be positive")
    output = args.output.resolve()
    shipped = (CODE.parent / "certificates").resolve()
    if output == shipped or shipped in output.parents:
        raise ValueError("Choose a location outside shipped certificates")
    raw = (shipped / "boundary/frozen-inputs.json").read_bytes()
    if hashlib.sha256(raw).hexdigest() != FROZEN_SHA256:
        raise ValueError("Frozen inputs changed")
    cases = json.loads(raw)["cases"]
    if len(cases) != 12:
        raise ValueError("All twelve frozen cases are required")
    output.mkdir(parents=True, exist_ok=False)
    boundary = output / "boundary"
    boundary.mkdir()
    (boundary / "frozen-inputs.json").write_bytes(raw)
    jobs = []
    for case in cases:
        name = case["id"]
        jobs.append((name, "generate_boundary.py",
                     ["--input-list", str(boundary / "frozen-inputs.json"), "--case", name,
                      "--output", str(boundary / (name + ".json")),
                      "--stats", str(boundary / (name + ".generation.json"))]))
    jobs += [("three_line_baseline", "generate_baseline.py",
              ["--output", str(output / "baseline")]),
             ("periodic_background", "generate_periodic_background.py",
              ["--output", str(output / "periodic-background")])]
    records = []
    for name, filename, arguments in jobs:
        proc = subprocess.run([sys.executable, "-B", str(CODE / filename), *arguments],
                              timeout=args.timeout, check=False)
        records.append({"id": name, "exit_code": proc.returncode})
        if proc.returncode != 0:
            print(json.dumps({"generated": False, "jobs": records}), flush=True)
            return 1
    shutil.copyfile(boundary / "B09.json", output / "symbolic-gate.json")
    proc = subprocess.run([sys.executable, "-I", "-B", str(CODE / "verify_all.py"),
                           "--results", str(output)], check=False)
    print(json.dumps({"generated": True, "acceptance_exit_code": proc.returncode,
                      "jobs": records}), flush=True)
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main())
