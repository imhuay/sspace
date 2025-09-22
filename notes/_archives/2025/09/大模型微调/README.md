大模型微调
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-09-13&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-23%2002%3A12%3A48&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-09-13 13:43:39
toc_title: 基础概念
top: false
draft: false
hidden: true
section_number: true
level: 99
tags: [llm_sft]
-->

<!--START_SECTION:keywords-->
> ***Keywords**: README*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [1. 基础概念](#1-基础概念)
    - [1.1. 大模型训练的三个阶段](#11-大模型训练的三个阶段)
    - [1.2. 有监督微调 (SFT) / 指令微调](#12-有监督微调-sft--指令微调)
    - [1.3. RLHF](#13-rlhf)
<!--END_SECTION:toc-->

---

<h3> 背景 </h3>

- 计算机背景;
- 了解 Transformer, BERT 等基础模型;
- 想要入门大模型领域需要了解的基础概念;

## 1. 基础概念

### 1.1. 大模型训练的三个阶段

- **预训练 (Pre-training)**:
    - 模型在海量文本数据上学习, 获得通用的语言能力和知识;
    - 产出是一个 **基础模型 (Base Model)**;
- **有监督微调 (Supervised Fine-Tuning, SFT)**:
    - 使用高质量的问答或指令遵循数据对基础模型进行微调, 教会它如何与用户交互、遵循指令;
    - 产出是一个 **SFT 模型**, **这也是 RLHF 的基础**;
- **基于人类反馈的强化学习** (**R**einforcement **L**earning from **H**uman **F**eedback, **RLHF**) / **偏好学习** / **对齐学习**:
    - 目标是让模型输出的答案不仅正确, 而且要**符合人类的偏好** (例如: 更有帮助、更无害、更诚实的、排版美观等);
    - SFT 可以教会模型 "回答问题", 而 RLHF 旨在教会模型 "更好地回答问题";

### 1.2. 有监督微调 (SFT) / 指令微调

- 全参数微调
- 参数高效微调 (Parameter-Efficient Fine-Tuning, PEFT)
    - LoRA (Low-Rank Adaptation)
    - Prefix Tuning, P-Tuning, Adapter, BitFit 等;

### 1.3. RLHF

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


