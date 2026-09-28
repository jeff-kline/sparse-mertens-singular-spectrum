# Release plan — version 0.1.0

Opened 2026-09-27. Standard: [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html),
draft 0.4 (2026-08-01); the live page was rechecked on 2026-09-27 and is unchanged.

State machine: DRAFT → CANDIDATE → TAGGED → ARCHIVED → ADMITTED. The current
state is recorded in `ADMISSION.md`.

## Principal claim

For the sparse Mertens matrix `B_n` (Kline 2019), the paper proves the exact
multiplicity of the singular value one, an additive comparison of the upper
singular values with parent degrees, fixed-index lower limits through an
explicit compact operator, and the unconditional equivalent
`σ_n(B_n) ~ |M(n)|/(√Q(n) W_n)` with `W_n = n exp(−(1+o(1))√(log n log log n))`.
No improved Mertens, prime-counting, or Riemann-hypothesis estimate.

## Gates

### P1 — prior work and credit

Bounded comparisons, with primary sources where obtainable:

1. Alladi (1982, JNT 14 and TAMS 272): what is proved about restricted Möbius
   sums, the error terms, and the range of `u = log x / log y`. Does any Alladi
   theorem give the saddle-range relative asymptotic (paper Lemma 3.2)?
2. The author's own work: Kline LAA 581, 584, 588; the released
   `sparse-mertens-singular-values` v0.1.0 (DOI 10.5281/zenodo.21774716);
   `extremal-eigenvalues` v0.1.0 (DOI 10.5281/zenodo.21764114). Record every
   overlapping statement as restated, refined, or new.
3. Hilberdink (2017): compact-Gram method; general rooted-tree results.
4. Kural–McDonald–Sah (2020) and Alladi's duality line for the thin-prime series.

Budget: at most 30 external source operations for delegated extraction,
plus root follow-up. No unbounded survey.

### A1 — claim and artifact consistency

Prose checkpoint first (abstract, introduction, README). Then bounded audits:

- proof lane A: spectral chapter (Sections 2, 4, 5), including zero-Mertens cases;
- proof lane B: arithmetic chapter (Section 3), especially Lemma 3.2 and the
  ranges of the smooth-number input; and Sections 6 and Appendix A;
- claim/prose lane: README, abstract, introduction, discussion, metadata;
- citation lane: every bibliography entry and attribution placement.

### R1 — reproducibility and stewardship

Deterministic `make paper` (fixed `SOURCE_DATE_EPOCH`), `make check`, rendered
inspection of every page, complete `MANIFEST.sha256`, `CITATION.cff`,
`CORRECTIONS.md`, GPL-3.0-only `LICENSE`, and the skill's mechanical
`release_audit.py` run from a tooling environment separate from the project
`.venv`.

## Ownership of actions

| Action | Owner | Status |
|---|---|---|
| Local edits, builds, audits, local commits | Agent (root integrates; auditors read-only) | authorized |
| Create private GitHub repository `jeff-kline/sparse-mertens-singular-spectrum` and push `main` | Author authorization, as recorded in `ADMISSION.md` | done 2026-09-27 |
| Make repository public | Author authorization | done 2026-09-27 |
| Further default-branch updates | Author authorization per candidate | records commit before the tag authorized 2026-09-27 |
| Annotated tag `v0.1.0` and push | Author authorization (freeze bundle) | authorized 2026-09-27 |
| GitHub Release | Author authorization (freeze bundle) | authorized 2026-09-27 |
| Zenodo repository enablement / DOI | Author, in the Zenodo portal; agent does not authenticate | enabled 2026-09-27 |
| Public-site listing and living-metadata push | Author approval required (admission bundle) | not authorized |
| Correction note in `sparse-mertens-singular-values` pointing here | Author approval required | proposed follow-on |

Commit identity for release commits and tags:
`Jeff Kline <2778446+jeff-kline@users.noreply.github.com>`.

## Archive route

**Zenodo GitHub integration**, matching the author's earlier releases. The
author enables the repository in Zenodo before the GitHub Release. The
candidate `CITATION.cff` carries no DOI and no `date-released`. After the tag
is pushed and before the Release is created, the GitHub API `zipball/v0.1.0`
is downloaded twice and pinned; the Zenodo file must match it byte for byte.
`git archive v0.1.0` is generated twice as a separate determinism check.

## Excluded from the release

The drafting workspace's local environment, temporary renders, third-party
source copies (Hilberdink PDF, standard HTML, extremal-eigenvalues source),
and the draft source bundle. The exploratory opportunity campaign of
2026-09-27 is not part of this release.
