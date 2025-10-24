PEFT (Parameter-Efficient Fine-Tuning) <!-- suffix --> [📋](#qa "面试问题整理(10)")$\color{Brown}^{10}$ <!-- suffix -->
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-09-16&labelColor=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-10-24%2016%3A35%3A33&labelColor=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-09-16 18:31:31
toc_title: 参数高效微调 (**PEFT**)
top: false
draft: false
hidden_in_recent: true
section_number: false
level: 1
tags: [llm_sft]
-->

<!--START_SECTION:keywords-->
> ***Keywords**: [SFT](SFT.md)*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [常用方法](#常用方法)
    - [LoRA 及其变体](#lora-及其变体)
    - [Adapter](#adapter)
    - [Prefix/Prompt Tuning](#prefixprompt-tuning)
    - [P-Tuning V1/V2](#p-tuning-v1v2)
    - [BitFit (Bias Fine-Tuning)](#bitfit-bias-fine-tuning)
- [Q\&A](#qa)
<!--END_SECTION:toc-->

---

## 常用方法

<!--START_SECTION:keyword-->
<!--keyword_info
name: '**LoRA**'
extra_url: true
-->
### LoRA 及其变体
> [LoRA 笔记](./SFT_LoRA.md)
<!--END_SECTION:keyword-->

- **基本思路**:
    - 对需要微调的 **线性层** (如 `nn.Linear`), 冻结其原始权重 $W \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$, 引入一个 **低秩更新矩阵** $\Delta W$, 用两个小矩阵参数化:
        <div align='center'><a href='_formulas/SFT_PEFT/f_001.js.tex'><img src='_formulas/SFT_PEFT/f_001.js.svg'/></a></div>

    - **前向过程** (**旁路相加**):
        <div align='center'><a href='_formulas/SFT_PEFT/f_002.js.tex'><img src='_formulas/SFT_PEFT/f_002.js.svg'/></a></div>

        - 缩放因子 $\dfrac{\alpha}{r}$ 控制 $\Delta W$ 的幅度, 避免训练初期过大扰动;
- **代码 Demo**:
    - [LoRA](./_code/lora.py)

### Adapter
- **思路**:
    - 在 Transformer 每层的前馈网络 (或注意力输出) 后插入一个小型可训练的 **瓶颈层** (bottleneck)
- **代码 Demo**
    - [Adapter](./_code/adapter.py)

### Prefix/Prompt Tuning

- **思路**:
    - Prefix Tuning 在 **Transformer 每一层的注意力机制** 中, 为 Key/Value 拼接可训练的 **前缀向量**;
    - Prompt Tuning 仅在 **输入嵌入层** 前拼接可训练的软提示向量;
- **代码 Demo**
    - [Prefix Tuning](./_code/prefix_tuning.py)
    - [Prompt Tuning](./_code/prompt_tuning.py)

### P-Tuning V1/V2

- **思路**:
    - 将原本人工设计的离散 Prompt 替换为可训练的连续向量 (virtual tokens);
    - 这些向量通过一个提示编码器 (Prompt Encoder)  (通常是 LSTM + MLP) 生成;
    - V1/V2 的区别类似 Prefix/Prompt Tuning, **仅作用于输入层 vs 作用于每一个 TransformerBlock**;
- **代码 Demo**
    - [P-Tuning V1](./_code/p_tuning.py)
    - [P-Tuning V2](./_code/p_tuning_v2.py)

### BitFit (Bias Fine-Tuning)

- **思路**:
    - 在微调大模型时, **只更新偏置参数** (bias), 冻结所有权重矩阵;
- **动机**:
    - 偏置参数占模型总参数量极小, 但 **在很多任务中对输出分布的平移有显著影响**;
- **缺点**:
    - 表达能力有限, 对需要大幅调整特征空间的任务效果可能不如 LoRA 等方法;
- **代码 Demo**
    - [BitFit](./_code/bitfit.py)

---

<!--START_SECTION:qa-->
<!--qa_info
subject: 'SFT'
subject_level: 98
topic: 'PEFT (参数高效微调)'
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