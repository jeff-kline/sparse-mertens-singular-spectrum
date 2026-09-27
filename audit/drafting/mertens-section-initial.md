# PAPER initial isolated examination

STAGE: INITIAL
VERDICT: NOT-BROKEN
CLAIM: P1--P4 and logical qualifications in assignments/PAPER-claims.md, read before exposure to the proposed section.

EVIDENCE:
- P1 survives the projection attack: h^2=M^2/Q is no larger than any squared residual. Q>=1, so multiplying through by Q is legal even when M=0. The claimed bound follows upon taking nonnegative square roots.
- P2 survives both routes: M^2<=QF is exactly the required implication. For the resolvent, the zero eigenspace contributes h^2 and every positive eigenspace contributes a nonnegative quantity, hence T(tau)>=h^2 for every tau>0. No tau->0 exchange is necessary.
- P3 survives normalization: dividing its proposed certificate bound by n gives F/n <= (n/Q)epsilon^2 ->0, because Q/n->c0>0. This contradicts the assumed strictly positive fixed-u limit. This blocks the specified certificate, not cancellation in M itself. No triangular-array claim follows from fixed-u convergence alone.
- P4 survives comparison: for each fixed c>0, C exp[-a(n)+cV(n)]->0 when a/V->infinity, since V->infinity. This is sufficient, not necessary, and does not assert the new bound exists.
- Determinant substitution cannot estimate the unknown M if the substituted least singular value already contains |M|. At zeros, use the exact zero singular value rather than an asymptotic ratio containing |M| in a denominator.
- Fixed-index limits do not control growing products without uniform errors; a number of small multiplicative errors tending to infinity can accumulate.

COVERAGE: algebra, quantifiers, positivity, M=0, certificate versus actual cancellation, fixed versus varying parameters, and sufficient versus necessary benchmarks. No computation, prior-art survey, or reproof of the accepted asymptotics was attempted.
DEPENDENCIES: accepted BASELINE identities and Q/n->c0. P3 is conditional on its displayed positive limit. P4's V should be used only for sufficiently large n (loglog n>0); the blanket packet wording n>=2 should not become a finite-n assertion about a real positive V at n=2.
EXPOSURE: CHARTER.md, BASELINE.md, assignments/PAPER-claims.md, and cold-examiner SKILL.md only. No proposed proof, other reviewer report, or external source was read. Parent task request provided scope only.
RESOURCES: less than three minutes; zero external source operations; zero numerical workloads. Initial file is sealed by SHA256 before proof exposure; subsequent corrections belong in PAPER-proof.md.
