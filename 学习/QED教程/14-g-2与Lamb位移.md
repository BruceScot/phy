# 第 14 章 精密结果：g−2 与 Lamb 位移

> 预计学时：30 ｜ 前置：第 6、13 章 ｜ 配套阅读：Peskin & Schroeder 第 6.3 节；Milonni《量子真空》第 3 章；Weinberg《量子场论》第 1 卷第 14 章

## 学习目标

- 理解顶点修正如何给出反常磁矩，记住 Schwinger 项 $a_e=\alpha/2\pi$；
- 知道 g−2 的现代理论与实验精度，以及它为什么受精细结构常数测定的限制；
- 用 Bethe 的方法估算氢原子 2S 的 Lamb 位移，得到约 1000 MHz；
- 理解 Welton 的"真空涨落抖动"图像，并知道它与辐射反作用图像的关系。

## 14.1 形状因子

完整的电子–光子顶点（计入所有圈图修正）可以写成

$$\bar u(p')\Gamma^\mu u(p)=\bar u(p')\left[\gamma^\mu F_1(q^2)+\frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2(q^2)\right]u(p),\qquad \sigma^{\mu\nu}=\frac i2[\gamma^\mu,\gamma^\nu]$$

这是洛伦兹不变性和规范不变性允许的最一般形式。

- $F_1(0)=1$：电荷由物理电荷定义（重整化条件）。
- $F_2(0)$：给出额外的磁矩。

在非相对论极限下，这一顶点给出磁矩 $\boldsymbol\mu=\frac{e}{m}[F_1(0)+F_2(0)]\mathbf S$，即

$$g=2[1+F_2(0)],\qquad a_e\equiv\frac{g-2}{2}=F_2(0)$$

## 14.2 Schwinger 项

计算一圈顶点图（第 13 章表中第三个），$F_2$ 部分是 **有限** 的，不需要重整化：

$$F_2(0)=\frac{\alpha}{2\pi}\approx0.0011614$$

这是 Schwinger（1948）的结果，与当年 Kusch 和 Foley 的测量相符，成为 QED 的第一个精密胜利。

## 14.3 现代精度

$$a_e=\frac12\left(\frac\alpha\pi\right)-0.328478965\ldots\left(\frac\alpha\pi\right)^2+1.181241456\ldots\left(\frac\alpha\pi\right)^3+\cdots$$

现在已计算到 $(\alpha/\pi)^5$，包含 12672 个五圈图，另有很小的强子和弱相互作用贡献。

- **实验**：Fan 等（2023）$a_e=0.00115965218059(13)$，相对精度约 0.11 ppb。
- **理论**：精度主要受 $\alpha$ 的测量限制，而不同方法测得的 $\alpha$ 之间存在约 5σ 的矛盾（灵感库 L046）。

所以 g−2 既可以看作 **对 QED 的检验**（用独立测得的 $\alpha$），也可以看作 **测量 $\alpha$ 的最精确方法**（假设 QED 正确）。

**μ 子 g−2**：μ 子比电子重约 200 倍，对重粒子的圈图贡献（包括可能的新粒子）敏感约 $4\times10^4$ 倍，但强子贡献的理论不确定性也大得多（L011）。

## 14.4 Lamb 位移：Bethe 的估算

狄拉克理论中氢原子的 $2S_{1/2}$ 与 $2P_{1/2}$ 简并，实验测得 $2S_{1/2}$ 高约 1058 MHz（L028）。

Bethe（1947）在实验结果公布后几天，用非相对论方法估算了电子自能的影响：

1. 原子中电子的自能（与真空模式的二阶相互作用）是发散的。
2. 自由电子也有同样的自能，它已经被包括在物理质量里了（质量重整化）。
3. 只有 **束缚电子与自由电子自能之差** 可观测。相减后，线性发散消失，只剩对数发散。
4. 相对论效应会在约 $m$ 处截断这一对数，所以取截断 $\Lambda\approx m$。

结果（$l=0$ 态，$n$ 为主量子数）：

$$\Delta E_{n,l=0}=\frac{4\alpha^5m}{3\pi n^3}\ln\frac{m}{\langle\Delta E\rangle_{n}}$$

其中 $\langle\Delta E\rangle$ 是原子激发能的一种加权平均（"Bethe 对数"），对 2S 约为 $17\ \mathrm{Ry}$。$l\neq0$ 的态在这一阶没有位移，因为它们在原点处波函数为零。

代入 $n=2$：$\ln\frac{511\ \mathrm{keV}}{17\times13.6\ \mathrm{eV}}\approx7.7$，得到 $\Delta E\approx4.3\times10^{-6}$ eV，即约 **1040 MHz**。

完整的 QED 计算（包括相对论修正、真空极化约 $-27$ MHz、顶点修正等）给出约 1057.8 MHz，与实验高度一致。

## 14.5 Welton 的图像：真空涨落使电子"抖动"

Welton（1948）给出一个直观的解释：

1. 电子受到真空电场涨落的推动，位置在平衡点附近有一个小的随机偏移 $\delta\mathbf r$。
2. 电子因此感受到的是库仑势在小范围内的平均：

$$\langle V(\mathbf r+\delta\mathbf r)\rangle\approx V(\mathbf r)+\frac16\langle(\delta r)^2\rangle\nabla^2V$$

3. 对氢原子，$\nabla^2V=4\pi\alpha\,\delta^3(\mathbf r)$（自然单位），所以能量移动 $\Delta E=\frac16\langle(\delta r)^2\rangle\cdot4\pi\alpha|\psi(0)|^2$，只影响在原点有概率的 S 态。
4. 用真空涨落场的谱估算 $\langle(\delta r)^2\rangle\approx\frac{2\alpha}{\pi m^2}\ln\frac{m}{\langle\Delta E\rangle}$，并代入 $|\psi_{nS}(0)|^2=\frac{(m\alpha)^3}{\pi n^3}$，**恰好重现 Bethe 的公式**。

**诠释提醒**：Welton 的图像直观，但不是唯一的。Dalibard、Dupont-Roc 与 Cohen-Tannoudji（1982）证明：选择不同的算符排序，Lamb 位移可以全部归于真空涨落，也可以部分归于辐射反作用（灵感库 L008）。对称排序下，Lamb 位移主要来自真空涨落；而自发辐射则是两者各占一半。**数学结果唯一，物理图像不唯一。**

## 与本项目的联系

- 14.3 节是对应原理的硬约束（L029、L046）：底层理论若在电子 g 因子中引入修正 $\delta a_e$，它必须小于约 $10^{-12}$。
- 14.5 节是"真空涨落是否真实"（L008、C002）讨论中最经典的例子。
- 正电子素（L048）和高电荷态离子（L045）是比氢原子更极端的束缚态 QED 检验。

## 习题

**14.1** 计算 $\alpha/2\pi$，并与实验值 $a_e=0.00115965$ 比较，相对差多少？加入二阶项后呢？

<details><summary>答案</summary>

$\alpha/2\pi\approx0.0011614$，比实验值大约 0.15%。加入 $-0.3285(\alpha/\pi)^2\approx-1.77\times10^{-6}$ 后得 0.00115964，相对差降到约 $10^{-5}$。每多一阶，精度约提高 $\alpha/\pi\approx1/430$ 倍。
</details>

**14.2** 用 Bethe 公式计算氢原子 2S 的 Lamb 位移，分别取 $\langle\Delta E\rangle=16.64$ Ry 和 17.8 Ry，换算成 MHz（$1\ \mathrm{eV}\leftrightarrow2.418\times10^8$ MHz）。

<details><summary>答案</summary>

$\frac{4\alpha^5m}{3\pi\times8}=\frac{4\times2.07\times10^{-11}\times511000}{75.4}\ \mathrm{eV}\approx5.6\times10^{-7}$ eV。对数分别为 7.72 和 7.66，结果约 $4.33\times10^{-6}$ eV（1047 MHz）和 $4.29\times10^{-6}$ eV（1038 MHz）。
</details>

**14.3** 验证 Welton 图像能重现 Bethe 公式：把 $\langle(\delta r)^2\rangle=\frac{2\alpha}{\pi m^2}L$ 和 $|\psi(0)|^2=\frac{(m\alpha)^3}{\pi n^3}$ 代入 $\Delta E=\frac16\langle(\delta r)^2\rangle\cdot4\pi\alpha|\psi(0)|^2$。

<details><summary>答案</summary>

$\Delta E=\frac16\cdot\frac{2\alpha L}{\pi m^2}\cdot4\pi\alpha\cdot\frac{m^3\alpha^3}{\pi n^3}=\frac{8\alpha^5mL}{6\pi n^3}=\frac{4\alpha^5m}{3\pi n^3}L$。
</details>

**14.4** 为什么 2P 态在 Bethe 的估算中没有 Lamb 位移？

<details><summary>答案</summary>

位移正比于 $|\psi(0)|^2$，而 $l\ge1$ 的态在原点处波函数为零。（更精确的计算中 2P 有一个很小的位移，约 $-13$ MHz，来自 Bethe 对数中与 $l$ 有关的部分。）
</details>
