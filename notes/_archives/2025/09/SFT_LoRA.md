LoRA (Low-Rank Adaptation, `ˈlɔːrə`) <!-- suffix --> [📋](#qa "面试问题整理(10)")<sup style="color:Brown">10</sup> <!-- suffix -->
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-09-15&labelColor=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-10-24%2018%3A18%3A57&labelColor=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-09-15 02:29:31
toc_title: LoRA
top: false
draft: false
hidden_in_recent: true
section_number: false
level: 2
tags: [llm_sft]
-->

<!--START_SECTION:keywords-->
> ***Keywords**: [SFT](./SFT.md)*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [基础概念](#基础概念)
    - [实现思路](#实现思路)
    - [实践细节](#实践细节)
    - [结构改进](#结构改进)
- [变体](#变体)
    - [QLoRA](#qlora)
    - [AdaLoRA](#adalora)
    - [DoLA](#dola)
- [Q\&A](#qa)
<!--END_SECTION:toc-->

---

## 基础概念

- **背景**:
    <!-- - **全参数微调** 大型预训练模型 (如 LLaMA) 的 **训练成本** 极高, 为每个下游任务独立部署一个模型副本的 **存储开销** 巨大; -->
    - 对大型预训练模型 (如 LLaMA) 进行 **全参数微调** 的 **训练成本** 极高; 此外, 为每个下游任务存储一套独立的模型参数也会带来巨大的 **存储开销**;
- **核心假设 (低秩假设)**:
    <!-- - 研究发现, 模型在适应下游任务时, 并不需要在完整的 **高维空间** (权重矩阵 $W \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$) 中进行更新; 这个空间巨大, 参数极多; -->
    - 研究发现, 模型在适应下游任务时, 并 **不需要在完整的高维空间中更新权重矩阵** $W \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$;
    - 真正有效的更新具有明显 **结构和模式** (**低秩性/低秩结构**), 即 **微调过程中真正重要的变化是低维的**;
    - 这意味着在微调时, **权重更新矩阵** $\Delta W \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$ 可以用一个 **低秩分解** 来有效近似:
        <div align='center'><a href='_formulas/SFT_LoRA/f_001.js.tex'><img src='_formulas/SFT_LoRA/f_001.js.svg'/></a></div>

        其中 $B \in \mathbb{R}^{d_{\text{out}} \times r}, \quad A \in \mathbb{R}^{r \times d_{\text{in}}}$, 且 **秩** $r \ll \min(d_{\text{out}}, d_{\text{in}})$
    - **这个假设被实践证明是正确的**;

### 实现思路

- 基于上述 **低秩假设**, 对需要微调的 **线性层** (如 `nn.Linear`), **冻结其原始权重** $W_0$, **不直接计算其更新** $\Delta W_0 \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$;
- 而是 **参数化** 两个小矩阵 $B \in \mathbb{R}^{d_{\text{out}} \times r}$ 和 $A \in \mathbb{R}^{r \times d_{\text{in}}}$, 且 $r \ll \min(d_{\text{out}}, d_{\text{in}})$;
- 然后通过 **旁路** 的方式学习一个低秩更新矩阵 $\Delta W = B \cdot A$, **间接模拟权重更新**;
- **推理时**, 将低秩更新与原始权重合并/相加;
    - 为了在改变秩 $r$ 时灵活调整更新量/**控制更新幅度**, **避免重新调整学习率等训练超参**, 还会引入一个缩放因子 $\dfrac{\alpha}{r}$ 作用于低秩通路的输出 (**软约束**);
        > 其中 $\alpha$ 用于控制整体更新强度, $\dfrac{1}{r}$ 用于 **抵消秩带来的线性放大效应**;
    - **前向过程** 为:
    <div align='center'><a href='_formulas/SFT_LoRA/f_002.js.tex'><img src='_formulas/SFT_LoRA/f_002.js.svg'/></a></div>

### 实践细节

- **代码示例**:
    - [LoRA.py](./_code/lora.py)
- **初始化策略**:
    <div align='center'><a href='_formulas/SFT_LoRA/f_003.js.tex'><img src='_formulas/SFT_LoRA/f_003.js.svg'/></a></div>

    - $A$: **正态分布** 或 Kaiming/Xavier 初始化;
    - $B$: 全零, 使训练开始时等价于无适配器 (即使 $\Delta W = 0$)
    - **目的**: **保证训练稳定性** (训练开始时仅在原模型附近做微扰);
- **超参选择**:
    - $r$ (**秩**):
        - 控制了更新子空间的参数量和表征能力;
        - **域内单一任务** 一般取 `4-16`;
        - **指令/跨域任务** 可以取 `16-64` 或更高;
    - $\dfrac{\alpha}{r}$ (**缩放因子**):
        - 一般取 $\alpha \approx r$, 简化训练时调参, 主要调学习率;
    - dropout:
        - LoRA 路径上的 dropout, 缓解过拟合 (如 0.05–0.2);
- **放置位置**:
    - **注意力层**: $W_q, W_v$ (原论文) 或 $W_q, W_k, W_v, W_o$;
        > 实践上分配到多处通常优于集中在单一矩阵;
    - **MLP 层:** $W_{up}, W_{down}, W_{gate}$;
        > LLaMA 中的 MLP 使用 **SwiGLU** 激活函数, 有三个子层:
        >> $\text{MLP}(x) = W_{\text{down}} \cdot (\text{Swish}(xW_{\text{gate}}) \otimes (xW_{\text{up}}))$
    - **归一化与嵌入层:** 很少, 主流收益集中在注意力与 MLP 层;
- **参数比例 (LoRA 参数 / 全量参数)**:
    <div align='center'><a href='_formulas/SFT_LoRA/f_004.js.tex'><img src='_formulas/SFT_LoRA/f_004.js.svg'/></a></div>

- **合并与可拔插**:
    - 推理时可将 $\Delta W$ 合并进 $W$ 得到 $W' = W + \dfrac{\alpha}{r} BA$, 不增加推理延迟; 也可保持 **可拔插** 以多任务切换;

### 结构改进
> 改进 LoRA 结构的 **核心** 是在不显著增加参数与算力的前提下 **扩展可调维度与控制粒度**, 通过分头分组、正则与门控等手段稳态放大表达空间, 更接近全参微调效果;

- **分组 LoRA**:
    - **思路**: 将大矩阵按 **维度/轴** 分块, 对每个分组独立应用低秩分解, 提升低秩近似的灵活性;
    - **前向公式**:
        <div align='center'><a href='_formulas/SFT_LoRA/f_005.js.tex'><img src='_formulas/SFT_LoRA/f_005.js.svg'/></a></div>

    - **细节**:
        - 组间参数独立初始化;
    - **收益与风险**:
        - 提升表达灵活性, 参数利用率高; 过拟合;
    - **代码**:
        - [group_lora](./_code/group_lora.py)
- **分头 LoRA**:
    - 分组 LoRA 的一种特殊情况, 对 `head` 维进行分组;
- **门控 LoRA**:
    - **思路**: 为 LoRA 分支增加一个 **可学习的** 标量或向量门 $g$, 控制注入强度与时机
    - **前向公式**:
        <div align='center'><a href='_formulas/SFT_LoRA/f_006.js.tex'><img src='_formulas/SFT_LoRA/f_006.js.svg'/></a></div>

    - **收益与风险**:
        - 提升稳定性与可控性; 过强的门稀疏可能造成欠拟合, 需配合学习率与正则退火;


## 变体

### QLoRA
> - 在 LoRA 基础上加了 **权重量化**, 显存占用更低;
> - 基座权重量化到 4-bit (如 NF4), LoRA 在低精度基座上训练, 极致节省显存;

### AdaLoRA
> 动态分配每层 rank, 将容量预算投向更 "重要" 的层;

### DoLA
> 将权重分解为幅度与方向, 单独调整, 有时更稳更准;

> [PDF](./_assets/DoRA.pdf)

---

<!--START_SECTION:qa-->
<!--qa_info
subject: 'SFT'
subject_level: 0
topic: 'PEFT · LoRA'
topic_level: 0
with_section_title: true
use_section_number: true
-->
## Q&A

<!--START_SECTION:qa_toc-->
- [1. 🏷️ LoRA 相关](#1-️-lora-相关)
    - [1.1. ✅ 什么是 LoRA? 它解决了什么问题? 适用什么场景?](#11--什么是-lora-它解决了什么问题-适用什么场景)
    - [1.2. ✅ 与全参微调相比, LoRA 的 **表达上限** 如何?](#12--与全参微调相比-lora-的-表达上限-如何)
    - [1.3. ✅ LoRA 的参数量如何计算? 与原参数量的比例?](#13--lora-的参数量如何计算-与原参数量的比例)
    - [1.4. ✅ LoRA 一般作用于哪些层?](#14--lora-一般作用于哪些层)
    - [1.5. 💡 写出 LoRA 的 **数学形式**, 并解释各参数的含义与约束](#15--写出-lora-的-数学形式-并解释各参数的含义与约束)
    - [1.6. ✅ 为何需要 **缩放项** `α/r`? 去掉会怎样?](#16--为何需要-缩放项-αr-去掉会怎样)
    - [1.7. ✅ 为什么常将 `A` 正态初始化, `B` 初始化为 `0`? 如果不这么做会怎么样?](#17--为什么常将-a-正态初始化-b-初始化为-0-如果不这么做会怎么样)
    - [1.8. ✅ 如何选择 `r` (Rank)? 不同任务/数据规模下的建议是什么?](#18--如何选择-r-rank-不同任务数据规模下的建议是什么)
    - [1.9. 💡 如果希望逼近全参微调效果, 除了增大 r 还能做什么?](#19--如果希望逼近全参微调效果-除了增大-r-还能做什么)
- [2. 🏷️ LoRA 的变体](#2-️-lora-的变体)
    - [2.1. ✅ QLoRA/AdaLoRA/DoRA 的核心思路是什么?](#21--qloraadaloradora-的核心思路是什么)
<!--END_SECTION:qa_toc-->

---

<!-- omit in toc -->
### 1. 🏷️ LoRA 相关

<!-- omit in toc -->
#### 1.1. ✅ 什么是 LoRA? 它解决了什么问题? 适用什么场景?
> • **LoRA** 是一种当前非常流行的 **参数高效微调 (PEFT)** 技术; <br>
> • **优势/解决的问题**: 全参数微调成本高, 多任务存储冗余, 部署灵活性不足, 减少灾难性遗忘; <br>
> • **适用场景**: 资源受限, 快速迭代, 多任务部署, 避免灾难性遗忘; <br>

<!-- omit in toc -->
#### 1.2. ✅ 与全参微调相比, LoRA 的 **表达上限** 如何?
> • **表达上限**: LoRA 的权重更新被约束在了一个 **低秩子空间** 内, 其复杂性受限于 **秩 ($r$)** 的大小; <br>
> • 对于 **与预训练分布差异大** 的任务, 表达上限可能会低于全参微调; <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>

    - 从数学角度看, 当 $r$ 设置的足够大时, 模型完全有可能在新任务上重塑特征空间 (虽然这与 LoRA 设计的初衷不符);

    </details>

<!-- omit in toc -->
#### 1.3. ✅ LoRA 的参数量如何计算? 与原参数量的比例?
> • **参数量**: $r(d_{in}+d_{out})$; **参数比**: $\dfrac{r(d_{in}+d_{out})}{d_{in} \times d_{out}}$; 通常能压缩到百分之一到千分之一的量级; <br>

-   <details><summary><b> 显存减少量计算 ⬇️ </b></summary>

    - **计算公式**:
        - 显存占用 (字节) = `参数量 * 字节数 (byte)`
    - 主流精度的字节数:
        - `FP32 (32-bit)`: `4 bytes`
        - `FP16 (16-bit)`: `2 bytes`
        - `BF16 (16-bit)`: `2 bytes`
        - `INT8 (8-bit)`: `1 byte`
        - `INT4 (4-bit)`: `0.5 byte5`
            - 相比 `FP32` 降低 8 倍,
            - 相比 `FP16/BF16` 降低 4 倍,

    </details>

<!-- omit in toc -->
#### 1.4. ✅ LoRA 一般作用于哪些层?
> • 大部分线性层 `nn.Linear`: **1.** 注意力层中的 $W_q, W_k, W_v, W_o$; **2.** MLP 层中的 $W_{up}, W_{down}, W_{gate}$<br>

<!-- omit in toc -->
#### 1.5. 💡 写出 LoRA 的 **数学形式**, 并解释各参数的含义与约束
> • $h = Wx + \dfrac{\alpha}{r}B(Ax)$ <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>

    > [LoRA](./SFT_LoRA.md#基础概念)

    </details>

<!-- omit in toc -->
#### 1.6. ✅ 为何需要 **缩放项** `α/r`? 去掉会怎样?
> • **作用**: 稳定训练并控制更新幅度; 去掉会让更新量随秩变化而失控, 增加训练不稳定与调参难度; <br>

<!-- omit in toc -->
#### 1.7. ✅ 为什么常将 `A` 正态初始化, `B` 初始化为 `0`? 如果不这么做会怎么样?
> • **`A` 正态初始化**: 保证了各方向的更新潜力均衡, 避免某些方向先天缺乏梯度信号; <br>
> • **`B` 初始化为 `0`**: 在 **训练开始** 时保持与原模型一致, 确保模型从 **安全可控** 的状态开始学习; <br>
> • 不这么做: **梯度爆炸**, **训练震荡**, **收敛困难**, **灾难性遗忘**; <br>

<!-- omit in toc -->
#### 1.8. ✅ 如何选择 `r` (Rank)? 不同任务/数据规模下的建议是什么?
> • 简单任务/小数据从 r=4/8 开始, 中等任务从 r=16/32 开始, 复杂任务/大数据可尝试 r=64/128, 并配合缩放项与验证集监控动态调整; <br>

<!-- omit in toc -->
#### 1.9. 💡 如果希望逼近全参微调效果, 除了增大 r 还能做什么?
> • [改进 LoRA 结构](./SFT_LoRA.md#结构改进); **多位置接入** (MLP 层); **逐步解冻**/**混合训练**; **超参优化**(学习率/eopch 等); 更先进的算法 (DoRA 等); <br>


<!-- omit in toc -->
### 2. 🏷️ LoRA 的变体

<!-- omit in toc -->
#### 2.1. ✅ QLoRA/AdaLoRA/DoRA 的核心思路是什么?

-   <details><summary><b> 展开详情 ⬇️ </b></summary>

    - **QLoRA**: 低比特量化加载基座模型; LoRA 部分使用全精度 (FP16/BF16);
    - **AdaLoRA**: 在训练过程中 **动态调整** 每层 LoRA 的秩 $r$;
      - 初期用较高秩训练, 通过奇异值分布或梯度范数评估各层重要性;
      - 对重要层保留较高秩, 对不重要层降低秩;
    - **DoRA**: 将原始权重分解为幅度与方向 ($W_0 = m \frac{V}{\|V\|_c}$), 幅度由独立可训练参数控制 ($m$), LoRA 仅作用于方向部分的更新 ($\Delta V$), 避免低秩更新浪费在幅度缩放上;

    </details>
<!--END_SECTION:qa-->