# Corrections, withdrawals, and supersession

This repository keeps a visible record of material corrections to released
claims and artifacts.

## Policy

- Minor typographical or navigational fixes may be made on the living default
  branch without changing an archived release.
- A change to a theorem statement, hypothesis, proof dependency, citation that
  affects priority or scope, or verification artifact creates a new version.
  The earlier tag and permanent archive remain unchanged and identifiable.
- A material error that invalidates a principal claim will be marked
  prominently in the README and in this file. The affected release will not be
  deleted or silently replaced.
- A withdrawn result remains findable with the reason, date, affected
  versions, and any replacement or correction linked here.
- Public tags and archived files are immutable. Corrections are made in a new
  commit and, when material, a new tagged release.
- If earlier work is found that anticipates a result here, the novelty
  statements will be narrowed and the source credited in a new version.

Suspected errors may be reported through the repository issue tracker:
<https://github.com/jeff-kline/sparse-mertens-singular-spectrum/issues>.

## Relation to earlier releases

This paper sharpens the smallest-singular-value bracket of
[*The smallest singular value of a sparse Mertens matrix*](https://doi.org/10.5281/zenodo.21774716),
version 0.1.0. That release remains correct as stated; its upper exponent
`-4/3` is superseded here by an unconditional asymptotic equivalent, and its
Open Problem 1 (the shape of the inverse-vector norm) is resolved here.

## Version history

### 0.1.0 — release candidate

- Release preparation began 2026-09-27 from a drafting snapshot whose reading
  copy had SHA-256 `6d081a7476e8d2abacf83edbbd0db80395daaba3c69dc1e2bce68fed5d1a62da`.
- The candidate has no active DOI or permanent archive yet.
- Prepublication changes made during release preparation, before any tag:
  the relation to the earlier release was stated and its citation corrected
  from “working manuscript” to the archived version; attribution to Alladi
  (1977, 1982), Kline (LAA 588), and Tenenbaum (1990) was added; one sentence
  in Section 5 was reworded for accuracy. No theorem statement changed.
