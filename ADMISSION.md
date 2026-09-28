# Admission record

**Current state:** ADMITTED

**Version:** 0.1.0

**Tag:** `v0.1.0` → `6552b72c51dfc88014711658063d76a252694d04`

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html), draft 0.4, 2026-08-01

Current verdict: ADMITTED (2026-09-28)

**Version DOI:** [`10.5281/zenodo.23004980`](https://doi.org/10.5281/zenodo.23004980) · **Concept DOI:** `10.5281/zenodo.23004979` · **Record:** <https://zenodo.org/records/23004980>

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
| Adversarial checking | PASS | Spectral and arithmetic proof audits (`audit/reports/proof-audit-*.md`), both PASS; independent review of the candidate (`audit/reports/independent-review.md`) found no mathematical objection; all must-fix items resolved (`audit/LEDGER.md`). AI reviews, not peer review |

**A1 gate:** PASS. Any material claim edit reopens this gate.

## R1 — release and stewardship

| Check | Status | Evidence or residual |
|---|---|---|
| Reproduction commands and pinned tools | PASS | `VERIFICATION.md` |
| Deterministic document build and visual inspection | PASS | Clean-checkout build reproduces the recorded PDF hash (`VERIFICATION.md`); all 39 pages inspected |
| Complete tracked-file manifest | PASS | `MANIFEST.sha256` covers every tracked file except itself |
| Hygiene: credentials, private paths, placeholders | PASS | Local account and session paths in audit reports redacted 2026-09-27; tracked-tree rescan found none |
| Correction, withdrawal, supersession policy | PASS | `CORRECTIONS.md` |
| Machine-readable citation | PASS | `CITATION.cff`, candidate-safe: no DOI, no release date |
| Immutable semantic tag | PASS | Annotated `v0.1.0` (object `9d2b521`) → `6552b72`; tagger is the GitHub noreply identity |
| Public permanent archive with provider byte identity | PASS | Two pinned GitHub `zipball/v0.1.0` downloads and two Zenodo downloads are byte-identical: 711,753 bytes, SHA-256 `9bedd6f84b2c126843af8e442ae5f075847912686072ff92d739fc494dcbafe3`; Zenodo MD5 `5e8b6653978dc06d505dc0e0fe401ded` |
| DOI resolves; living repository identifies the version | PASS | `doi.org/10.5281/zenodo.23004980` redirects to the Zenodo record; README, `CITATION.cff`, and the living paper carry the version DOI |
| Archive metadata matches repository | PASS | Title, creator Kline, Jeffery, version v0.1.0, publication date 2026-09-28, license `gpl-3.0-only` (GNU GPL v3.0 only), resource type software, related identifier the `v0.1.0` tree |

**R1 gate:** PASS.

## External actions

| Action | Owner | Status |
|---|---|---|
| Create repository `jeff-kline/sparse-mertens-singular-spectrum` (private) and push `main` | Author authorization | done 2026-09-27 |
| Make the repository public; enable secret scanning and push protection | Author authorization | done 2026-09-27 |
| Annotated tag `v0.1.0`, push, GitHub Release | Author authorization (freeze bundle) | authorized 2026-09-27 |
| Enable the repository in Zenodo before the Release | Author, in the Zenodo portal | done 2026-09-27; Zenodo release webhook present |
| Living-metadata update (this commit) | Author authorization (admission bundle) | done 2026-09-28, pushed after the site listing was verified live |
| Public-site listing | Author authorization (admission bundle) | done 2026-09-28: landing entry at <https://jeff-kline.github.io/> (site commit `da0d5da`), Pages build and live HTML checked for title, blurb, repository link, and version DOI |

## Archive verification

- Route: Zenodo GitHub integration; no manual deposit.
- Pinned before the GitHub Release: GitHub API `zipball/v0.1.0`, downloaded
  twice, identical, 711,753 bytes, SHA-256 `9bedd6f84b2c126843af8e442ae5f075847912686072ff92d739fc494dcbafe3`.
- Zenodo file `sparse-mertens-singular-spectrum-v0.1.0.zip`, downloaded twice:
  identical to the pinned zipball.
- Separate determinism check: `git archive --format=zip
  --prefix=sparse-mertens-singular-spectrum-v0.1.0/ v0.1.0`, generated twice,
  identical, 710,337 bytes, SHA-256 `493a74b204383f78706eaed0f8e4a36cbe4ec4423c22c6fd7c6021b82624afcd`. This is a different file from
  the provider zipball and is not compared with it.
- Mechanical audit at the archived state, on the unchanged tagged tree:
  12 pass, 0 warnings, 0 fail.
- Tagged commit reproduced from a clean `git archive` extraction: PDF SHA-256
  `bf477dddf4d5d65ad5f26be42f2de4c4e37dda3dabe20b5f5a34152fb420b915`,
  `make check` PASS, 50 manifest entries OK.
- The tagged tree keeps its “release candidate” wording and has no DOI. The
  living paper was rebuilt with the DOI on its title page, so the living PDF
  differs from the archived one.

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
