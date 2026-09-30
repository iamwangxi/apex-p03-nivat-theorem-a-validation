**English** | [简体中文](README.zh-CN.md)

# Validation of Theorem A for star configurations

This companion archive validates the full Theorem A chain in §§0–7 of the convex Nivat paper, under its stated star-configuration hypotheses. New written arguments close the upstream interfaces and connect them to the reused constructive algebraic module. The result is $P_\theta(S)\ge |S|+1$ for every nonempty finite lattice-convex window, including points and segments. Section 8, Appendix D, the reduction from general configurations, and stronger window bounds are outside this submission.

Target: Apex Intelligence, *The Convex Nivat Conjecture: A Complexity Lower Bound for Star Configurations, and a Reduction from Low Convex Complexity to Star Configurations*. [Official PDF](https://math.apexin.net/papers/convex-nivat.pdf), published 2026-09-12; 891,962 bytes; SHA-256 `7fd67831155f4226c010fd6af32de558b76643771e6be12dea4eebafa21745a8`. The PDF is not bundled.

Companion archive: [GitHub v1.1](https://github.com/iamwangxi/apex-p03-nivat-theorem-a-validation/tree/v1.1); submission text version `v1.2`. Claude (Opus 5.5) independently re-derived the five load-bearing upstream interfaces from the paper and found no error, but did not line-check this manuscript.

v1.1 only corrects the review-status sentences in the companion files; mathematical content and certificates are unchanged, and v1.0 is preserved.

## Read and reproduce

- [Submission](proof/submission.md) / [Chinese translation](proof/submission.zh-CN.md)
- [Complete upstream proof and downstream connection](proof/upstream-proof.md) / [Chinese translation](proof/upstream-proof.zh-CN.md)
- [Reused constructive module proof](proof/expanded-proof.md) / [Chinese translation](proof/expanded-proof.zh-CN.md)
- [Appendix C statement audit](proof/appendix-c-audit.md) / [Chinese translation](proof/appendix-c-audit.zh-CN.md)
- [Reproduction](REPRODUCE.md) / [Chinese translation](REPRODUCE.zh-CN.md)
- [Packaging and provenance](PACKAGING.md) / [Chinese translation](PACKAGING.zh-CN.md)
- [Global configuration coverage](certificates/global-configurations.md) / [Chinese translation](certificates/global-configurations.zh-CN.md)

Run from the package root, without third-party dependencies:

```sh
shasum -a 256 -c MANIFEST.sha256
python3 -B code/verify_all.py
```

## New arguments and reused evidence

The new upstream proof covers common periods, finite support and Case A, a single spectrum-preserving encoding, divisibility and the affine dimension budget, the global periodic background using actual sectors only, and existence of a genuine nonzero quadratic witness. It then connects the same witness to the downstream quotient and lattice arguments, with the quantifier order $\exists d\,\exists q\,\forall S$. The Appendix C audit identifies a single-factor/full-product confusion in the stated example; it neither invalidates Theorem A nor settles the proposed all-tail generalization.

The symbolic gate, 12 frozen algebraic inputs and two global examples are reused without certificate regeneration or new sample coverage. The boundary collection checks 163 basic identities, 46 inverses and 128 spanning vectors. The complete acceptance run has 15 jobs and 368 rejected negative controls, including 348 from the boundary collection. The examples have 347 and 401 complete global patterns, witness supports of 12 and 32 points, and rational ranks $46\to55$. The algebraic inputs are not asserted to be star configurations.

The checkers use standard-library integer and rational arithmetic. Generators use pinned SymPy only for optional regeneration. Finite certificates do not replace the written general proof. There is no proof-kernel certification or human expert endorsement.

OpenAI Codex and GPT contexts prepared and reviewed the upstream mathematics, package and translations. The original mathematical checker was authored in a separate GPT context that did not read the generator. Claude Opus 5.5 previously checked the reused module's five load-bearing points and reran its acceptance entries; that historical review does not certify the new full chain. Claude (Opus 5.5) independently re-derived the five load-bearing upstream interfaces from the paper and found no error, but did not line-check this manuscript. Fresh GPT review of the final submission and bilingual documents is recorded separately.

English documents are authoritative. Code is MIT-licensed; original prose and certificates are offered under CC BY 4.0 to the extent applicable rights exist. See [LICENSE](LICENSE).
