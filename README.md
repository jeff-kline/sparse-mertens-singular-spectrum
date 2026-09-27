# The singular spectrum of a sparse Mertens matrix

Jeffery Kline — quarantined rough draft, September 27, 2026.

This manuscript studies a matrix built from simple parent links between integers. A squarefree integer has no repeated prime factor. Its parent is obtained by removing its largest prime factor. For example, among the integers from 1 to 6, the links are:

```text
1 ──→ 2 ──→ 6       4 (isolated)
├───→ 3
└───→ 5
```

Here 6 has parent 2 because 6 = 2 × 3 and its largest prime factor is 3. The integer 4 is not squarefree, so it has no parent link. To build the matrix, start with ones on the diagonal and put a one in row i, column j for every arrow j → i. Then replace the first row by ones. With rows and columns ordered 1 through 6, the result is:

```text
      1 2 3 4 5 6
    ┌             ┐
  1 │ 1 1 1 1 1 1 │
  2 │ 1 1 0 0 0 0 │
  3 │ 1 0 1 0 0 0 │
  4 │ 0 0 0 1 0 0 │
  5 │ 1 0 0 0 1 0 │
  6 │ 0 1 0 0 0 1 │
    └             ┘
```

The last row records the link from 2 to 6 and the diagonal entry at 6. The isolated index 4 keeps its diagonal one and is included in the new first row. The paper keeps this small parent-tree example and illustrates the larger structure with a side-by-side vector plot of transposed Redheffer and B at n = 120: 721 versus 313 nonzero entries. It explicitly identifies B as the earlier matrix called R in calligraphic notation, introduced in Kline (2019).

The manuscript gives an exact count of singular values equal to one, estimates the largest singular values from parent degrees, and describes the fixed smallest nonexceptional singular values through an explicit compact operator. A family of restricted Möbius sums controls the exceptional smallest singular value and products of singular values.

Every matrix, arithmetic sum, projection, and limiting operator is defined in the paper. The argument is self-contained relative to precisely stated classical analytic-number-theory inputs; it does not refer readers to earlier campaign notes for definitions or proofs. Geometric component projections and weighted least-prime sums are included as companion results.

## Novelty and status

The bounded survey supports a spectral manuscript with explicit credit to Hilberdink's compact-Gram method. The forest kernel, bordered-matrix deflation, exact unit spectrum, and degree comparison remain candidate contributions in the inspected corpus. Arithmetic novelty is unresolved because full Alladi (1982) theorem pages were inaccessible. The paper treats those arithmetic statements as derived tools and refinements, not a certified new analytic principle. It proves no improved bound for the Mertens function, prime counting, or the Riemann hypothesis.

This is DRAFT, not an admitted release or peer-reviewed paper. AI assisted the derivations, literature survey, exposition, and checks under the author's direction. Earlier process-separated AI examinations do not constitute independent expert review. See audit/novelty-gate.md, the two prior-art reports, and the final draft-review record for coverage and residuals.

## Artifacts

- `paper/main.tex`: master LaTeX source, with source sections in `paper/sections/`.
- `paper/main.pdf`: complete 37-page reading copy, produced by `make paper`.
- `draft-source.zip`: portable source and audit bundle (excludes third-party source copies and the local environment).
- `VERIFICATION.md`: build, review, and visual-check results.
- `STATE.md`: final drafting status and remaining release obligations.
- `audit/`: bounded source comparisons, proof/exposition review, and claim provenance.
- `CHARTER.md`: finite scope and local-only authority.

This folder is isolated from the earlier evidence and original project. No public repository, tag, DOI, or release has been created. Full release preparation follows only after the draft and its remaining source comparisons are settled.

## Rebuilding

Run `make paper` with pdfLaTeX installed. The Makefile fixes the source-date epoch for reproducibility. For `make check`, create this folder's own `.venv` with a managed Python interpreter; the checker needs only the standard library. The supplied environment was validated with Python 3.12.14 and `sys.prefix != sys.base_prefix`. Do not use a system or unrelated project's interpreter for checking. The manifest records this draft snapshot, not a public release.

The exact vector figure source is included in `paper/figures/redheffer-comparison.tex`. To regenerate it, run `.venv/bin/python paper/figures/build_comparison.py` from this folder before `make paper`; no third-party Python dependencies are needed.

Section 7.1, “What is needed for a stronger Mertens bound,” gives exact sufficient residual, component, and resolvent certificates and compares their required rates with the classical Mertens estimate. Speculative fleet proposals remain outside this manuscript.
