# Audit ledger

Append-only. Each entry records the scope, the auditor type, the pinned inputs,
the verdict, and the root agent's disposition of every finding. Raw reports
are in `audit/reports/`. All auditors were AI agents running in separate
contexts; this is process evidence, not independent expert review or peer
review.

## 2026-09-27 — Alladi source extraction (P1)

- Auditor: process-separated AI agent (Sonnet), read-only, one report file.
- Report: `reports/alladi-source-extraction.md`.
- Budget: 30 external operations allotted, 33 used (overrun of 3 recorded).
- Outcome: Alladi, JNT 14 (1982), obtained in full through a CORE mirror of
  the University of Michigan repository; Theorems 1–3 and (2.16) transcribed
  and checked against page images. Alladi, Trans. AMS 272 (1982), not
  obtained (publisher challenge page). Alladi, JNT 9 (1977): abstract only.
- Root follow-up: the report suggested that arXiv:2601.10636 (Alamoudi, 2026)
  might give a relative asymptotic for `M(x,y)` in the saddle range. The root
  agent read the preprint's LaTeX source. At `k = 1` the main-term sum in its
  Theorem 1.1 is empty (`1 ≤ J ≤ k−1`), so for `M(x,y)` it gives only the
  bound `≪ (x/log x)((log y/log x)^{N+1} + …)`, far larger than the true size
  `x·e^{−u log u}` at the saddle. **Disposition: not prior art for Lemma 3.2;
  the agent's reading was rejected.** One further search for Tenenbaum,
  *Sur un problème d'Erdős et Alladi* (1990), found no accessible copy; his
  2019 survey arXiv:1908.00488 does not mention Alladi.
- Paper changes: introduction credits Alladi Theorems 1–3 and (2.16) exactly;
  Alladi 1977, Alladi TAMS 1982, and Tenenbaum 1990 cited; the last two named
  as unread; priority of Lemma 3.2 stated as not established.

## 2026-09-27 — Self-overlap comparison (P1)

- Auditor: root agent.
- Report: `reports/self-overlap-comparison.md`.
- Outcome: this paper resolves Open Problem 1 of
  `sparse-mertens-singular-values` v0.1.0 and removes the dominance hypothesis
  from its conditional collapse. Shared identities are credited. The earlier
  release has the sharper `σ_1` estimate, and the paper says so.
- Paper changes: introduction Section 1.1 rewritten; `klineSmallest` cited
  with version DOI; LAA 588 credited for the base-volume identity; Section 2
  credits the earlier release for Propositions 2.1–2.2.

## 2026-09-27 — Proof audit, spectral lane (A1)

- Auditor: process-separated AI agent (Opus), read-only, one report file.
- Report: `reports/proof-audit-spectral.md` (file hashes recorded there).
- Verdict: **PASS**, no proof defects. 871 exact and floating-point
  falsification checks for `n ≤ 2000`, including nine zero-Mertens indices;
  none failed. Numerics are not cited as evidence.

| Finding | Severity | Disposition |
|---|---|---|
| `volumes.tex`: “their ordinary average … mean square” refers ambiguously to the non-unit values | must-fix exposition | **Fixed** with the auditor's replacement sentence |
| Constant `c'` undefined in the escape proof | optional | **Fixed**: `c' = 2^{-7/12} c` stated with its reason |
| `volumes.tex` should point to where `L` is defined | optional | Deferred; the reference to Theorem 4.6 already names it |
| Corollary 4.8 proves but does not state eventual simplicity | optional | Deferred; no claim depends on it |
| Overloaded symbols (`L`, `E`, `R`, `D`, `C`) across sections | optional | Deferred; each is defined locally. Recorded for a later version |
| Some definitions repeated; `L` called positive before proved | optional | Deferred; positivity is proved in the same lemma |

## 2026-09-27 — Proof audit, arithmetic lane (A1)

- Auditor: process-separated AI agent (Opus), read-only, one report file.
- Report: `reports/proof-audit-arithmetic.md` (file hashes recorded there).
- Verdict: **PASS**, no must-fix items. Lemma 3.2 checked line by line; the
  McNew equations (7), (13), (14), (17), the Tao Notes 10 Theorem 7 form of
  Halász, and Lee–Leong Theorem 1.1 (12) were fetched and compared; the
  saddle scale lies inside the stated ranges. Exact finite-identity checks
  passed; asymptotic exponents were deliberately not inferred numerically.

| Finding | Severity | Disposition |
|---|---|---|
| Also cite the unnumbered Saias display and McNew (11) | optional | Deferred; the cited equations carry the statements used |
| “uniformly as v → ∞” redundant | optional | Deferred |
| “weakened” slightly misdescribes Tao's form of Halász | optional | Kept: the form is weaker than the Granville–Harper–Soundararajan theorem also cited |
| Fan–Pomerance Theorem B and Alladi Theorem 1 not checked in this lane | scope note | Alladi Theorem 1 verified in the source-extraction lane; Fan–Pomerance assigned to the citation lane |
| Concurrent edits to discussion and references during the audit | process | Section 7.1 unchanged; references re-audited in the citation lane |

## 2026-09-27 — Rendered-page inspection (R1)

- Auditor: root agent.
- All 39 pages rendered and inspected as contact sheets: no overflow, the
  figure is intact, the title block is centered. The stale heading of
  Section 7.2 was retitled “Further questions”.

## 2026-09-27 — Claim and prose consistency (A1)

- Auditor: process-separated AI agent (Sonnet), read-only, one report file.
- Report: `reports/claim-prose-audit.md`; pinned at HEAD `9e3f175`.
- Verdict: **PARTIAL** (one must-fix). Title, author, version, and status
  agree; the principal claim matches the theorems with its `M(n) ≠ 0` and
  fixed-`r` conditions; every statement about the earlier release was checked
  against its paper; no process-history phrases in reader-facing prose.

| Finding | Severity | Disposition |
|---|---|---|
| README lists `ADMISSION.md` and runs `shasum -c MANIFEST.sha256`, neither yet present | must-fix | **Resolved at freeze**: both files are created before the candidate commit |
| README unit-multiplicity claim omits `n ≥ 4` | optional | **Fixed** |
| “singular value” not defined for a newcomer | optional | **Fixed**: one-sentence definition added to the README |
| `CITATION.cff` abstract omits `M(n) ≠ 0` | optional | **Fixed** |
| One README sentence on the lower-limit theorem re-readable | optional | Kept; the auditor found it accurate |

## 2026-09-27 — Citations and attribution placement (P1, A1)

- Auditor: process-separated AI agent (Sonnet), read-only, one report file.
- Report: `reports/citation-audit.md`; pinned at HEAD `9e3f175`.
- Budget: 25 web operations allotted, 31 used (overrun recorded in the report).
- Verdict: **PASS**. All 18 entries checked against Crossref, Zenodo, or
  arXiv; pinpoints for Hilberdink, McNew, Fan–Pomerance, Lee–Leong, and Tao
  checked against primary text; Alladi pinpoints checked against the source
  extraction; every statement about the earlier release checked against its
  paper. Unread sources (Alladi TAMS 1982, Tenenbaum 1990) are disclosed in
  the paper.

| Finding | Severity | Disposition |
|---|---|---|
| Alladi 1977 credited only in the introduction, not beside the thin-series theorem | optional | **Fixed** in Section 3.7 |
| Kural–McDonald–Sah entry lacks the published DOI | optional | **Fixed**; DOI 10.1007/s00013-020-01458-z confirmed through Crossref |

## 2026-09-27 — Checker regression after the README image (R1)

- Found by the root agent while preparing a review handoff.
- Commits `2df29bb` and `bae43fb` (README only) were pushed after the release
  audit but without rerunning `make check`. The new file
  `paper/figures/redheffer-comparison-standalone.tex`, which renders the README
  image, was picked up by the checker and its `\input` failed to resolve.
- **Fixed**: the checker now skips `*-standalone.tex` wrappers. `make check`
  passes with the recorded counts (39 pages, 11 source files, 121 labels).
  The paper and its PDF were not affected.
