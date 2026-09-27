# The singular spectrum of a sparse Mertens matrix

Jeffery Kline

**Version 0.1.0 — release candidate, not yet archived.** No DOI exists for
this version yet. It is prepared for release under the project's
[public research standard](https://jeff-kline.github.io/posts/research-program/index.html).
Admission under that standard is a release decision, not peer review or a
correctness certificate.

The paper is [paper/main.pdf](paper/main.pdf); its source is
[paper/main.tex](paper/main.tex).

## The matrix

This paper studies a matrix built from simple parent links between integers. A
squarefree integer has no repeated prime factor. Its parent is obtained by
removing its largest prime factor. For example, among the integers from 1 to 6,
the links are:

```text
1 ──→ 2 ──→ 6       4 (isolated)
├───→ 3
└───→ 5
```

Here 6 has parent 2 because 6 = 2 × 3 and its largest prime factor is 3. The
integer 4 is not squarefree, so it has no parent link. To build the matrix,
start with ones on the diagonal and put a one in row i, column j for every
arrow j → i. Then replace the first row by ones. With rows and columns ordered
1 through 6, the result is:

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

Call the n × n version `B_n`. It was introduced by Kline (2019), where it is
written as a calligraphic R. Its determinant is the Mertens function:

```text
det B_n = M(n) = μ(1) + μ(2) + ... + μ(n),
```

where μ is the Möbius function. Redheffer's classical matrix has the same
determinant but many more nonzero entries: at n = 120, 721 against 313. The
paper shows the two side by side.

## Main results

The singular values of a matrix measure how much it stretches vectors in
different directions; their product is the absolute value of the
determinant. They are listed in decreasing order, σ₁ ≥ … ≥ σₙ. Let `k_n` be the
number of integers up to n that have at least one child in the tree.

1. **Almost all singular values equal one.** For n ≥ 4, exactly
   `n − 2k_n − 1` of them do, and `k_n = O(n/(log n)^H)` for every fixed H.
2. **The upper singular values follow the parent degrees.** Apart from
   σ₁ ~ √n, each is within 3 of the square root of a parent's number of
   children. For fixed r, σ_{r+1} is asymptotic to `√(n / (a_r log n))`,
   where `a_r` is the r-th squarefree integer.
3. **The lower singular values have an explicit limit.** For each fixed r,
   `√n · σ_{n−r}` converges to `λ_r(L)^(−1/2)`, where L is an explicit
   compact operator built from the tree. This holds for every n, including
   those where `M(n) = 0` and the matrix is singular.
4. **The smallest singular value carries the Mertens sum.** Whenever
   `M(n) ≠ 0`,

   ```text
   σ_n(B_n) ~ |M(n)| / (√Q(n) · W_n),
   W_n = n · exp(−(1 + o(1)) √(log n · log log n)),
   ```

   where `Q(n)` counts the squarefree integers up to n and `W_n` is the norm of
   an explicit vector of restricted Möbius sums. Equivalently,
   `σ_n(B_n) = |M(n)| · n^(−3/2) · exp((1 + o(1)) √(log n · log log n))`.
   This holds unconditionally.

The paper also proves estimates for products of singular values, moments and
support-constrained sums of the restricted Möbius sums, and a Dickman–Buchstab
profile for a geometric residual.

**No stronger estimate for the Mertens function, prime counting, or the
Riemann hypothesis follows.** The formula in item 4 contains `M(n)`, so it
restates the Mertens sum rather than bounding it. Section 7.1 of the paper
explains what additional input a stronger Mertens bound would require.

## What is new, and what is not

The closest earlier work is the author's own release
[*The smallest singular value of a sparse Mertens matrix*](https://doi.org/10.5281/zenodo.21774716)
(version 0.1.0, 2026), on the same matrix. It proved

```text
|M(n)| n^(−3/2+o(1))  ≤  σ_n(B_n)  ≤  |M(n)| n^(−4/3+o(1)),
```

obtained the lower scale as an equivalent only under a hypothesis implied by
the Riemann hypothesis, and posed the shape of `W_n` in item 4 as an open
problem. This paper proves that shape. The hypothesis then holds
unconditionally, and the bracket becomes an asymptotic equivalent. The paper
also replaces the earlier `‖A_n⁻¹‖ = n^(1/2+o(1))` by an exact limiting
constant. The earlier release has the sharper estimate for the largest singular
value. Items 1–3, the products, and the geometric results do not appear there.

Other credit:

- **Hilberdink (2017)** developed compact Gram limits for arithmetic
  (multiplicative Toeplitz) matrices. The general method and the idea of a
  fixed lower-spectrum limit are his. The contribution here is the explicit
  kernel for this parent tree, the deflation for the bordered matrix, and the
  exact unit and degree results.
- **Alladi (1982)** studied the restricted Möbius sums and the bounded
  least-prime weighted extremum. His asymptotic for the sums holds as a
  relative estimate only while `u = log x / log y` stays below about
  `(log x)^(1/3)`. The estimate for `W_n` needs `u` near
  `(log n / log log n)^(1/2)`, where the paper proves the relative asymptotic
  from the classical Mertens bound and a two-term smooth-number expansion of
  de Bruijn and Saias, in the form stated by McNew (2017). Alladi's companion
  paper (Trans. AMS, 1982) and a related 1990 paper of Tenenbaum could not be
  read, so priority for this step is not established.
- **Kline (2019, 2020)** introduced the matrix, found its dominant
  eigenvalues, and proved the bordered-matrix identity behind the geometric
  base volume.
- **Kural, McDonald, and Sah (2020)** already give the zero value of the
  unweighted thin-prime reciprocal series; the paper adds a quantitative tail.

These comparisons come from a bounded literature search recorded in
[audit/](audit/). They do not establish worldwide novelty. Priority for the
arithmetic moment and support-constrained formulations is not established.

## Evidence and limits

- Every result is proved in the paper from explicitly stated classical inputs:
  the prime number theorem, a classical Mertens bound, smooth- and rough-number
  asymptotics, and, in an optional appendix only, Halász's theorem. No
  numerical computation is used as evidence for any theorem.
- The proofs were checked by process-separated AI audits. No independent human
  expert has reviewed them. Agreement among AI checks is evidence about a
  process, not independent validation.
- Limiting constants such as `‖K‖` and `λ_r(L)` are defined exactly but not
  evaluated numerically; certified values would need rigorous truncation
  bounds.

## Reproduce

Requirements: pdfLaTeX (tested with TeX Live 2021) and Poppler's `pdfinfo` and
`pdftotext`. The checker uses only the Python standard library and must run
from an isolated environment:

```sh
python3 -m venv .venv            # any Python 3.10+ interpreter
make paper                        # builds paper/main.pdf; fixed SOURCE_DATE_EPOCH
make check                        # labels, citations, TeX log, and PDF text
shasum -a 256 -c MANIFEST.sha256
```

`make check` checks the document's consistency; it does not check proofs. The
Redheffer comparison figure is exact vector source; regenerate it with
`.venv/bin/python paper/figures/build_comparison.py`.

## Repository contents

- `paper/`: LaTeX source (`main.tex`, `sections/`, `figures/`) and the reading
  copy `main.pdf`.
- `scripts/check_paper.py`: document consistency checker.
- `audit/`: prior-art comparisons, proof reviews, and their dispositions;
  `audit/drafting/` keeps the records from the drafting stage.
- `ADMISSION.md`, `VERIFICATION.md`, `CORRECTIONS.md`, `CITATION.cff`,
  `MANIFEST.sha256`: release records. `audit/LEDGER.md` lists every audit
  finding and its disposition.

## Role of AI

AI did the derivations, literature search, exposition, and audits under the
author's direction. The author chose the questions and is responsible for the
result and its corrections.

## License

GPL-3.0-only. See [LICENSE](LICENSE).
