# Admission record

**Current state:** CANDIDATE

**Version:** 0.1.0

**Planned tag:** `v0.1.0`

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html), draft 0.4, 2026-08-01

**Admission verdict:** NOT YET ADMITTED

Admission is a project release decision. It is not peer review, a correctness
certificate, or proof of global novelty.

## Principal claim

For the sparse Mertens matrix `B_n` of Kline (2019):

1. for `n ≥ 4`, exactly `n − 2k_n − 1` singular values equal one, and
   `k_n = O_H(n/(log n)^H)`;
2. `|σ_{r+1}(B_n) − √d_(r)(n)| < 3`, and `σ_{r+1}(B_n) ~ √(n/(a_r log n))` for
   fixed `r`;
3. `√n σ_{n−r}(B_n) → λ_r(L)^{−1/2}` for each fixed `r`, along all `n`, for an
   explicit positive compact operator `L`;
4. whenever `M(n) ≠ 0`, unconditionally,
   `σ_n(B_n) ~ |M(n)|/(√Q(n) W_n)` with
   `W_n = n exp(−(1+o(1))√(log n log log n))`.

No improved estimate for the Mertens function, prime counting, or the Riemann
hypothesis is claimed.

## P1 — prior work and credit

| Check | Status | Evidence or residual |
|---|---|---|
| Closest mechanisms and parameter families compared | PASS | Earlier release v0.1.0 statement by statement (`audit/reports/self-overlap-comparison.md`); Alladi JNT 1982 from primary text; Hilberdink 2017; Kural–McDonald–Sah; arXiv:2601.10636 read and rejected as prior art for Lemma 3.2 (`audit/LEDGER.md`) |
| Obtainable primary sources checked | PASS | `audit/reports/alladi-source-extraction.md`, `audit/reports/citation-audit.md` |
| Contribution types distinguished | PASS | README “What is new, and what is not”; introduction Section 1.1 |
| Novelty bounded to searched corpus | PASS | Paper and README state that priority for Lemma 3.2 and the moment formulations is not established |
| Inaccessible sources visible | PASS | Alladi, Trans. AMS 272 (1982) and Tenenbaum (1990) named as unread in the introduction and discussion |

**P1 gate:** PASS, with the named residuals below.

## A1 — claim and artifact consistency

| Check | Status | Evidence or residual |
|---|---|---|
| Principal claim precise and no broader than proof | PASS | `audit/reports/claim-prose-audit.md` |
| Parameters, hypotheses, and singular cases visible | PASS | `n ≥ 4`, fixed `r`, `M(n) ≠ 0`, and the zero-Mertens case stated at each claim |
| Proof, computation, and literature separated | PASS | No theorem rests on computation; README “Evidence and limits” |
| Prior work credited near the claims | PASS | `audit/reports/citation-audit.md`; placements fixed per `audit/LEDGER.md` |
| Public prose plain and process-history free | PASS | Claim audit grep and review |
| Version and status metadata agree | PASS | README, PDF title page and metadata, `CITATION.cff`, this file |
| Adversarial checking | PASS | Spectral and arithmetic proof audits (`audit/reports/proof-audit-*.md`), both PASS; all must-fix items resolved (`audit/LEDGER.md`). Process-separated AI audits, not peer review |

**A1 gate:** PASS. Any material claim edit reopens this gate.

## R1 — release and stewardship

| Check | Status | Evidence or residual |
|---|---|---|
| Reproduction commands and pinned tools | PASS | `VERIFICATION.md` |
| Deterministic document build and visual inspection | PASS | Two identical builds; all 39 pages inspected |
| Complete tracked-file manifest | PASS | `MANIFEST.sha256` covers every tracked file except itself |
| Hygiene: credentials, private paths, placeholders | PASS | Tracked-tree scan and the mechanical release audit |
| Correction, withdrawal, supersession policy | PASS | `CORRECTIONS.md` |
| Machine-readable citation | PASS | `CITATION.cff`, candidate-safe: no DOI, no release date |
| Immutable semantic tag | FAIL | Not authorized or created |
| Public permanent archive with provider byte identity | FAIL | Not created |
| DOI resolves; living repository identifies the version | FAIL | No DOI yet |
| Archive metadata matches repository | FAIL | No archive yet |

**R1 gate:** open until tagging and archiving are authorized and verified.

## External actions

| Action | Owner | Status |
|---|---|---|
| Create repository `jeff-kline/sparse-mertens-singular-spectrum` (private) and push `main` | Author authorization | done 2026-09-27 |
| Make the repository public | Author authorization | pending |
| Annotated tag `v0.1.0`, push, GitHub Release | Author authorization (freeze bundle) | pending |
| Enable the repository in Zenodo before the Release | Author, in the Zenodo portal | pending |
| Public-site listing and living-metadata update | Author authorization (admission bundle) | pending |

## Archive route

Zenodo GitHub integration. After the tag is pushed and before the GitHub
Release is created, the GitHub API `zipball/v0.1.0` is downloaded twice and
pinned; admission requires the Zenodo file to match it byte for byte.
`git archive v0.1.0` is generated twice as a separate determinism check.

## Named residual risks

- No independent human expert has examined the proofs.
- Alladi, Trans. AMS 272 (1982) and Tenenbaum (1990) were not read; either
  could contain the saddle-range relative asymptotic of Lemma 3.2.
- The smooth-number expansion is used as stated by McNew (2017); the original
  Saias proof was not read.
- Kline LAA 581, 584, and 588 were not reread in full; their statements were
  taken from the earlier release and the drafting survey.
