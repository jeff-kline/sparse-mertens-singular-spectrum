# Focused spectral prior gate — 2026-09-27

**Scoped verdict: PASS for a reasonable distinct contribution; PARTIAL for priority of the exact-core companion theorem.** This gate supports drafting a carefully attributed theorem paper about this sparse family. It does not establish worldwide novelty, validate the analytic input for `w`, or substitute for a correctness examination.

The strongest contribution is the explicit ancestor-Gram limit and the deflated limit for every fixed nonexceptional bottom singular value of the modified matrix, including zero-Mertens indices. Compact-Gram asymptotics themselves are established methodology. The upper-degree comparison and exact unit spectrum are useful companion results, but elementary standard linear algebra accounts for much of their mechanism.

## Corpus and local comparison

Read the four requested files in `rough-mobius-energy/spectral-limit/`: `README.md`, `operator-proof.md`, `core-and-priority.md`, `upper-spectrum.md`; inspected the complete output of the supplied sparse-Mertens manuscript, with focused rereads of its attribution and theorem passages; and read its existing `audit/reports/prior-art-audit.md`.

The supplied manuscript's Theorem `thm:max` establishes `||A_n^{-1}||=n^(1/2+o(1))`. Its final open problem asks about deeper singular values. The current explicit compact limit supplies a fixed constant and all fixed inverse singular-value limits. The deflated law for `B_n` is not stated in the supplied manuscript. Its forest inverse, Möbius column, sparse family, and rank-one inverse identity are already foundations and must not be presented as new.

Also read `mertens/claims/C0-ancestor-kernel.md` after the root agent identified it. This September 12 local candidate already proves the proposed order `Theta(sqrt(n))` through an ancestor-kernel row-sum estimate bounded by the reciprocal-primorial sum. Its header labels it UNEXAMINED; this gate does not change that status. Across the user's own work, the new claim is the **limiting constant and full fixed-index spectrum**, not the first proposed `Theta` bound or first ancestor-kernel argument.

## Hilberdink: actual hypotheses checked

Primary source: Titus Hilberdink, *Singular values of multiplicative Toeplitz matrices*, LMA 65 (2017), 813–829, [DOI](https://doi.org/10.1080/03081087.2016.1204978), [accepted PDF](https://centaur.reading.ac.uk/66059/1/finitetoeplitz.pdf). Manuscript pages 5, 7, 11–13 were inspected.

Write `M_n(f)_{ij}=f(i/j)1_{j|i}`, `F(x)=sum_{m<=x}|f(m)|²`.

- Corollary 2.3: completely multiplicative `f`, `F` regularly varying of index `rho`; Hilbert–Schmidt Gram convergence holds precisely for `rho>1/2`, giving fixed-index singular asymptotics.
- Theorem 3.2: multiplicative `f`; `F` regularly varying of index `rho`; each local series `sum_m |f(p^m)|² p^(-ms)` converges for `Re s>rho-delta_p` and is nonzero on `Re s=rho`. For convergence additionally require `rho>1/2`, `sum_n |lambda(n)|²/n^(2rho-eta)<infinity` for some `eta>0`, and, for every `epsilon>0`, `|F_{k,l}(x)| <<_epsilon (kl)^epsilon |lambda(kl)| F(x)` for coprime `k,l`.

Here `F_{k,l}(x)=sum_{m<=x} conjugate(f(km)) f(lm)` and `lambda` is the multiplicative local correlation ratio of Theorem 3.1; conjugation convention does not affect the real Möbius application. The limit kernel is `conjugate(lambda(i/gcd(i,j))) lambda(j/gcd(i,j))/lcm(i,j)^rho`.

Section 4(b), `f=mu`, proves **every fixed bottom singular-value asymptotic** for the dense divisibility factor `M_n(1)`, using `M_n(mu)=M_n(1)^(-1)`; it is not restricted to its smallest singular value.

### Applicability and novelty risk

These matrix hypotheses fail for the present forest inverse `C_n`: `C[2,1]=-1` but `C[6,3]=0`, although both quotients equal 2. Similarly `A[2,1]=1` and `A[6,3]=0`. The ancestor restriction depends on the starting vertex, not just the quotient. The modified `B_n` also has a dense first row outside that triangular class. Thus the inspected theorems do not directly deliver the claimed sparse-family results. This is a direct entry obstruction, not merely a difference in terminology.

The forest kernel also has zero entries on incomparable prime pairs, unlike the dense Möbius kernel. Its arithmetic descendant densities and summable ancestor tail bound therefore need their own proof. However, Hilberdink's proof already combines entrywise arithmetic limits, uniform Hilbert–Schmidt tails, and spectral convergence. Presenting that strategy as a new general method would fail this gate. The sparse proof is a new application with its own simpler tail geometry.

The most substantial additional step is `B_n`'s rank-one deflation: the moving input direction escapes finite coordinates; compactness makes its projected contribution vanish; the output projection produces `L`; the pseudoinverse handles `M(n)=0`. No corresponding modified-matrix theorem was found in the inspected Hilberdink text. The standard singular perturbation and compactness lemmas should be described as tools, with novelty located in their arithmetic application and explicit resulting operator.

## Other directly relevant primary comparison

[Clément–Steinerberger, arXiv:2502.09489v1](https://arxiv.org/html/2502.09489v1), Theorem in §1.3: for the **dense** Redheffer matrix and `v_n=(sum_{d|k}1/d)_{k<=n}`, the normalized inner product between `v_n` and `A_n^T A_n v_n` has an explicit limit approximately 0.9979. This is a quantitative approximate-singular-vector statement. Its hypotheses do not describe the sparse forest; its theorem does not supply our compact inverse kernel, deflated bottom spectrum, or exact unit multiplicity. Cite it accurately as largest-singular-vector work, rather than making its principal theorem sound like a full singular-value asymptotic.

Two focused forest searches found no directly matching theorem. They did surface standard adjacency/nullity and directed-tree singular-value material; those were not inspected as full texts and are not evidence of absence. The identity `S^T S=diag(degrees)` follows immediately from disjoint supports, and Weyl bounds and block inertia are standard. The exact count relies on the special supply of a private leaf to every active parent. A defensible companion claim is the exact arithmetic-family multiplicity/compression, not invention of low-rank compression or inertia. Broader general-tree priority remains PARTIAL.

## Drafting disposition

Proceed with: explicit sparse ancestor limit, its concrete constant for `||A_n^{-1}||`, all fixed deflated bottom limits for `B_n`, and the exact-core/upper-degree results as companions. Credit Hilberdink before stating novelty. Say these results sharpen the supplied sparse-family manuscript; do not claim the first compact-operator treatment of arithmetic singular values. No improved PNT, Mertens cancellation, RH result, certified decimal constant, or general optimality follows from this spectral gate.

One residual self-overlap issue: search results listed the user's `extremal-eigenvalues` repository as covering sparse divisor matrices and singular values. It was not opened in this worker's ten-operation allocation; the root agent reports its separate public GitHub access attempt was inaccessible. Its full content is not independently assessed here.

## Operation ledger and access record

Exactly ten individual external search/open/download operations, including failures:

1. Open `https://centaur.reading.ac.uk/66059/`: Anubis access denied, error `9e4edb5b6b850c41`.
2. Search `Hilberdink "Singular values of multiplicative Toeplitz matrices" pdf`.
3. Search `Redheffer forest matrix singular values unit multiplicity singular Hilberdink`.
4. Open `https://centaur.reading.ac.uk/66059/1/finitetoeplitz.pdf` with web reader: timeout.
5. Open `https://arxiv.org/html/2502.09489v1`: succeeded; primary theorem read.
6. Download the same Hilberdink PDF with `curl -L --max-time 40`: succeeded, valid PDF; locally extracted with `pdftotext -layout`.
7. Search `"forest" "singular values" "1" triangular matrix`.
8. Search `"sparse" "Mertens" "singular" spectrum`.
9. Search `"rooted tree" "singular values" "triangular"`.
10. Search `"forest" "singular values" "multiplicity" matrix identity`.

Search results from secondary sites were discovery aids only. No external operation beyond this ledger; no Python workload; no email or public mutation.

Saved source: `sources/hilberdink-2017.pdf`, SHA-256 `d040bf0f3df4da2d72b1f7728b80c6e3fed3d1214ed1e3a895e8dde81f71b518`; extracted text beside it. Earlier notes saying Hilberdink's full theorem remained inaccessible are superseded for this gate by the successful primary-PDF retrieval.
