[English](submission.md) | **简体中文**

# 凸 Nivat 论文中星形配置定理 A 的验证

本文验证 Apex Intelligence 的 *The Convex Nivat Conjecture: A Complexity Lower Bound for Star Configurations, and a Reduction from Low Convex Complexity to Star Configurations* 中 Sections 0–7 关于星形配置定理 A 的完整证明链。结论为 $P_\theta(S)\geq |S|+1$，适用于每个非空有限格凸窗口 $S$。Section 8 与 Appendix D 中从一般低复杂度配置出发的归约不在本验证范围内。我们还指出 Appendix C 的一处说明错误，它不影响这条证明链。

来源：[官方 PDF](https://math.apexin.net/papers/convex-nivat.pdf)，发布日期 2026-09-12，891,962 字节，SHA-256 为 `7fd67831155f4226c010fd6af32de558b76643771e6be12dea4eebafa21745a8`。下文使用印刷页码。Theorem A：p.2；Theorem T：p.4；Theorem 7.3：p.18。正文版本：**v1.2**。配套归档：[GitHub v1.1](https://github.com/iamwangxi/apex-p03-nivat-theorem-a-validation/tree/v1.1)。扩展论证：`proof/upstream-proof.md` 和 `proof/expanded-proof.md`。

## 1. 假设、共同周期与 Case A

固定素数 $p$。星形配置为和 $\theta=\sum_{i=1}^m F_i:\mathbb Z^2\to\mathbb F_p$，其中 $m\geq2$，$v_i$ 为两两不平行的原始整方向，$k_i v_i$ 是 $F_i$ 的周期，$k_i\geq1$。每个 $F_i$ 都不是双周期的。存在双周期尾场 $L_i,R_i$ 及整数 $\ell_i\leq r_i+1$，使得 $F_i=L_i$ 于 $\pi_i<\ell_i$，$F_i=R_i$ 于 $\pi_i>r_i$，其中 $\pi_i(z)=\det(v_i,z)$。允许过渡条带为空、左右尾不相同。颜色在 $\mathbb F_p$ 中相加；下文的指标、整数编码、Laurent 算子和维数均在特征零中。

所有尾场周期格的交 $\Gamma$ 具有有限指数。选择 $\kappa_i\in k_i\mathbb Z_{>0}$，使 $H_i=\kappa_i v_i\in\Gamma$。每个 $H_i$ 同时保持自身分量和所有尾场。记

$$
T^u f(z)=f(z+u),\qquad D=\prod_i(T^{H_i}-1),\qquad I_a=\mathbf1[\theta=a].
$$

算子 $D$ 是非零 Laurent 多项式。展开时保留形式子集 $C\subseteq\{1,\ldots,m\}$ 及 $H_C=\sum_{i\in C}H_i$，即使不同子集给出相同向量也不合并丢项。

对局部函数 $h(z)=\varphi(\theta|_{z+W})$，其中 $W$ 非空有限，令 $M=W+\{H_C\}_C$、$a_i=\max_{s\in M}|\pi_i(s)|$ 和 $\Sigma_i=\{z:\ell_i-a_i\leq\pi_i(z)\leq r_i+a_i\}$。在 $\Sigma_i$ 外，整个模板都位于同一侧尾场中，包括过渡条带为空的情况。在所有两两条带交之外，至多一个方向活跃，记为 $j$。局部配置由该分量加固定尾场组成，均被 $H_j$ 保持。将不含 $j$ 的子集与其并上 $\{j\}$ 的子集配对，对应窗口相同，项相消。因此 $\operatorname{supp}(Dh)$ 位于有限个非平行条带交内，仅含有限个格点。$W$ 为空时局部函数为常数，$Dh=0$。这在全局证明了 Lemma 1.1（pp.5–6）。

若 $J$ 非零且有限支撑，则 $\widehat J(X)=\sum_z J(z)X^{-z}$ 为非零 Laurent 多项式，并且

$$
\widehat{f(T)J}(X)=f(X)\widehat J(X)\ne0\qquad(f\ne0).
$$

这证明 Lemma 1.2（p.6）。Case A 中，某个 $DI_a\ne0$。若 $P_\theta(S)\leq|S|$ 对某个非空有限 $S$ 成立，则完整平移模式集上的 $|S|+1$ 个有理函数 $1,\mathbf1[\gamma(s)=a]$ 线性相关。它们给出非零 $f(T)=\sum_{s\in S}c_sT^s$，使 $f(T)I_a$ 为常数。施加 $D$ 与 Lemma 1.2 矛盾。Proposition 1.3（p.6）对每个非空有限窗口闭合 Case A。

以下 Case B 指每个颜色均满足 $DI_a=0$。于是 $Dg(\theta)=0$ 对每个单点颜色函数 $g$ 成立，包括下文使用的编码及其平方。

## 2. 一个编码保留全部异常频率

对每个 $i$ 和符号 $\sigma$，沿 $\sigma nH_i$ 的平移在每个有限集上稳定为 $\Xi_i^\sigma=F_i+B_i^\sigma$。这里 $B_i^\sigma$ 对分量 $j\ne i$ 在 $\sigma\pi_j(v_i)>0$ 时取右尾，否则取左尾，再求和。共同尾周期在极限过程中固定相位。因此 $\Xi_i^\sigma$ 属于轨道闭包 $X_\theta$。取行列式为一的格基 $(v_i,u_i)$，以及 $N\mathbb Z^2\subseteq\Gamma$。沿 $\pm nNu_i$ 平移这一极限，又得到纯尾 $G_i^{\sigma,\epsilon}=\epsilon_i+B_i^\sigma$，其中 $\epsilon=L,R$；它们属于 $X_\theta$。

颜色差分

$$
\delta_{i,\sigma,\epsilon,a}=\mathbf1[\Xi_i^\sigma=a]-\mathbf1[G_i^{\sigma,\epsilon}=a]
$$

具有 $H_i$ 周期，并在相应整个半平面上为零。对 $\lambda^{\kappa_i}=1$ 使用循环 Fourier 投影

$$
P_\lambda=\frac1{\kappa_i}\sum_{k=0}^{\kappa_i-1}\lambda^{-k}T^{kv_i}.
$$

令 $\Lambda_i$ 包含在某个差分中非零出现的频率。若它为空，则所有颜色差分为零，迫使 $F_i$ 等于一个双周期尾场。置

$$
d_i=|\Lambda_i|\geq1,\quad A_i(t)=\prod_{\lambda\in\Lambda_i}(t-\lambda),\quad
A(T)=\prod_i A_i(T^{v_i}),\quad Z=\sum_i[0,d_iv_i].
$$

每个 $A_i$ 首一、整除 $t^{\kappa_i}-1$，且常数项非零。它消灭对应的全部颜色差分。Newton 多边形的乘法对应 Minkowski 加法，所以 $\operatorname{Newt}(A)=Z$，是二维格 zonotope。

对每对 $(i,\lambda)$，固定法向坐标和尾选择，选一个跨颜色的非零 Fourier 系数向量。要求其加权和非零会排除 $\mathbb Q^p$ 的一个真有理线性子空间。再排除任意两个颜色权重相等的超平面。有限个真子空间不能覆盖 $\mathbb Q^p$。一次选取位于全部子空间之外的有理权重向量，再清除分母。得到的整数单射 $w:\mathbb F_p\to\mathbb Z$ 同时保留全部 $\Lambda_i$。仅有单射性不足以保证这一点。固定 $\eta=w(\theta)$；Case B 给出 $D\eta=D(\eta^2)=0$。

对 Lemma 2.3（p.9），设一个单侧消失的 $H_i$ 周期差分具有非零 $\lambda$ 投影，并被 $f(T)$ 消灭。在坐标 $X=T^{v_i},Y=T^{u_i}$ 下，投影序列满足 $f(\lambda,Y)c=0$，其中 $c\ne0$ 且在整数轴一端为零。若它在右端为零，取其最大非零下标和假定非零的 $f(\lambda,Y)$ 的最小指数，恰有一项存活。左侧消失时取相反端的极值。因此 $f(\lambda,Y)=0$，$X-\lambda$ 整除 $f$。

若 $f(T)\eta=c$ 为常数，则它在整个轨道闭包上成立：每个锚点给出一个只依赖有限坐标的闭条件。先分别将其用于 $\Xi_i^\sigma$ 和 $G_i^{\sigma,\epsilon}$，再相减。保留的频率与 Lemma 2.3 给出：有 $T^{v_i}-\lambda\mid f$，对每个 $\lambda\in\Lambda_i$ 均成立。每个因子都是复 Laurent 环中的素元，因为原始 $v_i$ 可扩展为格基，而模 $X-\lambda$ 的商是 Laurent 整环。不同根和非平行方向给出不相伴因子，因此其乘积整除 $f$：这证明 Lemma 2.4（pp.9–10）。

## 3. 仿射预算，包括退化窗口

对非空有限 $S$，令 $\mathcal L_S$ 为回拉到 $S$ 上的所有平移模式，并置

$$
U_S=\operatorname{span}_{\mathbb Q}\{1,\gamma\mapsto w(\gamma(s)):s\in S\},\qquad
R_Z(S)=\{r\in\mathbb Z^2:r+Z\subseteq\operatorname{Conv}(S)\}.
$$

这些函数之间的有理关系空间由行 $(-1,(\eta(u+s))_{s\in S})$ 定义，取遍所有整数锚点 $u$。其行空间的基可从至多 $|S|+1$ 个实际有理行中选出。因此无限系统等价于有限有理系统，其秩在扩域到 $\mathbb C$ 后不变。

对非零复关系 $f(T)\eta=c_0$，Lemma 2.4 给出 $f=Ag$。非零 $f$ 唯一确定 $c_0$。Newton 乘法给出

$$
Z+\operatorname{Newt}(g)=\operatorname{Newt}(f)\subseteq\operatorname{Conv}(S),
$$

因此 $\operatorname{supp}(g)\subseteq R_Z(S)$。除以 $A$ 是从关系空间到以该集合为支撑的系数空间的线性单射。由于 $0\in Z$，该集合有限。得到 Lemma 2.5（p.10）：

$$
\dim_{\mathbb Q}U_S\geq |S|+1-|R_Z(S)|.
$$

若 $R_Z(S)$ 为空，这已经证明定理。由于 $Z$ 有内点，点窗口和线段窗口尤其具有这一性质。$R_Z(S)$ 为空的二维窗口也被覆盖。

## 4. 全局周期背景及真实见证

$m$ 条方向直线产生 $2m$ 个实际开扇区。跨越边界射线 $\sigma v_i$ 时，相邻扇区的尾场恰为 $G_i^{\sigma,L}$ 和 $G_i^{\sigma,R}$。其颜色指标差被 $A_i$ 消灭，因而也被 $A$ 消灭。扇区循环列表的连通性说明，它们在 $A$ 下的像为共同的双周期向量场 $b$，且被每个 $H_i$ 保持（Lemma 3.1，p.11）。无需关于全部形式尾组合的声明。

以下给出 Lemma 3.2（p.12）的明确有限异常区域。置 $M=\operatorname{supp}(A)$，取整数 $c_i\geq1+\max(|\ell_i|,|r_i|)$，令

$$
\rho_i=c_i+\max_{s\in M}|\pi_i(s)|,\qquad \Sigma_i=\{z:|\pi_i(z)|\leq\rho_i\}.
$$

没有活跃条带时，整个模板位于一个实际扇区尾配置中。至少两个条带活跃时，锚点位于其有界交内。只有方向 $i$ 活跃时，写 $z=tv_i+qu_i$、$|q|\leq\rho_i$，置

$$
B_i=\frac{\rho_i\max_{j\ne i}|\pi_j(u_i)|+\max_{j\ne i}\rho_j}
{\min_{j\ne i}|\pi_j(v_i)|}.
$$

分母为正。若 $|t|>B_i$，则每个其他分量在 $z+M$ 上都等于 $\operatorname{sign}(t\pi_j(v_i))$ 指定的尾。整个模板与 $\Xi_i^{\operatorname{sign}(t)}$ 相同，其在 $A$ 下的像等于对应的相邻扇区像。因此 $Ae_\theta-b$ 支撑于以下有限集合：所有两两条带交，以及各格基中满足 $|q|\leq\rho_i,|t|\leq B_i$ 的格点盒子。这里 $e_\theta=(I_a)_a$。

Case B 与周期性给出 $D(Ae_\theta-b)=0$。Lemma 1.2 迫使有限余项恒为零。Proposition 3.3（p.12）在全局成立：

$$
Ae_\theta=b,\qquad A\eta=b_\eta=\sum_a w(a)b_a.
$$

每个 $H_i$ 都保持可能非零的 $b_\eta$。

对 Lemma 4.1（p.13），置 $Q_i=\prod_{j\ne i}(T^{H_j}-1)$ 与 $f_i=Q_i\eta$。Case B 使 $f_i$ 具有 $H_i$ 周期。沿 $nH_i$ 取隔离极限，再减去任一纯尾，得到全局等式

$$
f_i=Q_i\bigl(w(\Xi_i^+)-w(G_i^{+,R})\bigr)
=Q_i\bigl(w(\Xi_i^+)-w(G_i^{+,L})\bigr).
$$

两个单侧消失式将其支撑限制在平行于 $v_i$ 的条带内。由单射性和非双周期性，右尾差分非零，并有最大非零法向坐标。在 $Q_i$ 的形式展开中，子集 $\{j\ne i:\pi_i(H_j)<0\}$ 唯一最小化法向位移，因为每个 $\pi_i(H_j)\ne0$。在最大非零行减去该最小位移处求值，恰剩一个非零项。因此即使其他子集和碰撞，仍有 $f_i\ne0$。

取 $i\ne j$，以及这些条带场分别非零的点 $x_i,x_j$。令 $d_0=x_j-x_i$，则乘积 $C(z)=f_i(z)f_j(z+d_0)$ 非零且有限支撑。因此 $DC\ne0$。展开两个 $Q$ 算子，可将 $DC$ 写成下式各平移的有限带符号和：

$$
J(d,z)=D_z[\eta(z)\eta(z+d)].
$$

至少有一个 $J(d,\cdot)$ 非零。Lemma 1.1 保证每个固定 $d$ 下支撑有限，且 $J(0,\cdot)=D(\eta^2)=0$。这证明 Lemma 4.2（pp.13–14）。

## 5. 商代数与该见证的定位

写 $A(T)=\sum_s A_sT^s$。全局背景恒等式给出 Lemma 5.1（p.14）：

$$
\sum_s A_sJ(d+s,z)=0,\qquad \sum_s A_sJ(d-s,z+s)=0.
$$

它们分别是 $D_z[\eta(z)b_\eta(z+d)]$ 和 $D_z[b_\eta(z)\eta(z+d)]$。在形式子集展开中，背景不变，可以提出求和，再使用 $D\eta=0$。没有使用微分 Leibniz 法则。

置 $K=\mathbb C(X_1,X_2)$、$R=K[Y_1^{\pm1},Y_2^{\pm1}]$、$a_i=A_i(Y^{v_i})$、$c_i=A_i(X^{v_i}Y^{-v_i})$、$a=\prod_i a_i$、$c=\prod_i c_i$。复用的 Lemma 5.2（pp.15–16）构造证明建立

$$
R/(a,c)\simeq\prod_{i\ne j}R/(a_i,c_j),\qquad
\dim_K R/(a,c)=\sum_{i\ne j}|\det(v_i,v_j)|d_i d_j,
$$

并证明可由 $Y^e$ 张成，其中 $e\in(Z-Z)\cap\mathbb Z^2$。

首先，一元 Euclid 算法给出 $(a_i,c_i)=R$：若有共同根，超越元 $X^{v_i}$ 就会成为常数根的乘积。对 $i\ne k$，取正整数 $N$，使 $Nv_j=\alpha\kappa_iv_i+\beta\kappa_kv_k$，其中 $\alpha,\beta$ 为整数。恒等式 $(t-1)S_n(t)=t^n-1$ 中，即使 $n$ 为负也可取有限 Laurent 和，由此将 $Y^{Nv_j}-1$ 写入 $(a_i,a_k)$。再对 $t^N-1$ 和 $t^{d_j}A_j(X^{v_j}/t)$ 应用 Euclid 算法，得到 $(a_i,a_k,c_j)=R$。对合 $Y^u\mapsto X^uY^{-u}$ 给出 $(a_i,c_j,c_\ell)=R$，其中 $j\ne\ell$。对所有 $j$ 的见证相乘，得到 $(a_i,a_k,c)=R$，完成在 $R/(c)$ 中使用 CRT 所需的合并步骤。再在各 $R/(a_i)$ 中使用 CRT，其中 $c_i$ 为单位，得到所示乘积。

对分量 $(i,j)$，取代表元 $r$ 位于半开平行四边形 $\{\rho v_i-\tau v_j:0\leq\rho,\tau<1\}$ 中，它们 将 Laurent 环分解为格余类。在 $Y^{v_i}$ 和 $Y^{-v_j}$ 中作首一除法，得到以如下指数为基：

$$
r+\alpha v_i-\beta v_j,\qquad 0\leq\alpha<d_i,\quad 0\leq\beta<d_j.
$$

非零常数项使两个变量都可逆；即使第一个商中有零因子，首一除法仍有效。基向量共 $|\det(v_i,v_j)|d_i d_j$ 个。置 $E_{ij}=\prod_{k\ne i}a_k\prod_{\ell\ne j}c_\ell$。它在其他分量为零，在自身分量可逆。把逆元乘上所需分量后在局部基中展开，再乘以 $E_{ij}$。所得张成向量的支撑包含于

$$
\sum_{k\ne i}[0,d_kv_k]+\sum_{\ell\ne j}[0,-d_\ell v_\ell]
 +[0,d_iv_i]+[0,-d_jv_j]=Z-Z.
$$

不需要对逆元的支撑作限制。

定义 $K$ 线性泛函，使 $L(Y^d)=\widehat J(d;X)=\sum_zJ(d,z)X^{-z}$。只需每个 $d$ 分别具有有限支撑。第一递推消灭所有 $Y^da$；第二递推中换元 $z'=z+s$ 产生 $X^{+s}$，并消灭所有 $Y^dc$。线性性使整个理想 $(a,c)$ 被消灭。若所有 $J(d,\cdot)$ 在 $d\in Z-Z$ 时均为零，则张成定理迫使 $L=0$，与真实见证矛盾。因此 Proposition 5.3（pp.16–17）给出固定非零 $d\in(Z-Z)\cap\mathbb Z^2$，使 $J(d,\cdot)\ne0$。

## 6. 两个格点与定理 A 的完成

对 Lemma 6.1（p.17），置 $c_0=\sum_i d_iv_i$。中心对称性给出 $Z-Z=2Z-c_0$。对 $x=d+c_0\in2Z\cap\mathbb Z^2$，在 $Z$ 中取包含 $x/2$ 的格三角形。在非顶点格点处细分，每次保留包含 $x/2$ 的非退化闭子三角形，直到单模。正整数归一化面积严格递减；配套证明给出了格点构造并处理边界点。在最终单模三角形中，两个重心坐标的两倍是非负整数，且和至多为二。六种可能将 $x$ 表示为两个顶点之和。关于 $c_0/2$ 反射即可得到格点 $q,q+d\in Z$。

将该构造用于 Proposition 5.3 已固定的非零见证。随后固定 $q$，再选窗口：量词顺序为 $\exists d\,\exists q\,\forall S$。对格凸 $S$ 和 $r\in R_Z(S)$，位置 $r+q,r+q+d$ 都属于 $S$。定义

$$
\Phi_r(\gamma)=w(\gamma(r+q))w(\gamma(r+q+d)).
$$

若这些函数的非平凡有理组合属于 $U_S$，则代入每个平移模式并施加 $D$，得到

$$
\left(\sum_r c_rT^{r+q}\right)J(d,\cdot)=0.
$$

算子的指数互异，所以它非零。见证非零且有限支撑，与 Lemma 1.2 矛盾。因此 Lemma 7.2（p.18）给出模 $U_S$ 的独立性，并有

$$
P_\theta(S)\geq\dim U_S+|R_Z(S)|\geq|S|+1.
$$

结合 Case A 和 $R_Z(S)$ 为空的分支，这在原始星形配置假设下完成定理。本文不主张更强下界或新增窗口类别。

## 7. 附录 C：一处说明错误，主链未断

Remark 3.1′（p.11）和 Appendix C.3（p.32）使用三方向实例，反对将完整乘积 $A$ 作用于任意尾组合后得到相等像。其方向为 $(1,0),(0,-1),(1,-1)$；全部尾场只依赖横坐标，纵向分量及其隔离背景也如此。因此其非空异常谱为 $\Lambda_2=\{1\}$，给出因子 $A_2=T^{(0,-1)}-1$。这一因子消灭全部八种尾组合的颜色指标，所以完整 $A$ 消灭它们全部。所列混合差分的横向六周期值为 $(-1,0,1,0,1,0)$；施加 $A_1=T^{(2,0)}-1$ 得到 $(2,0,0,0,-2,0)$。这个正确的单因子计算不足以证明所声称的完整乘积反例。Case B 下的一般任意尾推广是否成立，在此仍未证明。主证明只用实际扇区，所以这一错误不影响定理 A，也不另作质疑类投稿。配套审计还核对了 Observation C.1（pp.31–32），限于其所述 $m=2,L_i=R_i$ 假设；Appendix C 的随机实验没有获得独立认证。

## 8. 复用证据、新验证与 AI 披露

新增贡献是上游认证和全链接入，解除先前模块的条件性前提。代数构造模块、格点构造、两个全局实例和十二个固定输入是复用的辅助证据，不是新增覆盖或第二份模块投稿。

两个全局实例分别有 347 和 401 个完整平移模式，见证支撑分别含 12 和 32 个点，由整数子式和核向量认证的有理矩阵秩均为 $46\to55$。第二个具有真实非零背景 $A\eta=4$。归档包含全局覆盖证明和精确证书。十二个代数输入覆盖二至四个方向、方向反转、负行列式、非原始方向、至多十一的指数和分圆多项式乘积。它们不被称为十二个星形配置，也不放松定理假设。

这些固定输入的有理证书包含 163 个基本单位恒等式、46 个局部逆元恒等式和 128 个局部基／张成向量。标准库检查器从固定输入重建目标，并检查精确整数／Fraction 恒等式、分量完备性和支撑。它不导入生成器。符号生成仅为可选重生成使用固定版本 SymPy。归档检查命令为：

```sh
python3 -B code/verify_all.py
```

完整测试包括符号闸门和两个实例，共十五项检查及 368 个规定负控；打包记录记载实际复跑。定理建立在书面论证上，包括 Laurent 唯一分解、Newton 乘法和有限维线性代数，并非建立在有限计算或证明内核上。

OpenAI Codex 与 GPT 上下文起草了证明、代码和文字。独立 GPT 上下文重建并审阅了上游链。检查器的 GPT 上下文没有读取或调用生成器。全新 GPT 上下文对本稿与配套文档作了对抗审阅。Claude Opus 5.5 此前检查过复用代数模块的五个承重点并复跑其验收检查；这不认证新的上游链。Claude（Opus 5.5）依据论文独立重推了上游链的五个关键接口，未发现错误，但未逐行核对本稿。 这些 AI 检查不构成人类专家背书。我们不主张整篇论文验证、新颖性优先权或获奖资格。
