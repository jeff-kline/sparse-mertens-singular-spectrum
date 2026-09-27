# Proof and parameter audit: arithmetic lane (Sections 3, 6, Appendix A, Section 7.1)

Date: 2026-09-27. Auditor: AI agent (Claude), process-separated from the drafting session. This is process evidence only. It is not independent expert review or peer review.

## Audited files (working tree, SHA-256)

| File | SHA-256 |
|---|---|
| paper/sections/arithmetic.tex | 27840a2947ad3d276f519327e90658a6117201f0d4ad247ce67678271545efe7 |
| paper/sections/geometry.tex | efec2c0346c55508d04ea68e5084197afd3dd64fd25dc5f6876e6966743a4f20 |
| paper/sections/halasz.tex | cdfade640175f1830a4cf060445b0436eef5eb496ff20a86d7fb6668108bc8c1 |
| paper/sections/discussion.tex | 071a49464bb577facec21a7acac5e0803da55f5edbeea6b9bdf3ce274f6a7e7b |
| paper/sections/definitions.tex (consulted for definitions) | 51fd60d6bc4a4eab4deb7b6d2ee1451781249aef6ec593474fe8d32a877701ae |
| paper/sections/references.tex (consulted for citations) | db5ef6ff0d081fe55a0cfac85dacfc57e897f6059addb14bca9149a1503854a3 |
| paper/main.tex | 026efc91fb6cb58ef2c52ab7e0c8f541225991a521775e276087e785f495d390 |

HEAD at audit time: 6d8980ca9627d661346d3ccb8bc4064898fb892a. The working tree was being edited concurrently. discussion.tex was first read at hash c7d425f4…; the only change since then is one paragraph of Section 7.2 (the Alladi comparison). Section 7.1, the part audited here, is unchanged. references.tex also changed during the audit. The McNew, Tao, and Lee–Leong entries I checked were read before that change. I did not re-read them afterwards.

## Verdict: PASS

I found no must-fix proof defect and no must-fix exposition defect. Every step in the lane was checked line by line, including the load-bearing Lemma arith:bridge. Every classical input was checked against its cited source, and every one I could fetch is quoted correctly and used inside its stated range. The items below are optional. Two cited sources were not checked by me (Fan–Pomerance Theorem B and Alladi Theorem 1). Both are flagged as unverified; the results that use them do not depend on them alone.

## Sources checked (6 web operations)

- Research standard, https://jeff-kline.github.io/posts/research-program/index.html. Read; it requires that model agreement not be called peer review, and I follow that here.
- McNew author manuscript, https://www.nathanmcnew.com/PopularPrimes.pdf, downloaded and read as extracted text.
  - (7) is Hildebrand: Ψ = xρ(u)(1+O(log(u+1)/log y)) for exp((log log x)^{5/3+ε}) < y < x.
  - The unnumbered display before (13) is Saias: Ψ = Λ(1+O(exp(−(log y)^{3/5−ε}))) "in the same range as Hildebrand's result".
  - (13) is the Saias expansion Λ = x Σ_{j≤k} a_j ρ^{(j)}(u)/(log y)^j + O_{k,ε}(x ρ^{(k+1)}(u)/(log y)^{k+1}). It holds uniformly for x ≥ 2 and (log x)^{1+ε} < y ≤ x, provided (u−j)/(k+1−j) ≥ log log y/log y for 0 ≤ j ≤ min(k,u). The a_j are the Taylor coefficients of (s−1)ζ(s)/s at s = 1, with a_0 = 1 and a_1 = γ−1. I checked a_1 independently: (s−1)ζ(s) = 1+γ(s−1)+…, and 1/s = 1−(s−1)+….
  - The text between (13) and (14) gives ρ'' = O(log²(u+1)ρ(u)), citing Tenenbaum III.5 Cor. 8.3.
  - (14) is Ψ = x(ρ + (γ−1)ρ'/log y)(1+O((log(u+1)/log y)²)).
  - (17) is ρ(u−1)/ρ(u) = uξ(u)(1+O(1/u)).
  - The paper's restatement in arithmetic.tex:37-89 matches all of these. Its two boundary inequalities (lines 74-78) are exactly McNew's condition for k = 1, since log t/t = log log y/log y.
- Tao, 254A Notes 10, Theorem 7, fetched as HTML. The statement is: "Let X be sufficiently large. Then for any 1-bounded multiplicative function f, (1/X) Σ_{n≤X} f(n) ≪ exp(−c min_{|t|≤T} D(f, n ↦ n^{it}; X)²) + 1/T for an absolute constant c > 0 and any T > 0." Definition 5 gives D(f,g;X)² = Σ_{p≤X}(1 − Re f(p) conj g(p))/p. This matches halasz.tex:7-13 exactly.
- Lee–Leong, arXiv:2208.06141v5 (abstract and HTML). Theorem 1.1, eq. (12), is |M(x)| < 25.85 x (log x) exp(−(5/(3·53.99³)·(1−log 53.99/log log x)^{−1})^{1/5} (log x)^{3/5}(log log x)^{−1/5}) for x ≥ exp(e^{10.01}). This implies arithmetic.tex (arith:mertens) with the log factor absorbed, as the paper states.

## Exact falsification checks

Script: scratchpad `checks.py`, run with /Users/klinellc/.venvs/claude/bin/python in under 1 s, exact integer or Fraction arithmetic. All checks passed with 0 failures:

- (arith:convolutions), both forms, and the tail identity (arith:tail-exact), for x ∈ {97, 500, 1234, 3000}, y ∈ {2, 3, 7, 13, 31}, K ∈ {5, 10, 30}.
- The least-prime identity (arith:least-prime), the multiplier decomposition (arith:multiplier-decomposition), and the floor identity (arith:floor), for n ∈ {100, 777, 3000}.
- The variance identity (geo:variance) and the plateau bound (geo:plateaubound), for n ∈ {200, 1000, 3000} with several values of y.
- The explicit form (geo:explicitJ) against the definition (geo:J) at u = 2.3, 2.7, 3.0. Simpson quadrature agrees to about 5e-8. The partition identity (geo:partitionlimit) equals 1 to about 3e-9.
- ζ(2)/ζ(4) = 15/π² numerically.

These checks cover the finite identities only. At these sizes the asymptotic exponents cannot be observed, so I did not test or interpret them.

## Line-by-line results (proof content)

### Section 3, classical inputs (arithmetic.tex:17-107)
- The exponent change 3/5 → 7/12 (l.29-32) is correct: 3/5 − 7/12 = 1/60.
- The smooth input (l.37-48) is correctly specialized. In the range t ≍ s, v ≍ √(L/log L):
  - Hildebrand's range needs (log log z)^{5/3+ε} < t. It holds.
  - Saias needs (log z)^{1+ε} < y. It holds.
  - The two k = 1 conditions hold with a diverging margin.
  - The Ψ/Λ error exp(−(cs)^{3/5−ε}) is o(β²), where β² ≍ log L/L.
  - The conversion from multiplicative to additive remainder uses κ ≍ ρ, which follows from |ρ'|/(tρ) ≍ β = o(1). It is correct.
- (arith:dickman-input) follows from (17), McNew's ρ'' bound, and ξ(u) ~ log u. The last relation, log ρ = −(1+o(1))v log v, comes from integrating −ρ'/ρ = ξ(v)(1+O(1/v)).

### Lemma arith:upper-local (Rankin)
Correct.
- Below xe^{−h} the bound is e^{−cL^{21/40}+O(log L)}, which is e^{−ω(s)} because 21/40 > 1/2.
- The Rankin product has log O(log L + u) = o(s).
- αh ≍ L^{0.4} log L = o(s).
- α log x = u log u = (1/(2c)+o(1))s uniformly in c ∈ [c_−, c_+] and |log x − L| ≤ Ds. I verified this: log u = ½(1+o(1)) log L.
- The majorant claim holds, since the argument only uses |M| and a/x ≤ … bounds.

### Lemma arith:bridge (load-bearing)
Every step checks.
1. **Parameters.** β = log(u+1)/t ≍ √(log L/L). Arguments in [u − L^{9/10}/t, u] are (1−o(1))u, because (L^{9/10}/s)/u ≍ L^{−1/10}. Hence (arith:dickman-shift) holds.
2. **Tail identity (l.191-196).** Exact. The interchange gives Σ_{a≤x/K, P^+(a)≤y}(M(x/a) − M(K)), and the endpoint x/a = K contributes 0. This was also checked exactly.
3. **M(K) term.** |M(K)|·Ψ(x/K,y) ≤ CKe^{−c(log K)^{7/12}}·(x/K)ρ(u)e^{Cβ log K}(1+O(β)). The smooth input applies at z = x/K because log K = (log L)² ≤ L^{9/10}.
4. **Dyadic range K ≤ x/a < H.**
   - For each dyadic block, #a ≤ Ψ(x/q,y), with log q < L^{9/10}, so both the smooth input and the shift apply.
   - The absorption factor is β(log q)^{5/12} ≤ βL^{3/8} ≍ L^{−1/8}√(log L) = o(1). The paper's exponent −1/2 + (9/10)(5/12) is correct.
   - There are O(L) blocks, and (log K)^{7/6} ≫ log L.
   - The separate M(K) accounting is consistent: T_K = Σ M(x/a) − M(K)Ψ(x/K,y).
5. **x/a ≥ H.** The bound is x e^{−cL^{21/40}+O(log L)}. It is o(xρ(u)β) because |log ρ(u)| = O(s) = O(√(L log L)) and 21/40 > 1/2. The earlier bounds are also o(xρ(u)β), because (log L)^{7/6} ≫ |log β|.
6. **Taylor expansion (l.240-245).** Both remainder orders are right: h² sup|ρ''| ≪ ρ(u)β²(log k)² and h sup|ρ''|/t ≪ ρ(u)β² log k, where h = log k/t. The sup is controlled by monotonicity of ρ and the shift, with e^{Cβ log K} = O(1). The sum Σ_{k≤K}(1+log k)²/k ≪ (1+log K)³ is correct.
7. **Short expansion (arith:short-expansion).** Signs and coefficients are correct.
8. **Möbius moments.** Partial summation gives tails of size poly(log K)·e^{−c(log K)^{7/12}}. Abelian continuity of the convergent Dirichlet series as σ ↓ 1 gives Σμ(k)/k = 0 and Σμ(k)log k/k = −1: the derivative of 1/ζ is −ζ'/ζ², and ζ'/ζ² → −1. The paper's values 0 and −1 are correct.
9. **Assembly.** The −(xρ'/t)A_1 term gives xρ'(u)/t(1+o(1)). The remaining terms are small relative to it:
   - xρA_0 = O(xρ e^{−c(log L)^{7/6}}) = o(xρβ);
   - (γ−1)(xρ'/t)A_0 = o(xρ'/t);
   - the error term is O(xρβ²(log L)^6) = o(xρβ), using |ρ'|/t ≍ ρβ.
   The resulting relative error is O(β(log L)^6) + o(1). The result is uniform, and the sign is negative.
10. **Consistency.** The sign and main term agree with the fixed-v asymptotic (geo:signedfixed), R ≈ xρ'(v)/log y. The remark at l.277-279 is correct: a first-order O(β) relative error would swamp the surviving term.

### Theorem arith:moments
Correct.
- Bin cost: (q−1)a + q/(2b). f_q has minimum √(2q(q−1)) at c_q = √(q/(2(q−1))).
- Small primes: the majorant has monotone y, and the Lemma applies at x = n/p, y_0 = e^{c_− s} with D = c_−. The prime sum Σp^{−q} converges.
- Large primes: the trivial bound |R| ≤ x for x ≥ 1 suffices.
- Order of limits: endpoints and mesh are fixed first, then n → ∞. This is correct.
- Maximum: cost c + 1/(2c), with minimum √2 at 1/√2. No limit q → ∞ is used.
- Lower bound: block law via the bridge plus log|ρ'| = log ρ + O(log log u). Then (q−1)c + q/(2c) at c_q.
- Concentration: at q = 2 the cost is c + 1/c with a unique minimum at c = 1. The remote costs are 1/c_− and c_+.
- The claim "no assertion uniform in varying q" (l.363) is accurate.

### Theorem arith:energy
Correct.
- Multiplier decomposition j = ap with p = P^+(j): exact and checked.
- Tail a > A = e^{3s}: O(n²e^{−3s}) = o(E_P).
- Floor identity: exact.
- s(N_a)/s → 1 uniformly and min N_a → ∞, so concentration at N_a with δ = 1/3 gives n²e^{−(2+η/2)s}ζ(2) = o(E_P).
- Central range: the bridge applies at (n/(ap),p) with D = 5 and c ∈ [1/2, 2].
- Ratio (arith:multiplier-ratio): correct. Because u − v ≤ 6 and |(log(−ρ'))'| ≪ log, we get |ρ'(v)/ρ'(u)| ≤ a^{O(β)} = a^{o(1)}. This gives the domination a^{−2+ε}, uniform in n.
- Pointwise limit: μ(a)²/a², because the central prime energy is (1−o(1))E_P.
- Dominated convergence gives Σμ(a)²/a² = ζ(2)/ζ(4) = 15/π².
- (M(n)−1)² = o(E_P) because L^{7/12}/s → ∞. n − Q = o(E_P). W_n then follows.

### Theorem arith:sparse and Corollary arith:exceptional
- Hölder saving √(2θ) − κθ, optimized at θ = 1/(2κ²) < 1 exactly when κ > 1/√2, gives 1/(2κ). The two branches agree at 1/√2.
- For κ < 1/√2, the lower construction has enough primes in [e^{s/√2}, 2e^{s/√2}], since e^{κs} = o(e^{s/√2}/s). All coefficients have the same sign by the bridge.
- For κ ≥ 1/√2, the block count e^{κs}/(κs) ≤ ⌊e^{κs}⌋.
- Corollary: the minimizer q = (1+λ/r)/2 with r = √(λ²−2) gives value (λ+r)/2. I verified this algebraically: 2q(q−1) = 1/r².
- The lower root argument is correct. At λ = √2 the Markov cost √2/(1+√(1−1/q)) decreases to 1/√2, and only the upper bound is claimed.

### Theorem arith:thin-series
Correct.
- T(x) = −Σa_p b_p(x), with support ≤ ⌊e^{κs(x)}⌋ at integers.
- The integral bound uses dv/dz = 2z/(log v+1) ≤ 2z.
- The partial-summation tail is right.
- Euler-product grouping for σ > 1 is correct, including the product over q ≤ p.
- N_S(x) ≤ x^{1/2} gives Σ log(2p)/p < ∞, which dominates the prime sum while 1/ζ(σ) → 0.
- Dominated convergence of σ∫T(t)t^{−σ−1}dt identifies the value 0.
- The smaller-support case is correct.

### Section 6 (geometry.tex)
- **Projection and variance.** Correct. The kernel vector on each component is μ(ad) = μ(a)μ(d). The row count n − |A|, the variance expansion, and the monotonicity via Cauchy–Schwarz are correct. In the plateau case N − S²/N = 4 − 4/N ∈ [0,4), and at most n/q_1 roots are nonsingletons. All of this was checked exactly.
- **geo:signedfixed induction.** Correct.
  - Base: R = 1 − π(x) + π(y) with coefficient −1/v = ρ'(v) on (1,2].
  - The least-prime identity is correct.
  - The strip bound is O(εx/log x).
  - PNT partial summation with λ = 1/(w+1) gives dλ/λ² = −dw, so the leading term is (x/log x)∫_1^{v−1}r.
  - The recurrence vr(v) = −1 − ∫_1^{v−1}r is solved by ρ', since ∫_1^{v−1}ρ' = ρ(v−1) − 1.
  - The limit order is x → ∞ first, then ε ↓ 0. This is correct.
- **Profile J(u).** Correct.
  - The squarefree-smooth limit and the weak convergence of ν_Y (partial summation, dominated by 1) are right.
  - Singletons give c_0nρ(u).
  - The central sum uses a continuous g and an atomless limit.
  - The strip contributes O(εn).
  - The bound ω ≥ 1/2 by induction gives g ≤ 2/v², so dominated convergence gives J → 0.
- **Explicit J on [2,3].** Correct. ρ' = (log(v−1) − 1)/v and ω = (1+log(v−1))/v. Also ω − g = 4ℓ/(v(1+ℓ)), which is 2(v−2) + O((v−2)²), so J(2+h) = 1 − h² + O(h³). Checked numerically.
- **Cutoff equivalence.** Correct. Monotonicity in y plus J(U) → 0 gives one direction. J(1/δ) > 0 along a subsequence gives the other.
- **Fixed threshold and matching.** Correct.

### Appendix A (halasz.tex)
- The imported form (app:H) matches Tao's Theorem 7 verbatim, including "X sufficiently large", "any T > 0", and absolute c.
- (app:phase) has three error terms, each O(1) uniformly in v.
- The ζ bound for 1 < σ ≤ 2 is right: |ζ| ≪ 1 + |v| + 1/|v|.
- The inequality 1 − cos 2v = 2(1−cos v)(1+cos v) ≤ 4(1+cos v) is right.
- Small |t|: (1+cos 1)/2 > 1/8.
- Distance: D(f_y,t;x)² = E(t;x) − Σ_{p≤y}cos(t log p)/p is exact.
- With y = (log n)^α, exp(−c_H D²) ≪ (log n)^{−c_H/8}(log log n)^{c_H} ≤ (log n)^{−c_H/16}, and T = (log n)^{1/4} ≤ √(log x) since x ≥ √n. So δ = min(c_H/16, 1/4) is correct.
- P_y ≤ y^y = n^{o(1)}.
- Denominator: Φ_sf ≫ x/log y.
- Final sum: Π(1+1/p) ≪ log y.
- The slow-rate case (y = T = log log n) is also correct.

### Section 7.1 (discussion.tex:5-37)
Every implication is correct, and none is overstated.
- Certificate: M(n) = μ^T(1 − H^Tz), and Cauchy–Schwarz with ‖μ‖² = Q gives |M| ≤ nε.
- Component certificate: via M²/Q ≤ F.
- Resolvent certificate: via h² = M²/Q ≤ τ1^T(G+τI)^{−1}1.
- The claims that F(n,n^{1/u}) ~ c_0nJ(u) cannot certify ε → 0, that a(n)/V(n) → ∞ would be an improvement, and that o(n) proofs are not improvements are all accurate. No stronger claim is made.

## Findings table

| # | Severity | Evidence | Finding | Suggested disposition |
|---|---|---|---|---|
| 1 | optional | arithmetic.tex:59-62, 82-83; references.tex mcnew entry | The Saias Ψ/Λ relative error exp(−(log y)^{3/5−ε}), used at l.82 ("the exponentially small relative error in the Saias estimate"), is an unnumbered display in McNew placed just before (13). It is not among the cited (7), (13), (14), (17). McNew's (14) asserts "the same range as (7)" without checking the (13) side conditions, but the paper checks them itself (l.74-81), which is correct. | Add "and the unnumbered Ψ/Λ comparison preceding (13)" to the McNew citation list. |
| 2 | optional | arithmetic.tex:59-60 | The text says McNew "records ... the derivative estimates" and cites (17). (17) is the ratio ρ(u−1)/ρ(u) = uξ(u)(1+O(1/u)). The ρ'' bound is in McNew's text (quoting Tenenbaum III.5 Cor. 8.3), and −ρ'/ρ ≍ log also needs ξ(u) ~ log u from McNew (11). | Cite "(11), (17) and the ρ'' bound following (13)". |
| 3 | optional | arithmetic.tex:49 | "uniformly as v → ∞" is redundant for single-variable asymptotics. | Replace with "as v → ∞". |
| 4 | optional | halasz.tex:9 | The paper calls (app:H) a "weakened quantitative form". It is exactly Tao's Theorem 7. It is weaker only relative to the (1+M)e^{−M} form of Montgomery–Tenenbaum and Granville–Harper–Soundararajan. | Consider "the following quantitative form of Halász's theorem, as stated in ...". |
| 5 | optional (unverified source) | geometry.tex:85 | I did not fetch Fan–Pomerance Theorem B, cited for Φ(x,y) = (x/log y)(ω(v)+o(1)) uniformly on compact v ⊂ [2,∞). The statement itself is the classical Buchstab–de Bruijn asymptotic, as in Tenenbaum III.6, so it is correct as stated. | Optionally add Tenenbaum (Part III, Ch. 6) as a second source. |
| 6 | optional (unverified source) | geometry.tex:127 | The attribution of the main term of (geo:signedfixed) to Alladi Theorem 1 was not checked; introduction.tex:77 says those pages were inaccessible. The paper proves the statement independently, and I verified that proof. | None required. Keep the independent proof. |
| 7 | optional | arithmetic.tex:271-274 | The relative error in (arith:rough-asymptotic) is effectively O(β(log L)^6) + O(e^{−c(log L)^{7/6}}/β). Stating this would make the o(1) quantitative at no cost. | Optional remark. |
| 8 | optional | geometry.tex:135 | "Chebyshev and partial summation, or the prime number theorem" for the strip: the bound on Σ1/p over [x^{1/(2+ε)}, x^{1/2}] uses Mertens' second theorem (elementary). The leading-term integral uses the PNT, which the section already imports. | None required. |

No finding has severity must-fix. For the load-bearing Lemma arith:bridge, I checked every truncation parameter (K, H, a_0), every exponent comparison (21/40 vs 1/2; 3/8 vs 1/2; (log L)^{7/6} vs log L), and the range of the smooth-number input against the source ranges. All hold with a margin.

## Limits of this audit
- Numerics were limited to exact finite identities and one quadrature check of J. Asymptotic claims were verified by reading the proofs, not by computation.
- Fan–Pomerance, Alladi, and Saias's original paper were not read. Saias was checked only through McNew's quotation, as references.tex itself states.
- Lee–Leong was checked only at Theorem 1.1, eq. (12).
