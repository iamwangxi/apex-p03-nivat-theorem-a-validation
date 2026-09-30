**English** | [简体中文](REPRODUCE.zh-CN.md)

# Reproduce the reused certificates for Theorem A

These are the reused algebraic and global-configuration checks. They do not execute or certify the new general upstream proof in `proof/upstream-proof.md`. Claude review of the full Theorem A chain remains **pending**. No new configuration samples are claimed.

Run the commands from the package root using Python 3.9 or later. Do not use `-O`: assertions participate in validation. Verification needs only the Python standard library and no network.

## Integrity and acceptance

```sh
shasum -a 256 -c MANIFEST.sha256
python3 -B code/verify_all.py
```

On systems with GNU coreutils, `sha256sum -c MANIFEST.sha256` is equivalent. Manifest success establishes byte integrity only. The acceptance command must exit zero and report success for all 15 jobs: the symbolic gate, 12 boundary inputs and two global examples. Expected boundary totals are 163 basic unit identities, 46 local inverse identities and 128 basis/spanning vectors. Expected negative-control rejections are 348 from the boundary inputs and 20 from the remaining checks, totaling 368.

The frozen input list is `certificates/boundary/frozen-inputs.json`, SHA-256 `f988d2c2f79c155535cebe9afafb0bd513cea0d8d69f4456ddcfbc89e01dc2f6`. The checker reconstructs target expressions from these inputs. It rejects incomplete identity/component sets and wrong denominators, representatives, basis data or supports. It neither imports nor invokes a generator.

The global examples must recover 347 and 401 patterns, respectively, and rank $46\to55$ in each case. Read `certificates/global-configurations.md` for why a finite enumeration covers every translation on the infinite lattice; a bounded sample alone would not suffice.

## Optional regeneration

Generation is separate from acceptance. It uses the versions in `code/requirements.txt`: `sympy==1.14.0` and `mpmath==1.3.0`. If these packages are already available, regeneration can remain offline; dependency installation otherwise requires a separately authorized network step. No generator or dependency installation is needed to check the shipped certificates.

Use a fresh destination and follow the generator help; preserve failed attempts rather than replacing frozen inputs:

```sh
python3 -B code/regenerate_all.py --help
python3 -B code/regenerate_all.py --output reproduced
python3 -B code/verify_all.py --results reproduced
```

A generator result is not accepted until the independent checker passes. Regeneration timings and machine-specific paths are not part of certificate validity. The original boundary generation took 121.202406 seconds; this is a historical observation, not a runtime bound. The 12 shipped boundary certificates total 1,583,170 bytes. `B09.json` matches `certificates/symbolic-gate.json` byte for byte.
