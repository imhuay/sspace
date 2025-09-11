RLHF 及其实现 (PPO, DPO, GRPO 等)
===
<!--START_SECTION:badge-->

![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-08-19&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-21%2012%3A39%3A06&label_color=gray&color=thistle&style=flat-square)

<!--END_SECTION:badge-->
<!--info
date: 2025-08-19 22:16:00
top: false
draft: true
hidden: true
level: 0
tag: []
-->

> ***Keywords**: 强化学习*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [背景](#背景)
    - [什么是 RLHF](#什么是-rlhf)
    - [为什么 LLM 需要强化学习](#为什么-llm-需要强化学习)
    - [LLM 中的强化学习算法演进](#llm-中的强化学习算法演进)
- [参考](#参考)
<!--END_SECTION:toc-->

<!--

<div align='center'><img src='path/to/xxx.png' height='300'/></div>

<details><summary><b>点击展开</b></summary>
</details>

[xxx - imhuay/studis](https://github.com/imhuay/studies/blob/master/notes/_archives/2022/04/xxx.md)

特殊符号:
  空格: <&nbsp;>
-->

---

## 背景

### 什么是 RLHF
> RLHF 与 PPO 等强化学习算法之间的关系?

- RLHF (Reinforcement Learning from Human Feedback) 是一种**训练范式**, 用于让语言模型更符合人类偏好;
- RLHF 本身不是指某个具体的算法, 而是一种包含多个阶段的训练策略;
- RLHF 的核心流程:
  1. **预训练语言模型** (如 GPT)
  2. **收集人类偏好数据** (例如对多个回答进行排序)
  3. **训练奖励模型** (根据人类偏好预测回答质量)
  4. **使用强化学习算法优化语言模型** (这一步通常使用 PPO)
- **RLHF 是一种训练范式或方法论**, 而 **PPO 是实现该方法的一种具体强化学习算法**


### 为什么 LLM 需要强化学习

- 传统的监督微调 (SFT) 虽然能让模型模仿人类回答, 但难以捕捉人类的主观偏好.
- RLHF (Reinforcement Learning from Human Feedback) 通过引入奖励模型或偏好数据, 进一步优化模型行为, 使其更 "有帮助" "无害" "符合人类价值" .


<details><summary><b>待整理</b></summary>

```markdown

## 🔧 什么是 PPO (Proximal Policy Optimization) ?

- PPO 是一种强化学习算法, 属于策略梯度方法的一种改进版本.
- 它的特点是通过限制策略更新的幅度 (使用 KL 散度或剪切函数) 来提高训练稳定性.
- 在 RLHF 中, PPO 被用来根据奖励模型的反馈来优化语言模型的输出策略.

```

### LLM 中的强化学习算法演进

```markdown
当然可以, huay! 你在 RLHF 和多智能体系统方面的经验让我可以直接深入技术细节. 下面我将按照时间演进顺序, 系统性地介绍大语言模型中常用的强化学习算法: **PPO → DPO → GRPO**, 并对它们的核心思想、数学机制和适用场景进行对比分析.

---

## 🧠 背景: 为什么 LLM 需要强化学习?

传统的监督微调 (SFT) 虽然能让模型模仿人类回答, 但难以捕捉人类的主观偏好. RLHF (Reinforcement Learning from Human Feedback) 通过引入奖励模型或偏好数据, 进一步优化模型行为, 使其更 "有帮助" "无害" "符合人类价值" .

RLHF 通常分三阶段:

1. **SFT**: 用高质量指令-回答对微调模型.
2. **奖励模型训练**: 用人类偏好数据训练一个打分器.
3. **强化学习优化**: 用 RL 算法 (如 PPO) 引导模型生成更优回答.

---

## 🧩 PPO (Proximal Policy Optimization) ——稳定性之锚 (2017)

PPO 是 RLHF 的经典之选, 由 OpenAI 提出, 首次在 InstructGPT 中大规模应用.

### ✅ 核心思想
- 通过限制策略更新幅度, 避免模型剧烈变化导致性能崩溃.
- 使用奖励模型对生成文本打分, 结合优势函数进行策略更新.

### 🧮 数学机制
PPO 的目标函数如下:

$$
L^{PPO}(\theta) = \mathbb{E}_t \left[ \min \left( r_t(\theta) \hat{A}_t, \text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}_t \right) \right]
$$

其中:
- \( r_t(\theta) \) 是新旧策略概率比;
- \( \hat{A}_t \) 是优势函数;
- clip 限制策略更新在可信区间内.

### 📌 优缺点
| 优点 | 缺点 |
|------|------|
| 稳定、成熟、广泛应用 | 训练复杂, 需奖励模型和价值函数 |
| 支持多目标奖励设计 | 算法实现和调参成本高 |

---

## 🧭 DPO (Direct Preference Optimization) ——去奖励建模 (2023)

由斯坦福提出, DPO 是一种更简洁的 RLHF 方法, 跳过奖励模型训练, 直接用人类偏好进行优化.

### ✅ 核心思想
- 输入为两个回答 (chosen vs rejected) , 优化目标是让模型更偏好 chosen.
- 类似 SFT 的训练范式, 稳定易实现.

### 🧮 数学机制
损失函数如下:

$$
\mathcal{L}_{DPO} = \log \frac{\exp(\beta f_\theta(x, y^+))}{\exp(\beta f_\theta(x, y^+)) + \exp(\beta f_\theta(x, y^-))}
$$

其中:
- \( f_\theta(x, y) \) 是模型对回答的打分 (logit) ;
- \( \beta \) 控制偏好强度.

### 📌 优缺点
| 优点 | 缺点 |
|------|------|
| 无需奖励模型, 训练更简单 | 无法支持复杂 reward 设计 |
| 与 SFT 接近, 易于部署 | 不适合多目标或动态奖励场景 |

---

## 🧪 GRPO (Group Relative Policy Optimization) ——多智能体协同优化 (2024–2025)

由 DeepSeek AI 引入, GRPO 是 PPO 的进化版, 适用于多智能体协同任务和复杂推理场景.

### ✅ 核心思想
- 引入 "组别" 概念, 在多个智能体之间进行相对策略优化.
- 支持多维度奖励设计 (如意图理解、属性匹配、推理过程等) .

### 🧮 数学机制 (简化)
GRPO 在 PPO 基础上, 引入 group-wise 相对优势函数:

$$
L^{GRPO}(\theta) = \sum_{g \in G} \mathbb{E}_{t \in g} \left[ \min \left( r_t(\theta) A_t^g, \text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon) A_t^g \right) \right]
$$

其中 \( A_t^g \) 是组别内的相对优势.

### 📌 优缺点
| 优点 | 缺点 |
|------|------|
| 支持多智能体协同优化 | 实现复杂, 需组别定义和奖励分解 |
| 更适合复杂推理和结构化任务 | 训练资源消耗大 |

---

## 🧠 总结对比

| 算法 | 提出时间 | 是否需奖励模型 | 是否支持多目标 | 稳定性 | 实现复杂度 |
|------|----------|----------------|----------------|--------|--------------|
| PPO  | 2017     | ✅ 是           | ✅ 是           | ✅ 高   | ❌ 高         |
| DPO  | 2023     | ❌ 否           | ❌ 否           | ✅ 高   | ✅ 低         |
| GRPO | 2024–25  | ✅ 是           | ✅ 是           | ✅ 高   | ❌ 高         |
```

</details>

## 参考
