# Assembled spectral and geometry proof audit

STAGE: PROOF-AUDIT (proof-aware translation/assembly review, not an isolated initial attack).

VERDICT: **VERIFIED within the supplied-premise scope.** The checked arguments establish the finite identities and spectral, product, sum, geometry, and Halász-application conclusions below. I found no load-bearing GAP and no proven refutation. This is not independent verification of the imported analytic theorems, the arithmetic energy theorem, or priority claims. Those broader obligations are **INCOMPLETE / outside this assignment**, rather than silently certified by this verdict.

## Scope, exposure, and dependencies

I read `paper/main.tex` and the complete files `definitions.tex`, `spectral.tex`, `volumes.tex`, `geometry.tex`, and `halasz.tex` in `paper/sections`. I used the cold-examiner skill's stage-2 reporting conventions. The coordinator explicitly supplied this as the proof-aware assembled-manuscript stage following earlier staged attacks; I did not inspect those earlier reports or claim new initial-stage isolation.

Supplied premises, as authorized: `W_n = n exp(-(1+o(1)) sqrt(log n log log n))`; the stated classical Mertens/Vinogradov–Korobov input (including its weakened exponent used here); the prime number theorem and elementary prime estimates; the stated fixed-parameter smooth and rough counting limits; and the displayed quantitative Halász inequality. Source attribution and the arithmetic section were not audited. Standard finite-dimensional SVD, congruence/inertia, compact positive-operator spectral theory, and elementary dominated-convergence facts were checked at their actual uses.

No external sources, Python, numerical experiments, nested agents, TeX builds, email, or manuscript edits were used. The only artifact written is this report. Exact source hashes are recorded below.

## Checked argument chain

### Definitions and finite identities — VERIFIED

The parent rule produces precisely an initial segment of the increasing prime factors, not arbitrary divisibility. Descendants of squarefree `j` are `jd` with squarefree `d` and `P^-(d)>P^+(j)`. This validates the degree and descendant counts, the path-sign inverse, and the example at `n=6`. Nonsquarefree vertices contribute identity blocks before the border.

The determinant lemma has scalar `1+u^T C e_1=M(n)`. The inverse correction has the stated order `muvec w^T/M`, and polynomial continuation of the rank-one parameter proves the adjugate identity even at zero determinant. The first coordinate `w_1=M(n)-1`, the other restricted sums, the isolated-coordinate ones, and `W_n^2=E+(M-1)^2+n-Q` all check. The degree sum and both Frobenius counts count disjoint entries correctly.

### Unit singular values and upper spectrum — VERIFIED

Every active parent has a leaf child: choosing the largest prime at most `n/a` prevents any further larger prime extension of `ap`. Those leaf supports are disjoint, so `F` has full column rank. Consequently the reducing space has dimension `2k`, and the off-diagonal block `R` is invertible. The substitution in the quadratic form really removes `T_0`, giving inertia `(k,k,0)`.

For `B`, coordinate 4 supplies a nonzero component of the all-ones vector in the identity complement when `n>=4`. The Schur complement removes `bb^T` and leaves precisely the subtraction `e_1e_1^T` in the parent block; it does not alter the invertible off-diagonal blocks. Thus the enlarged core has inertia `(k+1,k,0)` and dimension `2k+1`. A zero singular value correctly counts below one. Both matrix and transpose vanish after subtracting the identity on the stated complement, so this is a reducing-space claim, not merely a Gram invariant-space claim.

The parent bound uses an admissible fixed `alpha<1` with `H(1-alpha)<1`; its Euler-product bound is sufficient. The upper-spectrum comparison separates orthogonal domain and range summands and accounts for the extra zero in the full `S P` matrix. The errors `1+eta` and `eta` combine to the asserted bound. The sorted fixed-index asymptotics are justified by the supplied uniform diagonal-tail estimate, not assumed from coordinatewise convergence alone.

### Compact Gram limit and both projections — VERIFIED

Common descendants exist exactly for comparable ancestors, and their inverse-entry products have constant sign `mu(k/j)`. The fixed-coordinate density calculation yields exactly `delta_k`, including `delta_1=c_0`. The squarefree Hilbert–Schmidt tail is summable because all entries of maximum coordinate `k` are bounded by `1/k` and occur at most twice per ancestor. The nonsquarefree diagonal contributes at most `1/n` to the squared Hilbert–Schmidt norm and disappears. Finite-block convergence plus these tails proves the claimed norm convergence, hence positivity. Arbitrarily large prime-coordinate diagonal compressions prove infinite rank.

Weak escape of `v_n` follows from the actual fixed-coordinate convolution and the supplied arithmetic scales: `(log n)^(7/12)` dominates `sqrt(log n log log n)`. Normalization alone is not being used as a substitute for this argument. The formula for `J_n=D_n^T P_{a_n}D_n` has the correct denominator `Q(n)/n` and limit `L`. Compactness then gives `J_n v_n ->0`, and the expansion of both domain projections has the stated norm bound. These are projections **onto perpendicular complements**. The finite products and their zero extensions agree with the specified ambient `ell^2` interpretation. Positivity and infinite rank of `L` follow from positive finite approximants and the rank-one change to prime-coordinate compressions.

### Deflation, zero Mertens values, and minimum — VERIFIED

The elimination multipliers in the deflation lemma are correctly ordered and dimension-independent; their norms and inverse norms approach one. After removing the divergent scalar block the remaining singular values stay bounded, so the multiplicative comparison becomes an absolute error tending to zero. The appended zero in the doubly projected full matrix causes no fixed-index shift error.

At `M(n)!=0`, `t_n=sqrt(Q)W/(M sqrt(n))` diverges in absolute value, and inversion changes index `r+1` to `n-r`. At `M(n)=0`, the right kernel is `span(muvec)` and the left kernel is `span(w)`. The identity `B C=I+e_1 w^T` implies `B(P_a C P_v)=P_v`; range and kernel conditions then identify the Moore–Penrose inverse. Its largest singular values reciprocate the smallest **positive** singular values, again yielding index `n-r`. The two cases prove the all-integer result. The exceptional minimum, condition number, and stable rank follow with their stated constants and exclude invertibility only where necessary.

### Cofactor products, volume, and sums — VERIFIED

The operator norm of the adjugate equals the product of the largest `n-1` singular values also at rank deficiency, by continuity. The finite error inequality therefore holds without division by `M`. Its relative error is `O(|M|/W)=o(1)` and becomes exactly zero at every zero-Mertens index. Removing any fixed number of positive bottom axes gives the factors `n^((r-1)/2) product sqrt(lambda_j(L))` in the stated order. No growing collection of fixed-index equivalents is multiplied. Rank at least `n-1` licenses every division, and removing the largest axis gives `sqrt(c_0)W`.

The exterior-volume interpretation agrees with the Gram determinant of an orthonormal tuple. The second sum is exactly Frobenius squared. For the first sum, Cauchy–Schwarz is applied only to the `2k+1` nonunit axes, with squared total `n+Q-2+(2k+1)`, and the trace supplies the lower bound `n`. Using the parent estimate with exponent `2H` yields the stated error. In the upper-band second moment, the unit band and largest singular value each contribute `n+o(n)`, and the bottom band is `o(n)`, leaving `c_0 n`. Fixed-index bounds also bound any fixed number of selected upper-band terms by `O(n/log n)`.

### Geometric residual and fixed-power profile — VERIFIED

The unit triangular minor fixes the sign normalization of the maximal-minor vector. Cauchy–Binet gives base volume `sqrt(Q)`; projection onto the one-dimensional kernel gives height `|M|/sqrt(Q)`. The signless-Laplacian conjugation is restricted correctly to squarefree coordinates, and the regularized inverse weights give an upper bound decreasing to the exact residual.

Deleting edges partitions squarefree vertices by their squarefree smooth part. Each signed component sum is **`mu(a)R(n/a,y)`**. This sign is essential in the variance identity and is present. Kernel projection, the weighted variance identity, monotonicity under splitting, and the `4n/y` plateau deficit are correct, including singleton components.

The squarefree smooth density follows by a dominated square-divisor expansion. Harmonic root measures converge by partial summation, with the atom at 1 tending to zero. The signed rough recurrence is exact by the least-prime decomposition; the induction uses parameters at most `v-1`. Under prime partial summation the weight `dp/(p(log p)^2)` becomes `-dw/log x`, giving exactly the displayed recurrence for `rho'`, with no missing factor. The endpoint strip is bounded before removing it, and squareful rough terms are negligible uniformly on the fixed compact ranges.

Singleton roots contribute the indispensable `c_0 rho(u)` term. The other roots contribute the stated convolution with `rho'(v)^2/omega(v)`; the summed uniform error and the `v=1` strip are controlled. The same partition argument with component masses gives the identity used for the plateau. The lower bound `omega>=1/2` and `|rho'(v)|<=1/v` give an integrable majorant for the convolution, so `J(u)->0`. The formulas for `2<=u<=3` and the quadratic expansion at 2 check algebraically. Monotonicity proves both directions of the arbitrary-threshold cutoff using only fixed-parameter limits. The fixed-threshold equivalence and matching bound also check; the text correctly does not turn the matching bound into a lower bound for the residual.

### Halász application — VERIFIED conditional on the supplied inequality

The phase/Euler-product comparison has errors uniform in the imaginary part: prime powers, exponent replacement, and the prime tail each cost `O(1)`. The elementary zeta bound in the half-plane of absolute convergence suffices for the two frequency ranges and the `1/8 log log x` distance estimate. The loss from small-prime zero values of `f_y` is at most `log log y+O(1)` with the correct sign.

For `y=(log n)^alpha`, `alpha<1`, the primorial bound places **every** root in `a<=n^(o(1))`, so `x=n/a>=sqrt(n)` uniformly. The chosen `T` is admissible, and the exponent `delta=min(c_H/16,1/4)` absorbs the distance loss. Inclusion–exclusion followed by removing prime squares gives a uniform denominator lower bound. Summing over root divisors introduces exactly one further `log y`, yielding the squared logarithmic factor. The slower threshold and `T=log log n` similarly give the second rate. The concluding disclaimer correctly identifies where arithmetic cancellation entered.

### Added full-inverse corollary — VERIFIED

During review the coordinator added `spec:inversefrob`; I read and checked the complete new statement and proof. Each squarefree row contains exactly its ancestor-chain entries, giving the asserted Frobenius bound. The relative remainder is `O(|M| sqrt(log n)/W)=o(1)` under the supplied scales, so both inverse norms are asymptotic to the same rank-one norm and its stable rank tends to one. Operator-norm perturbation of each normalized inverse Gram matrix from a rank-one projection gives convergence of its top eigendirection: explicitly, if the error is at most epsilon, a top unit eigenvector has squared overlap at least `1-2 epsilon` with that direction. The isolated limiting eigenvalue also gives eventual simplicity. Inverting swaps the left/right singular vectors, yielding the stated right direction `muvec/sqrt(Q)` and left direction `w/W` for the minimum of `B`, up to signs. This new corollary is covered by the verdict.

## Minimal exposition fixes, not theorem defects

1. The originally reviewed `spectral.tex:192` used undefined `omega(k)` for the number of distinct prime factors. The coordinator independently replaced it during this review by an explicit prime count. **Resolved; no remaining action.** The ancestor count and tail proof were already correct.
2. `geometry.tex:54` writes `min_z` without its explicit ambient dimension. For the requested fully explicit presentation, write `z in R^(n-|A(n,y)|)`: the forest has `Q-|A|` retained squarefree edge rows and `n-Q` nonsquarefree diagonal rows. This is a notation clarification, not a projection-direction defect.

No mathematical repair is required by this audit. Neither suggestion is a proven refutation or an unsupported load-bearing step. The verdict does not cover unassigned introduction/discussion claims, bibliography accuracy, release readiness, or novelty.

## Reviewed revision fingerprints (SHA-256)

The first complete pass used the following revisions. During the audit the coordinator made minor definition/notation and cross-reference repairs and added the corollary checked above. The later observed hashes for those changed files are `a16a237ef7b331b168e505b8b8422eee829f916bca5abe72b77d1a9faaca3f62` (`main.tex`), `8c7a673139f445827962d2c346e1bd24c2f9ccf02be58451727b00c8c1deb6fd` (`definitions.tex`), and `91ee3c0aedf3b78dd85c5a7602f40dd08c855ee174fb5d2b6c49d62407b4eb00` (`spectral.tex`). The substantive new corollary was rechecked; the other minor changes were identified by the coordinator and targeted reads, not a second full proof pass. The other three section hashes remained unchanged.

```text
4c4262f98c7dfd55f3f29ab155c41d62f45d60d012d8728e3bc63fc7c4ff1f37  paper/main.tex
d38ef3c1a2c799141072ddde50dd1463450f7afacaa6494c20ea2aa2ed87098d  paper/sections/definitions.tex
6e61ea9c9211bce51a3166f9c907617ee3b14b96adcfc38f3a2eeaa38b5ae515  paper/sections/spectral.tex
3dd3be16cee97592390fabae956b156046101f47e3671108656421bd5d8c05b1  paper/sections/volumes.tex
443e737b7128c88a78d5ec9bf365f8aafa612c2f9e9cac3dd92013227034f2cd  paper/sections/geometry.tex
cdfade640175f1830a4cf060445b0436eef5eb496ff20a86d7fb6668108bc8c1  paper/sections/halasz.tex
```
