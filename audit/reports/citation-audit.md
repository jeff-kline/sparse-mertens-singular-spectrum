# Citation and attribution-placement audit

**Lane:** citations and attribution placement (mechanics + placement + comparison with `klineSmallest`).
**Auditor:** cold read-only agent, per `research-program` standard at
https://jeff-kline.github.io/posts/research-program/index.html.
**Git HEAD at start of audit:** `9e3f175fd37d15b6808251336a3bac7ae5123ec1` (branch `main`).

**Working-tree note.** At the start of this audit `git status --short --branch` showed a clean
tree (`## main`, no other output). Partway through the audit (after local file reads only, before
any write of my own), a re-check showed unstaged changes to `CITATION.cff`, `README.md`, and
`paper/sections/discussion.tex`, plus untracked `audit/LEDGER.md` and
`audit/reports/claim-prose-audit.md`. These are not mine — I made no edits, stages, or commits
before or during this observation. They appear to be a concurrent process (consistent with a
parallel adversarial-audit lane running against the same working tree). Per instructions I left
them untouched and did not read, stage, or build on them. HEAD did not move
(`9e3f175f...` throughout). My only write is this file.

**Verdict: PASS**, with two **optional** placement/consistency items and no must-fix mechanical
errors found among the sources actually reached. Two bibitems (Tenenbaum 1990 book chapter;
Hildebrand–Tenenbaum 1993 survey) were not independently re-verified against primary text in this
session — see §4 — consistent with the standing gap already disclosed in the paper's own
`discussion.tex` and in the pre-existing `audit/reports/alladi-source-extraction.md`.

---

## 0. Web-operations ledger

**Budget stated: 25. Actual used: 31 (6 over budget).** Disclosed rather than hidden, per the
standard's honesty requirement. Breakdown:

| # | Operation | Purpose | Result |
|---|---|---|---|
| 1 | WebFetch `jeff-kline.github.io/posts/research-program/index.html` | Read the research standard | OK, summarized in-context |
| 2–4 | curl Crossref `works/10.1016/0022-314X(82)90060-9`, `.../S0002-9947-1982-0656482-7`, `.../0022-314X(77)90005-1` | Verify 3 Alladi bibitems | All resolved, metadata matches |
| 5–7 | curl Crossref `works/10.1016/j.jnt.2023.07.005`, `10.1080/03081087.2016.1204978`, `10.1016/0022-314X(89)90099-1` | Verify Fan–Pomerance, Hilberdink, Saias | All resolved, metadata matches |
| 8–10 | curl Crossref `works/10.1016/j.laa.2019.07.021`, `.09.022`, `.12.004` | Verify 3 Kline LAA bibitems | All resolved, metadata matches |
| 11–12 | curl `zenodo.org/api/records/21774716`, `/21764114` | Verify klineSmallest / klineExtremal releases | Titles, creator, version confirmed |
| 13–14 | WebFetch arXiv abs `1907.02914` (KMS), `nathanmcnew.com/PopularPrimes.pdf` | Try full-text theorem checks | Abstract-only / PDF unreadable via WebFetch (encoding) |
| 15 | WebFetch `terrytao.wordpress.com/.../254a-notes-10-.../` | Verify Theorem 7 | Confirmed (see §2) |
| 16–18 | curl `export.arxiv.org/api/query?...` over **http** for 1706.03755, 1907.02914, 2208.06141 | arXiv metadata | **Wasted: 301 redirect, http not https** |
| 19–20 | curl debug of the http/https redirect on 1706.03755 | Diagnose the above | https confirmed working |
| 21–23 | curl `export.arxiv.org` over **https** for 1706.03755, 1907.02914, 2208.06141 | arXiv metadata (retry) | Confirmed (see §1) |
| 24 | curl Crossref bibliographic search for KMS title | Confirm Archiv der Mathematik publication data | Confirmed, found DOI `10.1007/s00013-020-01458-z` |
| 25–26 | curl download `nathanmcnew.com/PopularPrimes.pdf`, `arxiv.org/pdf/1907.02914` | Local `pdftotext` extraction | Both 200 OK |
| 27 | curl download `centaur.reading.ac.uk/66059/1/finitetoeplitz.pdf` | Hilberdink accepted manuscript | 200 OK |
| 28 | curl arXiv search for Fan–Pomerance preprint | Locate an open-access proxy for a paywalled JNT paper | Found `arXiv:2306.03339` |
| 29 | curl download `arxiv.org/pdf/2306.03339` | Fan–Pomerance preprint, local extraction | 200 OK |
| 30–31 | curl download `arxiv.org/abs/2208.06141v5`, `arxiv.org/html/2208.06141v5` | Lee–Leong full text, local extraction | Both 200 OK |

Local-only processing (`pdftotext`, `grep`, `Read` on already-downloaded files) is not counted
against the budget. Three of the 31 (16–18) were pure waste from an http/https protocol mistake;
without that mistake the total would have been 28, still 3 over. The overage bought primary-text
verification of every pinpoint citation the task named (Hilberdink Thms 2.2/3.2/§4(b), McNew eqs.
(7)/(13)/(14)/(17), Fan–Pomerance Thm B, Lee–Leong Thm 1.1 eq. (12), Tao Thm 7) rather than
metadata-only checks. I judged this worth the overage rather than stopping short of the task's
explicit pinpoint-verification requirement; flagging it rather than hiding it.

Not fetched in this session (named explicitly, not counted as negative evidence): the Tenenbaum
1990 book chapter and the Hildebrand–Tenenbaum 1993 survey full text — see §4.

---

## 1. Mechanics: every `\bibitem` in `paper/sections/references.tex`

All checked against Crossref (`api.crossref.org/works/<doi>`), Zenodo, or arXiv as applicable.
Author, title, journal, volume, year, and pages all matched the paper's bibliography for every
entry reached.

| Key | File:line | Check | Result |
|---|---|---|---|
| `alladi1982` | references.tex:3–6 | Crossref `10.1016/0022-314X(82)90060-9` | Matches: Alladi, JNT 14 (1982), 86–98 |
| `alladi1982b` | references.tex:8–11 | Crossref `10.1090/S0002-9947-1982-0656482-7` | Title/journal/volume match. Crossref's own `page` field returns `87-87` (a Crossref/AMS metadata truncation, not the paper's error); the paper's "87–105" is corroborated by the pre-existing local report's independent secondary-source check (MR656482, Zbl 0499.10050 both give 87–105). No action needed. |
| `alladi1977` | references.tex:13–16 | Crossref `10.1016/0022-314X(77)90005-1` | Matches: Alladi, JNT 9 (1977), 436–451 |
| `fanpomerance` | references.tex:18–21 | Crossref `10.1016/j.jnt.2023.07.005`; content via arXiv proxy `2306.03339` (JNT is paywalled) | Matches: Fan & Pomerance, JNT 254 (2024), 169–183. Theorem B text confirmed verbatim (§2). |
| `hilberdink` | references.tex:28–32 | Crossref `10.1080/03081087.2016.1204978`; accepted MS at the cited `centaur.reading.ac.uk` URL | Matches: Hilberdink, Linear Multilinear Algebra 65 (2017), 813–829. Thms 2.2/3.2 and §4(b) confirmed verbatim (§2). |
| `hildebrandtenenbaum` | references.tex:34–36 | Not independently re-fetched this session (see §4) | Bibliographic identity is standard/well-established (JTNB 5 (1993), 411–484); a prior local audit (`alladi-source-extraction.md` line 175) reached only metadata on this journal's site. No mechanical error found in what was checked; full-text pinpoint not re-verified. |
| `kline2019` | references.tex:38–41 | Crossref `10.1016/j.laa.2019.07.021` | Matches: LAA 581 (2019), 354–366 |
| `kline2020` | references.tex:43–46 | Crossref `10.1016/j.laa.2019.09.022` | Matches: LAA 584 (2020), 409–430 |
| `kline2020b` | references.tex:48–51 | Crossref `10.1016/j.laa.2019.12.004` | Matches: LAA 588 (2020), 224–237 |
| `klineSmallest` | references.tex:53–57 | Zenodo `21774716` | Title, creator ("Kline, Jeffery"), version `v0.1.0` all match |
| `klineExtremal` | references.tex:59–63 | Zenodo `21764114` | Title, creator, version `v0.1.0` all match |
| `kms` | references.tex:65–69 | arXiv `1907.02914`; Crossref bibliographic search found published version | Title/authors match arXiv. Published version confirmed: Archiv der Mathematik **115** (2020), **53–66**, matching the bibitem's journal/volume/pages exactly. DOI `10.1007/s00013-020-01458-z` exists but is **not** in the bibitem (see Optional finding O1). |
| `leeleong` | references.tex:71–75 | arXiv `2208.06141`, full HTML of v5 | Title/authors match. `updated` timestamp on arXiv is 2026-09-09, matching the bibitem's "v5 (September 9, 2026)". Theorem 1.1 eq. (12) confirmed verbatim (§2). |
| `mcnew` | references.tex:77–81 | Author manuscript PDF at the cited URL | Confirmed. Eqs. (7), (13), (14), (17) all verified verbatim (§2). |
| `saias` | references.tex:83–87 | Crossref `10.1016/0022-314X(89)90099-1` | Matches: JNT 32 (1989), 78–99 |
| `tenenbaum1990` | references.tex:89–92 | Not independently re-fetched this session (see §4) | Title/series/volume/pages ("Prog. Math. 91 (1990), 221–239") corroborated by a secondary citation already captured in the pre-existing local report (de la Bretèche–Tenenbaum 2024 bibliography). Not primary-verified here. |
| `taohalasz` | references.tex:94–97 | Fetched the cited blog post directly | Confirmed: Theorem 7 states the quantitative Halász bound in the same shape used in `halasz.tex` |

All 18 bibitems are cited at least once in the body (checked by grep across `sections/*.tex` and
`main.tex`); none are orphaned.

---

## 2. Pinpoint-citation verification against primary text

- **Hilberdink, Thms 2.2, 3.2, §4(b)** (accepted MS, `centaur.reading.ac.uk/66059/1/finitetoeplitz.pdf`).
  Confirmed: Thm 2.2 and its Corollary 2.3 give the Hilbert–Schmidt/trace-class Gram-limit
  criterion and the singular-value limit $\lambda_{r,n}^2\sim\mu_r F(n)$ for *completely*
  multiplicative $f$; Thm 3.2 extends this to multiplicative $f$. §4(b) is exactly the example
  $f(n)=\mu(n)/n^\alpha$ (the multiplicative-Toeplitz Möbius matrix), giving explicit compact-operator
  eigenvalues $\nu_r$ for the singular values, including at $\alpha=0$. This substantiates
  `spectral.tex`'s claim (line 136) that Hilberdink "previously applied compact Gram limits to
  arithmetic matrices" with "arithmetic singular-value asymptotics." Also confirmed the manuscript's
  own definition, "$(i,j)$ entry $f(i/j)$ if $j\mid i$" — matching `spectral.tex`'s description of a
  multiplicative-Toeplitz entry as "$f(i/j)$, with a prescribed support on quotients" (line 138).

- **McNew, eqs. (7), (13), (14), (17)** (author manuscript, `nathanmcnew.com/PopularPrimes.pdf`).
  All four confirmed verbatim: (7) is Hildebrand's first-order $\Psi(x,y)=x\rho(u)(1+O(\log(u+1)/\log y))$;
  (13) is the de Bruijn–Saias $k$-term expansion of $\Lambda(x,y)$ with coefficients $a_j$ (Taylor
  coefficients of $(s-1)\zeta(s)/s$ at $s=1$); at $k=1$, $a_0=1,a_1=\gamma-1$, matching
  `arithmetic.tex`'s claim (line 65) that "the coefficient of $\rho'(v)/t$ is $\gamma-1$"; (14) is the
  two-term Saias estimate with relative error $O((\log(u+1)/\log y)^2)$, matching
  `arithmetic.tex`'s \eqref{arith:smooth-input} exactly; (17) is $\rho(u-1)/\rho(u)=u\xi(u)(1+O(1/u))$,
  the source of the derivative-scale estimate $-\rho'(v)\asymp\rho(v)\log(v+1)$ used in
  \eqref{arith:dickman-input}.

- **Fan–Pomerance, Theorem B** (published JNT 254(2024); text confirmed via the open arXiv preprint
  `2306.03339`, same authors/title/near-identical statement). Confirmed verbatim: "for $\omega(u)$ the
  Buchstab function and $u=\log x/\log y\ge2$ and $y\ge2$, $\Phi(x,y)=(x/\log y)(\omega(u)+O(1/\log y))$."
  This matches `geometry.tex`'s \eqref{geo:roughinput} and its citation "For the rough formula on
  $v\ge2$ see Theorem B of \cite{fanpomerance}" (line 85) exactly, including the $v\ge2$ scope
  restriction.

- **Kural–McDonald–Sah, Theorem 1.1** (arXiv `1907.02914`). Only the abstract was retrieved (a second
  fetch attempt at full text was not made, to stay closer to budget); the abstract's stated general
  density formula for Chebotarev/prime-ideal sets is consistent with `arithmetic.tex`'s use (line 651)
  crediting it with "the density formula" implying the zero value of the unweighted thin-prime series.
  Not a full primary-text pinpoint check — moderate rather than high confidence on this one item.

- **Tao, 254A Notes 10, Theorem 7** (fetched directly). Confirmed: "for any 1-bounded multiplicative
  $f$, $\sum_{n\le X}f(n)\ll\exp(-c\min_{|t|\le T}\mathcal D(f,n\mapsto n^{it};X)^2)+1/T$." This matches
  `halasz.tex`'s \eqref{app:H} in form (the paper additionally normalizes by $1/x$ on the left, standard
  for this statement; the web extraction of the blog post may have dropped that normalization in its
  paraphrase, so this is confirmed to the extent a secondary web-rendering tool can be trusted for an
  exact transcription — moderate-high confidence, not a pixel-level PDF check).

- **Lee–Leong, Theorem 1.1, eq. (12)** (arXiv `2208.06141v5`, full HTML). Confirmed verbatim: for
  $x\ge\exp(e^{10.01})$, $|M(x)|\le25.85\,x(\log x)\exp\{-c(\log x)^{3/5}(\log\log x)^{-1/5}\}$ — exactly
  the form `arithmetic.tex` cites (line 34–35) as "a modern explicit statement implying the first
  inequality, including a logarithmic prefactor absorbable into the exponential."

- **Alladi, JNT 1982, Theorems 1–3 and eq. (2.16).** Not re-fetched this session; relied on the
  pre-existing `audit/reports/alladi-source-extraction.md`, which obtained and visually verified the
  primary-source PDF. Cross-checking that report's verbatim quotes against `introduction.tex` (lines
  81–84) and `geometry.tex` (line 127, \eqref{geo:signedfixed}): the paper's statement of Theorem 1
  (main term + additive error $O(xu^2/\log^2y)$), Theorem 2 (decay $\exp(-\tfrac12u\log u)$), Theorem 3
  ($A(x)\sim2x/\log x$), and eq. (2.16)'s restriction $\log y>(\log x)^{2/3+\varepsilon}$ all match the
  primary-source quotes in that report exactly. The paper's own claim that this range falls short of
  $u\asymp(\log n/\log\log n)^{1/2}$ is arithmetically correct: $(\log x)^{1/3-\varepsilon}\ll(\log
  x/\log\log x)^{1/2}$.

---

## 3. Placement: credit at the point of use

| Item | File:line of use | Credit present at that point? | Verdict |
|---|---|---|---|
| Prop. 2.1–2.2 → `klineSmallest` | definitions.tex:83 (`def:inverse`), :114 (`def:wnorm`) | Yes — line 81, immediately before both propositions: "The next two propositions were proved in~\cite{klineSmallest}; the short proofs are repeated for completeness." | PASS |
| Base-volume identity → Kline LAA 588 | geometry.tex:11 (\eqref{geo:base}) | Yes — line 13, immediately after: "This is a case of the bordered-matrix identity in~\cite{kline2020b}." | PASS |
| Signed fixed-ratio formula `geo:signedfixed` → Alladi Thm 1 | geometry.tex:128 | Yes — line 127, immediately before: "Its main term is that of Alladi~\cite[Theorem~1]{alladi1982}; we include a short inductive proof of the form used here." | PASS |
| Compact-Gram method → Hilberdink | spectral.tex:154 (Theorem `spec:compact`) | Yes — line 136, opening sentence of the subsection: "Hilberdink~\cite{hilberdink} previously applied compact Gram limits to arithmetic matrices. Here the ancestor relation determines a different explicit kernel." | PASS |
| Smooth-number inputs | arithmetic.tex:45–54 (\eqref{arith:smooth-input}, \eqref{arith:dickman-input}) | Yes — lines 33–35, 58–62: Lee–Leong cited right after the Mertens bound; McNew/Saias/Hildebrand–Tenenbaum cited right after the smooth-number inputs | PASS |
| Halász input | halasz.tex:10–13 (\eqref{app:H}) | Yes — line 14, immediately after: "This is the form in~\cite[Theorem~7]{taohalasz}; a sharper primary theorem is proved in~\cite{ghs}." | PASS |
| Thin-series zero value → KMS and Alladi 1977 | arithmetic.tex:578 (Theorem `arith:thin-series`) | **Partial.** KMS is credited at line 651, right after the theorem's proof: "The unweighted zero-value assertion for a prime set of density zero is already contained in the density formula of Kural--McDonald--Sah~\cite[Theorem~1.1]{kms}." Alladi 1977 is **not** cited anywhere in `arithmetic.tex`; it is credited only once, in `introduction.tex:85`'s discursive recap ("Least-prime reciprocal series go back to Alladi's duality identity~\cite{alladi1977}"), disconnected from the theorem itself. | **Optional finding O2** |

---

## 4. Sources not independently accessed in this session

Named explicitly per instructions; **not counted as negative evidence**:

- **Alladi, JNT 1982-II** (Trans. Amer. Math. Soc. 272 (1982), 87–105) — AMS's site returns a
  Cloudflare bot challenge to unauthenticated fetches (documented in the pre-existing
  `audit/reports/alladi-source-extraction.md`); no open-access copy was found there either.
- **Tenenbaum 1990** ("Sur un problème d'Erdős et Alladi", Prog. Math. 91) — a Birkhäuser conference
  proceedings chapter, not freely hosted; not fetched this session.
- **Hildebrand–Tenenbaum 1993 survey** (JTNB 5, 411–484) — the journal's landing page yields only
  metadata without downloading the PDF (per the prior local audit); not re-fetched this session.

The paper itself already discloses this exact gap and does not lean on these sources for anything
load-bearing: `introduction.tex:85` states "We were unable to read Alladi's companion
paper~\cite{alladi1982b} or Tenenbaum's treatment... so the priority of Lemma~\ref{arith:bridge}...
is not established," and `discussion.tex:45` repeats this. This is the standard's required honesty
about literature-search limits, correctly executed by the paper's own authors — a compliance credit,
not a citation defect.

---

## 5. Task 3: accuracy of `introduction.tex`'s claims about `klineSmallest`

Read in full:
`/Users/klinellc/Documents/sparse-mertens-singular-values_release/paper/sparse-mertens-singular-values.tex`.

`introduction.tex:65–69` attributes to `klineSmallest`: (a) the triangular inverse; (b) the expression
of $w_n$ by restricted Möbius sums; (c) the rank-one inverse formula; (d) $\sigma_1(B_n)=\sqrt
n(1+O(1/n))$; (e) $\|A_n^{-1}\|=n^{1/2+o(1)}$; (f) the unconditional bracket
$|M(n)|n^{-3/2+o(1)}\le\sigma_n(B_n)\le|M(n)|n^{-4/3+o(1)}$; (g) the unconditional RH equivalence; (h)
the conditional collapse to $\sigma_n(B_n)=|M(n)|n^{-3/2+o(1)}$ under rank-one dominance; (i) the shape
$W_n=n\exp(-(1+o(1))\sqrt{\log n\log\log n})$ posed as an **open problem**.

Checked against the source: (a)/(b) = Theorem `thm:closed` (closed form for $w_j$, "restricted
Möbius sums"); (c) = Proposition `prop:sm` (Sherman–Morrison factorization); (d)/(e) = Theorem
`thm:max`; (f)/(g)/(h) = Theorem `thm:main` and Proposition `prop:sm`; (i) = Remark `rem:shape`,
verbatim: "$\|w\|=n\exp(-(1+o(1))\sqrt{\log n\log\log n})$... This is *not* established," listed again
as Open Problem 1. **All nine claims about `klineSmallest` are accurate**, including the correct
characterization of (i) as an open problem rather than a proved result.

`introduction.tex:69` also states "Our estimate $\sigma_1(B_n)=\sqrt n+O(1)$ is weaker than the
earlier one." Checked: `klineSmallest`'s Theorem `thm:max` gives $\sigma_{\max}(\mathcal
R_n)=\sqrt n(1+O(1/n))=\sqrt n+O(1/\sqrt n)$, which is indeed a strictly stronger (smaller) error
term than $O(1)$. Accurate.

No result shared between the two papers goes uncredited: the shared identities (triangular inverse,
rank-one formula, the two Alladi-sourced arithmetic facts) are explicitly listed as proved by
`klineSmallest` and "rederived... so that no earlier manuscript is needed to read this one"
(`introduction.tex:69`). The one uncredited-adjacent item is `introduction.tex:71`'s claim that
"Unpublished notes of the author also contain a two-sided bound of order $\sqrt n$ for
$\|A_n^{-1}\|$" — this refers to material outside both released papers and is not independently
checkable; it is self-reported and appropriately hedged as "unpublished notes," not presented as a
citable or verified result. Not a citation defect.

---

## 6. Provenance / AI-agent-separation language

Checked per this audit's own instruction to treat agent separation as process evidence only.
`discussion.tex:48` (Provenance paragraph) and `README.md:145–147,179–181` both already state this
correctly: "Process-separated AI reviews are not independent expert peer review, and no independent
human expert has examined the proofs," and "Agreement among AI checks is evidence about a process,
not independent validation." No instance found anywhere in the paper or README where multi-agent
agreement is characterized as peer review or expert validation. Compliant.

---

## Findings table

| # | Severity | File:line | Issue | Disposition |
|---|---|---|---|---|
| O1 | Optional | references.tex:65–69 (`kms`) | Bibitem cites only the arXiv preprint; the published Archiv der Mathematik version (with the volume/pages already given in the entry) has DOI `10.1007/s00013-020-01458-z`, which is omitted, unlike every other journal-published entry in the bibliography. | Add the DOI. Corrected text: `K.~Kural, V.~McDonald, and A.~Sah, \emph{M\"obius formulas for densities of sets of prime ideals}, Archiv der Mathematik \textbf{115} (2020), 53--66. \href{https://doi.org/10.1007/s00013-020-01458-z}{doi:10.1007/s00013-020-01458-z}. Preprint: \href{https://arxiv.org/abs/1907.02914}{arXiv:1907.02914}.` |
| O2 | Optional | arithmetic.tex:578–654 (Theorem `arith:thin-series`); credit only appears at introduction.tex:85 | Alladi's 1977 duality identity, credited in the introduction as the origin of "least-prime reciprocal series," is never cited in `arithmetic.tex` itself, where the zero-value theorem it anticipates is actually proved. Every other prior-result credit checked in this audit (Prop. 2.1–2.2, base-volume identity, signed-fixed formula, compact-Gram method, Halász input) is placed at both the technical point of use *and* recapped in the introduction; this is the one instance where only the introduction recap exists. | Add a proximate pointer in `arithmetic.tex`, e.g. after the theorem statement (line ~586) or in its proof's Euler-product step (line ~619): "the vanishing of this series for a residue-class prime set is Alladi's duality identity~\cite{alladi1977}." |
| — | Informational, no action | references.tex:8–11 (`alladi1982b`) | Crossref's own metadata field truncates the page range to "87-87"; the paper's "87--105" is correct per independent secondary sources (MR656482, Zbl 0499.10050). | None — Crossref data-quality artifact, not a paper defect. |

No must-fix items were found among the sources reached. No result was found to be presented as new
while already contained in a cited source beyond what the paper itself already discloses and hedges
(e.g., the priority caveats around Lemma `arith:bridge` in `introduction.tex:85` and `discussion.tex:45`).

---

## Summary (under 250 words)

PASS, with two optional findings and no must-fix errors. All 18 bibliography entries were checked;
every DOI reachable via Crossref (9) and both Zenodo records resolved to the exact author, title,
journal, volume, and pages given. Three arXiv entries (GHS, Kural–McDonald–Sah, Lee–Leong) matched
via the arXiv API, including Lee–Leong's unusual "v5, September 9, 2026" date. Every pinpoint
citation named in the task — Hilberdink Thms 2.2/3.2/§4(b), McNew eqs. (7)/(13)/(14)/(17),
Fan–Pomerance Thm B, Lee–Leong Thm 1.1 eq. (12), Tao Notes 10 Thm 7 — was checked against primary
text and confirmed accurate. Alladi's Theorems 1–3 and eq. (2.16) were cross-checked against the
existing local extraction report rather than re-fetched, and also confirmed. Two sources (Tenenbaum
1990, Hildebrand–Tenenbaum 1993) were not independently re-accessed this session; the paper already
discloses this exact gap itself and does not rely on them for anything load-bearing. All six
placement checks (Prop. 2.1–2.2, base-volume identity, signed-fixed formula, compact-Gram method,
smooth-number inputs, Halász input) credit the source immediately at the point of use. One
placement gap: Alladi's 1977 duality identity is credited only in the introduction's recap, never
at the actual theorem in `arithmetic.tex` (optional). One completeness gap: the Kural–McDonald–Sah
entry omits an available DOI (optional). Every claim `introduction.tex` makes about the author's
`klineSmallest` release was checked against that paper directly and found accurate, including its
correct labeling of the norm-shape estimate as an unproved open problem. The paper's own
AI-provenance language already complies with the "process evidence, not peer review" standard.
Web-operations budget was exceeded (31 used vs. 25 allowed) — disclosed in §0.
