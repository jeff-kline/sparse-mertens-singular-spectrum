# Review of the release candidate — September 27, 2026

**Reviewed commit:** `96fe778433660853b7c908e9b7b32a6ae4493c60`.
**Recommendation:** do not tag this exact candidate yet. The central mathematical claims pass this bounded proof-aware review, but the clean-checkout build recipe fails and several audit records need correction. These are repairable release issues; I found no reason to withdraw the principal theorem.

## Scope and exposure

This is an AI review, not expert certification or peer review. The coordinator helped develop the earlier draft and therefore is not a cold, independent examiner of that mathematics. It reviewed the submitted proofs and primary-source ranges directly, rather than treating prior PASS verdicts as proof. A fresh-context read-only subagent separately examined README/prose and the predecessor comparison. No new blind initial proof examination is claimed.

The live draft-0.4 research standard and release checklist were read. The review used nine external operations, counting failed retrieval attempts: standard/McNew/arXiv-source web opens (three), failed sandbox downloads of standard/source (two), successful retries (two), Alladi PDF download (one), and read-only GitHub visibility verification (one). It did not repeat the broad literature survey.

Repository edits, publication, staging, commits, tags, pushes, and settings changes were not performed. Builds ran only in scratch copies extracted with `git archive HEAD`. The only intended repository write is this report, which must be included or explicitly excluded when the next candidate manifest is regenerated.

## Verdicts

| Requested area | Verdict | Scope |
|---|---|---|
| Lemma 3.2, Theorem 3.4, Theorem 4.7 | PASS | Checked the main proof chain and relevant classical-source ranges; not a fresh audit of all 39 pages |
| Comparison with predecessor | PASS | Open Problem 1, dominance condition, upper/lower exponents, and inverse-norm comparison agree with predecessor source |
| Prior-art dispositions | PARTIAL | Alladi (2.16) and the rejection of the proposed arXiv overlap are supported; raw extraction report contains errors; unread sources remain unresolved |
| Reader-facing claims and README | PASS | Main claims and qualifications are faithful; optional readability improvements below |
| Release mechanics and record accuracy | FAIL as-is | Clean documented build fails; hygiene and current-state claims do not match tracked files |

## 1. Mathematics: checked argument, not merely no counterexample

### Lemma 3.2

`paper/sections/arithmetic.tex:37–86` correctly specializes the two-term smooth-number expansion. In [McNew's author manuscript](https://www.nathanmcnew.com/PopularPrimes.pdf), Section 2, equations (7), (13), and (14), the conditions used here hold uniformly: log z=L(1−o(1)), log y comparable to sqrt(L log L), and v comparable to sqrt(L/log L). The extra k=1 boundary inequalities have a diverging margin. The exponentially small Saias relative error is smaller than the required second-order remainder. The derivative bound and ratio estimate, including (17), provide the stated Dickman controls. This checks the published statement as reported by McNew, not Saias's original proof.

The cancellation-preserving tail identity at `arithmetic.tex:189–235` is exact, including the floor endpoint. With beta comparable to sqrt(log L/L), log K comparable to (log L)^2, and log H=L^(9/10), the comparisons needed for both tails are valid:

- beta (log H)^(1−7/12)=O(L^(−1/8)sqrt(log L)) tends to zero;
- (log K)^(7/12) is comparable to (log L)^(7/6), absorbing the O(L) dyadic count and the reciprocal beta;
- L^(21/40) dominates sqrt(L log L), including its square-root logarithm.

At `arithmetic.tex:237–274`, Taylor remainders sum to O(x rho(u) beta^2 (1+log K)^3), which is little-o of x rho(u) beta. The Möbius moments are 0 and −1, with the indicated tails from partial summation. Consequently the surviving main term has the stated sign and size. I found no missing uniformity or order-of-limits step in this argument.

### Theorem 3.4

The prime moment upper bound first fixes endpoints and mesh and then lets n grow (`arithmetic.tex:299–357`); it does not improperly vary q. The lower bound uses a fixed dyadic prime block and the uniform relative estimate, supplying the matching exponent.

For the full energy (`arithmetic.tex:374–480`), the a>exp(3s) tail is negligible relative to prime energy. The noncentral-prime tail remains uniform as N_a=floor(n/a) tends to infinity uniformly. The central ratio is dominated by C a^(−2+epsilon), with fixed epsilon<1; dominated convergence gives the squarefree multiplier sum zeta(2)/zeta(4)=15/pi^2. The remaining Mertens and isolated-coordinate terms are negligible. Both bounds for W_n are supplied; the result is a logarithmic asymptotic, not a multiplicative equivalent for the prime energy itself.

### Theorem 4.7

The exact inverse and the compact-Gram estimate give the error O(sqrt n) at `spectral.tex:378–388`. In particular,

    |M(n)|/W_n <= C exp(−c L^(7/12) + (1+o(1))sqrt(L log L)) -> 0.

Thus the relative inverse-norm error tends to zero and taking reciprocals is valid on M(n)≠0. The zero case is handled separately. The unconditional claim is supported by this proof chain. It does not independently bound M(n).

## 2. Predecessor comparison

The predecessor's `paper/sparse-mertens-singular-values.tex:748–751` explicitly asks for the W_n shape now established. Its lines 444–475 state the rank-one dominance hypothesis and explain that RH supplies it. The current README (`92–98`), introduction (`65–71`), abstract, and correction record accurately describe removal of that hypothesis. Shared finite identities are credited in `definitions.tex:81`. The predecessor's sharper largest-singular-value estimate is acknowledged. I found no substantive misstatement in this comparison.

## 3. Prior art: main dispositions supported, extraction record needs repair

I retrieved [Alladi's JNT paper](https://core.ac.uk/download/3088217.pdf) and visually checked pp. 86 and 91. Equation (2.16) does require exp((log x)^(2/3+epsilon))<y=o(x), hence u<(log x)^(1/3−epsilon); it does not directly cover this paper's saddle range.

I downloaded and read [the arXiv LaTeX source](https://arxiv.org/src/2601.10636). Theorem 1.1's main sums require 1<=J<=k−1. They are empty at k=1. For fixed N, the resulting polynomial-in-1/u error estimate is much larger than the desired saddle-scale main term. One cannot choose N growing with x without controlling the N-dependent constants. The preparing agent's rejection of the extraction agent's proposed overlap is justified. This is not a proof of global novelty.

**Must-fix R2 — mathematical transcription errors in the retained source audit.** `audit/reports/alladi-source-extraction.md:54,63,70,184` contains errors unrelated to the already-recorded arXiv correction:

- the target u has a quotient log x/log log x under the square root, not their product;
- the Dirichlet series at line 63 omits the Möbius coefficient;
- the identity for A(x) at line 70 inserts an erroneous 1/p. Alladi's (1.3), visually checked on p. 86, has no such weight.

Minimal disposition: preserve the original report as history, but prepend a dated erratum and link it from the ledger. Exact replacement/erratum text:

> Corrections to this extraction: throughout the saddle-range comparison, the target is u comparable to sqrt(log x / log log x), while log y is comparable to sqrt(log x log log x). The Dirichlet series in the discussion of (3.1) has summand mu(n)/n^s. Alladi's equation (1.3) is A(x)=sum over primes p<=x of |M(x/p,p)|, with no factor 1/p. These corrections do not alter the comparison with (2.16). The earlier tentative interpretation of arXiv:2601.10636 is superseded by the source-based disposition in audit/LEDGER.md.

Alladi TAMS and Tenenbaum 1990 remain unread; I have not converted their absence into a novelty finding. A bounded P1 disposition with explicit residuals is defensible under the standard after the retained evidence is corrected.

## 4. README: good structure, light tightening recommended

The progression from explicit matrix rule to picture, results, predecessor, credit, and reproduction works. The README faithfully restates the abstract and makes the no-improved-Mertens limitation clear. It does not need a wholesale rewrite.

Optional improvements:

1. Define squarefree and singular values at first use. For example: “An integer is squarefree if no prime square divides it. The singular values are the nonnegative square roots of the eigenvalues of B_n^T B_n.”
2. At `README.md:56–59`, replace the awkward “holds for every n” description of a limit with:
   > For each fixed r≥1, sqrt(n) sigma_(n−r) converges to lambda_r(L)^(−1/2), where lambda_r(L) is the r-th largest positive eigenvalue of an explicit compact operator built from the tree. The limit runs through all positive integers n, including those where M(n)=0.
3. At line 96 identify A_n as the matrix before its first row is replaced. At line 139 replace the unexplained K with “the limiting inverse-norm constant.”
4. At lines 92–95 say “a rank-one dominance condition implied by RH,” rather than only “a hypothesis.”
5. Remove the introductory no-improvement sentence at lines 42–43; retain the fuller explanation at lines 77–80. The latter explains why the formula is not a Mertens bound.

## 5. Release mechanics: new findings

### Must-fix R1 — clean documented reproduction fails

Evidence: `Makefile:8–10`, `README.md:149–153`, and `VERIFICATION.md:32–38`.

From a clean `git archive HEAD` extraction, one `make paper` (two TeX passes) leaves “Label(s) may have changed. Rerun to get cross-references right.” `make check` then returns FAIL, and manifest verification rejects paper/main.pdf. Its hash is:

    4ad47dafe6c802f03f7720a29f32981a52b817a82d6f5a5c5ea4ff7c2e232124

A second `make paper` settles the references and produces exactly the recorded hash:

    bf477dddf4d5d65ad5f26be42f2de4c4e37dda3dabe20b5f5a34152fb420b915

A separate clean extraction reproduced the first failure. This explains why verification in a warm working tree passed. It is not the known standalone-wrapper regression.

Minimal tested disposition: make the paper target perform four passes (or use a separately validated convergence-aware build). Exact four-pass replacement:

```make
paper:
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
```

Update the verification instruction to “make paper # four pdfLaTeX passes, including clean-checkout reference convergence”; rerun in a fresh archive and regenerate the manifest after all changes. Do not claim that warm repeat-build identity alone established clean reproduction.

### Must-fix R3 — hygiene PASS overstates the tracked-tree result

`ADMISSION.md:66` asserts no private paths, but tracked reports contain local account/workspace paths: `claim-prose-audit.md:10`, `citation-audit.md:192`, `proof-audit-arithmetic.md:39`, and temporary account/session paths in `proof-audit-spectral.md:47` and `alladi-source-extraction.md:15,136,235`. These are not credentials, but they violate the explicit release hygiene claim and are not portable evidence locators. The mechanical audit's PASS does not test this whole assertion.

Replace the audit locators with logical ones, preserving provenance and marking the redaction, for example:

> Predecessor source: sparse-mertens-singular-values v0.1.0, paper/sparse-mertens-singular-values.tex (local absolute path redacted).

> Numerical checks ran in an isolated tooling environment. The scripts were scratch-only and are not included in this release; their local account/session paths have been redacted. These checks are not reproducible release evidence.

For source downloads, keep the public retrieval URL and name the local copy only by filename. Until this is done, the exact admission row should read:

> | Hygiene: credentials, private paths, placeholders | PARTIAL | Local account and temporary-session paths remain in audit reports; redact them and rerun a tracked-tree scan before tagging. |

### Must-fix R4 — current records contradict the candidate

`audit/RELEASE-PLAN.md:60–61` still says repository creation/default-branch push are unauthorized, while `ADMISSION.md:80` records author-authorized private creation and push as done. I verified the GitHub repository is private. This is a stale record, not evidence that the original action lacked authorization.

Replace the plan rows with:

> | Create private GitHub repository and push main | Author authorization, as recorded in ADMISSION.md | done 2026-09-27 |
> | Make repository public | Author approval required | pending |
> | Further default-branch updates | Scope to be established for the next exact candidate | pending |

Also, `audit/LEDGER.md:98` claims a singular-value definition was added to README, but no such definition exists in the current file. Either add the optional definition above or append this exact correction:

> The singular-value definition recorded as added in the earlier prose disposition is absent from the current README. That optional suggestion remains deferred; the earlier “Fixed” disposition is superseded.

## Mechanical checks that did pass

At the reviewed commit, the original tree was clean and HEAD equaled the local origin/main ref. All seven existing commits use the stated noreply author and committer identity. Local tags are absent. GitHub reports private=true. Remote release absence was not independently queried.

The original working-tree checker passes: 39 pages, 11 sources, 121 labels, 151 references, 18/18 bibliography entries cited. All 49 manifest entries match, covering all 50 tracked files except the manifest. The mechanical candidate audit reproduces seven PASS, zero FAIL, one missing-tag warning. Its citation-key check reports 0/0; the project checker, not that generic check, supplies the actual LaTeX citation check. Its outgoing-identity check reports zero outgoing commits, so I separately inspected all existing commit identities.

CITATION.cff is safe for the selected candidate route: no DOI/date-released, bounded abstract, publication-safe message, consistent version/license. The Zenodo GitHub-integration route and distinction between provider zipball and git archive are stated correctly. Pending tag/archive/DOI work is disclosed and is not itself a newly discovered defect.

I did not repeat all-page visual inspection, re-audit every spectral/geometric theorem, inspect original Saias proofs, or certify global priority. Known issues listed in the handoff are not presented as new discoveries.

## Ranked must-fix list before tagging

1. **R1:** make clean-checkout reproduction pass and regenerate verified artifacts/manifest.
2. **R2:** append the source-extraction erratum (wrong weight, omitted mu, wrong saddle parameter).
3. **R3:** redact local account/session paths and make the hygiene disposition truthful.
4. **R4:** reconcile the action-ownership table and stale README-definition disposition.

**Would I authorize tagging v0.1.0 as-is? No.** After these bounded fixes and a fresh candidate check, this review supplies no mathematical objection to advancing the release. That remains a scoped AI review conclusion, not a proof of correctness or novelty.
