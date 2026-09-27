# Comparison with the author's earlier releases and papers

Root-agent record, 2026-09-27. Sources read directly:

- `sparse-mertens-singular-values` v0.1.0, tag `v0.1.0`, paper
  `paper/sparse-mertens-singular-values.tex` (abstract; Theorems closed,
  norm, main, max; Theorem alladi; Remark shape; Proposition sm; Section
  "Open problems"), version DOI 10.5281/zenodo.21774716. Zenodo record
  metadata checked through the public API on 2026-09-27: title, creator
  Kline, Jeffery, version 0.1.0, publication date 2026-08-03.
- `extremal-eigenvalues` v0.1.0 README (DOI 10.5281/zenodo.21764114).
- Bibliographic records for Kline, LAA 581 (2019), 584 (2020), 588 (2020);
  the LAA 588 DOI 10.1016/j.laa.2019.12.004 was confirmed through Crossref.

Same matrix: `B_n` here is the calligraphic `R_n` of LAA 581 and of v0.1.0.

## Statement-by-statement

| This paper | v0.1.0 or earlier | Classification |
|---|---|---|
| Prop. 2.1: inverse by parent chains, `det B_n = M(n)`, rank-one inverse | v0.1.0 Thm "closed form", Prop. "sm"; LAA 581 for the determinant | **Restated** (credited in Section 2 and the introduction) |
| Prop. 2.1: adjugate identity valid at `M(n)=0` | v0.1.0 treats `M(n)=0` only by noting singularity | **Refined** (short polynomial-continuity argument) |
| Prop. 2.2: coordinates of `w_n` as restricted Möbius sums | v0.1.0 Thm "closed form" | **Restated** |
| Thm 4.1: exactly `n−2k_n−1` unit singular values; reducing core; `k_n = O(n/(log n)^H)` | not present | **New relative to these sources** |
| Thm 4.2: `σ_1(B_n) = √n + O(1)` | v0.1.0 Thm "max": `√n (1+O(1/n))` | **Weaker restatement**; the paper says so |
| Thm 4.2: upper singular values within 3 of `√(parent degree)`; fixed-index asymptotics | v0.1.0 has only `σ_max/|λ_max| ≍ √log n` | **New relative to these sources** |
| Thm 4.3: `‖A_n^{-1}‖/√n → ‖K‖^{1/2}` and all fixed `s_r(A_n^{-1})/√n` | v0.1.0 Thm "max": `‖A_n^{-1}‖ = n^{1/2+o(1)}`, remarking the `o(1)` was a method artefact; unpublished notes gave `≍ √n` | **Refined** to an exact limit |
| Thm 4.6: fixed lower singular values `√n σ_{n−r} → λ_r(L)^{-1/2}`, all `n` | not present | **New relative to these sources** (method credited to Hilberdink 2017) |
| Thm 3.4: `W_n = n exp(−(1+o(1))√(log n log log n))`, `W_n^2/E_P → 15/π^2` | v0.1.0 Thm "norm": `‖w‖ = n^{1+o(1)}`; Remark "shape" and Open Problem 1 pose exactly this shape as open | **Resolves the earlier open problem** |
| Thm 4.7: `σ_n ~ |M(n)|/(√Q W_n)` unconditionally | v0.1.0 Thm "main": bracket `n^{−3/2+o(1)}`…`n^{−4/3+o(1)}` unconditionally; the equivalent only under a dominance condition implied by RH | **Sharpens**; dominance is now unconditional |
| RH ⇔ `σ_n ≪ n^{−1+ε}` (stated in the introduction) | v0.1.0 main theorem | **Restated**, now immediate from Thm 4.7 |
| Section 5 products, sums, volume laws | not present | **New relative to these sources** |
| Section 6 base volume `det(H H^T) = Q(n)` | LAA 588 Theorems 1 and 3 (as quoted in v0.1.0) | **Restated**; credited in Section 6 |
| Section 6 component profile, Appendix A | not present | **New relative to these sources** |
| Row-modified weighted divisor matrices | `extremal-eigenvalues` v0.1.0 | Different matrices; related method only |

## Consequence for the earlier release

v0.1.0 is not contradicted: its bracket and conditional collapse remain true.
Its upper exponent `−4/3` is superseded and its Open Problem 1 is resolved
here. A dated note in the v0.1.0 living repository (`CORRECTIONS.md` or
README) pointing to this release would keep the public record connected. That
note is a public action on another repository and needs the author's approval;
it is listed as a follow-on in `audit/RELEASE-PLAN.md`.

## Residual

LAA 581, 584, and 588 were not reread in full for this comparison. Their
relevant statements were taken from v0.1.0's citations and the drafting
survey. Theorem numbers attributed to LAA 588 are v0.1.0's.
