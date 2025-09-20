偏好学习 (RLHF) 面试问题整理
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-09-18&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-19%2017%3A06%3A45&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-09-18 16:48:03
toc_title: 偏好学习-QA
top: false
draft: false
hidden: true
section_number: false
level: 0
tags: []
-->

<!--START_SECTION:keywords-->
> ***Keywords**: 偏好学习-QA*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [🏷️ **基础概念**](#️-基础概念)
    - [什么是 RLHF? 它的背景/动机是什么? 相比 SFT 的优势在哪里? 怎么实现的?](#什么是-rlhf-它的背景动机是什么-相比-sft-的优势在哪里-怎么实现的)
    - [⬆️ RLHF 的一般流程是什么? 每一步的目的? 分别解决什么问题?](#️-rlhf-的一般流程是什么-每一步的目的-分别解决什么问题)
        - [指出每阶段的 **输入**, **输出** 与 **失败模式**](#指出每阶段的-输入-输出-与-失败模式)
        - [若 SFT 质量不高, RLHF 会发生什么连锁反应?](#若-sft-质量不高-rlhf-会发生什么连锁反应)
    - [为什么说 RLHF 比 SFT 具有 **更大的策略搜索空间**?](#为什么说-rlhf-比-sft-具有-更大的策略搜索空间)
    - [为什么说 RLHF 比 SFT 更容易 **对齐抽象偏好**?](#为什么说-rlhf-比-sft-更容易-对齐抽象偏好)
    - [在线 RLHF 与离线偏好优化 (如 DPO) 的本质差异是什么?](#在线-rlhf-与离线偏好优化如-dpo的本质差异是什么)
<!--END_SECTION:toc-->

---

<!-- 🔥✅❌⭕❓✔️☑️⚠️⏳🔄⬆️⬇️⬅️➡️↔️📌📍🔖🏷️💡📝 -->
## 🏷️ **基础概念**

### 什么是 RLHF? 它的背景/动机是什么? 相比 SFT 的优势在哪里? 怎么实现的?
> RLHF (Reinforcement Learning from Human Feedback, 基于人类反馈的强化学习)
> - 是一种通过结合 **人类偏好** 与 **强化学习** 来 **微调大语言模型** 的技术;
>> [RLHF 基础概念](./偏好学习.md#基础概念)

### ⬆️ RLHF 的一般流程是什么? 每一步的目的? 分别解决什么问题?

#### 指出每阶段的 **输入**, **输出** 与 **失败模式**

#### 若 SFT 质量不高, RLHF 会发生什么连锁反应?

### 为什么说 RLHF 比 SFT 具有 **更大的策略搜索空间**?

### 为什么说 RLHF 比 SFT 更容易 **对齐抽象偏好**?

### 在线 RLHF 与离线偏好优化 (如 DPO) 的本质差异是什么?

<!--
### 原因概述

- ** 目标从逐令拟合转为序列级回报 **: SFT 以逐 token 交叉熵为目标, 倾向最大化训练数据中每个下一个 token 的概率; 而把人类反馈作为 ** 奖励** 后, 优化目标变为**整个生成序列的标量回报**, 这允许策略评估并偏好在序列层面更高质量但在 token 层面未必最可能的输出;  
- ** 信号类型由点估计变为相对/全局评价 **: 偏好比较或等级评分提供的是 "哪个回复更好" 的相对信息, 比单条目标更能区分多种合理输出, 因此指引模型在更广的解空间中区分与选择;  
- ** 强化学习引入显式探索机制 **: RL 算法 (如 PPO) 通过概率采样、策略梯度和熵正则化鼓励探索低概率但可能高回报的策略路径, 使模型能试验训练集之外的表达与结构;  
- ** 序列级优化打破逐条复制的束缚 **: SFT 的最优策略是复制训练样本分布的高密度区, 而序列级奖励允许组合不同样本的优点或创造新表述, 因而可达成不在任何单条示例中的更优解;  
- ** 多维偏好信号放宽约束方向 **: 奖励可以同时编码准确性、简洁性、风格与安全性等多维偏好, 优化过程不再受单一标准约束, 从而在不同维度之间权衡并探索新的折衷解;  
- ** 受限而非无界的扩展保证可控探索 **: 通过加入 KL 惩罚或信任域, RLHF 在允许策略偏移以探索更优输出的同时, 仍把搜索局限在合理语义空间内, 从而安全地扩大可搜索策略集;  
- ** 优化器与损失景观不同 => 可到达不同解 **: 序列级非凸回报与策略梯度产生不同的优化路径, 使训练过程可能收敛到与 SFT 不同的局部最优, 包含在训练数据中未显式出现但人类偏好更高的输出;  

一句话总结: 因为把人类偏好变为序列级可优化的奖励后, 优化目标、信号类型和训练算法都发生变化, 这些变化共同允许模型在受控条件下探索并加强训练数据之外的高质量策略, 从而显著扩大可搜索的策略空间;
-->

---

<details><summary><b>参考</b></summary>

- [RLHF 模拟面试 - DeepSeek](https://chat.deepseek.com/a/chat/s/7099de24-b6c1-4c21-be27-37fc92f18074)
- [RLHF 模拟面试 - Copilot](https://copilot.microsoft.com/chats/DU9Kj4NXtfACbfjVZkJ1V)

</details>