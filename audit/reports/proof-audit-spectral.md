# Proof and parameter audit: linear algebra and spectral content (Sections 2, 4, 5)

Date: 2026-09-27. Auditor: an AI agent (Claude) working in a separate context. This is process evidence only. It is not independent expert review or peer review.

## Audited files (working tree, SHA-256 via `shasum -a 256`)

| File | SHA-256 | Role |
|---|---|---|
| paper/sections/definitions.tex | 51fd60d6bc4a4eab4deb7b6d2ee1451781249aef6ec593474fe8d32a877701ae | audited (uncommitted modifications present, `M` in git status) |
| paper/sections/spectral.tex | a121b4f59561d4b0f9aa3a37043bf7852f59b610582b4841ef4258f5f6d93d85 | audited |
| paper/sections/volumes.tex | 3dd3be16cee97592390fabae956b156046101f47e3671108656421bd5d8c05b1 | audited |
| paper/sections/introduction.tex | bb0561656ef28f863d344ef48ff218cc299d90b90de27dbcde6ae7e8d57021a7 | context only (uncommitted modifications present) |
| paper/sections/arithmetic.tex | 27840a2947ad3d276f519327e90658a6117201f0d4ad247ce67678271545efe7 | context only; `arith:energy` and `arith:mertens` taken as inputs |

Git state at start: branch `main`; modified: README.md, paper/main.pdf, paper/main.tex, paper/sections/{definitions,discussion,geometry,introduction,references}.tex, scripts/check_paper.py; untracked: CITATION.cff, CORRECTIONS.md, LICENSE, audit/RELEASE-PLAN.md. I changed nothing except this report file.

Standard applied: https://jeff-kline.github.io/posts/research-program/index.html. Claims should not be stated more strongly than their proofs allow, and model agreement is not described as peer review.

## Verdict: PASS

I re-derived every statement in the lane from the definitions and found no proof defect. No claimed statement is false or unsupported, given the two arithmetic inputs (`arith:energy`, `arith:mertens`) that another lane audits. There is one must-fix exposition item: a remark in volumes.tex whose literal grammatical reading is false. There are also several optional notation and cross-reference items.

## Re-derivations (summary of what was checked)

**Section 2 (definitions.tex)**
- Proposition `def:inverse` (l.83-112). $(S^r)_{ij}=1$ iff $j$ is the $r$-step ancestor of $i$, and $i/j$ is then a product of $r$ distinct primes, so $\sum_r(-S)^r$ gives $\mu(i/j)$. Nonsquarefree vertices are isolated. The matrix determinant lemma gives $\det B=1+u^TCe_1=M(n)$. Sherman-Morrison gives the inverse. Adjugate: $\det(A+te_1u^T)=1+t(M(n)-1)$ is affine in $t$ with constant term 1, so it vanishes for at most one $t$. Off that $t$, adj $=\delta(t)C-t\mu w^T$. Both sides are polynomial in $t$, so the identity extends to all $t$. Correct.
- Proposition `def:wnorm` (l.114-131). $(w_n)_j$ is the column-$j$ sum of $C$ over rows $2..n$. The descendant parametrisation $jd$ with $P^-(d)>P^+(j)$ gives $R(n/j,P^+(j))$. The norm identity follows by summing squares. Correct.
- (def:orthocolumns) and (def:frobenius). Each row of $S$ has at most one 1, so the column supports are disjoint. The number of edges is $Q(n)-1$. $\|B\|_F^2=n+(n-1)+(Q-1)$. $\operatorname{tr}B=n$. Correct.
- Worked example $n=6$ (l.59-63): $w_6=(-2,0,1,1,1,1)$ verified by hand and numerically.

**Section 4 (spectral.tex)**
- Theorem `spec:core`. The leaf-child argument holds: a child $apq$ of $ap$ would need a prime $q>p$ with $q\le n/(ap)<n/a$, which contradicts the maximality of $p$. Since $F$ has disjoint nonempty column supports, it has full column rank. $V=E\oplus\operatorname{range}F$ reduces $A$ because $S^T$ maps into $E$, $S$ kills $E^\perp$, and $U\perp\operatorname{range}S$. Gram displacement block $[[T_0,R],[R,0]]$: the substitution $y'=y+\tfrac12R^{-1}T_0x$ is exact because $R$ is diagonal and invertible, so the inertia is $(k,k,0)$. Bordered case: $\one=b+z$ with $z=\mathrm{proj}_U\one$. The Schur complement of $\rho^2$ is $(A^TA-I)|_V-e_1e_1^T$, and $e_1\in E$, so Sylvester's law of inertia gives $(k+1,k,0)$. $V_B^\perp=U\cap\one^\perp$, and $(B-I)$ and $(B-I)^T$ vanish there. Correct. **The condition $n\ge4$ is used only through $e_4\in U$, and it is sharp.** Numerically, $n=3$ gives $B$-counts $(1,1,1)$ against the formula's $(2,1,0)$, and $n=2$ gives $(1,1,0)$. The parent bound via Rankin with $y=(\log n)^H$ and $H(1-\alpha)<1$ is correct.
- Theorem `spec:upper`. Weyl's inequality with $\|I\|=1$ is correct. For $T=\sqrt n e_1h^T+SP$: $SP$ maps $h^\perp$ into $\operatorname{range}S\subset e_1^\perp$, which gives the orthogonal block structure. $\|S\|=\sqrt{\pi(n)}$ because $d_1=\pi(n)$ is the maximal degree. $B-T=(I-e_1e_1^T)+Shh^T$, so the norm is at most $1+\eta$. Then $\|SP-S\|=\eta$ and $\eta<1$, giving the bound $1+2\eta<3$. Sorted-degree limits: the operator-norm convergence of the diagonal operators (Chebyshev for $J<a\le\sqrt n$, trivial for $a>\sqrt n$) justifies taking the sorted eigenvalues. Correct.
- Theorem `spec:compact`. $(C^TC)_{jk}=\mu(k/j)D_k(n)$ for $j\preceq k$ holds because ancestors form a chain and $\mu(i/j)\mu(i/k)=\mu(k/j)$. The density $\prod_{p\le y}(1-1/p)\prod_{p>y}(1-p^{-2})=c_0\prod_{p\le y}p/(p+1)$ checks. The HS tail bound $2(1+\log_2k)/k^2$ (ancestors $\le1+\log_2k$, entries $\le1/k$) holds uniformly in $n$. The nonsquarefree diagonal contributes $\le1/n$. Positivity passes to the limit. Infinite rank follows from the prime compression $\operatorname{diag}(\delta_p)$. Correct.
- Lemma `spec:escape`. The identity $R(x,y)=\sum_{P^+(b)\le y}M(x/b)$ holds (Euler-factor cancellation, as a finite coefficient identity). The split at $\sqrt x$ is valid: $x/b\ge\sqrt x$ gives the $7/12$-bound with a changed constant, and the tail is $O_y(x^{3/4})$. $s(n)=o((\log n)^{7/12})$, so each fixed coordinate of $w_n$ is $o(W_n)$. This uses only the lower bound $W_n\ge n e^{-(1+\varepsilon)s}$ from `arith:energy`. $J_n=G_n-(G_ne_1)(G_ne_1)^T/(G_n)_{11}$ checks with $(G_n)_{11}=Q/n$. $\|P_vJP_v-J\|\le3\|Jv\|$ holds. $L$ has infinite rank via a rank-one subtraction on prime compressions. Correct.
- Lemma `spec:deflation`. I verified the block elimination product by direct multiplication. The multiplier norms $\le1+C/|z_n|$ and the two-sided multiplicative singular-value bounds are correct, and the lower block is uniformly bounded, so the absolute error is $o(1)$. The use of bounded $\|D_n\|$ (from Theorem `spec:compact`) is sufficient.
- Theorem `spec:bottom`. $t_n=\sqrt Q\,W_n/(M\sqrt n)$ and $|t_n|\to\infty$ because $W_n/|M(n)|\to\infty$ (the inputs). At $M(n)=0$ the identities $B\mu=M e_1=0$, $w^TB=u^T+(M-1)u^T=0$ and $BC=I+e_1w^T$ all check. $BP_aCP_v=BCP_v=P_v+e_1w^TP_v=P_v$. The Moore-Penrose characterisation (range $\subset a^\perp$, zero on $v$, $BX=P_v$, and $B$ injective on $a^\perp$) determines $X$ uniquely. The two subsequences share the same limit. $\sigma_{n-r}$ ordering: the $(r+1)$th largest singular value of $B^{-1}$ is $1/\sigma_{n-r}$. Correct.
- Theorem `spec:minimum`. The reverse triangle inequality gives relative error $O(\sqrt n|M|/(\sqrt QW))=O(|M|/W)$. $\kappa_2\sim\sqrt n\cdot\sqrt{c_0n}\,W/|M|$. Stable rank $(2n+Q-2)/(n+O(\sqrt n))\to2+c_0$. Correct.
- Corollary `spec:inversefrob`. $\|C_n\|_F^2\le n(1+\log_2n)$. Relative size $O(|M|\sqrt{\log n}/W)$. The left/right assignment is consistent: the top left singular vector of $B^{-1}$ approximates $a_n$, which is the right singular vector of $B$ for $\sigma_n$. Correct.

**Section 5 (volumes.tex)**
- $\|\operatorname{adj}T\|=\prod_{i\le n-1}\sigma_i$, which gives (vol:finite). The codimension product divides by $\sigma_{n-1},\dots,\sigma_{n-r+1}>0$ (rank $\ge n-1$) and has exponent $n^{(r-1)/2}$. (vol:middle) divides by $\sigma_1\sim\sqrt n$. Correct.
- Sums: $n-r_n$ unit values with $r_n=2k_n+1$. The complement squared-sum is $n+Q-2+r_n$. Cauchy-Schwarz with $k_n=O(n/(\log n)^{2H})$ gives an $O(n/(\log n)^H)$ error. The trace lower bound $\sum\sigma_i\ge n$ holds. Band: $2n+Q-2-(n+O(\sqrt n))-(n-2k-1)-O(k)=Q+o(n)$. Correct.

## Numerical falsification attempts (none falsified; not proof)

Script: `scratch script `audit_spec.py` (local path redacted; not included in this release)` (plus `audit2.py`), run with `~/.venvs/claude/bin/python`; 871 checks, 0 failures; about 73 s.
- Exact integer checks for $n=2..59$, 97, 210, 331: $A C=I$ with the closed-form $C$; $Ce_1=\mu$; the $w_n$ coordinates against direct $R(n/j,P^+(j))$; the $W_n^2$ identity; $B\,\operatorname{adj}=\operatorname{adj}B=M(n)I$ with adj $=MC-\mu w^T$ (including $M(2)=M(39)=M(40)=M(58)=0$); $\det B=M(n)$ (exact Fraction elimination for $n\le12$); the degrees, $\sum d_j=Q-1$, $S^TS=\operatorname{diag}(d)$, and the Frobenius and trace identities.
- Floating SVD for $n\in\{2..8,10,12,30,64,100,210,500,997,1000,1500,2000\}$ and the zero-Mertens indices 39, 40, 58, 65, 93, 101, 1866, 1929, 1938. Results:
  - Unit, above-one and below-one counts are exactly $(k+1,k,n-2k-1)$ for all $n\ge4$ tested, and $(k,k,n-2k)$ for $A$. The minimum distance of a nonunit value from 1 is about 0.16-0.21, so the result is not a tolerance artefact.
  - Bounds (spec:Adegree) and (spec:Bdegree), and $|\sigma_1-\sqrt n|\le1+\eta$, hold.
  - $\prod_{i\le n-1}\sigma_i=\|\operatorname{adj}B\|$ to $10^{-7}$ relative accuracy, and (vol:finite) holds.
  - $\sum\sigma_i^2=2n+Q-2$ and $\sum\sigma_i\ge n$.
  - $B^\dagger=P_aCP_v$ at every zero-Mertens index tested.
- Trends at $n=2000$: $\sigma_n/(|M|/(\sqrt QW))=1.005$; stable rank 2.603 against $2+c_0=2.608$; $\|C_n\|/\sqrt n\approx0.849$. $\sqrt n\,\sigma_{n-r}$ for $r=1..4$ is $2.48, 3.51, 4.78, 4.95$, against $\lambda_r(J_n)^{-1/2}=2.43, 3.51, 4.75, 4.95$ and $1/s_r(P_aD_nP_v)=2.48, 3.51, 4.78, 4.95$. Zero-Mertens indices near 1900 give the same values, which is consistent with the all-integer claim. The corollary overlaps are $|\langle v_{\min},a_n\rangle|=0.99998$ and $|\langle u_{\min},v_n\rangle|=0.9992$.
- Observation, not a defect: the weak escape of $v_n$ is numerically very slow. At $n=2000$ the first few coordinates of $v_n$ are still about 0.1-0.4, and $\|J_nv_n\|\approx0.036$ has not visibly decreased from $n=500$. This fits $W_n/n=e^{-(1+o(1))s(n)}$ decaying only sub-polynomially. It implies nothing about the proof, but numerical agreement at $n\le2000$ should not be cited as evidence for the rate.

## Findings

| # | Severity | Evidence (file:line) | Issue | Disposition |
|---|---|---|---|---|
| 1 | must-fix exposition | volumes.tex:68 | "In particular the empirical proportion of singular values different from one tends to zero, and their ordinary average tends to one, but their mean square tends to $2+c_0$." Grammatically, "their" refers to the singular values *different from one*. Under that reading the claims are false: the average of the $2k_n+1$ nonunit values is not shown to tend to 1, and their mean square is about $(n+Q)/(2k_n)\to\infty$. The intended statement is about all $n$ singular values, for which it is correct by (vol:first) and (vol:second). | Replace the sentence with: "In particular the proportion of singular values different from one tends to zero, and the average of all $n$ singular values tends to one, while the average of their squares tends to $2+c_0$." |
| 2 | optional | spectral.tex:243, 252 | The constant $c'$ is never defined. (arith:mertens) uses $c$. It is $c\,2^{-7/12}$ because $\log(x/b)\ge\frac12\log x$. | Add "with $c'=2^{-7/12}c$, since $\log(x/b)\ge\tfrac12\log x$". |
| 3 | optional | volumes.tex:22 | "$L$ is the compact operator of Theorem~\ref{spec:bottom}". $L$ is defined in (spec:Ldefinition) and Lemma `spec:escape`, and is only used in `spec:bottom`. | Point to \eqref{spec:Ldefinition}. |
| 4 | optional | spectral.tex:404, 411 | "Eventual simplicity of the exceptional singular value" is proved but not stated, and the directional claim implicitly needs it. | Add "and $\sigma_n(B_n)$ is eventually simple" to the corollary statement. |
| 5 | optional | spectral.tex:23-37 vs definitions.tex:21-27, 36; spectral.tex:218; spectral.tex:285; arithmetic.tex:9 vs spectral.tex:210 | Symbol overloading. $E$ is the energy, the subspace and the block $E_n$. $R$ is the signed count $R(x,y)$ and the diagonal block. $D$ is the block, $D_n=C_n/\sqrt n$, and $D_j(n)$ (descendants). $C$ is the lemma constant, the Chebyshev constant and $C_n$. $L$ is $\log n$ in Section 3 and the operator in Section 4. $a_n$ against $a_r$ is already flagged at l.222. None of these creates a logical error in context. | Optionally rename the blocks in the proof of `spec:core` (e.g. $\mathcal E$, $\Delta$, $\Lambda$) and the operator $L$ (e.g. $K^\flat$ or $\mathcal L$). |
| 6 | optional | definitions.tex:79 and spectral.tex:7; definitions.tex:74-78 and spectral.tex:212-216; definitions.tex:43 and spectral.tex:7, 72 | "Reduces", $\mathsf P_z$, $k_n$, the sorted degrees and $Q(n)$ are each defined twice, consistently. | Optionally replace the repeats with back-references. |
| 7 | optional | spectral.tex:208 | "Define the positive compact operator $L$" asserts positivity before Lemma `spec:escape` proves it. | "Define the operator $L$ ... (positive and compact by Lemma~\ref{spec:escape})". |
| 8 | optional | spectral.tex:10; introduction.tex:37 | The hypothesis $n\ge4$ is sharp: $n=3$ has $B$-counts $(1,1,1)$, not $(2,1,0)$. A reader may wonder whether it is merely convenient. | Optionally add "(the counts differ for $n=2,3$, where $\one\in V$)". |

No must-fix proof defects.

## Dependencies recorded
- `spec:escape`, `spec:bottom` ($|t_n|\to\infty$), `spec:minimum`, `spec:inversefrob` and `vol:product` all rely on $|M(n)|/W_n\to0$ (and, for escape, fixed coordinates $=o(W_n)$). These need only the **lower** bound $W_n\ge n\exp(-(1+\varepsilon)s(n))$ from `arith:energy` together with (arith:mertens). If the arithmetic lane weakens `arith:energy`, these results survive exactly as long as $W_n\ge n\exp(-o((\log n)^{7/12}))$ still holds.
- `spec:upper` fixed-index asymptotics use the prime number theorem and Chebyshev. `spec:core` is unconditional and elementary.
