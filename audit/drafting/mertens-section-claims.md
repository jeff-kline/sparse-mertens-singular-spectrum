# Statement-only packet: proposed Mertens improvement section

Use the definitions and accepted identities in BASELINE.md. Do not read paper-section-proposal.tex before recording an initial attack report.

For n>=2 and any positive epsilon(n):

P1. If some z in R^(n-1) satisfies ||1-H^T z||^2 <= n^2 epsilon(n)^2/Q(n), then |M(n)|<=n epsilon(n).

P2. The same conclusion follows from F(n,y)<=n^2 epsilon(n)^2/Q(n) for some y>=2, or from tau 1^T(H^T H+tau I)^(-1)1 <=n^2 epsilon(n)^2/Q(n) for some tau>0.

P3. If fixed finite u>=1 satisfies F(n,n^(1/u))/n ->c0 J(u)>0, that choice of y cannot satisfy the bound in P2 with epsilon(n)->0. The limit alone supplies no rate for varying u(n)->infinity.

P4. For V(n)=(log n)^(3/5)/(loglog n)^(1/5), a uniform bound |M(n)|<=Cn exp(-a(n)) with a(n)/V(n)->infinity is stronger in asymptotic scale than any fixed-positive-c VK bound n exp(-c V(n)). This sufficient benchmark is not claimed necessary for every improvement.

The section makes no assertion of obtaining the required witnesses/estimates. It argues that substituting sigma_min~|M|/(sqrtQ W) and product_others~sqrtQ W into the determinant identity merely reproduces |M|, and that fixed-index spectral laws alone do not justify growing products. Check that the later supplied text does not overstate necessity or claim no conceivable improvement can use these tools.
