**English** | [简体中文](global-configurations.zh-CN.md)

# Two complete global configurations

These certificates concern two fixed configurations on the entire integer lattice. The finite lists are exhaustive because of the global reductions proved below. They do not constitute a proof of the full convex Nivat theorem. The algebraic boundary inputs form a separate test collection; no configuration is asserted for those inputs.

## Common geometry and translation convention

$$
v_i=(1,2i),\quad \pi_i(x,y)=y-2ix,\quad
\delta_i(x,y)=\mathbf 1[\pi_i(x,y)=i],\quad i\in\{0,1,2\}.
$$

Translation means $T^h f(z)=f(z+h)$. Every direction is primitive, and any two directions are nonparallel. Each indicator has period group exactly $\mathbb Z v_i$: a period must preserve its nonempty support line. Its tails are zero, with a single transition layer. Thus each indicator is singly periodic and is not doubly periodic.

The supports are pairwise disjoint on the integer lattice: the intersection of any two supporting lines has horizontal coordinate

$$
x=\frac{i-j}{2j-2i}=-\frac12\notin\mathbb Z.
$$

Both examples use the binary encoding $w(0)=0,w(1)=1$ and the same window and column ordering:

$$
S=\{0,\ldots,5\}\times\{0,\ldots,8\},\qquad |S|=54.
$$

Columns are ordered lexicographically by the horizontal coordinate and then the vertical coordinate. Define

$$
Z=\sum_{i=0}^2[0,v_i],\quad
q_0=(0,0),\quad q_1=(1,1),\quad d=q_1-q_0=(1,1).
$$

The counterclockwise vertices and the complete lattice-point set are

$$
(0,0),(1,0),(2,2),(3,6),(2,6),(1,4),
$$

$$
Z\cap\mathbb Z^2=\{(0,0),(1,0),(1,1),(1,2),(1,3),(1,4),
(2,2),(2,3),(2,4),(2,5),(2,6),(3,6)\}.
$$

For an independent membership test, write $\alpha_2=t$, $\alpha_1=y/2-2t$, and $\alpha_0=x-y/2+t$. The point belongs to the zonotope exactly when

$$
\max\!\left(0,\frac{y/2-1}{2},y/2-x\right)
\le\min\!\left(1,y/4,1-x+y/2\right).
$$

The coordinate ranges of the zonotope are $[0,3]$ and $[0,6]$. Containment in the rectangular window therefore gives exactly

$$
R_Z(S)=\{r\in\mathbb Z^2:r+Z\subseteq\operatorname{Conv}(S)\}
=\{0,1,2\}^2,\qquad |R_Z(S)|=9.
$$

In particular, the two observation points belong to the zonotope, and all translated observations lie in the window.

## Three-line baseline

Over the binary field take $F_i=\delta_i$ and $\theta=F_0+F_1+F_2$. The preceding geometry establishes the star-configuration assumptions: each component is singly periodic, not doubly periodic, and has doubly periodic tails. Disjoint support gives the integer identity

$$
\eta=w(\theta)=\delta_0+\delta_1+\delta_2,\qquad
D=\prod_{i=0}^2(T^{v_i}-1),\qquad D\eta=D(1-\eta)=0.
$$

Each summand is killed by its own difference factor, which proves these identities globally and puts this configuration in Case B. The common tail lattice is $\mathbb Z^2$; the exceptional spectra and factors are $\Lambda_i=\{1\}$ and $A_i(t)=t-1$.

For any anchor $u$, set $O_i=\{\pi_i(s):s\in S\}$ and $b_i=i-\pi_i(u)$. The translated window meets line $i$ exactly when $b_i\in O_i$. The offset-set cardinalities are $9,19,29$. Every anchor belongs to one of the following exhaustive classes.

- With no line hit, the pattern is zero; anchor $(0,1000)$ realizes it.
- With exactly one line hit, the pattern is $\mathbf 1[\pi_i(s)=b_i]$. Every offset is realized by $u=(1000,i-b_i+2i\cdot1000)$.
- With at least two lines hit, choose any pair $i<j$. The two offsets determine the anchor uniquely:

$$
u_x=\frac{b_j-b_i-(j-i)}{2j-2i},\qquad u_y=i+2iu_x-b_i.
$$

Retain exactly the integer solutions. A third line, if present, is included by evaluating the actual configuration at that anchor. For the single-line representatives, the other normal offsets have leading term $(2i-2j)1000$ with absolute value at least $2000$; the remaining bounded terms cannot cancel it. Hence these are actual single-line patterns, not hypothetical ones.

There are $425+57+1=483$ coverage events, $295$ distinct pair anchors, and exactly $347$ distinct patterns. `baseline/patterns.json` contains every event and a real anchor for every pattern. The checker reconstructs the classes with exact rational linear algebra and compares the entire sets. Global coverage follows from the exhaustive classification, not from a finite sampling box.

For the quadratic witness $J(d,z)=D_z[\eta(z)\eta(z+d)]$, the diagonal products $\delta_i(z)\delta_i(z+d)$ are periodic in direction $v_i$ and vanish after applying the corresponding factor. Every off-diagonal product has support given by

$$
\pi_i(z)=i,\qquad \pi_j(z)=j-\pi_j(d),\qquad i\ne j.
$$

These nonparallel equations have either one integer solution or none. The six ordered pairs thus produce the complete finite cross-term support. Applying the difference factors successively yields the full nonzero support of $J$, consisting of $12$ points. The checker also evaluates the original pixel formula at all $22$ possible support points. The global expansion proves vanishing elsewhere. All solutions and coefficients are in `baseline/witness.json`.

## Nonconstant periodic background

Set $B(x,y)=x\bmod2$ and, in the binary field, $F_0=B+\delta_0$, $F_1=\delta_1$, $F_2=\delta_2$. Write $C=\sum_i\delta_i\in\{0,1\}$ and $s=(-1)^x=1-2B$. Then

$$
\eta=B+sC,\qquad 2\eta=1-s+2\sum_i s\delta_i.
$$

The first component has tail $B$ on both sides and is periodic along $2v_0$. If it were doubly periodic, its sum with the doubly periodic background would make $\delta_0$ doubly periodic, since the intersection of two finite-index period lattices has finite index. This is impossible. The other components have zero tails and the period groups already proved above. Thus this is also a genuine star configuration.

The common tail lattice is $\Gamma=2\mathbb Z\times\mathbb Z$, so take $H_i=2v_i$. The isolated directional configuration is $B\oplus\delta_i$. Its color-indicator difference from the tail is $s\delta_i$ or its negative, and

$$
T^{v_i}(s\delta_i)=-s\delta_i,\quad s\delta_i\ne0,\quad
\Lambda_i=\{-1\},\quad A_i(t)=t+1.
$$

Consequently, with the following operators one has global identities

$$
A=\prod_i(T^{v_i}+1),\qquad D_2=\prod_i(T^{2v_i}-1),\qquad
A\eta=4,\quad D_2\eta=D_2(1-\eta)=0.
$$

Each line term is killed by its corresponding factor. On the background, the successive factors of $A$ give $1,2,4$. The checker expands $2\eta$ into translated constant, parity, and parity-times-line atoms; exact collection for $A$ gives the constant $8$, and for $D_2$ it gives zero. No finite sample is used to establish these identities. The configuration is in Case B, but its periodic tail after applying $A$ is nonzero.

For global pattern coverage retain the preceding offset sets and introduce the phase $p=u_x\bmod2$. There are two no-line patterns, realized by $(p,1000)$. For each single-line offset and phase, the pattern and a realizing anchor are

$$
\gamma_{i,b,p}(s_x,s_y)=((p+s_x)\bmod2)\oplus\mathbf1[s_y-2is_x=b],
\qquad u=(1000+p,i-b+2i(1000+p)).
$$

For at least two line hits, the same pair equations determine the anchor and therefore also its phase; a second independent phase must not be added. There are $425+114+2=541$ events and exactly $401$ distinct patterns. Every listed pattern has a real anchor, and every global anchor is covered by this classification. The complete collection is `periodic-background/patterns.json`.

The zonotope remains $Z=\sum_i[0,v_i]$, the Newton polygon of $A$, rather than the larger polygon of $D_2$. With a subscript denoting translation by $d$, expand

$$
\eta\eta_d=BB_d+Bs_dC_d+sCB_d+ss_d\sum_{i,j}\delta_i(\delta_j)_d.
$$

The background term is doubly periodic. Every single-line term and each diagonal product is periodic along the corresponding $2v_i$, so is killed by $D_2$. Since $s(z)s(z+d)=(-1)^{d_x}$, this gives the global support identity

$$
J(d,z)=(-1)^{d_x}D_2\!\left[\sum_{i\ne j}\delta_i(z)\delta_j(z+d)\right].
$$

The same six ordered intersection equations give all cross-term support. Successive differences give $32$ nonzero points; the direct pixel formula is checked at all $32$ possible support points. Here $d_x=1$, so the cross-term sign is $-1$. All points, coefficients, operators, and equations are in `periodic-background/witness.json`. Vanishing outside this finite set follows from the global expansion.

## Exact rational ranks and software boundary

For each configuration, the linear matrix has a constant column followed by all single-site values. The extended matrix appends the quadratic columns

$$
\Phi_r(\gamma)=\gamma(r+q_0)\gamma(r+q_1),\qquad r\in R_Z(S).
$$

The baseline matrix sizes are $347\times55$ and $347\times64$; the periodic-background sizes are $401\times55$ and $401\times64$. In both examples the rational ranks are exactly $46$ and $55$.

The independent checkers rebuild the matrices from the complete pattern lists. Each rank lower bound is certified by a specified minor, of order $46$ or $55$, whose integer determinant is recomputed with the Bareiss algorithm and equals $-1$. Each upper bound is certified by $9$ integer right-kernel vectors; every matrix-vector product is exactly zero, and the specified free columns form a nonzero diagonal matrix, proving independence. Rank-nullity gives the matching upper bounds $55-9=46$ and $64-9=55$. Thus the rank increase is exactly $9$ over the rationals.

The generator selects minors and constructs kernel vectors; the checker uses separate exact arithmetic to validate them. The periodic-background checker reuses only the baseline checker’s rank routine, zonotope membership routine, and assertion helper. It does not import or read any generator. Each global example has $6$ in-memory negative controls, all of which must be rejected. The shipped evidence files are read-only during acceptance.

The complete matrix and rank files are `baseline/matrices.json`, `baseline/rank-certificates.json`, `periodic-background/matrices.json`, and `periodic-background/rank-certificates.json`. Run `python3 -B code/verify_all.py` from the package root to check both configurations together with the symbolic gate and frozen algebraic inputs.

These configuration certificates and their checkers validate the two fixed examples. They do not by themselves establish the upstream general theorem, the later reduction, or formal correctness in a proof assistant.
