# Verification of Theorem A for Star Configurations in the Convex Nivat Paper

This note verifies the full proof chain of Theorem A, for star configurations, in Sections 0–7 of Apex Intelligence, *The Convex Nivat Conjecture: A Complexity Lower Bound for Star Configurations, and a Reduction from Low Convex Complexity to Star Configurations*. The conclusion is $`P_\theta(S)\geq |S|+1`$ for every nonempty finite lattice-convex window $`S`$. The reduction from general low-complexity configurations in Section 8 and Appendix D is outside this verification. We also identify an explanatory error in Appendix C that does not affect this proof chain.

Source: [official PDF](https://math.apexin.net/papers/convex-nivat.pdf), published 2026-09-12, 891,962 bytes, SHA-256 `7fd67831155f4226c010fd6af32de558b76643771e6be12dea4eebafa21745a8`. References below use printed pages. Theorem A: p.2; Theorem T: p.4; Theorem 7.3: p.18. Manuscript **v1.2**; archive [v1.1](https://github.com/iamwangxi/apex-p03-nivat-theorem-a-validation/tree/v1.1). Expanded proofs: `proof/upstream-proof.md` and `proof/expanded-proof.md`.

## 1. Hypotheses, common periods and Case A

Fix a prime $`p`$. A star configuration is a sum $`\theta=\sum_{i=1}^m F_i:\mathbb Z^2\to\mathbb F_p`$, with $`m\geq2`$, pairwise nonparallel primitive integer directions $`v_i`$, and periods $`k_i v_i`$ of $`F_i`$, $`k_i\geq1`$. Each $`F_i`$ is not doubly periodic. There are doubly periodic tails $`L_i,R_i`$ and integers $`\ell_i\leq r_i+1`$ such that $`F_i=L_i`$ where $`\pi_i<\ell_i`$ and $`F_i=R_i`$ where $`\pi_i>r_i`$, with $`\pi_i(z)=\det(v_i,z)`$. Empty transition strips and unequal tails are allowed. Colors are added in $`\mathbb F_p`$; indicators, integer encodings, Laurent operators and dimensions below are in characteristic zero.

The intersection $`\Gamma`$ of the period lattices of all tails has finite index. Choose $`\kappa_i\in k_i\mathbb Z_{>0}`$ with $`H_i=\kappa_i v_i\in\Gamma`$. Each $`H_i`$ preserves its own component and every tail. Write

```math
T^u f(z)=f(z+u),\qquad D=\prod_i(T^{H_i}-1),\qquad I_a=\mathbf1[\theta=a].
```

The operator $`D`$ is a nonzero Laurent polynomial. In its expansion retain formal subsets $`C\subseteq\{1,\ldots,m\}`$ with $`H_C=\sum_{i\in C}H_i`$, even when different subsets give the same vector.

For a local function $`h(z)=\varphi(\theta|_{z+W})`$ with nonempty finite $`W`$, put $`M=W+\{H_C\}_C`$, $`a_i=\max_{s\in M}|\pi_i(s)|`$ and $`\Sigma_i=\{z:\ell_i-a_i\leq\pi_i(z)\leq r_i+a_i\}`$. Outside $`\Sigma_i`$ the whole stencil lies in one side’s tail, including when the transition strip is empty. Outside all pairwise strip intersections, at most one direction, say $`j`$, is active. The local configuration is its component plus fixed tails, all preserved by $`H_j`$. Pair subsets not containing $`j`$ with their union with $`\{j\}`$; the corresponding windows agree and their terms cancel. Thus $`\mathop{\mathrm{supp}}\nolimits(Dh)`$ lies in finitely many intersections of nonparallel strips, a finite set of lattice points. An empty $`W`$ gives a constant and $`Dh=0`$. This proves Lemma 1.1 (pp.5–6) globally.

If $`J`$ has nonzero finite support, then $`\widehat J(X)=\sum_z J(z)X^{-z}`$ is a nonzero Laurent polynomial, and

```math
\widehat{f(T)J}(X)=f(X)\widehat J(X)\ne0\qquad(f\ne0).
```

This proves Lemma 1.2 (p.6). In Case A, some $`DI_a\ne0`$. If $`P_\theta(S)\leq|S|`$ for a nonempty finite $`S`$, the $`|S|+1`$ rational functions $`1,\mathbf1[\gamma(s)=a]`$ on the complete translated pattern set are dependent. They yield a nonzero $`f(T)=\sum_{s\in S}c_sT^s`$ with $`f(T)I_a`$ constant. Applying $`D`$ contradicts Lemma 1.2. Proposition 1.3 (p.6) closes Case A for every nonempty finite window.

Henceforth Case B means $`DI_a=0`$ for every color. Consequently $`Dg(\theta)=0`$ for every single-site color function $`g`$, including both the encoding and its square used below.

## 2. One encoding preserves every exceptional frequency

For each $`i`$ and sign $`\sigma`$, the translates along $`\sigma nH_i`$ stabilize on every finite set to $`\Xi_i^\sigma=F_i+B_i^\sigma`$. Here $`B_i^\sigma`$ sums the right tail of component $`j\ne i`$ when $`\sigma\pi_j(v_i)>0`$, and its left tail otherwise. Common tail periods fix phases throughout the limit. Thus $`\Xi_i^\sigma`$ is in the orbit closure $`X_\theta`$. Choose a lattice basis $`(v_i,u_i)`$ of determinant one and $`N\mathbb Z^2\subseteq\Gamma`$. Translating this limit along $`\pm nNu_i`$ also gives the pure tails $`G_i^{\sigma,\epsilon}=\epsilon_i+B_i^\sigma`$, for $`\epsilon=L,R`$, in $`X_\theta`$.

The color differences

```math
\delta_{i,\sigma,\epsilon,a}=\mathbf1[\Xi_i^\sigma=a]-\mathbf1[G_i^{\sigma,\epsilon}=a]
```

are $`H_i`$-periodic and vanish on the corresponding entire half-plane. For $`\lambda^{\kappa_i}=1`$ use the cyclic Fourier projections

```math
P_\lambda=\frac1{\kappa_i}\sum_{k=0}^{\kappa_i-1}\lambda^{-k}T^{kv_i}.
```

Let $`\Lambda_i`$ contain the frequencies appearing nontrivially in some such difference. If it were empty, all color differences would vanish, forcing $`F_i`$ to equal a doubly periodic tail. Set

```math
d_i=|\Lambda_i|\geq1,\quad A_i(t)=\prod_{\lambda\in\Lambda_i}(t-\lambda),\quad
A(T)=\prod_i A_i(T^{v_i}),\quad Z=\sum_i[0,d_iv_i].
```

Each $`A_i`$ is monic, divides $`t^{\kappa_i}-1`$, and has nonzero constant term. It kills every corresponding color difference. Newton polygons multiply by Minkowski addition, so $`\mathop{\mathrm{Newt}}\nolimits(A)=Z`$, a two-dimensional lattice zonotope.

For each pair $`(i,\lambda)`$ choose one nonzero Fourier coefficient vector across colors, at a fixed normal coordinate and fixed choices of tails. Requiring its weighted sum to be nonzero excludes a proper rational linear subspace of $`\mathbb Q^p`$. Also exclude the hyperplanes where two color weights coincide. Finitely many proper subspaces cannot cover $`\mathbb Q^p`$. Choose a single rational weight vector outside all of them, then clear denominators. The resulting integer injection $`w:\mathbb F_p\to\mathbb Z`$ preserves all the $`\Lambda_i`$ simultaneously. Injectivity alone would not prove this. Fix $`\eta=w(\theta)`$; Case B gives $`D\eta=D(\eta^2)=0`$.

For Lemma 2.3 (p.9), let a one-sided-vanishing $`H_i`$-periodic difference have nonzero $`\lambda`$ projection and be killed by $`f(T)`$. In coordinates $`X=T^{v_i},Y=T^{u_i}`$, the projected sequence satisfies $`f(\lambda,Y)c=0`$, where $`c\ne0`$ and vanishes on one end of the integer line. If it vanishes on the right, use its largest nonzero index and the smallest exponent of a purported nonzero $`f(\lambda,Y)`$; exactly one term survives. The left-vanishing case uses the opposite extrema. Hence $`f(\lambda,Y)=0`$ and $`X-\lambda`$ divides $`f`$.

If $`f(T)\eta=c`$ is constant, it holds on the entire orbit closure: each anchor imposes a closed condition depending on finitely many coordinates. Apply it separately to $`\Xi_i^\sigma`$ and $`G_i^{\sigma,\epsilon}`$ before subtracting. The preserved frequencies and Lemma 2.3 give $`T^{v_i}-\lambda\mid f`$ for every $`\lambda\in\Lambda_i`$. Each factor is prime in the complex Laurent ring, since a primitive $`v_i`$ extends to a lattice basis and the quotient by $`X-\lambda`$ is a Laurent domain. Distinct roots and nonparallel directions give nonassociated factors. Their product therefore divides $`f`$: this proves Lemma 2.4 (pp.9–10).

## 3. The affine budget, including degenerate windows

For finite nonempty $`S`$ let $`\mathcal L_S`$ be all translated patterns, pulled back to $`S`$, and put

```math
U_S=\mathop{\mathrm{span}}\nolimits_{\mathbb Q}\{1,\gamma\mapsto w(\gamma(s)):s\in S\},\qquad
R_Z(S)=\{r\in\mathbb Z^2:r+Z\subseteq\mathop{\mathrm{Conv}}\nolimits(S)\}.
```

The rational relation space among these functions is defined by rows $`(-1,(\eta(u+s))_{s\in S})`$ for all integer anchors $`u`$. Its row space has a basis selected from at most $`|S|+1`$ actual rational rows. Thus the infinite system is equivalent to one finite rational system, whose rank is unchanged over $`\mathbb C`$.

For a nonzero complex relation $`f(T)\eta=c_0`$, Lemma 2.4 gives $`f=Ag`$. The nonzero $`f`$ uniquely determines $`c_0`$. Newton multiplication gives

```math
Z+\mathop{\mathrm{Newt}}\nolimits(g)=\mathop{\mathrm{Newt}}\nolimits(f)\subseteq\mathop{\mathrm{Conv}}\nolimits(S),
```

so $`\mathop{\mathrm{supp}}\nolimits(g)\subseteq R_Z(S)`$. Division by $`A`$ is an injective linear map from the relation space into the coefficient space supported there. Since $`0\in Z`$, this set is finite. Lemma 2.5 (p.10) follows:

```math
\dim_{\mathbb Q}U_S\geq |S|+1-|R_Z(S)|.
```

If $`R_Z(S)`$ is empty, this already proves the theorem. In particular, point and segment windows have this property because $`Z`$ has interior. Two-dimensional windows with empty $`R_Z(S)`$ are covered too.

## 4. A global periodic background, then a genuine witness

The $`m`$ direction lines have $`2m`$ actual open sectors. Across a boundary ray $`\sigma v_i`$, adjacent sector tails are precisely $`G_i^{\sigma,L}`$ and $`G_i^{\sigma,R}`$. Their color-indicator difference is killed by $`A_i`$, hence by $`A`$. Connectivity of the cyclic list of sectors shows that their images under $`A`$ are one common doubly periodic vector field $`b`$, preserved by every $`H_i`$ (Lemma 3.1, p.11). No statement about all formal tail combinations is needed.

Here is an explicit finite exceptional region for Lemma 3.2 (p.12). Put $`M=\mathop{\mathrm{supp}}\nolimits(A)`$, choose integers $`c_i\geq1+\max(|\ell_i|,|r_i|)`$, and let

```math
\rho_i=c_i+\max_{s\in M}|\pi_i(s)|,\qquad \Sigma_i=\{z:|\pi_i(z)|\leq\rho_i\}.
```

With no active strip, the entire stencil lies in an actual sector-tail configuration. With at least two active strips the anchor belongs to their bounded intersection. With only direction $`i`$ active write $`z=tv_i+qu_i`$, $`|q|\leq\rho_i`$, and set

```math
B_i=\frac{\rho_i\max_{j\ne i}|\pi_j(u_i)|+\max_{j\ne i}\rho_j}
{\min_{j\ne i}|\pi_j(v_i)|}.
```

The denominator is positive. If $`|t|>B_i`$, every other component on $`z+M`$ has the tail prescribed by $`\mathop{\mathrm{sign}}\nolimits(t\pi_j(v_i))`$. The whole stencil agrees with $`\Xi_i^{\mathop{\mathrm{sign}}\nolimits(t)}`$, whose image under $`A`$ equals the appropriate adjacent-sector image. Thus $`Ae_\theta-b`$ is supported in the finite set consisting of the pairwise strip intersections and the lattice boxes $`|q|\leq\rho_i,|t|\leq B_i`$ in these bases. Here $`e_\theta=(I_a)_a`$.

Case B and periodicity give $`D(Ae_\theta-b)=0`$. Lemma 1.2 forces this finite remainder to vanish identically. Proposition 3.3 (p.12) holds globally:

```math
Ae_\theta=b,\qquad A\eta=b_\eta=\sum_a w(a)b_a.
```

Every $`H_i`$ preserves the possibly nonzero $`b_\eta`$.

For Lemma 4.1 (p.13) set $`Q_i=\prod_{j\ne i}(T^{H_j}-1)`$ and $`f_i=Q_i\eta`$. Case B makes $`f_i`$ $`H_i`$-periodic. Passing along $`nH_i`$ to the isolation limit, then subtracting either pure tail, gives globally

```math
f_i=Q_i\bigl(w(\Xi_i^+)-w(G_i^{+,R})\bigr)
=Q_i\bigl(w(\Xi_i^+)-w(G_i^{+,L})\bigr).
```

The two one-sided vanishings bound its support in a strip parallel to $`v_i`$. The right-tail difference is nonzero by injectivity and non-double-periodicity, with a largest nonzero normal coordinate. In the formal expansion of $`Q_i`$, the subset $`\{j\ne i:\pi_i(H_j)<0\}`$ uniquely minimizes the normal displacement, since every $`\pi_i(H_j)\ne0`$. Evaluating at the largest nonzero row shifted by this minimum leaves exactly one nonzero term. Thus $`f_i\ne0`$ even when other subset sums collide.

Choose $`i\ne j`$ and points $`x_i,x_j`$ where these strip fields are nonzero. With $`d_0=x_j-x_i`$, the product $`C(z)=f_i(z)f_j(z+d_0)`$ is nonzero and finitely supported. Hence $`DC\ne0`$. Expanding both $`Q`$ operators expresses $`DC`$ as a finite signed sum of translates of

```math
J(d,z)=D_z[\eta(z)\eta(z+d)].
```

At least one $`J(d,\cdot)`$ is nonzero. Each fixed $`d`$ has finite support by Lemma 1.1, and $`J(0,\cdot)=D(\eta^2)=0`$. This proves Lemma 4.2 (pp.13–14).

## 5. Quotient algebra and localization of that witness

Write $`A(T)=\sum_s A_sT^s`$. The global background identity yields Lemma 5.1 (p.14):

```math
\sum_s A_sJ(d+s,z)=0,\qquad \sum_s A_sJ(d-s,z+s)=0.
```

These are $`D_z[\eta(z)b_\eta(z+d)]`$ and $`D_z[b_\eta(z)\eta(z+d)]`$. In the formal subset expansion the background is unchanged and factors out; $`D\eta=0`$ then applies. No differential Leibniz rule is used.

Set $`K=\mathbb C(X_1,X_2)`$, $`R=K[Y_1^{\pm1},Y_2^{\pm1}]`$, $`a_i=A_i(Y^{v_i})`$, $`c_i=A_i(X^{v_i}Y^{-v_i})`$, $`a=\prod_i a_i`$, $`c=\prod_i c_i`$. The reused constructive proof of Lemma 5.2 (pp.15–16) establishes

```math
R/(a,c)\simeq\prod_{i\ne j}R/(a_i,c_j),\qquad
\dim_K R/(a,c)=\sum_{i\ne j}|\det(v_i,v_j)|d_i d_j,
```

and spanning by $`Y^e`$ with $`e\in(Z-Z)\cap\mathbb Z^2`$.

First, $`(a_i,c_i)=R`$ follows by univariate Euclid: a common root would make the transcendental $`X^{v_i}`$ a product of constant roots. For $`i\ne k`$, choose a positive $`N`$ with $`Nv_j=\alpha\kappa_iv_i+\beta\kappa_kv_k`$ for integers $`\alpha,\beta`$. The identities $`(t-1)S_n(t)=t^n-1`$, with finite Laurent sums also for negative $`n`$, express $`Y^{Nv_j}-1`$ in $`(a_i,a_k)`$. Euclid applied to $`t^N-1`$ and $`t^{d_j}A_j(X^{v_j}/t)`$ then gives $`(a_i,a_k,c_j)=R`$. The involution $`Y^u\mapsto X^uY^{-u}`$ yields $`(a_i,c_j,c_\ell)=R`$ for $`j\ne\ell`$. Multiplying the witnesses over $`j`$ gives $`(a_i,a_k,c)=R`$, the needed merging step for CRT in $`R/(c)`$. CRT again in each $`R/(a_i)`$, where $`c_i`$ is a unit, gives the displayed product.

For component $`(i,j)`$, representatives $`r`$ in the half-open parallelogram $`\{\rho v_i-\tau v_j:0\leq\rho,\tau<1\}`$ split the Laurent ring into lattice cosets. Monic division in $`Y^{v_i}`$ and $`Y^{-v_j}`$ gives a basis with exponents

```math
r+\alpha v_i-\beta v_j,\qquad 0\leq\alpha<d_i,\quad 0\leq\beta<d_j.
```

Nonzero constant terms make both variables invertible; monic division remains valid over the first quotient even if it has zero divisors. There are $`|\det(v_i,v_j)|d_i d_j`$ basis vectors. Put $`E_{ij}=\prod_{k\ne i}a_k\prod_{\ell\ne j}c_\ell`$. It vanishes in other components and is a unit in its own. Expand the inverse times any desired component in the local basis, then multiply by $`E_{ij}`$. The resulting spanning vectors have support in

```math
\sum_{k\ne i}[0,d_kv_k]+\sum_{\ell\ne j}[0,-d_\ell v_\ell]
+[0,d_iv_i]+[0,-d_jv_j]=Z-Z.
```

No support bound on the inverse is needed.

Define a $`K`$-linear functional by $`L(Y^d)=\widehat J(d;X)=\sum_zJ(d,z)X^{-z}`$. Separate finite support for each $`d`$ suffices. The first recurrence kills all $`Y^da`$; changing variables $`z'=z+s`$ in the second contributes $`X^{+s}`$ and kills all $`Y^dc`$. Linearity kills the whole ideal $`(a,c)`$. If all $`J(d,\cdot)`$ with $`d\in Z-Z`$ vanished, the spanning theorem would force $`L=0`$, contrary to the genuine witness. Proposition 5.3 (pp.16–17) therefore gives a fixed nonzero $`d\in(Z-Z)\cap\mathbb Z^2`$ with $`J(d,\cdot)\ne0`$.

## 6. Two lattice sites and completion of Theorem A

For Lemma 6.1 (p.17), put $`c_0=\sum_i d_iv_i`$. Central symmetry gives $`Z-Z=2Z-c_0`$. For $`x=d+c_0\in2Z\cap\mathbb Z^2`$, take a lattice triangle in $`Z`$ containing $`x/2`$. Refine at nonvertex lattice points, keeping a nondegenerate closed subtriangle containing $`x/2`$, until it is unimodular. Positive integer normalized area strictly decreases; the companion proof gives the lattice-point construction and treats boundary points. In the final unimodular triangle, twice the two barycentric coordinates are nonnegative integers of sum at most two. The six possibilities express $`x`$ as the sum of two vertices. Reflection about $`c_0/2`$ gives lattice points $`q,q+d\in Z`$.

Apply this construction to the nonzero witness already fixed in Proposition 5.3. Fix $`q`$ next, before choosing a window: the quantifier order is $`\exists d\,\exists q\,\forall S`$. For lattice-convex $`S`$ and $`r\in R_Z(S)`$ the sites $`r+q,r+q+d`$ are in $`S`$. Define

```math
\Phi_r(\gamma)=w(\gamma(r+q))w(\gamma(r+q+d)).
```

If a nontrivial rational combination of these functions belonged to $`U_S`$, substitution of every translated pattern and application of $`D`$ would give

```math
\left(\sum_r c_rT^{r+q}\right)J(d,\cdot)=0.
```

The operator is nonzero because its exponents are distinct. The witness is nonzero with finite support, contradicting Lemma 1.2. Thus Lemma 7.2 (p.18) gives independence modulo $`U_S`$, and

```math
P_\theta(S)\geq\dim U_S+|R_Z(S)|\geq|S|+1.
```

Together with Case A and the empty-$`R_Z(S)`$ branch, this completes the theorem under its original star-configuration assumptions. We claim no stronger bound or additional class of windows here.

## 7. Appendix C: one explanatory error, no break in the chain

Remark 3.1′ (p.11) and Appendix C.3 (p.32) use a three-direction example to argue against equality after applying the full product $`A`$ to arbitrary tail combinations. Its directions are $`(1,0),(0,-1),(1,-1)`$; all tails depend only on the horizontal coordinate, and the vertical component and its isolation backgrounds do also. Thus its nonempty exceptional spectrum is $`\Lambda_2=\{1\}`$, giving the factor $`A_2=T^{(0,-1)}-1`$. This factor kills the color indicators of every one of the eight tail combinations, so the full $`A`$ kills them all. The displayed mixed difference has horizontal period-six values $`(-1,0,1,0,1,0)`$; applying $`A_1=T^{(2,0)}-1`$ gives $`(2,0,0,0,-2,0)`$. That valid single-factor calculation does not establish the claimed full-product counterexample. Whether the general arbitrary-tail extension holds under Case B remains unproved here. The main proof uses only actual sectors, so this error has no effect on Theorem A and is not a separate challenge submission. The companion audit also checks Observation C.1 (pp.31–32) under its stated $`m=2,L_i=R_i`$ assumptions; Appendix C's random experiments are not independently certified.

## 8. Reused evidence, new verification and AI disclosure

The new contribution is upstream certification and full-chain integration, closing the earlier module’s conditional premises. The constructive algebraic module, lattice construction, two global examples and twelve frozen inputs are reused supporting evidence, not new coverage or a second module submission.

The two global examples have respectively 347 and 401 complete translated patterns, witness supports of 12 and 32 points, and rational matrix ranks $`46\to55`$ established by integer minors and kernel vectors. The second has the genuine nonzero background $`A\eta=4`$. The archive includes global coverage proofs and exact certificates. The twelve algebraic inputs cover two to four directions, reversed orientations, negative determinants, nonprimitive directions, indices up to eleven and cyclotomic products. They do not assert twelve star configurations or relax the theorem’s hypotheses.

The saved rational certificates contain 163 basic unit identities, 46 local inverse identities and 128 local basis/spanning vectors for those twelve inputs. The standard-library checker reconstructs targets from the frozen inputs and checks exact integer/Fraction identities, component completeness and support. It imports no generator. Symbolic generation uses pinned SymPy only for optional regeneration. The archive's checking command is:

```sh
python3 -B code/verify_all.py
```

The full suite, including the symbolic gate and both examples, has fifteen checks and 368 prescribed negative controls; packaging records document the rerun. The theorem rests on the written arguments, including Laurent unique factorization, Newton multiplication and finite-dimensional linear algebra, not finite computations or a proof kernel.

OpenAI Codex and GPT contexts prepared the proofs, code and exposition. Separate GPT contexts reconstructed and reviewed the upstream chain. The checker’s GPT context did not read or call its generator. A fresh GPT context adversarially reviewed this manuscript and companion documents. Claude Opus 5.5 previously checked five load-bearing points of the reused algebraic module and reran its acceptance checks; this does not certify the new upstream chain. Claude (Opus 5.5) independently re-derived the five load-bearing upstream interfaces from the paper and found no error, but did not line-check this manuscript. These AI checks are not human expert endorsement. We make no claim of full-paper validation, novelty priority or award eligibility.
