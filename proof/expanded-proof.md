**English** | [简体中文](expanded-proof.zh-CN.md)

# Constructive proof of the Nivat algebraic module, v1.1

This is the reused downstream module proof, not the scope statement for this package. The configuration premises listed here are discharged by [the upstream proof](upstream-proof.md), which also handles Case A and the affine budget. Together they validate Theorem A under its star-configuration hypotheses. The historical Claude review described below applies to this module only; Claude (Opus 5.5) independently re-derived the five load-bearing upstream interfaces and found no error; it did not line-check this document.

Date: 2026-09-30. Scope: Lemma 5.2 → Proposition 5.3 → Lemma 6.1 → Lemma 7.2. General mathematical arguments are distinguished from computational certificates for fixed inputs.

This expanded proof incorporates the clarifications from an adversarial review in a fresh GPT context; they are summarized in the final section. The English text is authoritative; the Chinese text is its corresponding translation.

Under the input hypotheses below, the three classes of unit ideals, the two Chinese remainder theorem (CRT) steps, the component bases and the support bounds admit explicit constructions. No break in this chain was found. This is an independently reviewable proof outline, not a complete validation of the paper or the preceding structure theory of star configurations. Certificates and configuration examples are separate evidence checked by the repository's independent checkers; they are not used to establish the general statements here.

References are to Apex Intelligence, [*The Convex Nivat Conjecture: A Complexity Lower Bound for Star Configurations, and a Reduction from Low Convex Complexity to Star Configurations*](https://math.apexin.net/papers/convex-nivat.pdf), dated 2026-09-12, SHA-256 `7fd67831155f4226c010fd6af32de558b76643771e6be12dea4eebafa21745a8`, 891,962 bytes. Page references use the PDF's printed page numbers. The explicit constructions below supplement the paper's arguments.

## 1. Inputs, coefficient field and proof boundary

Take nonzero, pairwise nonparallel integer vectors \(v_1,\ldots,v_m\), with \(m\ge2\). The paper additionally requires primitive directions (§0.1, p.4); the construction for Lemma 5.2 below does not itself need primitivity. Let \(\kappa_i\) be positive integers and let the monic polynomials satisfy

\[
A_i(t)\mid t^{\kappa_i}-1,\qquad d_i=\deg A_i\ge1.
\]

They are squarefree and have nonzero constant terms. The paper obtains these conditions from the nonempty exceptional spectra (Lemma 2.1, p.8). Work over a characteristic-zero field \(F\subseteq\mathbb C\) containing all coefficients of the \(A_i\). The general argument may use \(F=\mathbb C\); effectively represented algebraic-number inputs may use a number field. Put

\[
K=F(X_1,X_2),\quad R=K[Y_1^{\pm1},Y_2^{\pm1}],\quad
a_i=A_i(Y^{v_i}),\quad c_i=A_i(X^{v_i}Y^{-v_i}),
\]
\[
a=\prod_i a_i,\quad c=\prod_i c_i,\quad
Z=\sum_i[0,d_iv_i].
\]

\(X_1,X_2\) remain independent indeterminates throughout. Nonzero \(v\) ensures that \(X^v\) is transcendental over \(F\). Every denominator is a nonzero polynomial representing an element of \(K\); no numerical specialization is made.

The gate polynomials all lie in \(\mathbb Q[t]\), so its certificate can work over \(\mathbb Q(X_1,X_2)\). This fixed rational input does not establish software coverage of arbitrary complex coefficients. The Galois-stability remark in the paper (Remark 2.1′, p.8) separately explains why the actual exceptional spectra give \(A_i\in\mathbb Z[t]\), but the general proof below does not depend on that remark.

The configuration hypotheses used from Proposition 5.3 onward are:

1. \(\eta=w(\theta)\) is an integer-valued single-site encoding; \(D=\prod_i(T^{H_i}-1)\), \(H_i=\kappa_i v_i\); for every single-site color function \(g(\theta)\), one has \(Dg(\theta)=0\) (Case B, equation (1.1), p.6).
2. \(A(T)\eta=b_\eta\), and every \(H_i\) preserves \(b_\eta\) (Proposition 3.3, p.12).
3. \(J(d,z)=D_z[\eta(z)\eta(z+d)]\) has finite support for each fixed \(d\), and some \(d\) gives a nonzero function (Lemma 4.2, pp.13–14).

Their uses are identified in §§6–8. The entirety of §§0–4 is not recertified here.

## 2. Bézout constructions for three classes of unit ideals

The paper uses absence of common zeros, the Nullstellensatz and faithfully flat descent to prove these unit-ideal statements (Lemma 5.2, pp.15–16). This section gives an alternative route that produces explicit identities.

### 2.1 First class: \((a_i,c_i)=R\)

Put \(x=X^{v_i}\), \(u=Y^{v_i}\), and run extended Euclid in \(F(x)[t]\) on

\[
P(t)=A_i(t),\qquad Q(t)=t^{d_i}A_i(x/t).
\]

They are coprime: if a common root \(\lambda\) satisfies \(P(\lambda)=0\), then \(\lambda\ne0\) and it is an algebraic constant root. The equation \(Q(\lambda)=0\) would make \(x/\lambda=\mu\) another constant root of \(A_i\); hence \(x=\lambda\mu\) would be algebraic over \(F\), contradicting transcendence. Even when \(F\) is not algebraically closed, this contradiction can be carried out after adjoining its algebraic constant roots. Euclid therefore produces

\[
p(t)A_i(t)+q(t)t^{d_i}A_i(x/t)=1.
\]

Substituting \(t=u\) gives the explicit identity

\[
\boxed{p(Y^{v_i})a_i+q(Y^{v_i})Y^{d_i v_i}c_i=1.}\tag{B1}
\]

Each coefficient is a finite Laurent polynomial in \(R\). Coprimality ensures that the resultant is nonzero. Extended Euclid divides only by nonzero elements of the coefficient field; no evaluation of the resultant at numerical points is needed.

### 2.2 Second class: \((a_i,a_k,c_j)=R\), \(i\ne k\), arbitrary \(j\)

This makes the corresponding step of Lemma 5.2 (p.15) constructive; \(j=i\) or \(j=k\) is allowed. Set

\[
\Delta=\det(v_i,v_k)\ne0,\quad
L=\operatorname{lcm}(\kappa_i,\kappa_k),\quad N=L|\Delta|.
\]

The planar determinant identity gives

\[
\Delta v_j=\det(v_j,v_k)v_i+\det(v_i,v_j)v_k.
\]

Thus setting

\[
\alpha=\frac{N\det(v_j,v_k)}{\Delta\kappa_i},\qquad
\beta=\frac{N\det(v_i,v_j)}{\Delta\kappa_k}
\]

gives integers \(\alpha,\beta\) and \(Nv_j=\alpha\kappa_iv_i+\beta\kappa_kv_k\). The sign of \(\Delta\) is retained: replacing every denominator by \(|\Delta|\) would lose the orientation sign.

For any integer \(n\), define the finite Laurent geometric sum

\[
S_n(t)=\begin{cases}
\sum_{r=0}^{n-1}t^r,&n>0,\\
0,&n=0,\\
-\sum_{r=n}^{-1}t^r,&n<0.
\end{cases}
\quad (t-1)S_n(t)=t^n-1.
\]

Put \(U=Y^{\kappa_iv_i}\), \(V=Y^{\kappa_kv_k}\), and use the known exact quotients

\[
Q_i(t)=\frac{t^{\kappa_i}-1}{A_i(t)},\qquad
Q_k(t)=\frac{t^{\kappa_k}-1}{A_k(t)}.
\]

Expanding \(U^\alpha V^\beta-1=V^\beta(U^\alpha-1)+(V^\beta-1)\) yields

\[
Y^{Nv_j}-1=P_i a_i+P_k a_k,\tag{2.1}
\]
\[
P_i=V^\beta S_\alpha(U)Q_i(Y^{v_i}),\qquad
P_k=S_\beta(V)Q_k(Y^{v_k}).
\]

Next put \(x=X^{v_j}\). In \(F(x)[t]\), apply extended Euclid to \(t^N-1\) and \(t^{d_j}A_j(x/t)\). These polynomials are coprime: a common root would make \(t\) a root of unity and \(x/t\) a root of unity, forcing the transcendental \(x\) to be a constant. The output is

\[
f(t)(t^N-1)+g(t)t^{d_j}A_j(x/t)=1.
\]

Substituting \(t=Y^{v_j}\) and using (2.1) gives

\[
\boxed{f(Y^{v_j})P_i a_i+f(Y^{v_j})P_k a_k+
g(Y^{v_j})Y^{d_jv_j}c_j=1.}\tag{B2}
\]

The algorithm needs only integer-vector arithmetic, finite Laurent geometric sums, exact polynomial division and univariate extended Euclid. A large \(N\) affects cost, not termination or correctness.

### 2.3 Third class: \((a_i,c_j,c_\ell)=R\), \(j\ne\ell\), arbitrary \(i\)

Define the \(K\)-algebra automorphism

\[
\sigma(Y^u)=X^uY^{-u},\qquad \sigma|_K=\mathrm{id}.
\]

It is an involution exchanging \(a_s,c_s\). First apply (B2) to \((a_j,a_\ell,c_i)\), obtaining \(p a_j+q a_\ell+r c_i=1\). Applying \(\sigma\) term by term gives

\[
\boxed{\sigma(r)a_i+\sigma(p)c_j+\sigma(q)c_\ell=1.}\tag{B3}
\]

This is only a Laurent substitution. It introduces no second set of independent parameters and leaves \(X_1,X_2\) unchanged. It implements the symmetry argument in Lemma 5.2 (p.15).

## 3. The two CRT steps and explicit projections

### 3.1 Merging the third generator from individual \(c_j\) to \(c\)

For fixed \(i\ne k\), (B2) gives, for each \(j\), an identity

\[
1=p_j a_i+q_j a_k+r_j c_j.
\]

Multiply these identities. Every term other than the product selecting only \(r_jc_j\) contains \(a_i\) or \(a_k\). Grouping in a fixed order gives

\[
1=P_{ik}a_i+Q_{ik}a_k+R_{ik}c,
\qquad R_{ik}=\prod_jr_j.\tag{3.1}
\]

The grouping can use successive multiplication while retaining only three coefficients, without storing every expanded term. This proves that \(a_i,a_k\) generate the unit ideal pairwise in \(R/(c)\).

### 3.2 First CRT

For any commutative ring \(S\) and pairwise comaximal elements \(f_1,\ldots,f_m\), start from

\[
u_{ik}f_i+v_{ik}f_k=1
\]

and construct

\[
e_i=\left(\prod_{k\ne i}v_{ik}\right)\left(\prod_{k\ne i}f_k\right).
\]

Then \(e_i\equiv1\pmod{f_i}\), and \(e_i\equiv0\pmod{f_k}\) for \(k\ne i\). Pairwise comaximal ideals have intersection equal to product. For two ideals, if \(s+t=1\), \(s\in I,t\in J\), then \(z\in I\cap J\) satisfies \(z=zt+zs\in IJ\). Multiplying identities that are 1 modulo a chosen ideal shows that it is still comaximal with the product of the others, so induction handles finitely many ideals. Thus the natural projection has kernel \((\prod f_i)\), and \((g_i)_i\mapsto\sum_i e_i g_i\) is its inverse on the quotient.

Use \(S=R/(c)\), \(f_i=a_i\), and (3.1) for the required \(u,v\), obtaining

\[
R/(a,c)\simeq\prod_iR/(a_i,c).\tag{CRT1}
\]

This is the first CRT in Lemma 5.2 (p.15), with an algorithm for its selector elements.

### 3.3 Second CRT

In \(R/(a_i)\), (B1) gives an inverse for \(c_i\), so \((c)=(\prod_{j\ne i}c_j)\). For distinct \(j,\ell\ne i\), (B3) makes \(c_j,c_\ell\) pairwise comaximal. Applying the same explicit CRT construction gives

\[
R/(a_i,c)\simeq\prod_{j\ne i}R/(a_i,c_j),
\qquad
\boxed{R/(a,c)\simeq\prod_{i\ne j}R/(a_i,c_j).}\tag{CRT2}
\]

When \(m=2\), the second step has only one nonunit factor and needs no three-generator comaximality check. All maps are natural quotient projections, as in Lemma 5.2 (p.15).

## 4. Nonunimodular direction pairs, component bases and dimensions

Fix \(i\ne j\), and put

\[
u=Y^{v_i},\quad w=Y^{-v_j},\quad
L_{ij}=\mathbb Zv_i+\mathbb Z(-v_j),\quad
\nu_{ij}=|\det(v_i,v_j)|.
\]

The lattice points in the half-open parallelogram

\[
\Pi_{ij}=\{\rho v_i-\tau v_j:0\le\rho,\tau<1\}
\]

are unique representatives of \(\mathbb Z^2/L_{ij}\). An executable enumeration scans the lattice points \(r\) in the integer bounding rectangle of the four vertices, then uses rational arithmetic with \([v_i,-v_j]^{-1}\) to test whether both coordinates belong to \([0,1)\). Exactly \(\nu_{ij}\) points remain.

For any \(d\in\mathbb Z^2\), write \([v_i,-v_j]^{-1}d=(\xi,\zeta)\) and take \(s=\lfloor\xi\rfloor\), \(t=\lfloor\zeta\rfloor\). Then

\[
r=d-sv_i+t v_j\in\Pi_{ij}\cap\mathbb Z^2,
\qquad Y^d=Y^r u^s w^t.
\]

The unique coset decomposition proves

\[
R=\bigoplus_{r\in\Pi_{ij}\cap\mathbb Z^2}Y^r K[u^{\pm1},w^{\pm1}].
\]

The generators \(a_i=A_i(u)\), \(c_j=A_j(X^{v_j}w)\) belong to this subring, so the quotient has the same direct-sum decomposition: no additional relations mix different cosets. Both univariate polynomials have nonzero leading and constant coefficients, giving univariate quotients of dimensions exactly \(d_i,d_j\). Explicitly, if \(P(t)=p_0+\cdots+p_dt^d\) and \(p_0p_d\ne0\), then

\[
t^d\equiv-p_d^{-1}\sum_{s<d}p_st^s,
\qquad
t^{-1}\equiv-p_0^{-1}\sum_{s=1}^dp_st^{s-1}\pmod P.
\]

Repeated application reduces every integer power; ordinary polynomial division proves the independence of \(1,t,\ldots,t^{d-1}\).

To make explicit that no additional mixed relations occur between the two variables, let \(B=K[u]/(A_i(u))\). The nonzero constant term makes \(u\) invertible in \(B\), and \(B\) has a \(K\)-basis \(1,u,\ldots,u^{d_i-1}\). Let

\[
\widetilde A_j(w)=(X^{d_jv_j})^{-1}A_j(X^{v_j}w)\in K[w].
\]

This is monic of degree \(d_j\), with constant term a nonzero element of \(K\). Even if \(B\) has zero divisors, division by a monic polynomial in \(B[w]\) has a unique remainder: the leading coefficient of the product of a nonzero multiplier with a monic polynomial cannot vanish. Thus \(B[w]/(\widetilde A_j)\) is a free \(B\)-module with basis \(1,w,\ldots,w^{d_j-1}\). Its constant term is a unit, which also makes \(w\) invertible. Hence

\[
K[u^{\pm1},w^{\pm1}]/(A_i(u),A_j(X^{v_j}w))
\simeq B[w]/(\widetilde A_j(w))
\]

has a product basis with exactly \(d_id_j\) elements \(u^\alpha w^\beta\). Combining this with the lattice-coset direct sum above shows that

\[
\mathcal B_{ij}=\{Y^{r+\alpha v_i-\beta v_j}:
r\in\Pi_{ij}\cap\mathbb Z^2,\ 0\le\alpha<d_i,\ 0\le\beta<d_j\}
\]

is a basis of \(R/(a_i,c_j)\), not just a spanning set. Lemma 5.2 (pp.15–16) gives the spanning argument; the unique coset reduction and independence are made explicit here. Therefore

\[
\dim_KR/(a_i,c_j)=\nu_{ij}d_id_j,
\qquad
\boxed{\dim_KR/(a,c)=\sum_{i\ne j}|\det(v_i,v_j)|d_id_j.}\tag{4.1}
\]

Each basis exponent \(e\) has coordinates with respect to \(v_i,-v_j\) in \([0,d_i)\), \([0,d_j)\), respectively. Consequently

\[
e\in P_{ij}:=[0,d_iv_i]+[0,-d_jv_j].\tag{4.2}
\]

Closed intervals cannot replace the half-open intervals when enumerating representatives, because boundary representatives would be repeated. A closed polygon is harmless for an upper bound on support.

## 5. Inverses of \(E_{ij}\), support and the actual spanning set

Lemma 5.2 (p.16) defines

\[
E_{ij}=\prod_{k\ne i}a_k\prod_{\ell\ne j}c_\ell.
\]

It vanishes on every component other than \((i,j)\): if \(i'\ne i\), the factor \(a_{i'}\) vanishes; otherwise \(j'\ne j\), and the factor \(c_{j'}\) vanishes.

On component \((i,j)\), it is invertible:

- For every \(k\ne i\), (B2) for \((a_i,a_k,c_j)\) has a coefficient of \(a_k\) that is an inverse of \(a_k\).
- For every \(\ell\ne j\), (B3) for \((a_i,c_j,c_\ell)\) has a coefficient of \(c_\ell\) that is an inverse of \(c_\ell\).

Their product \(U_{ij}\) satisfies \(U_{ij}E_{ij}\equiv1\pmod{(a_i,c_j)}\). For \(\ell=i\), (B1) can also be used directly. No boundary index is omitted.

For an arbitrary quotient class \(f\), first take its \((i,j)\) projection, then reduce \(U_{ij}f\) uniquely as in §4 to the expansion \(\sum_{b\in\mathcal B_{ij}}\lambda_{ij,b}b\). CRT gives

\[
f\equiv\sum_{i\ne j}\sum_{b\in\mathcal B_{ij}}
\lambda_{ij,b}E_{ij}b\pmod{(a,c)}.\tag{5.1}
\]

Thus the actual spanning vectors are \(E_{ij}b\). The inverses \(U_{ij}\) serve only to compute scalar coefficients: **their Laurent support need not be contained in \(Z-Z\), and the proof requires no such bound**.

Estimate support directly, term by term, without a Newton-polygon equality:

\[
\operatorname{supp}_Y(a_k)\subseteq[0,d_kv_k],\qquad
\operatorname{supp}_Y(c_\ell)\subseteq[0,-d_\ell v_\ell].
\]

Each actual nonzero product term comes from adding exponents from the factors; cancellation can only remove exponents. Combining this with (4.2), for every \(b=Y^e\in\mathcal B_{ij}\),

\[
\begin{aligned}
\operatorname{supp}_Y(E_{ij}Y^e)
&\subseteq\sum_{k\ne i}[0,d_kv_k]+
\sum_{\ell\ne j}[0,-d_\ell v_\ell]+P_{ij}\\
&=\sum_k[0,d_kv_k]+\sum_\ell[0,-d_\ell v_\ell]=Z-Z.
\end{aligned}\tag{5.2}
\]

Every spanning vector in (5.1) is therefore already a finite linear combination of monomials with exponents in \(Z-Z\). This proves

\[
\boxed{R/(a,c)\text{ is spanned by }\{Y^d:d\in(Z-Z)\cap\mathbb Z^2\}.}
\]

This completes the general constructive proof of Lemma 5.2. These additional constructions remove this lemma's dependence on the Nullstellensatz, faithfully flat descent and the Newton-polygon product equality. They do not remove every Newton-polygon dependency from Theorem A: Lemma 2.5 still uses it.

## 6. Proposition 5.3: the two recurrences, transform sign and nonzero witness

First check the interface with Lemma 5.1. Write \(A(T)=\sum_sA_sT^s\). By the premise \(A\eta=b_\eta\), with \(b_\eta\) preserved by every \(H_i\), Lemma 5.1 (p.14) gives

\[
\sum_sA_sJ(d+s,z)=D_z[\eta(z)b_\eta(z+d)]=b_\eta(z+d)D\eta(z)=0.
\]

For the second combination of variables, \((d,z)\mapsto(d-s,z+s)\) preserves the second observation point \(z+d\). Thus Lemma 5.1 (p.14) gives

\[
\sum_sA_sJ(d-s,z+s)=D_z[b_\eta(z)\eta(z+d)]=b_\eta(z)D\eta(z+d)=0.\tag{6.1}
\]

Here \(D\) cannot be treated as a differential operator satisfying an ordinary Leibniz rule. The background can be factored out because it is invariant under every formal shift \(H_C\).

Following Proposition 5.3 (p.16), for each fixed \(d\) define the finite Laurent transform

\[
\widehat J(d;X)=\sum_zJ(d,z)X^{-z}\in K,
\qquad L(Y^d)=\widehat J(d;X),
\]

and extend to a \(K\)-linear functional \(L:R\to K\). No common bound on the supports for different \(d\) is needed: each input in \(R\) has only finitely many \(Y\)-monomials.

The first recurrence gives \(L(Y^da)=0\). In the second, substitute \(z'=z+s\), so that

\[
\sum_zJ(d-s,z+s)X^{-z}=X^s\widehat J(d-s;X),
\]

Hence \(L(Y^dc)=0\). The essential positive sign in \(X^s\) matches \(c=\sum_sA_sX^sY^{-s}\), as in Proposition 5.3 (p.17). Every \(h(Y)=\sum_d k_dY^d\in R\) is a finite sum with \(k_d\in K\), so
\[
L(ha)=\sum_dk_dL(Y^da)=0,\qquad L(hc)=\sum_dk_dL(Y^dc)=0.
\]
Only coefficients from \(K\) are taken outside \(L\), not \(Y\) or arbitrary elements of \(R\). Thus \(L\) annihilates the whole ideal \((a,c)\), not merely its two generators.

If every \(J(d,\cdot)\) for \(d\in(Z-Z)\cap\mathbb Z^2\) vanished, the spanning statement of Lemma 5.2 would force \(L\) to vanish, and then every finite Laurent polynomial \(\widehat J(d;X)\) would be zero. Independence of monomials would give \(J(d,z)=0\) everywhere, contradicting the nonzero premise from Lemma 4.2. This reconstructs Proposition 5.3 (p.17).

Finally, \(J(0,z)=D(\eta^2)(z)=0\), since \(\eta^2=w'(\theta)\) is still a single-site color function, and Case B annihilates all such functions. The resulting nonzero witness therefore satisfies \(d\ne0\), as in Proposition 5.3 (p.17).

## 7. Lemma 6.1: constructing two lattice points

Lemma 6.1 (p.17) uses unimodular triangulation of a planar lattice polygon. The following adds executable point selection and a termination argument.

Let \(c_0=\sum_i d_iv_i\in\mathbb Z^2\). Taking complements in each segment gives \(c_0-Z=Z\), while convexity gives \(Z+Z=2Z\). Hence

\[
Z-Z=2Z-c_0.
\]

Given \(d\in(Z-Z)\cap\mathbb Z^2\), put \(x=d+c_0\), so that \(x/2\in Z\). The set \(Z\) is a planar lattice polygon: at least two directions are nonparallel, and all vertices are subset sums of integer-vector segment endpoints.

Construct a unimodular triangle containing \(x/2\):

1. Compute the rational convex hull of the finite vertex set and a fan triangulation; choose a lattice triangle containing \(x/2\).
2. If its normalized area is \(D=|\det(B-A,C-A)|>1\), its half-open fundamental parallelogram has a nonzero lattice representative \(r=\alpha(B-A)+\beta(C-A)\), with \(0\le\alpha,\beta<1\). If \(\alpha+\beta\le1\), the point \(A+r\) is a nonvertex point in the triangle; otherwise \(B+C-A-r\) is such a point.
3. Subdivide at this lattice point, discard degenerate zero-area subtriangles, and choose a nondegenerate closed subtriangle containing \(x/2\). These closed triangles cover the original one, including its boundary; if several contain the point, choose any one. Every nondegenerate subtriangle has positive integer normalized area strictly less than \(D\). Thus after at most \(D_0-1\) refinements the process reaches normalized area 1, where \(D_0\) is the initial normalized area.

Only local recursion along the triangle containing \(x/2\) is needed; selecting this point does not require a compatible refined triangulation of the entire polygon.

In the final triangle, write

\[
x/2=A+\alpha(B-A)+\beta(C-A),\qquad
\alpha,\beta\ge0,\ \alpha+\beta\le1.
\]

Since \((B-A,C-A)\) is a lattice basis, \(2\alpha,2\beta\) are nonnegative integers with sum at most 2. The six possibilities \((0,0),(1,0),(0,1),(2,0),(0,2),(1,1)\) give, respectively,

\[
x=A+A,\ A+B,\ A+C,\ B+B,\ C+C,\ B+C.
\]

Thus \(x=p+q\), with \(p,q\in Z\cap\mathbb Z^2\). Output

\[
q_0=c_0-q,\qquad q_1=p;
\quad q_0,q_1\in Z\cap\mathbb Z^2,\quad q_1-q_0=d.
\]

This proves the nontrivial inclusion in Lemma 6.1. The reverse inclusion follows immediately by taking the difference of two lattice points in \(Z\). This agrees with the paper and does not use the false generalization that every lattice polytope in arbitrary dimension is normal.

## 8. Lemma 7.2: valid windows and independence modulo linear observables

**First, in §6 (Proposition 5.3), fix the witness \(d\ne0\), for which \(J(d,\cdot)\ne0\) and the support is finite. Apply §7 only to this \(d\), fixing \(q=q_0\) so that \(q,q+d\in Z\cap\mathbb Z^2\).** Thereafter \(d,q\) do not vary with the window. The conclusion below holds for each finite nonempty lattice-convex \(S\): the complete order is \(\exists d\,\exists q\,\forall S\), not a claim for every legal input of §7, namely \(d\). For example, \(d=0\) is legal in §7 but, by §6, satisfies \(J(0,\cdot)=0\), so it cannot be used here.

Pull each translated pattern back to the same window \(S\):

\[
\mathcal L_S=\{\gamma_u:S\to\mathbb F_p:\gamma_u(s)=\theta(u+s),\ u\in\mathbb Z^2\},
\qquad
U_S=\operatorname{span}_{\mathbb Q}\{1,\gamma\mapsto w(\gamma(s)):s\in S\}
\subseteq\{\mathcal L_S\to\mathbb Q\}.
\]

The set \(\mathcal L_S\) contains all patterns realized by translations, with each repeated pattern retained only once; it is not a subset sampled in a finite box. Since the alphabet and \(S\) are finite, \(\mathcal L_S\) is finite. Define

\[
R_Z(S)=\{r\in\mathbb Z^2:r+Z\subseteq\operatorname{Conv}(S)\}.
\]

Since \(0\in Z\), one has \(R_Z(S)\subseteq\operatorname{Conv}(S)\cap\mathbb Z^2=S\), so the coefficient families and all Laurent sums below are finite. If \(r\in R_Z(S)\), the two lattice points \(r+q,r+q+d\) lie in \(\operatorname{Conv}(S)\), and lattice convexity puts both in \(S\). The quadratic observable used in Lemmas 7.1–7.2 (p.18),

\[
\Phi_r(\gamma)=w(\gamma(r+q))w(\gamma(r+q+d))
\]

is therefore well-defined on the window \(S\) and its global pattern set \(\mathcal L_S\).

Suppose a nonzero rational coefficient family \((c_r)\) and \(\psi\in U_S\) satisfy \(\sum_r c_r\Phi_r(\gamma)=\psi(\gamma)\) for every \(\gamma\in\mathcal L_S\). Substituting all actual translated patterns, and writing \(h(z)=\eta(z)\eta(z+d)\), gives

\[
\sum_r c_r h(u+r+q)=c_*+\sum_{s\in S}\mu_s\eta(u+s)\qquad(u\in\mathbb Z^2).
\]

In the variable \(u\), apply \(D\). Differences annihilate the constant, and \(D\eta=0\); on the other hand \(Dh=J(d,\cdot)\ne0\) and has finite support. Thus

\[
\left(\sum_r c_rT^{r+q}\right)J(d,\cdot)=0.
\]

The exponents \(r+q\) are distinct, so the parenthesized Laurent polynomial is nonzero. The finite-support transform would make the product of two nonzero Laurent polynomials zero, contradicting the integral-domain property (Lemma 1.2, p.6). Therefore \(\{\Phi_r\}\) is linearly independent in \(\{\mathcal L_S\to\mathbb Q\}/U_S\), reconstructing Lemma 7.2 (p.18).

This step requires the pattern identity for all translations \(u\); a numerical relation in a matrix of sampled patterns alone does not imply it. If \(R_Z(S)=\varnothing\), independence is vacuous; the paper's final theorem handles this case through Remark 2.6 (p.10), as stated in the proof of Theorem 7.3 (p.18).

## 9. Predicted gate dimensions and the verification boundary

For the specified input

\[
v_1=(1,0),\quad v_2=(0,1),\quad v_3=(1,2),\qquad
(A_1,A_2,A_3)=(t-1,t+1,t^2+1)
\]

one may take \((\kappa_1,\kappa_2,\kappa_3)=(1,2,4)\), \((d_1,d_2,d_3)=(1,1,2)\).

| Ordered components \((i,j)\) | \(\lvert\det(v_i,v_j)\rvert\) | Component dimension \(\nu_{ij}d_id_j\) |
|---|---:|---:|
| \((1,2),(2,1)\) | 1 | 1 each |
| \((1,3),(3,1)\) | 2 | 4 each |
| \((2,3),(3,2)\) | 1 | 2 each |

The total quotient dimension is \(1+1+4+4+2+2=14\). This covers both a nonunimodular direction pair and nontrivial root-of-unity spectra. The value follows from the general CRT and component-basis proof; certificates for the fixed input must separately establish every identity output by the program.

No star configuration is constructed from this gate input, and no claim is made that every admissible algebraic spectrum is realizable by a star configuration. A generator covering only this gate must not be described as a universal implementation for all \(F,A_i,v_i\). The supplied software has its own stated rational-input boundary; the general proof is distinct from its finite certificates.

## 10. Clarifications incorporated after adversarial review

The following records the mathematical clarifications retained in this version. The substantive omission concerned this proof note, not an omission in the original paper.

| Finding | Severity and location | Clarification | Scope |
|---|---|---|---|
|A1|Substantive: omitted binding of the witness in this proof note|§8 fixes the nonzero witness d from §6, then q from §7, before quantifying over all S; d=0 is an excluded boundary case|The paper already gives the premise at the opening of §7 (p.18); this is not a flaw in the paper|
|A2|Exposition: missing definitions of the pattern set and U_S|§8 defines all translated patterns pulled back to S and the single-site affine observable space, states the identity pattern by pattern, and proves R_Z(S) finite|No extension to finite sampling or arbitrary linear observable spaces|
|A3|Exposition: omitted bridge to the product basis of the double quotient|§4 uses successive monic division, allowing zero divisors in the intermediate quotient; unit constant terms make Laurent localization introduce no extra relations|The dimension formula has an explicit independence proof; no error in the paper's conclusion is claimed|
|A4|Exposition: boundary details in local subdivision|§7 discards degenerate subtriangles and selects any containing nondegenerate closed subtriangle; the descent bound is D_0−1|Used only in the plane, with no higher-dimensional extension|

These clarifications leave B1–B3, both CRT steps and the support formula unchanged. A fresh GPT reviewer rechecked v1.1 and closed all four findings. Claude, from a different model family, subsequently checked the five load-bearing points and reran the acceptance entry points. OpenAI Codex (GPT) prepared this English version and the corresponding Chinese text. These checks are neither human expert certification nor formal verification.
