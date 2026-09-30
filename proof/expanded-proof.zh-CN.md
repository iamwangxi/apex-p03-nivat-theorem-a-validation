[English](expanded-proof.md) | **简体中文**

# Nivat 代数模块构造证明 v1.1

本文是复用的下游模块证明，不是本包的总体验证范围声明。这里列出的配置前提由[上游证明](upstream-proof.md)解除，上游证明也处理 Case A 与仿射预算。二者合起来验证星形配置假设下的定理 A。下文所述既往 Claude 审阅仅适用于本模块；Claude（Opus 5.5）独立重推了五个上游承重接口，未发现错误；未逐行审阅本文件。

日期：2026-09-30。范围：Lemma 5.2 → Proposition 5.3 → Lemma 6.1 → Lemma 7.2；一般数学论证与固定输入计算证书分开。

本扩展证明纳入了全新 GPT 上下文对抗审阅后的修补，末节汇总。英文为准；中文为对应译本。

在下述输入前提下，三类单位理想、两次中国剩余定理（CRT）、分量基与支撑定位均可作显式构造，未发现影响这一主链的断点。本文是可独立审阅的证明骨架，不是整篇论文或星形配置前置结构的完整核验。证书与配置实例是经仓库独立检查器检查的单独证据，不用于证明本文的一般命题。

引用论文为 Apex Intelligence，[《The Convex Nivat Conjecture: A Complexity Lower Bound for Star Configurations, and a Reduction from Low Convex Complexity to Star Configurations》](https://math.apexin.net/papers/convex-nivat.pdf)，日期 2026-09-12，SHA-256 为 `7fd67831155f4226c010fd6af32de558b76643771e6be12dea4eebafa21745a8`，891,962 字节。页码均指 PDF 印刷页码。下述显式构造是对论文论证的补充。

## 1. 输入、系数域与证明边界

取非零、两两不平行的整向量 \(v_1,\ldots,v_m\)，\(m\ge2\)。论文另要求方向原始，见 §0.1，第 4 页；以下 Lemma 5.2 的构造本身不需要原始性。给定正整数 \(\kappa_i\) 及首一多项式

\[
A_i(t)\mid t^{\kappa_i}-1,\qquad d_i=\deg A_i\ge1.
\]

它们无重根，且常数项非零。论文由非空异常谱给出这些条件（Lemma 2.1，第 8 页）。可以在包含所有系数的特征零域 \(F\subseteq\mathbb C\) 中工作，这里系数指各 \(A_i\) 的系数；一般论证可取 \(F=\mathbb C\)，可有效表示的代数数输入可取一个数域。记

\[
K=F(X_1,X_2),\quad R=K[Y_1^{\pm1},Y_2^{\pm1}],\quad
a_i=A_i(Y^{v_i}),\quad c_i=A_i(X^{v_i}Y^{-v_i}),
\]
\[
a=\prod_i a_i,\quad c=\prod_i c_i,\quad
Z=\sum_i[0,d_iv_i].
\]

\(X_1,X_2\) 始终是独立不定元。非零 \(v\) 保证 \(X^v\) 在 \(F\) 上超越。所有分母都是非零多项式，表示 \(K\) 中的元素；不作数值特化。

闸门多项式都在 \(\mathbb Q[t]\)，故闸门证书可在 \(\mathbb Q(X_1,X_2)\) 上工作。不能由这一固定有理输入反推任意复系数输入的程序覆盖。论文的 Galois 稳定性备注（Remark 2.1′，第 8 页）另给出真实异常谱 \(A_i\in\mathbb Z[t]\) 的理由，但下面的一般证明不依赖该备注。

本轮从 Proposition 5.3 向后使用的配置前提为：

1. \(\eta=w(\theta)\) 为整数值单点编码；\(D=\prod_i(T^{H_i}-1)\)，\(H_i=\kappa_i v_i\)；对每个单点颜色函数 \(g(\theta)\)，均有 \(Dg(\theta)=0\)（Case B，式 (1.1)，第 6 页）。
2. \(A(T)\eta=b_\eta\)，且每个 \(H_i\) 都保持 \(b_\eta\)（Proposition 3.3，第 12 页）。
3. \(J(d,z)=D_z[\eta(z)\eta(z+d)]\) 对每个固定 \(d\) 有有限支撑，且某个 \(d\) 给出非零函数（Lemma 4.2，第 13–14 页）。

这些前提的使用点在 §§6–8 逐一标出；没有把整个 §§0–4 重新认证为正确。

## 2. 三类单位理想的 Bézout 构造

原论文以无公共零点、Nullstellensatz 和忠实平坦下降证明单位理想（Lemma 5.2，第 15–16 页）。本节给出可输出恒等式的替代路径。

### 2.1 第一类：\((a_i,c_i)=R\)

置 \(x=X^{v_i}\)、\(u=Y^{v_i}\)，在 \(F(x)[t]\) 中运行扩展 Euclid，输入

\[
P(t)=A_i(t),\qquad Q(t)=t^{d_i}A_i(x/t).
\]

二者互素：若某个共同根 \(\lambda\) 满足 \(P(\lambda)=0\)，则 \(\lambda\ne0\) 且为常数根；\(Q(\lambda)=0\) 会使 \(x/\lambda=\mu\) 也是 \(A_i\) 的常数根，从而 \(x=\lambda\mu\) 在 \(F\) 上代数，与超越性矛盾。即使 \(F\) 不是代数闭域，也可在其代数闭包中进行此反证。因此 Euclid 输出

\[
p(t)A_i(t)+q(t)t^{d_i}A_i(x/t)=1.
\]

代入 \(t=u\)，得到显式恒等式

\[
\boxed{p(Y^{v_i})a_i+q(Y^{v_i})Y^{d_i v_i}c_i=1.}\tag{B1}
\]

每个系数都是 \(R\) 中有限 Laurent 多项式。上面的互素论证保证二者的 resultant 非零；扩展 Euclid 只在系数域中除以非零元，无需在数值点检查 resultant。

### 2.2 第二类：\((a_i,a_k,c_j)=R\)，\(i\ne k\)，\(j\) 任意

这是Lemma 5.2（第 15 页）的构造化；允许 \(j=i\) 或 \(j=k\)。设

\[
\Delta=\det(v_i,v_k)\ne0,\quad
L=\operatorname{lcm}(\kappa_i,\kappa_k),\quad N=L|\Delta|.
\]

二维行列式恒等式给出

\[
\Delta v_j=\det(v_j,v_k)v_i+\det(v_i,v_j)v_k.
\]

故令

\[
\alpha=\frac{N\det(v_j,v_k)}{\Delta\kappa_i},\qquad
\beta=\frac{N\det(v_i,v_j)}{\Delta\kappa_k}
\]

可得整数 \(\alpha,\beta\) 及 \(Nv_j=\alpha\kappa_iv_i+\beta\kappa_kv_k\)。这里保留 \(\Delta\) 的符号；不能把所有分母替换成 \(|\Delta|\) 而漏掉方向符号。

对任意整数 \(n\)，定义有限 Laurent 几何和

\[
S_n(t)=\begin{cases}
\sum_{r=0}^{n-1}t^r,&n>0,\\
0,&n=0,\\
-\sum_{r=n}^{-1}t^r,&n<0.
\end{cases}
\quad (t-1)S_n(t)=t^n-1.
\]

置 \(U=Y^{\kappa_iv_i}\)、\(V=Y^{\kappa_kv_k}\)，以及已知的精确商

\[
Q_i(t)=\frac{t^{\kappa_i}-1}{A_i(t)},\qquad
Q_k(t)=\frac{t^{\kappa_k}-1}{A_k(t)}.
\]

展开 \(U^\alpha V^\beta-1=V^\beta(U^\alpha-1)+(V^\beta-1)\)，得到

\[
Y^{Nv_j}-1=P_i a_i+P_k a_k,\tag{2.1}
\]
\[
P_i=V^\beta S_\alpha(U)Q_i(Y^{v_i}),\qquad
P_k=S_\beta(V)Q_k(Y^{v_k}).
\]

接着置 \(x=X^{v_j}\)，在 \(F(x)[t]\) 中对 \(t^N-1\) 和 \(t^{d_j}A_j(x/t)\) 做扩展 Euclid。这两个多项式互素，因为共同根会使 \(t\) 为单位根、\(x/t\) 为单位根，从而使超越元 \(x\) 成为常数。输出

\[
f(t)(t^N-1)+g(t)t^{d_j}A_j(x/t)=1.
\]

代入 \(t=Y^{v_j}\) 并使用 (2.1)，即有

\[
\boxed{f(Y^{v_j})P_i a_i+f(Y^{v_j})P_k a_k+
g(Y^{v_j})Y^{d_jv_j}c_j=1.}\tag{B2}
\]

算法只需要整向量运算、有限 Laurent 几何和、精确多项式除法及一元扩展 Euclid。大 \(N\) 会影响代价，不影响终止与正确性。

### 2.3 第三类：\((a_i,c_j,c_\ell)=R\)，\(j\ne\ell\)，\(i\) 任意

定义 \(K\)-代数自同构

\[
\sigma(Y^u)=X^uY^{-u},\qquad \sigma|_K=\mathrm{id}.
\]

它是对合，并交换 \(a_s,c_s\)。先对三元组 \((a_j,a_\ell,c_i)\) 应用 (B2)，得到 \(p a_j+q a_\ell+r c_i=1\)；逐项作用 \(\sigma\) 后，

\[
\boxed{\sigma(r)a_i+\sigma(p)c_j+\sigma(q)c_\ell=1.}\tag{B3}
\]

此处只是 Laurent 替换，不需要引入第二组独立参数，也不改变 \(X_1,X_2\)。这实现Lemma 5.2（第 15 页）的对称论证。

## 3. 两次 CRT 及显式投影

### 3.1 把第三生成元从单个 \(c_j\) 合并成 \(c\)

对固定 \(i\ne k\)，从 (B2) 得到每个 \(j\) 的恒等式

\[
1=p_j a_i+q_j a_k+r_j c_j.
\]

把这些等式相乘；凡不是全选 \(r_jc_j\) 的项都含 \(a_i\) 或 \(a_k\)，按固定顺序归组，得到

\[
1=P_{ik}a_i+Q_{ik}a_k+R_{ik}c,
\qquad R_{ik}=\prod_jr_j.\tag{3.1}
\]

归组可以逐次乘法完成并保留三个系数，不必保存所有展开项。这证明 \(a_i,a_k\) 在 \(R/(c)\) 中两两生成单位理想。

### 3.2 第一次 CRT

对任意交换环 \(S\) 的两两 comaximal 元 \(f_1,\ldots,f_m\)，由

\[
u_{ik}f_i+v_{ik}f_k=1
\]

构造

\[
e_i=\left(\prod_{k\ne i}v_{ik}\right)\left(\prod_{k\ne i}f_k\right).
\]

则 \(e_i\equiv1\pmod{f_i}\)，且 \(e_i\equiv0\pmod{f_k}\)（\(k\ne i\)）。两两 comaximal 理想满足交等于积：对两个理想，若 \(s+t=1\)、\(s\in I,t\in J\)，则 \(z\in I\cap J\) 有 \(z=zt+zs\in IJ\)；再把模某个理想为 1 的等式相乘，证明该理想与其余理想之积仍 comaximal，归纳到有限多个理想。因而自然投影的核是 \((\prod f_i)\)，而 \((g_i)_i\mapsto\sum_i e_i g_i\) 是逆映射。

以 \(S=R/(c)\)、\(f_i=a_i\)，并用 (3.1) 取得所需的 \(u,v\)，得到

\[
R/(a,c)\simeq\prod_iR/(a_i,c).\tag{CRT1}
\]

这就是Lemma 5.2（第 15 页）的第一次 CRT，并给出了投影选择元的算法。

### 3.3 第二次 CRT

在 \(R/(a_i)\) 中，(B1) 给出 \(c_i\) 的逆元，故 \((c)=(\prod_{j\ne i}c_j)\)。对不同 \(j,\ell\ne i\)，(B3) 给出 \(c_j,c_\ell\) 两两 comaximal。使用同一显式 CRT 构造，

\[
R/(a_i,c)\simeq\prod_{j\ne i}R/(a_i,c_j),
\qquad
\boxed{R/(a,c)\simeq\prod_{i\ne j}R/(a_i,c_j).}\tag{CRT2}
\]

当 \(m=2\) 时，第二次只有一个非单位因子，无需三因子的 comaximal 检查。所有映射均为自然商投影，匹配Lemma 5.2（第 15 页）。

## 4. 非单模方向对、分量的基与维数

固定 \(i\ne j\)，置

\[
u=Y^{v_i},\quad w=Y^{-v_j},\quad
L_{ij}=\mathbb Zv_i+\mathbb Z(-v_j),\quad
\nu_{ij}=|\det(v_i,v_j)|.
\]

半开平行四边形

\[
\Pi_{ij}=\{\rho v_i-\tau v_j:0\le\rho,\tau<1\}
\]

中的整点是 \(\mathbb Z^2/L_{ij}\) 的唯一代表。可执行枚举法：枚举四个顶点外接整数矩形内的整点 \(r\)，用矩阵 \([v_i,-v_j]^{-1}\) 的有理运算检查两坐标属于 \([0,1)\)。结果恰有 \(\nu_{ij}\) 个。

对任意 \(d\in\mathbb Z^2\)，写 \([v_i,-v_j]^{-1}d=(\xi,\zeta)\)，取 \(s=\lfloor\xi\rfloor\)、\(t=\lfloor\zeta\rfloor\)，则

\[
r=d-sv_i+t v_j\in\Pi_{ij}\cap\mathbb Z^2,
\qquad Y^d=Y^r u^s w^t.
\]

唯一余类分解证明

\[
R=\bigoplus_{r\in\Pi_{ij}\cap\mathbb Z^2}Y^r K[u^{\pm1},w^{\pm1}].
\]

生成元 \(a_i=A_i(u)\)、\(c_j=A_j(X^{v_j}w)\) 属于该子环，故商也按相同直和分解；不会在不同余类之间产生附加关系。两一元多项式的首项、常数项均非零，分别给出恰为 \(d_i,d_j\) 维的一元商。具体地，若 \(P(t)=p_0+\cdots+p_dt^d\) 且 \(p_0p_d\ne0\)，则

\[
t^d\equiv-p_d^{-1}\sum_{s<d}p_st^s,
\qquad
t^{-1}\equiv-p_0^{-1}\sum_{s=1}^dp_st^{s-1}\pmod P.
\]

反复应用即约化任意整数次幂；而普通带余除法证明 \(1,t,\ldots,t^{d-1}\) 独立。

为明确两个变量之间没有额外的混合关系，令 \(B=K[u]/(A_i(u))\)。其常数项非零使 \(u\) 在 \(B\) 中可逆，且 \(B\) 的 \(K\)-基为 \(1,u,\ldots,u^{d_i-1}\)。令

\[
\widetilde A_j(w)=(X^{d_jv_j})^{-1}A_j(X^{v_j}w)\in K[w].
\]

这是次数为 \(d_j\) 的首一多项式，常数项是 \(K\) 的非零元。即使 \(B\) 有零因子，在 \(B[w]\) 中除以首一多项式仍有唯一余式：非零乘数与首一多项式之积的最高项系数不消失。因此 \(B[w]/(\widetilde A_j)\) 为自由 \(B\)-模，基为 \(1,w,\ldots,w^{d_j-1}\)；其常数项为单位又使 \(w\) 可逆。由此

\[
K[u^{\pm1},w^{\pm1}]/(A_i(u),A_j(X^{v_j}w))
\simeq B[w]/(\widetilde A_j(w))
\]

具有恰好 \(d_id_j\) 个元素的乘积基 \(u^\alpha w^\beta\)。再与上面的格余类直和合并，得到

\[
\mathcal B_{ij}=\{Y^{r+\alpha v_i-\beta v_j}:
r\in\Pi_{ij}\cap\mathbb Z^2,\ 0\le\alpha<d_i,\ 0\le\beta<d_j\}
\]

是 \(R/(a_i,c_j)\) 的基，不只是张成集。Lemma 5.2（第 15–16 页）给出张成论证；这里补充唯一余类约化与独立性。因此

\[
\dim_KR/(a_i,c_j)=\nu_{ij}d_id_j,
\qquad
\boxed{\dim_KR/(a,c)=\sum_{i\ne j}|\det(v_i,v_j)|d_id_j.}\tag{4.1}
\]

每个基指数 \(e\) 对 \(v_i,-v_j\) 的坐标分别位于 \([0,d_i)\)、\([0,d_j)\)，从而

\[
e\in P_{ij}:=[0,d_iv_i]+[0,-d_jv_j].\tag{4.2}
\]

半开端点不可改成闭区间来枚举代表，否则边界会重复；支撑上界采用闭多边形则无妨。

## 5. \(E_{ij}\) 的逆元、支撑与真正的张成集

Lemma 5.2（第 16 页）定义

\[
E_{ij}=\prod_{k\ne i}a_k\prod_{\ell\ne j}c_\ell.
\]

它在非 \((i,j)\) 分量消失：若 \(i'\ne i\)，因子 \(a_{i'}\) 消失；否则 \(j'\ne j\)，因子 \(c_{j'}\) 消失。

在 \((i,j)\) 分量，它可逆：

- 每个 \(k\ne i\)，(B2) 针对 \((a_i,a_k,c_j)\) 的 \(a_k\) 系数是 \(a_k\) 的一个逆元；
- 每个 \(\ell\ne j\)，(B3) 针对 \((a_i,c_j,c_\ell)\) 的 \(c_\ell\) 系数是 \(c_\ell\) 的一个逆元。

这些逆元的乘积 \(U_{ij}\) 满足 \(U_{ij}E_{ij}\equiv1\pmod{(a_i,c_j)}\)。也可以对 \(\ell=i\) 直接用 (B1)。边界索引没有遗漏。

给定任意商类 \(f\)，先取其 \((i,j)\) 投影，再把 \(U_{ij}f\) 用 §4 的唯一约化展开成 \(\sum_{b\in\mathcal B_{ij}}\lambda_{ij,b}b\)。CRT 保证

\[
f\equiv\sum_{i\ne j}\sum_{b\in\mathcal B_{ij}}
\lambda_{ij,b}E_{ij}b\pmod{(a,c)}.\tag{5.1}
\]

这证明实际用到的张成向量是 \(E_{ij}b\)。逆元 \(U_{ij}\) 仅用来计算标量系数，**其 Laurent 支撑不受 \(Z-Z\) 限制，证明也不需要这一限制**。

逐项直接估计支撑，无需用 Newton 多边形等号：

\[
\operatorname{supp}_Y(a_k)\subseteq[0,d_kv_k],\qquad
\operatorname{supp}_Y(c_\ell)\subseteq[0,-d_\ell v_\ell].
\]

乘积的每个实际非零项来自各因子指数相加，取消只会删掉指数。结合 (4.2)，对每个 \(b=Y^e\in\mathcal B_{ij}\)，

\[
\begin{aligned}
\operatorname{supp}_Y(E_{ij}Y^e)
&\subseteq\sum_{k\ne i}[0,d_kv_k]+
\sum_{\ell\ne j}[0,-d_\ell v_\ell]+P_{ij}\\
&=\sum_k[0,d_kv_k]+\sum_\ell[0,-d_\ell v_\ell]=Z-Z.
\end{aligned}\tag{5.2}
\]

所以 (5.1) 的每个张成向量自身已是指数落在 \(Z-Z\) 的有限单项式线性组合。由此严格推出

\[
\boxed{R/(a,c)\text{ is spanned by }\{Y^d:d\in(Z-Z)\cap\mathbb Z^2\}.}
\]

这完成 Lemma 5.2 的一般构造式证明。补构造可移除该引理对 Nullstellensatz、忠实平坦下降以及 Newton 乘积等号的依赖；不意味着整篇定理 A 已移除所有 Newton 多边形依赖（Lemma 2.5 仍用它）。

## 6. Proposition 5.3：双递推、变换符号及非零见证

先核对 Lemma 5.1 的接口。令 \(A(T)=\sum_sA_sT^s\)。由前提 \(A\eta=b_\eta\)，且 \(b_\eta\) 被每个 \(H_i\) 保持，Lemma 5.1（第 14 页）给出

\[
\sum_sA_sJ(d+s,z)=D_z[\eta(z)b_\eta(z+d)]=b_\eta(z+d)D\eta(z)=0.
\]

对第二个变量组合，\((d,z)\mapsto(d-s,z+s)\) 保持第二观察点 \(z+d\) 不变；故Lemma 5.1（第 14 页）给出

\[
\sum_sA_sJ(d-s,z+s)=D_z[b_\eta(z)\eta(z+d)]=b_\eta(z)D\eta(z+d)=0.\tag{6.1}
\]

这里不能将 \(D\) 当作满足普通 Leibniz 法则的微分算子；可提取背景，是因为其对所有形式平移 \(H_C\) 不变。

按Proposition 5.3（第 16 页），对每个固定 \(d\) 定义有限 Laurent 变换

\[
\widehat J(d;X)=\sum_zJ(d,z)X^{-z}\in K,
\qquad L(Y^d)=\widehat J(d;X),
\]

并延拓为 \(K\)-线性泛函 \(L:R\to K\)。不同 \(d\) 的支撑无需统一上界，因为 \(R\) 中每个输入仅含有限多个 \(Y\) 单项式。

第一个递推给 \(L(Y^da)=0\)。第二个递推的变量替换为 \(z'=z+s\)，所以

\[
\sum_zJ(d-s,z+s)X^{-z}=X^s\widehat J(d-s;X),
\]

从而 \(L(Y^dc)=0\)。关键正号 \(X^s\) 与 \(c=\sum_sA_sX^sY^{-s}\) 匹配，见Proposition 5.3（第 17 页）。任意 \(h(Y)=\sum_d k_dY^d\in R\) 是有限和，且 \(k_d\in K\)，所以
\[
L(ha)=\sum_dk_dL(Y^da)=0,\qquad L(hc)=\sum_dk_dL(Y^dc)=0.
\]
这里只把 \(K\) 中的系数提出 \(L\)，不把 \(Y\) 或一般 \(R\) 元素提出。因此 \(L\) 消灭整个理想 \((a,c)\)，不只是两个生成元。

若所有 \(J(d,\cdot)\) 对 \(d\in(Z-Z)\cap\mathbb Z^2\) 都为零，Lemma 5.2 的张成结论使 \(L\) 为零，于是所有有限 Laurent 多项式 \(\widehat J(d;X)\) 都为零。单项式的线性独立性推出所有 \(J(d,z)=0\)，与 Lemma 4.2 的非零前提矛盾。这重建 Proposition 5.3（第 17 页）。

最后，\(J(0,z)=D(\eta^2)(z)=0\)，因为 \(\eta^2=w'(\theta)\) 仍是单点颜色函数，Case B 杀掉所有这种函数。因此得到的非零见证满足 \(d\ne0\)，见Proposition 5.3（第 17 页）。

## 7. Lemma 6.1：构造两个整点

Lemma 6.1（第 17 页）使用二维格多边形的 unimodular 三角剖分。以下补充可执行的选点与终止说明。

令 \(c_0=\sum_i d_iv_i\in\mathbb Z^2\)。逐段取补点得 \(c_0-Z=Z\)，而凸性给 \(Z+Z=2Z\)，故

\[
Z-Z=2Z-c_0.
\]

给定 \(d\in(Z-Z)\cap\mathbb Z^2\)，置 \(x=d+c_0\)，则 \(x/2\in Z\)。\(Z\) 是二维格多边形，因为至少两方向不平行，所有顶点是整向量段端点的子集和。

构造一个含 \(x/2\) 的 unimodular 三角形：

1. 由有限顶点做有理凸包和扇形三角剖分，选一个含 \(x/2\) 的格三角形。
2. 若其整面积 \(D=|\det(B-A,C-A)|>1\)，其半开基本平行四边形有非零格代表 \(r=\alpha(B-A)+\beta(C-A)\)，\(0\le\alpha,\beta<1\)。若 \(\alpha+\beta\le1\)，点 \(A+r\) 在三角形中且非顶点；否则 \(B+C-A-r\) 在三角形中且非顶点。
3. 用该格点细分此三角形，丢弃面积为零的退化子三角形，再从包含 \(x/2\) 的非退化闭子三角形中选一个；这些闭三角形覆盖原三角形，故边界点也能选到，落入多个时任择一个。每个非退化子三角形的正整面积都严格小于 \(D\)，所以至多细分 \(D_0-1\) 次后终止于整面积 1，其中 \(D_0\) 为初始整面积。

只需局部沿 \(x/2\) 所在三角形递归；无需为了选这一点构造全多边形的相容精细剖分。

终态写成

\[
x/2=A+\alpha(B-A)+\beta(C-A),\qquad
\alpha,\beta\ge0,\ \alpha+\beta\le1.
\]

\((B-A,C-A)\) 为格基，故 \(2\alpha,2\beta\) 为非负整数，和至多 2。六种可能 \((0,0),(1,0),(0,1),(2,0),(0,2),(1,1)\) 分别给

\[
x=A+A,\ A+B,\ A+C,\ B+B,\ C+C,\ B+C.
\]

于是 \(x=p+q\)，\(p,q\in Z\cap\mathbb Z^2\)。输出

\[
q_0=c_0-q,\qquad q_1=p;
\quad q_0,q_1\in Z\cap\mathbb Z^2,\quad q_1-q_0=d.
\]

这给出 Lemma 6.1 的非平凡包含方向。反方向由两个 \(Z\) 中整点作差立得。与原文结论一致，没有使用任意高维格多胞体均正常这样的错误推广。

## 8. Lemma 7.2：窗口合法性与模线性观测量的独立性

**先固定 §6（Proposition 5.3）给出的见证 \(d\ne0\)，满足 \(J(d,\cdot)\ne0\) 且有限支撑。仅对这个 \(d\) 应用 §7，固定 \(q=q_0\)，使 \(q,q+d\in Z\cap\mathbb Z^2\)。**此后 \(d,q\) 不随窗口变化。对每个有限非空格凸 \(S\)，下文结论都成立；完整顺序为 \(\exists d\,\exists q\,\forall S\)，不是对 §7 的每个合法输入 \(d\) 均成立。例如 \(d=0\) 虽是 §7 的合法输入，却由 §6 满足 \(J(0,\cdot)=0\)，不能用于本节。

把每个平移模式拉回同一个窗口 \(S\)：

\[
\mathcal L_S=\{\gamma_u:S\to\mathbb F_p:\gamma_u(s)=\theta(u+s),\ u\in\mathbb Z^2\},
\qquad
U_S=\operatorname{span}_{\mathbb Q}\{1,\gamma\mapsto w(\gamma(s)):s\in S\}
\subseteq\{\mathcal L_S\to\mathbb Q\}.
\]

\(\mathcal L_S\) 包含全部平移实现的模式，重复模式只保留一次；不是有限方框采样得到的子集。由于字母表和 \(S\) 有限，\(\mathcal L_S\) 有限。定义

\[
R_Z(S)=\{r\in\mathbb Z^2:r+Z\subseteq\operatorname{Conv}(S)\}.
\]

由于 \(0\in Z\)，有 \(R_Z(S)\subseteq\operatorname{Conv}(S)\cap\mathbb Z^2=S\)，所以系数族及下列所有 Laurent 和均有限。若 \(r\in R_Z(S)\)，两个整点 \(r+q,r+q+d\) 位于 \(\operatorname{Conv}(S)\)，由格凸性都在 \(S\)。所以Lemma 7.1–7.2（第 18 页）的二次观测量

\[
\Phi_r(\gamma)=w(\gamma(r+q))w(\gamma(r+q+d))
\]

确实定义在 \(S\) 的全局模式集 \(\mathcal L_S\) 上。

设存在非零有理系数族 \((c_r)\) 和 \(\psi\in U_S\)，使 \(\sum_r c_r\Phi_r(\gamma)=\psi(\gamma)\) 对每个 \(\gamma\in\mathcal L_S\) 成立。代入所有实际平移模式，记 \(h(z)=\eta(z)\eta(z+d)\)，可写成

\[
\sum_r c_r h(u+r+q)=c_*+\sum_{s\in S}\mu_s\eta(u+s)\qquad(u\in\mathbb Z^2).
\]

对 \(u\) 施加 \(D\)：常数被差分杀掉，且 \(D\eta=0\)；另一方面 \(Dh=J(d,\cdot)\ne0\) 且有限支撑。因此

\[
\left(\sum_r c_rT^{r+q}\right)J(d,\cdot)=0.
\]

各 \(r+q\) 不同，所以括号内是非零 Laurent 多项式。有限支撑变换把这变成两个非零 Laurent 多项式的乘积为零，与整环性矛盾（Lemma 1.2，第 6 页）。因此 \(\{\Phi_r\}\) 在 \(\{\mathcal L_S\to\mathbb Q\}/U_S\) 中线性独立，重建Lemma 7.2（第 18 页）。

本步必须使用“对全部平移 \(u\)”的模式恒等式；有限采样模式矩阵上的数值关系本身不足以推出它。\(R_Z(S)=\varnothing\) 时独立性是空命题，论文最终主定理通过 Remark 2.6（第 10 页）处理此情形，见 Theorem 7.3 的证明（第 18 页）。

## 9. 闸门输入的纸面预测与后续核验边界

指定输入

\[
v_1=(1,0),\quad v_2=(0,1),\quad v_3=(1,2),\qquad
(A_1,A_2,A_3)=(t-1,t+1,t^2+1)
\]

可取 \((\kappa_1,\kappa_2,\kappa_3)=(1,2,4)\)，\((d_1,d_2,d_3)=(1,1,2)\)。

| 有序分量 \((i,j)\) | \(\lvert\det(v_i,v_j)\rvert\) | 分量维数 \(\nu_{ij}d_id_j\) |
|---|---:|---:|
| \((1,2),(2,1)\) | 1 | 各 1 |
| \((1,3),(3,1)\) | 2 | 各 4 |
| \((2,3),(3,2)\) | 1 | 各 2 |

总商维数为 \(1+1+4+4+2+2=14\)。这同时覆盖非单模方向对及非平凡单位根频谱。此值来自一般 CRT 与分量基证明，固定输入的证书须另外证明程序输出的每个恒等式。

本文未由此闸门输入构造星形配置，也不主张任意合法代数频谱必能被某个星形配置实现。生成器若只覆盖该闸门，不应被描述为所有 \(F,A_i,v_i\) 的通用实现。所附软件有其明确的有理输入边界；一般证明与有限证书相互独立。

## 10. 对抗审阅后纳入的修补

下表记录本版保留的数学澄清。实质遗漏属于本独立证明稿，而非原论文的遗漏。

|意见|严重度及归属|作者修补|范围判断|
|---|---|---|---|
|A1|实质；本独立稿的见证绑定遗漏|§8 明确固定 §6 的非零见证 d，再用 §7 固定 q，最后量化所有 S；列 d=0 作为不可套用的边界|原论文 §7 开头（第 18 页）已有该前提，不是原论文漏洞|
|A2|表述；模式集及 U_S 定义缺失|§8 定义拉回 S 的全部平移模式、单点仿射观测空间，明确恒等式逐模式成立，并证明 R_Z(S) 有限|不扩大为有限采样或任意线性观测空间|
|A3|表述；双商乘积基桥接省略|§4 逐次首一带余除法，允许中间商有零因子；常数项为单位确保 Laurent 化无额外关系|维数公式得到明确独立性证明；不是新发现原文结论错误|
|A4|表述；局部细分的边界实现细节|§7 丢弃退化子三角形，使用非退化闭三角形覆盖并任择；给 D_0−1 次下降上界|只在二维使用，不作高维推广|

这些澄清没有更改 B1–B3、两次 CRT 或支撑公式。全新 GPT 审阅者复核 v1.1 后关闭了四项意见。随后，来自不同模型家族的 Claude 核对了五个承重点并复跑验收入口。OpenAI Codex（GPT）准备本英文版及对应中文文本。这些检查不是人类专家认证，也不是形式化验证。
