# PAPER proof and editorial audit

STAGE: PROOF-AUDIT
VERDICT: VERIFIED for P1--P4 and the certificate implications, relative to the explicitly accepted baseline; GAP in one broader prose assertion about growing u, repaired by the wording below. The whole proposed section should not be called unconditionally verified until that sentence is narrowed.
CLAIM: The local section paper-section-proposal.tex explains sufficient routes to a stronger Mertens estimate without claiming to supply the new cancellation input. This is not a priority survey or a fresh audit of all analytic results in the manuscript.

EVIDENCE:
1. P1: The displayed identity M=mu^T(1-H^Tz) follows from H mu=0. Cauchy--Schwarz gives M^2<=Q||1-H^Tz||^2<=n^2 epsilon^2. No nonzero-Mertens restriction is needed. The least-squares warning agrees with geo:height, whose proof uses the one-dimensional kernel and full row rank.
2. P2 component route: geo:variance has exactly M^2/Q plus a nonnegative sum. Its denominators are positive component sizes and sum to Q, while the signed component sums sum to M. The proposal preserves the normalization and sign requirements. The resolvent route agrees with geo:resolvent: diagonalizing H^T H gives factors tau/(lambda+tau); the kernel weight is M^2/Q and all other contributions are nonnegative. The claimed implication is valid for every tau>0, including M=0.
3. P3 fixed-u obstruction: the cited profile gives a positive c0 J(u), whereas the certificate would imply F/n<=(n/Q)epsilon^2->0. Positivity is explicitly stated in geo:profile. The submitted claim that a fixed-power regime cannot certify epsilon->0 is therefore correct.
4. P4: For each fixed c>0, [Cn exp(-a)]/[n exp(-cV)]=C exp(-a+cV)->0 when a/V->infinity. The text presents this as an example, not a necessary condition, and expressly disclaims establishing it. Its sufficiently-large-n qualification resolves the initial packet's concern about loglog at n=2. arith:mertens uses the same scale and quantifier.
5. The spectral discussion accurately identifies the dependence on |M| in spec:minimumformula and the independent product law in vol:product. On M!=0 indices multiplication only gives |M|(1+o(1)); at M=0 the exceptional singular value is exactly zero. The phrase “returns the determinant identity” is reasonable shorthand for reproducing its unknown size, although “reproduces |M(n)|, rather than bounding it independently” is more exact.
6. Fixed-index asymptotics cannot alone control growing products. For example, k growing factors each equal 1+1/sqrt(k) have individual ratio tending to one but product tending to infinity. The paragraph does not prohibit independent uniform spectral input and does not claim that geometry can never improve Mertens bounds.

GAP / REQUIRED WORDING CORRECTION:
The sentence “Letting u grow requires quantitative uniform estimates beyond the fixed-parameter limit” is too broad. The existing geo:cutoff proves F(n,y(n))=o(n) whenever log y/log n->0 using only monotonicity and fixed-u limits. Indeed for every fixed U, eventually y<=n^(1/U), so limsup F/n<=c0 J(U); then U->infinity gives zero. Thus qualitative growing-u control already exists, although no quantitative rate for it is obtained this way.

Replace that sentence with:
“Fixed-parameter limits and monotonicity already give the qualitative cutoff in \\eqref{geo:cutoff}; an explicit decay rate for growing $u$ needs additional quantitative control.”

This correction fully addresses the identified gap without changing P1--P4. It also makes clear that the missing input concerns a rate strong enough to compete with arith:mertens, rather than any epsilon tending to zero.

OPTIONAL PRECISION:
- Write “for every fixed $u\\ge1$” in the profile sentence, matching the actual theorem's domain.
- Change “The resolvent certificate requires the weights ...” to “The displayed resolvent depends on the weights ...; the eigenvalue information established here alone does not control its smallness.” This avoids a universal necessity assertion about all conceivable bounding methods. The current version is acceptable when read as a description of the displayed formula.
- Change “returns the determinant identity” as in item 5 to distinguish an asymptotic substitution from an exact equality.

COVERAGE: All new certificate implications and every load-bearing comparison in the proposed section. Read the draft's exact height, variance, and resolvent arguments, profile theorem and its monotonicity cutoff, arithmetic baseline statement, smallest-singular-value theorem/proof, and product-law context. Accepted fixed-u analytic asymptotics and classical VK input were source/substitution checked against their manuscript statements, not independently reproved or bibliographically audited. No evidence of a new stronger bound is claimed or needed.
DEPENDENCIES: Baseline analytic theorems remain the expressly accepted premises. Local linear algebra, normalization, positivity, zero cases, and scale-comparison arguments are discharged. One prose correction remains for coordinator adoption.
EXPOSURE: Initial report PAPER-initial.md sealed before reading the proposal, SHA256 8b242343d579edbe6a61476bc3796321113419de989e6649c9eff69a194e9e8e. Stage 2 saw paper-section-proposal.tex and relevant portions of definitions/arithmetic/spectral/geometry/volumes via local file tools. No other reviewer report or external source was read.
RESOURCES: Under eight minutes; zero external operations; zero numerical workloads; zero TeX invocations. Only the two assigned review files were written.
