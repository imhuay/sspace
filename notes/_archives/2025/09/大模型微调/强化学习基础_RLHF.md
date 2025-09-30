强化学习基础 (RLHF 视角)
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-09-25&labelColor=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-30%2020%3A54%3A40&labelColor=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-09-25 02:59:27
toc_title: '**强化学习基础** ( **LLM-based** )'
top: false
draft: false
hidden: true
omit_in_tag_toc: false
section_number: false
level: 99
tags: []
-->

<!--START_SECTION:keywords-->
> ***Keywords**: [偏好学习](./偏好学习.md)*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [**基础概念**](#基础概念)
    - [核心术语体系](#核心术语体系)
    - [术语释义及其在 RLHF 中的含义](#术语释义及其在-rlhf-中的含义)
        - [**1. 智能体 • 环境 • 回合**](#1-智能体--环境--回合)
        - [**2. 状态 • 动作 • 策略 • 转移概率**](#2-状态--动作--策略--转移概率)
        - [**3. 奖励 • 回报 • 折扣因子**](#3-奖励--回报--折扣因子)
        - [**4. 价值函数 • 优势函数**](#4-价值函数--优势函数)
    - [策略梯度](#策略梯度)
        - [在线策略 • 离线策略](#在线策略--离线策略)
- [优化目标](#优化目标)
    - [通用优化目标](#通用优化目标)
- [相关概念](#相关概念)
- [贝尔曼方程 (Bellman Equation)](#贝尔曼方程-bellman-equation)
    - [**状态价值函数** 的贝尔曼方程](#状态价值函数-的贝尔曼方程)
    - [**动作价值函数** 的贝尔曼公式](#动作价值函数-的贝尔曼公式)
- [时序差分算法 (Temporal Difference, TD)](#时序差分算法-temporal-difference-td)
    - [TD (0) 与 **时序差分误差** (TD Error)](#td-0-与-时序差分误差-td-error)
    - [TD (λ)](#td-λ)
- [**广义优势估计** (GAE)](#广义优势估计-gae)
<!--END_SECTION:toc-->

---

## **基础概念**

<!--
- 强化学习算法可以分为两大类:
    - 基于 **值函数** 的强化学习
        - Q-Learning
        - SARSA
        - DQN
    - 基于 **策略** 的强化学习
        - REINFORCE
        - 自然策略梯度 (Natural Policy Gradient, NPG)
        - 信赖域策略优化 (Trust Region Policy Optimization, TRPO)
        - 近端策略优化 (Proximal Policy Optimization, PPO)
        - ...
-->

<!--START_SECTION:keyword-->
<!--keyword_info
name: '基础术语'
extra_url: false
-->
### 核心术语体系
<!--END_SECTION:keyword-->

<table>
<tr><td width='100px'>分组</td><td width='250px'>核心术语</td><td>解释</td>
</tr>
<tr>
<td>

<!-- **1. 核心交互实体** </td> -->
**1. 交互框架** </td>
<td>

• **智能体** (Agent) <br>
• **环境** (Environment) <br>
• **回合** (Episode) <br></td>
<td>

定义了交互的参与者和基本单元: <br>
• **智能体** 作为决策者, 在环境中执行一系列操作; <br>
• 一个完整的交互序列称为 **回合**, 从初始状态运行到终止状态. <br></td>
</tr>
<tr>
<td>

<!-- **2. 决策基础组件**</td> -->
**2. 决策机制**</td>
<td>

• **状态** (State) <br>
• **动作** (Action) <br>
• **策略** (Policy) <br>
• **转移概率** (Transition Probability) <br></td>
<td>

描述了决策循环的核心要素: <br>
• 从 **状态** 出发, 通过 **策略** 选择 **动作**; <br>
• 环境依据 **转移概率** 进入下一个状态. <br></td>
</tr>
<tr>
<td>

<!-- **3. 奖励与目标** </td> -->
**3. 目标定义** </td>
<td>

• **奖励** (Reward) <br>
• **回报** (Return) <br>
• **折扣因子** (Discount Factor) <br></td>
<td>

定义了问题的目标与价值衡量: <br>
• 环境在状态转换后给出即时 **奖励** 作为反馈; <br>
• 智能体的终极目标是最大化整个回合的 **回报**, 即未来所有奖励的总和; <br>
• **折扣因子** 决定了未来奖励在计算 **回报** 时的现值. <br></td>
</tr>
<tr>
<td>

<!-- **4. 评估与分析工具** </td> -->
**4. 评估工具** </td>
<td>

• **价值函数** (Value Function) <br>
&nbsp;&nbsp; ◦ **状态价值函数** (V 函数) <br>
&nbsp;&nbsp; ◦ **动作价值函数** (Q 函数) <br>
• **优势函数** (Advantage Function) <br></td>
<td>

为评估决策好坏, 以及优化策略所提供的内部工具: <br>
• **状态价值函数** 评估在特定状态下, 遵循当前策略的长期价值; <br>
• **动作价值函数** 评估在特定状态下执行某个动作, 并继续遵循策略的长期价值; <br>
• **优势函数** 通过比较 **动作价值** 与 **状态价值** , 来衡量动作的相对好坏. <br></td>
</tr>
</table>


<!-- omit in toc -->
#### 📌 术语之间的逻辑关系
> 构成了强化学习最核心, 最通用, 不依赖于任何特定算法的基础语言;

1. **智能体** 与 **环境** 是交互的两极;
2. 在每个 **回合** 中, 智能体与环境进行循环交互, 在每个时间步:
    1. 智能体基于当前 **状态**, 通过其 **策略** 选择一个 **动作**;
    2. 环境根据其内在的 **转移概率** 切换到新的状态, 并返回一个 **奖励**;
3. 智能体的核心目标是最大化整个回合的 **回报** (未来奖励经 **折扣因子** 折算后的总和);
4. 为了实现目标, 智能体使用 **价值函数** (包括 **状态价值函数** 和 **动作价值函数**) 和 **优势函数** 作为评估工具, 来分析和优化其策略.

---

### 术语释义及其在 RLHF 中的含义
> RL 一般应用于游戏智能体等场景, 其概念或术语在 LLM 背景下需要做相应调整或说明.

> 在描述当前某一术语时, 难免会涉及到之后的某个术语, 注意前后联系.

> **约定**: **大写字母** 表示 **随机变量**, 如 $R_t$; **小写字母** 为随机变量的 **观测值**, 如 $r_t$;

---

#### **1. 智能体 • 环境 • 回合**

<table>
<tr><th width='150px'>概念</th><th width='340px'>RL 中的含义</th><th>RLHF 中对应的含义</th></tr>

<tr>
<td>

**智能体 (Agent)** </td>
<td>

• 与环境交互的学习者与决策者; <br>
• 策略的载体, 优化的目标对象. <br></td>
<td>

• 待优化的 **语言模型本身**;<br>
• 在 RLHF 中也常被称为 **Actor 模型** 或 **策略模型 (Policy Model)**. <br></td>
</tr>
<tr>
<td>

**环境 (Environment)** </td>
<td>

• 智能体与之交互的外部系统; <br>
• 能够接收智能体的 **动作** 并反馈 **新的状态** 和 **奖励**. <br></td>
<td>

<!-- • 即当前 **上下文**, 由 **提示 (Prompt)** 和 **已经生成的 Token 序列** 共同构成; <br> -->
<!-- • 语言建模部分决定 **状态转移**, 奖励模型在序列完成后给出 **奖励信号**. <br></td> -->
• **文本生成任务本身**: 是一个为策略模型提供交互的 **反馈系统**, 由 **语言建模过程** 和 **奖励模型** 共同构成; <br>
• 语言建模过程提供 **状态反馈**, 决定状态转移; 奖励模型提供 **价值反馈**, 即奖励信号. <br></td>
</tr>
<tr>
<td>

**回合 (Episode)** </td>
<td>

• 一次从初始状态到终止状态的完整交互序列; <br>
• 是策略评估和优化的基本单位. <br></td>
<td>

• 一次完整的文本生成过程; <br>
• 从模型接收提示开始, 到生成结束符 (`<EOS>`) 或达到最大生成长度时结束. <br></td>
</tr>
</table>

---

#### **2. 状态 • 动作 • 策略 • 转移概率**

<table>
<tr><th width='150px'>概念</th><th width='340px'>RL 中的含义</th><th>RLHF 中对应的含义</th></tr>
<tr>
<td>

**状态 (State,  $s$)** </td>
<td>

• 环境在时刻 $t$ 的完整描述, 记 $s_t$; <br>
• 是智能体做出决策的全部依据, 通常假设其满足 **马尔可夫性质**. <br></td>
<td>

<!--  
• 当前上下文 (提示与已生成 Tokens) 在模型内部的 **向量表示**; <br>
• 它编码了用于生成下一个 Token 所需的全部信息. <br></td>
-->
• 模型生成过程中, 在时刻 $t$ 的具体上下文: 由 **提示 (Prompt)** 和 **已生成的 Token 序列** 构成; (或者它们在模型内部的向量表示). <br>
• 是策略模型做出下一个 Token 决策的全部依据. <br></td>
</tr>
<tr>
<td>

**动作 (Action, $a$)** </td>
<td>

• 智能体在时刻 $t$ 根据状态 $s_t$ 所执行的操作, 记 $a_t$; <br>
• 是智能体影响环境的唯一方式. <br></td>
<td>

<!-- • 策略模型在给定上下文的情况下 **生成下一个 Token** <br></td> -->
• 策略模型在给定上下文的情况下, 从词表中选择并生成下一个 Token ( $a_t$ ); <br>
• 这是语言模型在每个时间步影响后续文本生成的唯一方式. <br></td>
</tr>
<tr>
<td>

**策略 (Policy, $\pi$)** </td>
<td>

<!--  
• 智能体的行为函数, 通常参数化为 $\pi_{\theta}(\cdot)$; <br>
• 定义了从 **状态** $s_t$ 到 **动作** $a_t$ 的映射, 即 $a_t = \pi_{\theta}(s_t)$; <br></td>
-->
• 智能体的决策函数, 记 $\pi$; <br>
• 它定义了从状态到动作的映射关系, 通常被参数化为 $\pi_{\theta}(a|s)$, <br>
• 即 **给定状态下选择动作的概率分布**. <br></td>
<td>

<!-- • 策略模型根据当前 **上下文 (状态)** 输出下一个 **Token (动作)** 的概率分布, 即 $\pi(a_t | s_t)$ <br></td> -->
• 语言模型的前向过程; <br>
• 即根据当前上下文 (状态) 计算下一个 Token (动作) 的概率分布, 即: <br>
  $$\pi_{\theta}(\, token \,|\, context \,)$$
</td>
</tr>
<tr>
<td>

**转移概率 (Transition Probability)** </td>
<td>

• 环境动态的数学模型, 记: <br>
  $$P(s_{t+1} | s_t, a_t)$$
• 表示在状态 $s_t$ 执行动作 $a_t$ 后, 环境转移到状态 $s_{t+1}$ 的概率. <br></td>
<td>

<!-- 新状态 $s_{t+1}$ 是旧状态序列 $s_t$ 与动作 $a_t$ (Token $w_t$) 的拼接, 即 $P(s_{t+1} = s_t \oplus a_t | s_t, a_t) = 1$   -->
• **在语言生成任务中, 状态转移是一个确定性过程**; <br>
• 具体来说, 当基于 $t$ 时刻的上下文 $s_t$ 生成出下一个 Token ( $a_t$ ) 后, 在 $t{+1}$ 时刻的上下文就已经确定了, 即 $s_t \oplus a_t$; 即: <br>
  $$P(s_{t+1} | s_t, a_t) = 1$$
• **这是序列生成任务与经典 RL 问题的一个根本区别**; <br>
> [_核心影响_](#-rlhf-中转移概率确定带来的影响) <br></td>
<!-- 生成任务的随机性都来自于策略 (即 LLM) 本身如何选择下一个词; 环境本身是完全被动和可预测的; <br> -->
</tr>

</table>

<!-- omit in toc -->
#### 💡 RLHF 中转移概率确定带来的影响
- **环境建模简化**:
    - 在传统 RL 中, 需要估计或采样环境的转移概率;
    - 而在 RLHF 中, 状态转移就是拼接 Token 的确定性过程, 不需要额外建模.
- **随机性完全来自策略**
    - 环境不再引入随机性,
    - 唯一的随机性来源是 **策略** (即 LLM 本身) 对下一个词的概率分布.
- **优化目标**:
    - 这意味着 RLHF 的优化核心完全集中于 **如何调整策略的词表分布**, 而不是估计复杂的环境动态;
    - 从本质上讲, RLHF 的策略优化更像是一种 **带奖励信号的序列建模**, 其目标是执行 **序列级别的加权最大似然估计**, 即增加高回报序列的生成概率.
- **奖励稀疏性与信用分配挑战**
    - 由于状态转移是确定性的, **每次动作 (Token 选择) 并不会带来即时奖励**;
    - 奖励通常只在整段序列生成完毕后, 由 **奖励模型** 给出一个标量得分.
    - 这导致了典型的 **稀疏奖励** 和 **信用分配** 问题:
        - 需要将最终的总奖励合理地归因于序列中每一个生成 Token 的决策上;
        - PPO 等策略梯度算法与优势估计 (如 GAE) 正是解决此挑战的关键工具.
- **价值估计的简化**
    - 在计算价值函数时, 由于下一个状态 $s_{t+1}$ 是唯一确定的, 即
        $$P(s_{t+1} | s_t, a_t) = 1$$
    - 则 [贝尔曼方程](#贝尔曼方程-bellman-equation) 中关于下一个状态的期望退化为单点取值:
        $$
        \mathbb{E}_{S_{t+1}\sim P(\cdot|s_t,a_t)}\big\lbrack\, V(S_{t+1}) \,\big\rbrack
        = \sum_{s'} P(s'|s_t,a_t)V(s')
        = V(s_{t+1}).
        $$
    - 这在一定程度上降低了价值函数估计的复杂度.

---

#### **3. 奖励 • 回报 • 折扣因子**

<table>
<tr><th width='150px'>概念</th><th width='340px'>RL 中的含义</th><th>RLHF 中对应的含义</th></tr>
<tr>
<td>

**奖励 (Reward, $R$)** </td>
<td>

<!-- • 环境在智能体执行动作后反馈的 **标量信号**, 用于评估动作的好坏. <br> -->
• 环境在智能体执行动作后反馈的 **标量信号**; <br>
• 是评估动作即时好坏的核心依据. <br>
• 对时刻 $t$ 奖励的观测值, 记 $r_t$. <br></td>
<td>

<!--  
• ⚠️ 在 RLHF 中, **奖励** 通常指的是对一次 **完整输出** 的评分, 而不是对一次动作 (生成下一个 Token);<br>
• 具体的, **奖励** 由一个独立训练的 **奖励模型 (Reward Model, RM)** 计算, 负责评估 **Prompt+生成文本** 的整体质量;<br>
• 形式上是一个 **标量分数**;<br>
-->
<!-- • 在 RLHF 中, 奖励由一个独立训练的 **奖励模型 (Reward Model, RM)** 提供, 负责评估 **Prompt+生成文本** 的质量.<br> -->
• **在输出结束后**, 由奖励模型对 **完整上下文 (Prompt + Response)** 的标量打分;
<!-- 由一个独立训练的 **奖励模型** 给出的 **标量评分**; <br> -->
> ⚠️ **关键区别**: RLHF 中的奖励通常指对一个回合的整体评估, 而非过程中单个动作的即时反馈. <br></td>
</tr>
<tr>
<td>

**回报 (Return, $G$)** </td>
<td>

<!-- • 从特定时刻的状态开始, 到 **一轮交互完成/一个回合结束** 所能获得的 **累积奖励**;<br> -->
<!-- • 常用折扣因子 $\gamma$ 计算, 如 $G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k}$;<br> -->
• 从时刻 $t$ 起, 直到回合结束所获得的 **累积奖励**, 记 $G_t$: <br>
  $$G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$$
• 其中 $\gamma$ 为 **折扣因子**, 体现未来奖励的 **衰减**: <br>
> 长期累积奖励的等价说法; <br></td>
<td>

<!-- • 从当前 Token 位置开始, 到生成结束所能获得的 **累积奖励**<br> -->
<!-- • 由于语言生成中未来 Token 的重要性相近, 折扣因子 $\gamma$ 常设为 $1$, 即 $G_t = \sum_{k=0}^{T-t} r_{t+k}$; -->
• 从生成当前 Token 的时刻 $t$ 开始, 直到生成结束所能获得的 **累积奖励**; <br>
• 在 RLHF 中, 由于奖励的 **稀疏性** (仅在序列结束时给出), 其计算依赖于 **价值函数的估计**. <br></td>
</tr>
<tr>
<td>

**折扣因子 (Discount Factor, $\gamma$)** </td>
<td>

• 用于权衡即时奖励和未来奖励的重要性, 记 $\gamma \in (0,1)$;<br>
• $\gamma \to 0$ 时, 更注重短期收益,<br>
• $\gamma \to 1$ 时, 更注重长期回报.<br>

</td>
<td>

• 在文本生成任务中, 通常 **不考虑长期奖励衰减** (反而需要避免); <br>
• 因为序列中每个 Token 对于最终质量都至关重要, 不宜过度折扣未来贡献; <br>
• 故 RLHF 中 $\gamma$ 常被设置为 **接近或等于 $1$**. <br></td>
</tr>
</table>

---

<!--START_SECTION:keyword-->
<!--keyword_info
name: '价值函数 ↝ 优势函数'
extra_url: false
-->
#### **4. 价值函数 • 优势函数**
<!--END_SECTION:keyword-->

<table>
<tr><th width='160px'>概念</th><th width='340px'>RL 中的含义或作用</th><th>RLHF 中对应的含义或作用</th></tr>
<tr>
<td>

**价值函数 (Value Function)** </td>
<td>

• **估计** 一个 **状态** 或 **状态-动作对** 未来价值的 **工具**, 其结果是对 **未来回报** 的 **期望**. <br>
• 包括 **状态价值函数** 和 **动作价值函数**. <br></td>
<td>

\- </td>
</tr>
<tr>
<td>

**状态价值函数 (V 函数)** </td>
<td>

• 用于估计一个状态 $s$ 的长期价值; <br>
• 返回在状态 $s$ 下, 遵循策略 $\pi$ 所能获得的 **期望回报**: <br>
  $$V^{\pi}(s) = \mathbb{E}_{\pi}\big\lbrack\, G_t \mid S_t = s \,\big\rbrack$$
</td>
<td>

<!-- • 用于衡量在特定上下文中, 语言模型继续生成至结束所能获得的 **期望回报**; <br> -->
• 用于预测在给定上下文下继续生成至结束所能获得的 **期望回报**. <br>
> ◦ 在基于 Actor-Critic 框架的算法 (如 PPO) 中, 该函数由一个专门的 **价值模型 (Critic)** 进行学习和估计. <br>
> ◦ 在离线策略算法 (如 DPO) 中, 则通过直接从偏好数据中提取隐式价值信号来避免对显式 $V$ 函数的需求. <br></td>
</tr>
<tr>
<td>

**动作价值函数 (Q 函数)** </td>
<td>

• 用于估计在状态 $s$ 下采取某个特定动作 $a$ 的长期价值; <br>
• 返回在状态 $s$ 下执行动作 $a$ 后, 遵循策略 $\pi$ 所能获得的 **期望回报**: <br>
  $$Q^{\pi}(s, a) = \mathbb{E}_{\pi}\big\lbrack\, G_t \mid S_t = s, A_t = a \,\big\rbrack$$
</td>
<td>

• 用于预测在给定上下文下, 在生成某个特定 token 后, 继续生成至结束所能获得的 **期望回报**. <br>
> ◦ 在 RLHF 的经典设定中, 通常不显式学习独立的 Q 函数; 而是通过 **奖励** 和 **$V$ 函数** 间接估计. <br></td>
</tr>
<tr>
<td>

**优势函数 (Advantage Function)** </td>
<td>

• 用于衡量在状态 $s$ 下采取动作 $a$ 相对于所有动作 **平均水平** 的优势, 即: <br>
  $$A^{\pi}(s, a) = Q^{\pi}(s, a) - V^{\pi}(s)$$
</td>
<td>

• 用于衡量在特定上下文下, 生成某个特定 token 相对于模型平均生成水平的 **相对价值**; <br>
• 其值为策略优化提供了直接的梯度信号. <br></td>
</tr>
</table>

---

<!-- TODO -->
### 策略梯度



<!--  
• 对于 **在线策略 (On-Policy) 梯度算法** —— **基于 Actor-Critic 框架**, 如 TRPO/PPO 等;<br>
• 其特点是 **使用当前策略生成的数据来优化策略本身**;<br>
• 在这类算法中, 通常会训练一个 **价值模型 (Critic)** 来近似估计状态价值函数 $V(\cdot)$, 作为评价策略好坏的基线;<br>
• 但一般 **不直接建模** $Q(\cdot)$; 而是通过 **即时奖励** 和 **下一状态的价值函数** 来估计动作价值, 其关系由 [**贝尔曼方程**](#贝尔曼方程-bellman-equation) 定义:<br>
  $$Q(s_t,a_t) = r_t + \gamma V(s_{t+1})$$

---

• 对于 **离线策略 (Off-Policy)** 算法 (如 DPO 等),<br>
• 其特点是 **利用历史策略或其他策略产生的数据进行学习**;<br>
• 以 **避免显式地训练一个独立的价值模型**;<br>
• 其目标函数的理论推导与最优策略下的 **优势函数** 或 **Q 函数** 有关;<br>
-->

<!-- 其核心目标是 **直接学习并优化动作价值函数** $Q(s, a)$ 本身, 如 DPO 等.<br> -->
<!-- • **状态价值函数**: 在诸如 TRPO/PPO 等 **基于 Actor-Critic 框架** 的 **在线策略 (On-Policy) 梯度算法** 中, 通常会训练一个 **价值模型 (Critic)** 来近似 $V(s)$;<br> -->
<!-- • **动作价值函数**: On-Policy 算法中, 通常不直接训练一个模型来近似 $Q$ 函数, 而是通过 **奖励模型的反馈** 和 **价值模型的预测** 相结合来估算, 一般取 $$;<br> -->
<!-- • **离线策略 (Off-Policy)** 算法一般 **不需要价值模型**, 而其核心目标就是 **直接学习并优化动作价值函数** $Q(s, a)$ 本身.<br> -->
<!-- • **广义优势估计** (GAE): 一种高效且低方差的方法是使用 **时序差分误差 (TD Error)** 的累积来估算;<br> -->
<!-- • 定义 **单步 TD 误差**: $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$;<br> -->
<!-- • 则 $Q(s_t, a_t)$ 可以 **近似** 为 $r_t + \gamma V(s_{t+1})$;<br> -->

<!--  
• 在 LLM 语境下, 即评估给定上下文生成某个 Token 的相对好坏;<br>
• 根据 [**贝尔曼方程**](#贝尔曼方程-bellman-equation) 与 [**时序差分 (TD) 算法**](#时序差分算法-temporal-difference-td) 有:<br>
  $$A_t \approx \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t) \quad \scriptstyle\text{// 单步优势估计}$$
• **一个更通用的形式是** [**广义优势估计 (GAE)**](#广义优势估计-gae):<br>
  $$A_t^{\text{GAE}(\gamma, \lambda)} = \sum_{l=0}^{\infty} (\gamma \lambda)^l \delta_{t+l}$$
-->
<!-- • 其中 $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$ 为 **时序差分误差**, $\lambda \in \lbrack 0, 1\rbrack$ 为 GAE 参数; 当 $\lambda = 0$ 时, 即退化为单步优势估计;<br> -->
<!-- • **在 RLHF 中, 估计优势函数是策略梯度计算的核心**;<br> -->


#### 在线策略 • 离线策略

<!--
> • On-Policy 与 Off-Policy 的 **核心区别**: **用于训练的数据生成方式**;<br>
> • On-Policy **必须** 使用 当前策略 $\pi$ 最新生成的数据;<br>
> • Off-Policy **可以** 使用 历史数据 或 其他策略 生成的数据;<br>
-->

---

<!--START_SECTION:keyword-->
<!--keyword_info
name: 'RL 优化目标'
extra_url: false
-->
## 优化目标
<!--END_SECTION:keyword-->

<!-- TODO -->
### 通用优化目标
>


## 相关概念


<!--START_SECTION:keyword-->
<!--keyword_info
name: '贝尔曼方程'
extra_url: false
-->
## 贝尔曼方程 (Bellman Equation)
<!--END_SECTION:keyword-->
> • 贝尔曼方程描述了价值函数自身的递归关系, 是 **价值函数估计** 的理论基石;<br>
> • 一句话描述, 即 **当前时刻的价值** = **当前的即时奖励 (的期望)** + **折扣因子** × **下一时刻的价值 (的期望)**.<br>

### **状态价值函数** 的贝尔曼方程
- **定义**: 状态价值函数 $V(s_t)$ 表示从状态 $s_t$ 开始, 遵循策略所能获得的**期望回报**:
    $$V(s_t) = \mathbb{E}\big\lbrack\, G_t \,|\, S_t = s_t\,\big\rbrack$$
    其中 **回报** $G_t$ 为 **即时奖励** 和所有 **未来折扣奖励** 之和:
    $$\begin{aligned}
    G_t &= R_t + \gamma R_{t+1} + \gamma^2 R_{t+2} + \dots = \sum_{k=0}^{\infty} \gamma^k R_{t+k} \\
        &= R_t + \gamma\sum_{k=1}^{\infty} \gamma^{k-1} R_{t+k} \\
        &= R_t + \gamma G_{t+1}
    \end{aligned}$$
<!--
    $$G_t = R_t + \gamma R_{t+1} + \gamma^2 R_{t+2} + \dots = \sum_{k=0}^{\infty} \gamma^k R_{t+k} = R_t + \gamma\sum_{k=0}^{\infty} \gamma^k R_{t+1+k}$$
    或写作递归形式:
    $$G_t = R_t + \gamma G_{t+1}$$
    -->
- 根据期望的线性性质, 分离出即时奖励和未来奖励:
    $$V(s_t) = \mathbb{E}\big\lbrack\, R_t \,|\, S_t = s_t\big\rbrack + \gamma \mathbb{E}\big\lbrack\, G_{t+1} \,|\, S_t = s_t\,\big\rbrack$$
- 根据 **全期望公式 (塔性质)** 以及 **马尔可夫假设**, 有:
    $$
    \begin{aligned}
    \mathbb{E}\big\lbrack\, G_{t+1} \,|\, S_t = s_t\big\rbrack
        &= \mathbb{E}\Big\lbrack\,\mathbb{E}\big\lbrack\, G_{t+1} \,|\, S_{t+1}, S_t = s_t\,\big\rbrack \,\Big|\, S_t = s_t \,\Big\rbrack &\ \scriptstyle{//\ 期望迭代法则} \\
        &= \mathbb{E}\Big\lbrack\, \mathbb{E}\big\lbrack\, G_{t+1} \,|\, S_{t+1}\, \big\rbrack \,\Big|\, S_t = s_t \,\Big\rbrack &\ \scriptstyle{//\ 马尔可夫假设} \\
        &= \mathbb{E}\Big\lbrack\, V(S_{t+1}) \,\Big|\, S_t = s_t \,\Big\rbrack
    \end{aligned}
    $$
    > • **全期望公式**: $\mathbb{E}\big\lbrack\,\mathbb{E}\lbrack\,G_{t+1} \,|\, S_{t+1}, S_t\,\rbrack \mid S_t \,\big\rbrack = \mathbb{E}\lbrack\, G_{t+1} \mid S_t\,\rbrack$ —— 先在更多条件下取期望, 再在较少条件下取期望, 结果等于直接在较少条件下取期望;<br>
    > • **马尔可夫假设**: $\mathbb{E}\big\lbrack\, G_{t+1} \,|\, S_{t+1}, S_t\,\big\rbrack = \mathbb{E}\big\lbrack\, G_{t+1} \,|\, S_{t+1}\,\big\rbrack$ —— 给定当前状态 $S_{t+1}$, 未来回报 $G_{t+1}$ **不再依赖** 过去状态 $S_t$;<br>
- 综上:
    $$V(s_t) = \mathbb{E}\big\lbrack\, R_t \,|\, S_t = s_t\,\big\rbrack + \gamma \mathbb{E}\big\lbrack\, V(S_{t+1}) \,|\, S_t = s_t\,\big\rbrack$$
    > • 进一步引入策略 $\pi(a|s)$ 和状态转移概率 $P(s' \mid s, a)$, 可以得到更具体的表达式;<br>
    > • 智能体在状态 $s$ 下选择动作 $a$ 的概率是 $\pi(a|s)$, 执行动作 $a$ 后获得奖励 $\mathcal{R}(s, a, s')$, 并转移到状态 $s'$ 的概率是 $P(s' \mid s, a)$;<br>
    > • 下面是贝尔曼方程的完整形式 (**仅做参考, 具体推导略**):<br>
    > $$V(s) = \sum_{a} \pi(a | s) \sum_{s'} P(s' \mid s, a) \Big\lbrack\, \mathcal{R}(s, a, s') + \gamma V(s') \,\Big\rbrack$$
<!--
- _引入 **策略** 与 **动作** 的完整式_ (**仅做参考, 具体推导略**):
    $$V(s) = \sum_{a} \pi(a | s) \Big( \text{RM}(s,a) + \gamma \sum_{s'} P(s' \mid s,a) \, V(s') \Big)$$
    -->
- 在 **确定性环境** 下, 方程简化为:
    $$V(s_t) = r_t + \gamma V(s_{t+1})$$
- 在随机环境下, 可通过 **蒙特卡洛方法** 进行估计:
    - 单步采样 (无偏估计):
        $$\hat{V}(s_t) \approx r_t + \gamma \, V(s_{t+1})$$
        其中 $r_t$ 与 $s_{t+1}$ 来自采样轨迹;
    - 多样本平均可降低估计方差:
        $$\hat{V}(s_t) = \frac{1}{N} \sum_{i=1}^{N} \Big( r_t^{(i)} + \gamma \, V\big(s_{t+1}^{(i)}\big) \Big)$$
        > 这里 $N$ 条轨迹均从状态 $s_t$ 开始根据策略 $\pi$ 执行.

### **动作价值函数** 的贝尔曼公式
> 推导过程基本与 $V(\cdot)$ 相同
- **定义**: 动作价值函数 $Q(s_t, a_t)$ 表示在状态 $s_t$ 下执行动作 $a_t$ 后, 继续遵循策略 $\pi$ 所能获得的期望回报:
    $$Q(s_t, a_t) = \mathbb{E}\big\lbrack\, G_t \mid S_t = s_t, A_t = a_t\, \big\rbrack \xlongequal{简记} \mathbb{E}\big\lbrack\, G_t \mid s_t, a_t\, \big\rbrack$$
  > • 根据 $Q$ 函数的定义和 **全概率公式**, 有:<br>
  > $$\begin{aligned}
    V(s_t)
        = \mathbb{E}\big\lbrack\, G_t \mid S_t = s_t \,\big\rbrack
        &= \sum_{a} \pi(a \,|\, s_t)\ \mathbb{E}\big\lbrack G_t \mid S_t = s_t, A_t = a \big\rbrack \\
        &= \sum_{a} \pi(a \,|\, s_t) Q(s_t,a)
    \end{aligned}$$
- 类似 $V(s)$ 的推导, 应用期望的线性性质, 全期望公式及马尔可夫假设, 有:
    $$\begin{aligned}
    Q(s_t, a_t)
        &= \mathbb{E}\big\lbrack\, R_t \mid s_t, a_t \,\big\rbrack + \gamma \mathbb{E}\big\lbrack\, G_{t+1} \mid s_t, a_t \,\big\rbrack \\
        &= \mathbb{E}\big\lbrack\, R_t \mid s_t, a_t \,\big\rbrack + \gamma \mathbb{E}\Big\lbrack\, \mathbb{E}\big\lbrack\, G_{t+1} \mid S_{t+1}, s_t, a_t \,\big\rbrack \,\Big|\, s_t, a_t \,\Big\rbrack \\
        &= \mathbb{E}\big\lbrack\, R_t \mid s_t, a_t \,\big\rbrack + \gamma \mathbb{E}\Big\lbrack\, \mathbb{E}\big\lbrack\, G_{t+1} \mid S_{t+1} \,\big\rbrack \,\Big|\, s_t, a_t \,\Big\rbrack \\
        &= \mathbb{E}\big\lbrack\, R_t \mid s_t, a_t \,\big\rbrack + \gamma \mathbb{E}\Big\lbrack\, V(S_{t+1}) \,\Big|\, s_t, a_t \,\Big\rbrack \\
        &= \mathbb{E}\big\lbrack\, R_t + \gamma V(S_{t+1}) \,\Big|\, s_t, a_t \,\Big\rbrack
        \end{aligned}$$
    > • 引入状态转移概率, 其完整式为 (推导过程略):
    > $$Q(s, a) = \sum_{s'} P(s' \mid s, a) \Big\lbrack\, \mathcal{R}(s, a, s') + \gamma V(s') \,\Big\rbrack$$
    > • 代入 $V(s') = \sum_{a'} \pi(a'|s') Q(s', a')$, 得:
    > $$Q(s, a) = \sum_{s'} P(s' \mid s, a) \Big\lbrack\, \mathcal{R}(s, a, s') + \gamma \sum_{a'} \pi(a'|s') Q(s', a') \,\Big\rbrack$$
<!--
- 在 **确定性环境** 可简化为:
    $$Q(s_t, a_t) = r_t + \gamma Q(s_{t+1}, a_{t+1})$$
-->
- 在 PPO 等算法中, **通常不会直接建模** $Q(\cdot)$, 比如通过 **蒙特卡洛方法** 近似:
    $$\hat{Q}(s_t, a_t) \approx r_t + \gamma V(s_{t+1})$$
- 基于此近似, 可以构造 **优势函数** $\mathcal{A}(s_t, a_t)$ 的估计:
    $$\mathcal{A}(s_t, a_t) = Q(s_t, a_t) - V(s_t) \approx r_t + \gamma V(s_{t+1}) - V(s_t)$$
    > 此即 **一阶时序差分误差** (TD Error) 的形式;


<!--START_SECTION:keyword-->
<!--keyword_info
name: '时序差分算法'
extra_url: false
-->
## 时序差分算法 (Temporal Difference, TD)
<!--END_SECTION:keyword-->
> 一种结合 **蒙特卡洛采样** 与 **贝尔曼方程** (**动态规划思想**) 的强化学习方法, 通过 **时序差分误差 (TD Error)** 逐步逼近价值函数, 从而在 **无需环境模型** 的情况下高效学习策略.

### TD (0) 与 **时序差分误差** (TD Error)
> 最基础的时序差分算法, 通过 **bootstrap** 方式在线更新价值函数;

- **核心思想**:
    - **当前状态的价值估计 ≈ 即时奖励 + 下一状态的折扣价值**
- 根据价值函数的贝尔曼方程:
    $$V(s_t) = \mathbb{E}\big\lbrack\, r_t + \gamma V(s_{t+1}) \,\big\rbrack$$
- 在具体实现中, 通过一次采样将 $r_t + \gamma V(s_{t+1})$ 作为 $V(s_t)$ 的 **目标值**;
- 定义 **时序差分误差 (TD Error)**:
    $$\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$
- 则 **TD(0) 的更新规则** 为:
    $$V(s_t) \leftarrow V(s_t) + \alpha \big\lbrack\, r_t + \gamma V(s_{t+1}) - V(s_t) \,\big\rbrack$$
    > 其中 $\alpha$ 为 **学习率**

### TD (λ)
> TD(0) 的推广, 考虑了多步预测.

- **定义**: $n$-步 TD 回报:
    $$G_t^{(n)} = r_t + \gamma r_{t+1} + \cdots + \gamma^{n-1} r_{t+n-1} + \gamma^n V(s_{t+n})$$
- 特别地, 当 $n \to \infty$ 时, 得到 **完整轨迹回报** (蒙特卡洛方法)
    $$G_t^{(\infty)} = \sum_{k=0}^{\infty} \gamma^k r_{t+k}$$
- **TD(λ)** 将这些 $n$-步回报进行 **指数加权平均**:
    $$G_t^{\lambda} = (1-\lambda) \sum_{n=1}^{\infty} \lambda^{n-1} G_t^{(n)}$$
    ◦ 当 $\lambda = 0$ 时: $G_t^{\lambda} = G_t^{(1)} = r_t + \gamma V(s_{t+1})$, 退化为 TD(0);<br>
    ◦ 当 $\lambda \to 1$ 时: $G_t^{\lambda} = G_t^{(\infty)} = \sum_{k=0}^{\infty} \gamma^k r_{t+k}$, 即蒙特卡洛方法;<br>
    > ▪ 加权和系数 $(1-\lambda)\lambda^{n-1}$ 构成一个概率分布: <br>
    > $$\sum_{n=1}^{\infty} (1-\lambda)\lambda^{n-1} = 1, \ \ \lambda \in [0,1)$$
- **λ-回报的直观理解**:
    - $G_t^{\lambda}$ 是不同预测步长的加权平均, λ 控制了"向前看"的程度, λ 越小越依赖短期估计 (低方差但可能有偏), λ 越大越依赖长期回报 (无偏但高方差).


<!--START_SECTION:keyword-->
<!--keyword_info
name: '广义优势估计'
extra_url: false
-->
## **广义优势估计** (GAE)
<!--END_SECTION:keyword-->
> **广义优势估计** (Generalized Advantage Estimation, GAE) 是一种 **平衡偏差与方差** 的优势估计方法.

- GAE 的推导基于 **时序差分误差 (TD Error)**:
    $$ \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t) $$
- **$k$-步优势估计** 可以表示为未来 $k$ 步 TD 误差的折扣和:
    $$ A_t^{(k)} = \delta_t + \gamma \delta_{t+1} + \dots + \gamma^{k-1} \delta_{t+k-1} = \sum_{l=0}^{k-1} \gamma^l \delta_{t+l} $$
- 当 $k \to \infty$ 时, 即为无限步长的优势估计:
    $$ A_t^{(\infty)} = \sum_{l=0}^{\infty} \gamma^l \delta_{t+l} $$
- GAE 引入了参数 $\lambda \in [0, 1)$, 将不同步长的估计进行 **指数加权平均**, 公式如下:
    $$ A_t^{\text{GAE}(\gamma, \lambda)}
        = (1-\lambda) (A_t^{(1)} + \lambda A_t^{(2)} + \lambda^2 A_t^{(3)} + \dots )
        = (1-\lambda) \sum_{k=1}^{\infty} \lambda^{k-1} A_t^{(k)}
    $$
- 将 **$k$-步估计** 代入并整理, 得其紧凑形式:
    $$ A_t^{\text{GAE}(\gamma, \lambda)} = \sum_{l=0}^{\infty} (\gamma \lambda)^l \delta_{t+l} $$
- 当 $\lambda=0$ 时, GAE **退化为单步优势估计**: $A_t = \delta_t$;
- 当 $\lambda\to 1$ 时, GAE **等价于无限步长的 TD 误差和**, 即 $A_t^{(\infty)}$;
- 通过调整 $\lambda$, 可以在 **偏差** 与 **方差** 之间取得平衡;
    - 小 $\lambda$ → 方差较小, 偏差较大;
    - 大 $\lambda$ → 偏差较小, 方差较大.
