PEFT (Parameter-Efficient Fine-Tuning)
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-09-16&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-23%2002%3A12%3A48&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-09-16 18:31:31
toc_title: 参数高效微调 (**PEFT**)
top: false
draft: false
hidden: true
section_number: false
level: 0
tags: [llm_sft]
-->

<!--START_SECTION:keywords-->
> ***Keywords**: PEFT*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [常用方法](#常用方法)
    - [LoRA](#lora)
    - [Adapter](#adapter)
    - [Prefix/Prompt Tuning](#prefixprompt-tuning)
    - [P-Tuning V1/V2](#p-tuning-v1v2)
    - [BitFit (Bias Fine-Tuning)](#bitfit-bias-fine-tuning)
- [面试问题整理](#面试问题整理)
<!--END_SECTION:toc-->

---

## 常用方法

<!--START_SECTION:keyword-->
<!--keyword_info
name: '**LoRA**'
extra_url: true
-->
### LoRA
> [LoRA 笔记](./LoRA.md)
<!--END_SECTION:keyword-->

- **基本思路**:
    - 对需要微调的 **线性层** (如 `nn.Linear`), 冻结其原始权重 $W \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$, 引入一个 **低秩更新矩阵** $\Delta W$, 用两个小矩阵参数化:
        $$
        \Delta W = B \cdot A,\quad B \in \mathbb{R}^{d_{\text{out}} \times r},\; A \in \mathbb{R}^{r \times d_{\text{in}}},\; r \ll \min(d_{\text{out}}, d_{\text{in}})
        $$
    - **前向过程** (**旁路相加**):
        $$
        y = W x + \dfrac{\alpha}{r} \cdot B(Ax)
        $$
        - 缩放因子 $\dfrac{\alpha}{r}$ 控制 $\Delta W$ 的幅度, 避免训练初期过大扰动;
- **代码 Demo**:
    - [LoRA](./code/lora.py)

### Adapter
- **思路**:
    - 在 Transformer 每层的前馈网络 (或注意力输出) 后插入一个小型可训练的 **瓶颈层** (bottleneck)
- **代码 Demo**
    - [Adapter](./code/adapter.py)

### Prefix/Prompt Tuning

- **思路**:
    - Prefix Tuning 在 **Transformer 每一层的注意力机制** 中, 为 Key/Value 拼接可训练的 **前缀向量**;
    - Prompt Tuning 仅在 **输入嵌入层** 前拼接可训练的软提示向量;
- **代码 Demo**
    - [Prefix Tuning](./code/prefix_tuning.py)
    - [Prompt Tuning](./code/prompt_tuning.py)

### P-Tuning V1/V2

- **思路**:
    - 将原本人工设计的离散 Prompt 替换为可训练的连续向量 (virtual tokens);
    - 这些向量通过一个提示编码器 (Prompt Encoder)  (通常是 LSTM + MLP) 生成;
    - V1/V2 的区别类似 Prefix/Prompt Tuning, **仅作用于输入层 vs 作用于每一个 TransformerBlock**;
- **代码 Demo**
    - [P-Tuning V1](./code/p_tuning.py)
    - [P-Tuning V2](./code/p_tuning_v2.py)

### BitFit (Bias Fine-Tuning)

- **思路**:
    - 在微调大模型时, **只更新偏置参数** (bias), 冻结所有权重矩阵;
- **动机**:
    - 偏置参数占模型总参数量极小, 但 **在很多任务中对输出分布的平移有显著影响**;
- **缺点**:
    - 表达能力有限, 对需要大幅调整特征空间的任务效果可能不如 LoRA 等方法;
- **代码 Demo**
    - [BitFit](./code/bitfit.py)

---

<!--START_SECTION:keyword-->
<!--keyword_info
name: 'QA'
extra_url: true
-->
## 面试问题整理
> [PEFT QA](./PEFT_QA.md)
<!--END_SECTION:keyword-->