# 第 15 章 非相对论 QED：原子与光

> 预计学时：30 ｜ 前置：第 6、9 章 ｜ 配套阅读：Cohen-Tannoudji 等《光子与原子》；Haroche & Raimond《Exploring the Quantum》；Milonni《量子真空》第 4 章
>
> 本章回到国际单位制，因为原子物理和量子光学的文献大多使用它。

## 学习目标

- 写出原子与量子化电磁场相互作用的哈密顿量，并知道偶极近似；
- 用费米黄金规则推导自发辐射率，算出氢原子 2P 态的寿命；
- 理解 Jaynes–Cummings 模型和真空 Rabi 振荡；
- 理解 Purcell 效应：环境如何改变自发辐射；
- 把这些内容接到本项目的腔 QED 与光电子发射问题上。

## 15.1 为什么需要非相对论 QED

原子中电子的速度约为 $\alpha c\approx c/137$，相对论效应很小。完整的 QED 计算过于繁重，而非相对论 QED 保留了量子化的电磁场，同时用薛定谔方程描述电子，足以处理绝大多数原子–光问题。

**Pauli–Fierz 哈密顿量**：

$$\hat H=\frac{[\hat{\mathbf p}-e\hat{\mathbf A}(\hat{\mathbf r})]^2}{2m}+V(\hat{\mathbf r})+\sum_{\mathbf k,\lambda}\hbar\omega_k\left(\hat a^\dagger_{\mathbf k\lambda}\hat a_{\mathbf k\lambda}+\frac12\right)$$

**偶极近似**：光的波长远大于原子尺寸，场在原子范围内近似均匀。做一个幺正变换后，相互作用化为

$$\hat V=-\hat{\mathbf d}\cdot\hat{\mathbf E}(0),\qquad \hat{\mathbf d}=e\hat{\mathbf r}$$

其中 $\hat{\mathbf E}$ 现在是算符，单个模式的电场为 $\hat{\mathbf E}=i\sqrt{\frac{\hbar\omega}{2\epsilon_0V}}\boldsymbol\epsilon(\hat a-\hat a^\dagger)$（$V$ 为量子化体积）。

## 15.2 自发辐射

初态：原子激发态 $|e\rangle$，场处于真空 $|0\rangle$。末态：原子基态 $|g\rangle$，场中有一个光子 $|1_{\mathbf k\lambda}\rangle$。

与半经典理论（第 6 章）的关键区别：$\langle1_{\mathbf k\lambda}|\hat a^\dagger|0\rangle=1\neq0$。**即使没有入射光，跃迁矩阵元也不为零**，因为 $\hat{\mathbf E}$ 中含有产生算符。

对所有方向和极化求和，用自由空间的模式密度，由费米黄金规则得到

$$\boxed{\Gamma=\frac{\omega^3|\mathbf d_{eg}|^2}{3\pi\epsilon_0\hbar c^3}}$$

这就是爱因斯坦 A 系数的第一性原理推导（L030）。

**氢原子 2P → 1S**：$\hbar\omega=10.2$ eV，$|\langle1s|z|2p_0\rangle|=\frac{128\sqrt2}{243}a_0\approx0.745a_0$，代入得 $\Gamma\approx6.27\times10^8\ \mathrm s^{-1}$，寿命 $\tau\approx1.60$ ns，与实验一致。

**两种图像**：自发辐射可以说是真空涨落"触发"的，也可以说是原子自身辐射场的反作用。对称排序下两者各贡献一半（L008）。

## 15.3 Jaynes–Cummings 模型

一个两能级原子与腔中 **单个** 光学模式耦合，并做旋转波近似：

$$\hat H=\hbar\omega_c\hat a^\dagger\hat a+\frac{\hbar\omega_a}{2}\hat\sigma_z+\hbar g\left(\hat a\hat\sigma_++\hat a^\dagger\hat\sigma_-\right),\qquad g=\frac{d}{\hbar}\sqrt{\frac{\hbar\omega}{2\epsilon_0V}}$$

$\hat\sigma_+=|e\rangle\langle g|$。哈密顿量只耦合 $|e,n\rangle$ 与 $|g,n+1\rangle$，每一对构成一个两能级问题（第 4 章习题 4.4）。

**真空 Rabi 振荡**：若共振、初态为 $|e,0\rangle$（激发原子、腔中无光子），原子会以频率 $2g$ 在 $|e,0\rangle$ 与 $|g,1\rangle$ 之间来回振荡：**原子把光子放进腔里，又从腔里收回来**。这与自由空间中不可逆的自发辐射截然不同，是真空可以被"设计"的最直接展示。

能谱分裂为 $\pm\hbar g$ 的两条，即 **真空 Rabi 分裂**，在微波腔、光学腔和超导电路中都已观测到。

当 $g$ 接近 $\omega$ 时，旋转波近似失效，进入超强耦合区，基态中含有虚光子（L053）。

## 15.4 Purcell 效应

若原子–腔耦合较弱，而腔的损耗较快，原子仍然不可逆地衰变，但速率被改变。腔内的模式密度在共振时被提高，衰变率增强因子为

$$F_P=\frac{3}{4\pi^2}\left(\frac{\lambda}{n}\right)^3\frac{Q}{V}$$

$Q$ 为品质因数，$V$ 为模式体积。高 $Q$、小 $V$ 的腔可以大幅加快自发辐射；失谐时则可以抑制自发辐射（L031）。

**核心结论**：自发辐射率不是原子的固有性质，而是原子与它所处的电磁真空共同决定的。

## 15.5 Casimir–Polder 力

原子在导体表面附近时，原子与表面之间有吸引力：短距离时 $\propto1/z^3$（范德瓦尔斯），长距离时由于推迟效应变为 $\propto1/z^4$（Casimir–Polder）。它可以理解为真空模式被表面改变后，原子的 Lamb 位移随位置变化（L002）。

## 15.6 光电离与时间

光电离是束缚态到连续态的跃迁。第 6 章的黄金规则给出电离速率，但阿秒实验测的是跃迁振幅的 **相位**：出射电子波包的延迟等于相位对能量的导数，即 Wigner 延迟（L003）。

把这一章的工具组合起来，就能提出本项目的一个具体问题（C003）：在腔中，电子感受到的真空模式密度改变了，光电离振幅的相位是否也会改变？

## 与本项目的联系

- 15.2–15.4 节是腔 QED 与腔量子材料（L010、L031、L053）的理论基础。
- 15.3 节中 $g$ 依赖模式体积 $V$：单个分子在大腔中的 $g$ 很小，这正是 C003 中对"腔中光电子延迟"持低信心的原因。
- 15.6 节把本教程与光电子发射时间（L003、L009、L012）的研究问题直接连接起来。

## 习题

**15.1** 用 $\Gamma=\frac{\omega^3|d|^2}{3\pi\epsilon_0\hbar c^3}$ 计算氢原子 2P → 1S 的寿命。（$|d|=e\times0.745a_0$，$a_0=5.29\times10^{-11}$ m，$\hbar\omega=10.2$ eV）

<details><summary>答案</summary>

$\omega=1.55\times10^{16}\ \mathrm{rad/s}$，$|d|=6.32\times10^{-30}$ C·m。$\Gamma=\frac{(1.55\times10^{16})^3\times(6.32\times10^{-30})^2}{3\pi\times8.85\times10^{-12}\times1.055\times10^{-34}\times(3\times10^8)^3}\approx6.3\times10^8\ \mathrm s^{-1}$，$\tau\approx1.6$ ns。
</details>

**15.2** 估算一个偶极矩 $d=2.5ea_0$ 的原子，在模式体积 $V=\lambda^3$（$\lambda=780$ nm）的腔中的真空电场 $E_{\rm vac}=\sqrt{\hbar\omega/2\epsilon_0V}$ 和耦合 $g/2\pi$。

<details><summary>答案</summary>

$\omega=2.42\times10^{15}$ rad/s，$V=4.75\times10^{-19}\ \mathrm m^3$，$E_{\rm vac}\approx1.7\times10^5$ V/m。$g=dE_{\rm vac}/\hbar\approx3.5\times10^{10}$ rad/s，$g/2\pi\approx5.6$ GHz。实际光学腔的模式体积通常大得多，$g$ 相应更小。
</details>

**15.3** 在 Jaynes–Cummings 模型中，求初态 $|e,n\rangle$ 时原子的 Rabi 频率。为什么即使 $n=0$ 也会振荡？

<details><summary>答案</summary>

$\langle g,n+1|\hat H|e,n\rangle=\hbar g\sqrt{n+1}$，Rabi 频率为 $2g\sqrt{n+1}$。$n=0$ 时仍为 $2g$，因为 $\hat a^\dagger|0\rangle\neq0$：真空可以接收一个光子。
</details>

**15.4** $Q=10^4$、$V=\lambda^3$（$n=1$）的腔，Purcell 因子是多少？

<details><summary>答案</summary>

$F_P=\frac{3}{4\pi^2}\times10^4\approx760$。
</details>
