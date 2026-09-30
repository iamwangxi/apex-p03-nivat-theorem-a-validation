**English** | [简体中文](PACKAGING.zh-CN.md)

# Packaging, provenance and review boundaries

Companion archive [GitHub v1.0](https://github.com/iamwangxi/apex-p03-nivat-theorem-a-validation/tree/v1.0) contains submission text version `v1.2` at `proof/submission.md`. No bounty form submission is asserted. Claude (Opus 5.5) independently re-derived the five load-bearing upstream interfaces from the paper and found no error, but did not line-check this manuscript.

## Mathematical sources

`proof/upstream-proof.md` is the English packaging adaptation of the new general upstream proof, with its Chinese counterpart. It supplies the premises formerly accepted by the module and completes Theorem A together with `proof/expanded-proof.md`. The latter retains the existing module revision `v1.1`, including its historical review attribution, with an added scope note. `proof/appendix-c-audit.md` gives the separate Appendix C statement audit. The general all-tail extension under Case B remains undecided. Section 8 and Appendix D are excluded.

References are to the [official PDF](https://math.apexin.net/papers/convex-nivat.pdf), published 2026-09-12, SHA-256 `7fd67831155f4226c010fd6af32de558b76643771e6be12dea4eebafa21745a8`. Theorem identifiers and printed pages replace private text-line references. The target PDF and private discussions are not redistributed.

## Reused scientific payload

The former local archive `apex-p03-nivat-module-validation` supplies `certificates/symbolic-gate.json`, `certificates/boundary/`, both global-example certificate directories, their global-coverage explanation, all checker and generator code, dependency pins and the license. An explicit file whitelist was copied; no repository metadata, environment, cache or historical log was imported. Certificate and code bytes are preserved. The module proof and reproduction documents have scope notes added; they are not described as byte-identical copies.

The 12 fixed algebraic inputs and two global instances are reused evidence, not new configurations or new coverage. The independent checker is not newly authored here. Its original separate-context provenance survives reuse, but packaging adds no new independence claim. The acceptance run checks the copied certificates and prescribed negative controls; it does not execute the general upstream proof. Generators are provided for optional reproduction and were not run during preparation.

Claude Opus 5.5 previously reviewed the module and reran its historical acceptance entries. That review did not cover the new upstream proof. Claude (Opus 5.5) independently re-derived the five load-bearing upstream interfaces from the paper and found no error, but did not line-check this manuscript. Codex/GPT preparation and fresh GPT adversarial review are distinct from cross-model approval.

## Bilingual documents and integrity

`README.md`, `REPRODUCE.md`, `PACKAGING.md`, `proof/upstream-proof.md`, `proof/expanded-proof.md`, `proof/appendix-c-audit.md`, `proof/submission.md` and `certificates/global-configurations.md` each have a `.zh-CN.md` counterpart. English is authoritative. Navigation rows are excluded from bilingual comparisons; formulas, inline code, code blocks, link destinations and numbers are compared in order, alongside semantic review. The English submission has no navigation row and must match its external source byte for byte.

`MANIFEST.sha256` covers all release files except itself. Verification output is captured outside this release inventory. It contains no environment, cache, third-party PDF or conversation. Local release scripts copy only manifest-listed files, verify hashes and scan for sensitive information. Publication, anonymous retrieval verification and form submission are separate actions.

Code is MIT-licensed; original prose and certificates use CC BY 4.0 to the extent applicable rights exist. Other materials retain their own terms. Before any release, synchronize the submission, translations, form files and manifest. Once an actual tag `v1.0` is published, substantive corrections require a new version.
