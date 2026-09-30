**English** | [简体中文](upstream-proof.zh-CN.md)

# Complete upstream proof and connection to Theorem A, v1.0

Date: 2026-09-30. Scope: §§0–4 of the paper, connected explicitly to the reused algebraic module for §§5–7. This proof concerns Theorem A for star configurations. It excludes the reduction from general configurations. Claude (Opus 5.5) independently re-derived the five load-bearing upstream interfaces and found no error; it did not line-check this document.

References are to the [official PDF](https://math.apexin.net/papers/convex-nivat.pdf), published 2026-09-12, SHA-256 `7fd67831155f4226c010fd6af32de558b76643771e6be12dea4eebafa21745a8`. The downstream proof is [the constructive algebraic module](expanded-proof.md). The two proofs together establish the stated theorem; finite certificates are separate evidence.

## 1. Hypotheses, periods and the two cases

Fix a prime p. A star configuration is $\theta=\sum_{i=1}^mF_i:\mathbb Z^2\to\mathbb F_p$, where $m\ge2$; the primitive integer vectors $v_i$ are pairwise nonparallel; each $F_i$ has period $k_iv_i$, with $k_i\ge1$, and is not doubly periodic; and there are doubly periodic fields $L_i,R_i$ and integers $\ell_i\le r_i+1$ such that $F_i=L_i$ on $\pi_i<\ell_i$ and $F_i=R_i$ on $\pi_i>r_i$, with $\pi_i(z)=\det(v_i,z)$. Empty transition strips, unequal tails and nonprimitive tangential periods are allowed. Component addition is in $\mathbb F_p$; indicators, encodings, operators and dimensions are in characteristic zero.

Put

$$
\Gamma=\bigcap_j(\operatorname{Per}(L_j)\cap\operatorname{Per}(R_j)).
$$

A finite intersection of finite-index sublattices has finite index, so some positive integer N satisfies $N\mathbb Z^2\subseteq\Gamma$. Choose $\kappa_i$ to be a positive multiple of $k_i$ with $\kappa_iv_i\in\Gamma$, and put $H_i=\kappa_iv_i$. Each $H_i$ preserves both $F_i$ and **all** $L_j,R_j$. Preserving the tails alone would not suffice. Minimality of the positive multiple is unnecessary; the paper's choice in §0.3 has these properties.

Write $T^uf(z)=f(z+u)$, $D=\prod_i(T^{H_i}-1)$ and $I_a=\mathbf1[\theta=a]$. The Laurent ring is a domain and each factor is nonzero, hence $D\ne0$. For $C\subseteq[m]$, put $H_C=\sum_{i\in C}H_i$. Expand by **formal subsets C**: even when $H_C=H_{C'}$, retain both signs and multiplicities.

Case A means that $DI_a\ne0$ for some a. Case B means that $DI_a=0$ for every a, hence $Dg(\theta)=0$ for every single-site color function g. We close the cases separately.

## 2. Local functions, finite support and Case A

### 2.1 The global support bound of Lemma 1.1

Let $h(z)=\varphi(\theta|_{z+W})$ with W finite. If W is empty, h is constant and $Dh=0$. Otherwise put $E=\{H_C:C\subseteq[m]\}$, $M=E+W$ and $a_i=\max_{s\in M}|\pi_i(s)|$, and define widened strips

$$
\Sigma_i=\{z:\ell_i-a_i\le\pi_i(z)\le r_i+a_i\}.
$$

If $z\notin\Sigma_i$, then $F_i$ agrees with one fixed tail throughout $z+M$. When at most one direction is active, choose that direction as j, or any j if none is active. On $z+M$ the configuration has the form $G+B$, where G is $F_j$ or zero and B is the sum of the other selected tails; both are preserved by $H_j$. Pair C with $C\cup\{j\}$ in the formal expansion of D. Both windows are contained in $z+M$, their patterns agree pointwise, and their contributions cancel.

Thus

$$
\operatorname{supp}(Dh)\subseteq\bigcup_{i<j}(\Sigma_i\cap\Sigma_j).
$$

The intersection of two bounded-width strips in nonparallel directions is bounded, since $z\mapsto(\pi_i(z),\pi_j(z))$ is invertible. A finite union of such intersections contains finitely many lattice points. This bounds **all anchors**, without numerical boxes or any assumption that subset sums are distinct.

### 2.2 Injectivity in Lemma 1.2

For a nonzero finitely supported field J, $\widehat J(X)=\sum_zJ(z)X^{-z}$ is a nonzero Laurent polynomial. If $f(T)=\sum_uc_uT^u$ is nonzero, a change of variables gives

$$
\widehat{f(T)J}(X)=\left(\sum_uc_uX^u\right)\widehat J(X)\ne0.
$$

A nonzero Laurent operator therefore cannot annihilate a nonzero finitely supported field. The exponent is $X^u$, not $X^{-u}$.

### 2.3 Proposition 1.3 closes Case A independently

For a nonempty finite S, let $\mathcal L_S=\{\gamma_u:u\in\mathbb Z^2\}$, where $\gamma_u(s)=\theta(u+s)$ and duplicate patterns are removed. If $P_\theta(S)=|\mathcal L_S|\le|S|$, its $|S|+1$ rational functions $1,\mathbf1[\gamma(s)=a]$ are linearly dependent, giving

$$
\sum_{s\in S}c_s I_a(u+s)=c_0\quad\text{for all }u\in\mathbb Z^2.
$$

Put $q(T)=\sum_sc_sT^s$. If $q=0$, all $c_s=0$, and the nonempty pattern set forces $c_0=0$, contradicting nontriviality. Thus $q\ne0$. Applying D gives $q(DI_a)=0$, contradicting §2.2 because $DI_a$ is nonzero and finitely supported. Hence $P_\theta(S)\ge|S|+1$ for every nonempty finite window, including points and segments. Case A ends here, without the encoding or quadratic witness below.

Replacing each $H_i$ by a positive multiple multiplies D by a nonzero Laurent polynomial. By §2.2 and multiplication, respectively, nonvanishing in Case A and vanishing in Case B persist. Enlarging legal periods therefore preserves the case classification.

## 3. Case B: isolated limits, one spectrum-preserving encoding and divisibility

Fix Case B for the rest of the proof.

### 3.1 Isolated configurations and pure tails belong to the orbit closure

Fix i. Along $nH_i$, the component $F_i$ remains fixed while every other normal coordinate changes at nonzero speed $\pi_j(H_i)$. Because $H_i$ preserves all tails, on each fixed finite set the translates eventually stabilize pointwise to

$$
\Xi_i^\sigma=F_i+B_i^\sigma,\qquad
B_i^\sigma=\sum_{j\ne i}\varepsilon_j^\sigma,
$$

where $\varepsilon_j^\sigma$ is $R_j$ if $\sigma\pi_j(v_i)>0$, and $L_j$ otherwise. Thus $\Xi_i^\sigma\in X_\theta$.

Choose a lattice basis $(v_i,u_i)$ with $\det(v_i,u_i)=1$. Translating $\Xi_i^\sigma$ along $\pm Nu_i\in\Gamma$ yields $G_i^{\sigma,R}=R_i+B_i^\sigma$ and $G_i^{\sigma,L}=L_i+B_i^\sigma$. The orbit closure is closed and translation invariant, so both lie in $X_\theta$. The field $\Xi_i^\sigma$ is preserved by $H_i$; all pure tails G are preserved by every $H_j$.

### 3.2 Spectra, nonemptiness and a common encoding

Define $d_{i,\sigma,\epsilon,a}=\mathbf1[\Xi_i^\sigma=a]-\mathbf1[G_i^{\sigma,\epsilon}=a]$. It has period $H_i$ and vanishes on the corresponding entire left or right half-plane. Write $z=sv_i+tu_i$. For $\lambda^{\kappa_i}=1$, define

$$
P_\lambda=\kappa_i^{-1}\sum_{k=0}^{\kappa_i-1}\lambda^{-k}T^{kv_i},\qquad
(P_\lambda d)(sv_i+tu_i)=\lambda^s\widehat d_t(\lambda).
$$

Fourier decomposition for a finite cyclic group gives $\sum_\lambda P_\lambda d=d$ and $T^{v_i}P_\lambda d=\lambda P_\lambda d$. The projections commute with all Laurent operators. Let $\Lambda_i$ consist of frequencies occurring nontrivially in at least one difference field. If $\Lambda_i$ were empty, all color differences would vanish; in particular $\Xi_i^+=G_i^{+,R}$ would force $F_i=R_i$ to be doubly periodic, a contradiction. Thus $d_i=|\Lambda_i|\ge1$.

Put $A_i(t)=\prod_{\lambda\in\Lambda_i}(t-\lambda)$ and $A(T)=\prod_iA_i(T^{v_i})$. Each $A_i$ divides $t^{\kappa_i}-1$, is monic and squarefree with nonzero constant term, and annihilates every color difference in that direction. Newton-polytope multiplicativity gives

$$
\operatorname{Newt}(A)=Z=\sum_i[0,d_iv_i].
$$

Since at least two directions are nonparallel, Z has interior.

For every pair $(i,\lambda)$, **fix in advance** a choice of $\sigma,\epsilon,t$ such that $(\widehat d_{i,\sigma,\epsilon,a,t}(\lambda))_a$ is nonzero. Requiring

$$
\sum_aw(a)\widehat d_{i,\sigma,\epsilon,a,t}(\lambda)\ne0
$$

excludes a proper rational linear subspace of $\mathbb Q^p$: a nonzero complex linear form is nonzero on some rational coordinate vector. Also exclude the finitely many hyperplanes $w(a)=w(a')$. A finite union of proper linear subspaces cannot cover a finite-dimensional vector space over an infinite field. Choose **one** rational w satisfying every condition, then clear denominators to obtain an integer injection. The same w retains every $\Lambda_i$; a different encoding is not selected for each frequency, and injectivity alone is not confused with preservation of spectra.

Fix this w and put $\eta=w(\theta)$. Case B gives both $D\eta=0$ and $D(\eta^2)=0$. Galois stability is not needed as a premise of the subsequent dimension argument.

### 3.3 One-sided vanishing forces a prime factor: Lemma 2.3

Suppose d has period $H_i$, vanishes on one half-plane, and has $P_\lambda d\ne0$. If $f(T)d=0$, then $f(T)P_\lambda d=0$. In lattice-basis variables $X=T^{v_i},Y=T^{u_i}$, this is $g(Y)c=0$, where $g(Y)=f(\lambda,Y)$ and $c(t)=\widehat d_t(\lambda)\ne0$.

If c vanishes at the right end, its nonempty integer support has a largest element $t_0$. Were $g\ne0$, take its smallest exponent $\beta_-$. At $t_0-\beta_-$ only $g_{\beta_-}c(t_0)$ survives, a contradiction. For left-end vanishing, take the smallest support point of c and largest exponent of g. Hence $g=0$. Coefficient by coefficient in Y, a one-variable Laurent polynomial vanishing at nonzero $\lambda$ is divisible by $X-\lambda$. Thus $(T^{v_i}-\lambda)\mid f$. Normal support may extend infinitely in the other direction.

### 3.4 Transfer relations to the closure, subtract, and assemble: Lemma 2.4

If $f(T)\eta=c$ is a constant relation on the whole plane, it holds for every translate. At each anchor it involves only finitely many colors, so it is closed in the product topology and passes to every $\chi\in X_\theta$. Substitute $\Xi_i^\sigma$ and $G_i^{\sigma,\epsilon}$ separately, then subtract:

$$
f(T)\bigl(w(\Xi_i^\sigma)-w(G_i^{\sigma,\epsilon})\bigr)=0.
$$

For each $\lambda\in\Lambda_i$, the common encoding retains that frequency in at least one such difference, so §3.3 gives $T^{v_i}-\lambda\mid f$.

Primitivity of $v_i$ permits a lattice basis, in which $\mathbb C[X^{\pm1},Y^{\pm1}]/(X-\lambda)\simeq\mathbb C[Y^{\pm1}]$ is a domain; hence each factor is prime. Associates in different directions would have translated equal two-point supports, forcing $v_i=\pm v_j$. Different roots in the same direction are also nonassociate. Unique factorization therefore gives **$A\mid f$**, without invoking the desired complexity bound.

## 4. Affine dimension budget and degenerate windows: Lemma 2.5

Fix nonempty finite S and define $\mathcal L_S$ as in §2.3. Put

$$
U_S=\operatorname{span}_{\mathbb Q}\{1,\gamma\mapsto w(\gamma(s)):s\in S\},\qquad
R_Z(S)=\{r\in\mathbb Z^2:r+Z\subseteq\operatorname{Conv}(S)\}.
$$

Since $0\in Z$, the set $R_Z(S)\subseteq\operatorname{Conv}(S)\cap\mathbb Z^2$ is finite.

The rational relation space is defined by homogeneous equations with rows $(-1,(\eta(u+s))_{s\in S})$ for all integer anchors u. Although there are infinitely many anchors, the rows lie in dimension $|S|+1$. Choose a rational row-space basis from the actual rows, using at most $|S|+1$ rows. Every other actual row is their rational linear combination. These finitely many equations are equivalent to the original system over both $\mathbb Q$ and $\mathbb C$. Rank is determined by nonzero minors and does not change under field extension. Consequently,

$$
\mathcal R_{\mathbb C}=\mathcal R\otimes_{\mathbb Q}\mathbb C,
\qquad \dim_{\mathbb C}\mathcal R_{\mathbb C}=\dim_{\mathbb Q}\mathcal R.
$$

For a nonzero complex relation $(c_0,(c_s))$, the polynomial $f=\sum_sc_sT^s$ is nonzero and satisfies $f\eta=c_0$. By §3.4, write $f=Ag$. Newton multiplicativity gives $Z+\operatorname{Newt}(g)=\operatorname{Newt}(f)\subseteq\operatorname{Conv}(S)$, hence $\operatorname{supp}(g)\subseteq R_Z(S)$. The map $(c_0,f)\mapsto g$ is linear and injective: multiplication has no zero divisors, and f uniquely determines $c_0$. Therefore

$$
\dim\mathcal R\le|R_Z(S)|,\qquad
\dim U_S\ge |S|+1-|R_Z(S)|.
$$

This budget uses only $\operatorname{supp}(f)\subseteq S$, without requiring lattice convexity of S. Here it is used only for the original theorem, with no stronger-bound claim.

If $R_Z(S)=\varnothing$, then $P_\theta(S)\ge\dim U_S\ge|S|+1$ and no quadratic witness is needed. Points and segments have convex hull of dimension at most one, while Z has interior; they therefore lie in this branch. A two-dimensional window may also have empty $R_Z(S)$ and is handled identically.

## 5. A global periodic background from actual sectors only

### 5.1 Lemma 3.1

The m distinct lines through the origin divide the plane into $2m$ open sectors. A sector K has sign vector $\epsilon(K)=(\operatorname{sign}\pi_i)_i$ and pure-tail sum $\Theta_{\epsilon(K)}$. Across a boundary ray $\sigma v_i$, neighboring sectors differ only in the choice of the ith tail; their other tails are determined by $\operatorname{sign}(\sigma\pi_j(v_i))$ and sum to $B_i^\sigma$. Their tail sums are precisely $G_i^{\sigma,L},G_i^{\sigma,R}$.

For each color,

$$
\mathbf1[G_i^{\sigma,R}=a]-\mathbf1[G_i^{\sigma,L}=a]
=d_{i,\sigma,L,a}-d_{i,\sigma,R,a},
$$

which is annihilated by $A_i(T^{v_i})$, hence by A. Actual sectors form a connected cycle in angular order, so $Ae_{\Theta_{\epsilon(K)}}$ is the same for every actual K; call it b. It is a doubly periodic vector field preserved by all $H_j$. No assertion about all $2^m$ arbitrary tail combinations is required.

### 5.2 The finite exceptional region of Lemma 3.2

Put $M_A=\operatorname{supp}(A)$. Choose integers $c_i\ge1+\max(|\ell_i|,|r_i|)$ and set $\rho_i=c_i+\max_{s\in M_A}|\pi_i(s)|>0$ and $\Sigma_i^A=\{z:|\pi_i(z)|\le\rho_i\}$. These slightly wider strips avoid irrelevant zero-width wording issues.

If no direction is active, each component on $z+M_A$ equals the tail determined by $\operatorname{sign}\pi_i(z)$. The anchor z itself belongs to an actual sector, so $(Ae_\theta)(z)=b(z)$.

All anchors with at least two active directions lie in the finite set $\bigcup_{i<j}(\Sigma_i^A\cap\Sigma_j^A)\cap\mathbb Z^2$.

If only i is active, write $z=tv_i+qu_i$ with $|q|\le\rho_i$. Define the explicit threshold

$$
B_i=\frac{\rho_i\max_{j\ne i}|\pi_j(u_i)|+\max_{j\ne i}\rho_j}
{\min_{j\ne i}|\pi_j(v_i)|}.
$$

Its denominator is positive. If $|t|>B_i$, then for every $j\ne i,s\in M_A$,

$$
|t|\,|\pi_j(v_i)|>|q|\,|\pi_j(u_i)|+\rho_j,
$$

so $|\pi_j(z+s)|>c_j$ with sign $\operatorname{sign}(t\pi_j(v_i))$. On all of $z+M_A$ we therefore have $\theta=\Xi_i^{\operatorname{sign}(t)}$. The operator A annihilates its color difference from either corresponding pure tail, and that tail belongs to an adjacent actual sector. Hence $(Ae_\theta)(z)=b(z)$.

A complete finite exceptional envelope is thus

$$
F=\bigcup_{i<j}(\Sigma_i^A\cap\Sigma_j^A)\cap\mathbb Z^2
\ \cup\ \bigcup_i\{tv_i+qu_i:t,q\in\mathbb Z,\ |q|\le\rho_i,\ |t|\le B_i\}.
$$

We have $\operatorname{supp}(Ae_\theta-b)\subseteq F$. The t threshold excludes the unbounded parts of every isolated strip; only finitely many anchors remain.

### 5.3 Proposition 3.3

Case B gives $De_\theta=0$, and $Db=0$. Since the operators commute, $D(Ae_\theta-b)=0$. The remainder has finite support by §5.2, so §2.2 and $D\ne0$ force each color coordinate of the remainder to vanish. Therefore

$$
Ae_\theta=b\quad\text{on all of }\mathbb Z^2,\qquad
A\eta=b_\eta=\sum_aw(a)b_a.
$$

The background $b_\eta$ is doubly periodic and preserved by **every** $H_i$. It may be nonzero; the conclusion must not be replaced by an unproved $A\eta=0$.

## 6. Nonzero strip fields and a genuine nonzero quadratic witness

### 6.1 Lemma 4.1

Put $Q_i=\prod_{j\ne i}(T^{H_j}-1)$ and $f_i=Q_i\eta$. Case B gives $(T^{H_i}-1)f_i=0$. Use this global period and let $T^{nH_i}\theta$ tend to $\Xi_i^+$. Finite operators pass pointwise through the eventually stable limit, yielding

$$
f_i=Q_iw(\Xi_i^+)=Q_i\delta_i=Q_i\delta_i',
$$

where $\delta_i=w(\Xi_i^+)-w(G_i^{+,R})$ and $\delta_i'=w(\Xi_i^+)-w(G_i^{+,L})$. Each shift $T^{H_j}$ occurring in $Q_i$ preserves the pure tails, so $Q_i$ annihilates them. These are global equalities. Put $a_i'=\max_{C\subseteq[m]\setminus\{i\}}|\pi_i(H_C)|$. The two one-sided vanishing statements give

$$
\operatorname{supp}(f_i)\subseteq\{\ell_i-a_i'\le\pi_i\le r_i+a_i'\}.
$$

Injectivity of w and the fact that $F_i$ is not doubly periodic imply $\delta_i\ne0$. Its normal support has a largest value $\pi^*$. Choose $z^*$ on this row with $\delta_i(z^*)\ne0$, and put

$$
C_{\min}=\{j\ne i:\pi_i(H_j)<0\}.
$$

Every $\pi_i(H_j)\ne0$. For any other subset C, $\pi_i(H_C)-\pi_i(H_{C_{\min}})>0$: the difference is the sum of added positive terms and absolute values of removed negative terms. The formal term with smallest projection is therefore unique. At $z^*-H_{C_{\min}}$, only this term reaches the largest nonzero row without exceeding it, giving $f_i=\pm\delta_i(z^*)\ne0$. Other nonextreme subset sums may collide, but the unique extreme term cannot coincide with another term and cannot cancel.

### 6.2 Lemma 4.2

For each fixed d, $J(d,z)=D_z[\eta(z)\eta(z+d)]$ is the difference of a finite-window local function, so §2.1 gives finite support. A common support bound for all d is unnecessary.

Choose $i\ne j$ and $x_i,x_j$ with $f_i(x_i)f_j(x_j)\ne0$. Put $d_0=x_j-x_i$ and $C(z)=f_i(z)f_j(z+d_0)$. Then $C(x_i)\ne0$, and C has finite support in the intersection of two nonparallel strips. By §2.2, $DC\ne0$.

Expanding both Q operators by formal subsets gives the finite identity

$$
DC=\sum_{C_1,C_2}\pm T^{H_{C_1}}
J(d_0+H_{C_2}-H_{C_1},\cdot).
$$

If every J vanished, the right side would be zero, a contradiction. Thus a genuinely nonzero J exists. Since $J(0,\cdot)=D(\eta^2)=0$, its displacement is nonzero. This proves existence of some d; restricting it to $Z-Z$ requires the downstream module and is not assumed here.

## 7. Connect the algebraic module and close Theorem A

The configuration premises of [the constructive module](expanded-proof.md) are now discharged as follows.

| Module input | Proof here | Boundary |
|---|---|---|
| Nonparallel integer directions, $m\ge2$, $A_i\mid t^{\kappa_i}-1$, $d_i\ge1$ | §§1, 3.2 | Primitive directions from the paper are retained |
| Integer encoding and annihilation of every single-site function by D | §§1, 3.2 | Case B only; Case A is already closed |
| Global $A\eta=b_\eta$, with each $H_i$ preserving the background | §5 | Zero background is not required |
| Every J is finitely supported and some J is nonzero | §6 | An arbitrary d is not assumed to be a nonzero witness |
| Budget $\dim U_S\ge\lvert S\rvert+1-\lvert R_Z(S)\rvert$ | §4 | Includes the empty translation-set branch |

The following retains the downstream logic explicitly.

**Two recurrences and the transform.** Using $A\eta=b_\eta$ and invariance of the background under every formal shift $H_C$, expand D and take the background outside the sum. This gives

$$
\sum_sA_sJ(d+s,z)=0,\qquad
\sum_sA_sJ(d-s,z+s)=0.
$$

No invalid finite-difference Leibniz rule is used. Put $K=\mathbb C(X_1,X_2)$, $R=K[Y_1^{\pm1},Y_2^{\pm1}]$, $a=A(Y)$ and $c=A(X/Y)$. For $\widehat J(d;X)=\sum_zJ(d,z)X^{-z}$, finite for each d, define a K-linear functional by $L(Y^d)=\widehat J(d;X)$. The change of variables in the second recurrence gives the positive exponent $X^s$. Since the recurrences hold for every d and L is K-linear, it annihilates all polynomial multiples of $(a,c)$.

**Spanning the quotient.** Module §§2–5 prove three classes of unit ideals, two CRT steps and

$$
R/(a,c)\simeq\prod_{i\ne j}R/(A_i(Y^{v_i}),A_j(X^{v_j}Y^{-v_j})).
$$

For an ordered pair $(i,j)$, take half-open parallelogram representatives r for lattice cosets. The exponents $r+\alpha v_i-\beta v_j$, $0\le\alpha<d_i,0\le\beta<d_j$, form a component basis and lie in $[0,d_iv_i]+[0,-d_jv_j]$. Multiplication by $E_{ij}=\prod_{k\ne i}a_k\prod_{l\ne j}c_l$ gives zero in the other components and is invertible in this one. The actual Laurent supports of these vectors lie in $Z-Z$. Inverses compute coefficients only; their supports need not lie in $Z-Z$. Thus the monomials with $d\in(Z-Z)\cap\mathbb Z^2$ span $R/(a,c)$.

If J vanished at all these d, L would vanish on the quotient, hence every J would vanish, contradicting §6. Consequently some $d\in(Z-Z)\cap\mathbb Z^2$ satisfies $d\ne0$ and $J(d,\cdot)\ne0$.

**Lattice points and the same witness.** The zonotope Z is centrally symmetric about $c_0/2$, where $c_0=\sum_id_iv_i$, so $Z-Z=2Z-c_0$. A unimodular triangulation of a lattice polygon shows that every $x\in2Z\cap\mathbb Z^2$ is a sum of two lattice points of Z. In a unimodular triangle containing $x/2$, the two nonbase barycentric coordinates multiplied by two are nonnegative integers whose sum is at most two; the six possibilities give sums of two vertices. Apply this to $x=d+c_0$ to obtain $q,q+d\in Z\cap\mathbb Z^2$. The local subdivision, termination and boundary details are in module §7.

Fix this nonzero witness d first, then q, and only then quantify over all windows S. For lattice-convex S and $r\in R_Z(S)$, both $r+q,r+q+d$ belong to S. Hence

$$
\Phi_r(\gamma)=w(\gamma(r+q))w(\gamma(r+q+d))
$$

is a window-pattern function. If a nontrivial combination $\sum_rc_r\Phi_r$ belonged to $U_S$, substituting every translated pattern and applying D would give

$$
\left(\sum_rc_rT^{r+q}\right)J(d,\cdot)=0.
$$

The exponents are distinct, so the operator in parentheses is nonzero. The field J is nonzero and finitely supported, contradicting §2.2. Thus these quadratic observables are independent modulo $U_S$, and

$$
P_\theta(S)\ge\dim U_S+|R_Z(S)|\ge|S|+1.
$$

This closes Case B when the translation set is nonempty. Together with Case A in §2.3 and the empty-set, point and segment branches in §4, it proves Theorem A under all its hypotheses. The quantifier order is $\exists d\,\exists q\,\forall S$, not a nonvanishing assertion for every geometrically legal d.

## 8. Verification boundary

This written mathematical verification uses Laurent unique factorization, Newton multiplicativity, finite-dimensional linear algebra and the reconstructed module; it is not formal certification. Random or finite-box experiments do not replace the general proof.

The two existing global examples and twelve algebraic inputs are reused, with no new coverage claim. See [reproduction](../REPRODUCE.md). The separate [Appendix C audit](appendix-c-audit.md) is not a dependency of this proof. Claude (Opus 5.5) independently re-derived the five load-bearing upstream interfaces and found no error; it did not line-check this document.
