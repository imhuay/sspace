大模型微调 <!-- suffix --> [📋](#qa "面试问题整理(9)")$\color{Brown}^{9}$ <!-- suffix -->
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-09-13&labelColor=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-10-24%2018%3A18%3A57&labelColor=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-09-13 13:43:39
toc_title: SFT 基础概念
top: false
draft: false
hidden_in_recent: true
section_number: true
level: 99
tags: [llm_sft]
-->

<!--START_SECTION:keywords-->
> ***Keywords**: SFT*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [基础概念](#基础概念)
    - [大模型训练的三个阶段](#大模型训练的三个阶段)
    - [有监督微调 (SFT) / 指令微调](#有监督微调-sft--指令微调)
    - [RLHF](#rlhf)
- [PEFT](#peft)
    - [LoRA 及其变体](#lora-及其变体)
    - [Adapter](#adapter)
    - [Prefix/Prompt Tuning](#prefixprompt-tuning)
    - [P-Tuning V1/V2](#p-tuning-v1v2)
    - [BitFit (Bias Fine-Tuning)](#bitfit-bias-fine-tuning)
- [Q\&A](#qa)
<!--END_SECTION:toc-->

---

<h3> 背景 </h3>

- 计算机背景;
- 了解 Transformer, BERT 等基础模型;
- 想要入门大模型领域需要了解的基础概念;

## 基础概念

### 大模型训练的三个阶段

- **预训练 (Pre-training)**:
    - 模型在海量文本数据上学习, 获得通用的语言能力和知识;
    - 产出是一个 **基础模型 (Base Model)**;
- **有监督微调 (Supervised Fine-Tuning, SFT)**:
    - 使用高质量的问答或指令遵循数据对基础模型进行微调, 教会它如何与用户交互、遵循指令;
    - 产出是一个 **SFT 模型**, **这也是 RLHF 的基础**;
- **基于人类反馈的强化学习** (**R**einforcement **L**earning from **H**uman **F**eedback, **RLHF**) / **偏好学习** / **对齐学习**:
    - 目标是让模型输出的答案不仅正确, 而且要**符合人类的偏好** (例如: 更有帮助、更无害、更诚实的、排版美观等);
    - SFT 可以教会模型 "回答问题", 而 RLHF 旨在教会模型 "更好地回答问题";

### 有监督微调 (SFT) / 指令微调

- 全参数微调
- 参数高效微调 (Parameter-Efficient Fine-Tuning, PEFT)
    - LoRA (Low-Rank Adaptation)
    - Prefix Tuning, P-Tuning, Adapter, BitFit 等;

### RLHF

- RLHF 要解决的核心问题 (背景/目的)
- RLHF 的核心组件/模型;
    - **策略模型** (Policy Model) / 策略函数
        > **Actor 模型**
    - **优化算法** / 优化器
        > TRPO → PPO (Clip/KL) → DPO → GRPO/IPO/KTO/...
    - **参考模型** (Reference Model)
    - **奖励模型** (Reward Model, 可选) / 奖励函数
    - **价值模型** (Critic Model, 可选) / 价值函数
    <!--
    - **策略模型/函数** (Policy) / **Actor 模型**
        - 即我们要进一步对齐人类偏好的 SFT 模型;
    - **奖励模型/函数** (Reward Model, RM)
    - **价值模型/函数** / **Critic 模型**
    - **强化学习算法** (RL Algorithm) / 优化器
    -->

---

<!--START_SECTION:keyword-->
<!--keyword_info
name: ''
extra_url: false
-->
## PEFT
<!--END_SECTION:keyword-->

<!--START_SECTION:keyword-->
<!--keyword_info
name: 'LoRA'
extra_url: true
-->
### LoRA 及其变体
> [LoRA 笔记](./SFT_LoRA.md)
<!--END_SECTION:keyword-->

- **基本思路**:
    - 对需要微调的 **线性层** (如 `nn.Linear`), 冻结其原始权重 $W \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$, 引入一个 **低秩更新矩阵** $\Delta W$, 用两个小矩阵参数化:
        <div align='center'><a href='_formulas/SFT/f_001.js.tex'><img src='_formulas/SFT/f_001.js.svg'/></a></div>

    - **前向过程** (**旁路相加**):
        <div align='center'><a href='_formulas/SFT/f_002.js.tex'><img src='_formulas/SFT/f_002.js.svg'/></a></div>

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
subject_level: 97
topic: '基础概念'
topic_level: 1
with_section_title: true
use_section_number: true
-->
## Q&A

<!--START_SECTION:qa_toc-->
- [1. 🏷️ 基础概念](#1-️-基础概念)
    - [1.1. ✅ 什么是 **大模型微调**? 为什么需要 **微调**?](#11--什么是-大模型微调-为什么需要-微调)
    - [1.2. ✅ **微调** 与 **预训练** 的区别](#12--微调-与-预训练-的区别)
    - [1.3. ✅ 说明大模型微调的 **一般流程**](#13--说明大模型微调的-一般流程)
    - [1.4. ✅ 什么是 **灾难性遗忘**? 如何缓解?](#14--什么是-灾难性遗忘-如何缓解)
    - [1.5. ✅ 如何设计高质量 SFT 数据? 如何保证 **覆盖率**/**多样性**/**一致性**?](#15--如何设计高质量-sft-数据-如何保证-覆盖率多样性一致性)
    - [1.6. ❓ 有哪些提高 **训练稳定性** 的技巧?](#16--有哪些提高-训练稳定性-的技巧)
- [2. 🏷️ PEFT](#2-️-peft)
    - [2.1. ✅ 比较 **全量微调** 和 **参数高效微调 (PEFT)**](#21--比较-全量微调-和-参数高效微调-peft)
    - [2.2. ✅ 介绍常见的 **PEFT** 技术](#22--介绍常见的-peft-技术)
    - [2.3. 💡 比较 **LoRA** / **Prefix Tuning** / **P-Tuning V2** / **Adapter** / **BitFit**](#23--比较-lora--prefix-tuning--p-tuning-v2--adapter--bitfit)
<!--END_SECTION:qa_toc-->

---

<!-- omit in toc -->
### 1. 🏷️ 基础概念

<!-- omit in toc -->
#### 1.1. ✅ 什么是 **大模型微调**? 为什么需要 **微调**?
> • 大模型微调是利用 **特定数据** 对 **通用预训练模型** 进行 **再训练**, 以高效地让其 **适配下游任务** 的关键技术; <br>
> • **优势**: 高适配, 低成本, 高效率 <br>

<!-- omit in toc -->
#### 1.2. ✅ **微调** 与 **预训练** 的区别
> • 训练目标不同, 数据规模不同, 训练成本不同, 模型能力侧重不同 <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>

    | 维度 | 预训练 | 微调 |
    | --- | --- | --- |
    | 训练目标不同 | 学习通用语言模式与知识表示, 构建广泛的基础能力 | 适配特定任务或领域, 提升在该场景下的性能 |
    | 数据规模不同 | 使用大规模、跨领域的通用数据集 | 使用较小规模、领域相关或任务特定的数据集 |
    | 训练成本不同 | 需要极高的计算资源与时间成本 | 在已有模型基础上进行, 成本显著降低 |
    | 模型能力侧重不同 | 获得广泛的通用能力 | 强化特定任务能力, 可能牺牲部分通用性 |


    </details>

<!-- omit in toc -->
#### 1.3. ✅ 说明大模型微调的 **一般流程**
> • 1.需求分析, 2.数据准备, 3.模型选择, 4.微调策略, 5.训练与监控, 6.模型评估, 7.部署与持续优化 <br>
>> 大模型把所有任务统一到了 **生成任务**, 因此确定 **输入输出形式** 比 **任务类型** 更重要;

-   <details><summary><b> 展开详情 ⬇️ </b></summary>

    1\. **需求分析**: 确定 **输入输出** 形式, 评价指标; <br>
    2\. **数据准备/预处理**: 收集高质量数据, 清洗, 去噪, 格式化; 数据集划分; <br>
    3\. **模型选择**: 考虑因素包括 **模型能力** (通用/领域), **参数量** 和 **计算资源**; <br>
    4\. **微调策略**: 全参数微调 / 参数高效微调 (LoRA 等方法); 偏好学习 (RL) <br>
    5\. **训练与监控**: 训练环境, 超参数 (学习率、批大小、优化器), 验证集指标变化; <br>
    6\. **模型评估**: 测试集性能评估 (过拟合/欠拟合), case 分析; <br>
    7\. **部署与持续优化**: 模型部署; 收集反馈数据, 增量微调/再训练; <br>

    </details>

<!-- omit in toc -->
#### 1.4. ✅ 什么是 **灾难性遗忘**? 如何缓解?
> • **含义**: 模型在新数据上学习时, 覆盖了之前学到的知识; <br>
> • **缓解方法**: PEFT, 混合训练数据, 更小的学习率, 正则化约束, 参数隔离, 渐进式微调 <br>

<!-- omit in toc -->
#### 1.5. ✅ 如何设计高质量 SFT 数据? 如何保证 **覆盖率**/**多样性**/**一致性**?
> • **高质量**: 多样性, 覆盖率; 一致性; <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>

    - **覆盖率**:
        - **构建数据分类体系** (taxonomy)
        - **覆盖率取决于分类体系的完整度**;
    - **多样性**:
        - **指令多样性**: 模板参数化, 同义改写, 风格变换, 语言映射, 噪声与错别字扰动;
        - **深度多样性**: 直接回答, 思维链, 深度思考;
        - **风格多样性**: 角色, 语气;
        - **上下文多样性**: 单轮, 多轮;
    - **一致性**:
        - 多人/多 Agent/多 Prompt

    > [构建高质量SFT数据](./SFT_构建高质量训练数据.md)
    </details>

<!-- omit in toc -->
#### 1.6. ❓ 有哪些提高 **训练稳定性** 的技巧?
> • 数据质量, 模型结构, 初始化策略, 优化器, 训练策略, 调试与监控 <br>


<!-- omit in toc -->
### 2. 🏷️ PEFT

<!-- omit in toc -->
#### 2.1. ✅ 比较 **全量微调** 和 **参数高效微调 (PEFT)**
> • 参数更新范围, 资源成本/训练速度, 数据需求, 灾难性遗忘, 适用场景 <br>
> • **总结**: 全量微调追求极致性能但成本高, PEFT 以低成本实现高适配性并保留通用能力 (减轻灾难性遗忘); <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>

    | 对比维度 | 全量微调 | 参数高效微调 (PEFT) |
    |---|---|---|
    | **参数更新范围** | **全部参数** | **少量新增或选定的参数** |
    | **资源成本/训练速度** | 计算量与显存占用**高**, **训练慢** | 计算量与显存占用**低**, **训练快** |
    | **数据需求** | 需要**大规模数据**以避免过拟合 | 对数据量要求相对较低 |
    | **灾难性遗忘** | **严重** | **较轻** |
    | **适用场景** | **资源充足**, 追求极致性能 | **资源有限**, 多任务部署或快速迭代 |

    </details>

<!-- omit in toc -->
#### 2.2. ✅ 介绍常见的 **PEFT** 技术
> • LoRA/QLoRA, Adapter, Prefix/Prompt Tuning, P-Tuning V1/V2, BitFit <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>

    > [PEFT](#peft)

    </details>

<!-- omit in toc -->
#### 2.3. 💡 比较 **LoRA** / **Prefix Tuning** / **P-Tuning V2** / **Adapter** / **BitFit**
> • 几个关键维度: 表示能力, 推理延迟, 可训练参数量 <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>

    - **表示能力**: Adapter ≥ LoRA ≥ P‑Tuning V2 > Prefix Tuning > BitFit
    - **推理延迟**: LoRA ≈ BitFit < P‑Tuning V2 ≈ Prefix Tuning < Adapter
    - **参数量**: BitFit < P‑Tuning V2 ≈ Prefix Tuning < LoRA < Adapter

    </details>
<!--END_SECTION:qa-->