QA 合集 <!-- suffix --> 🧣[📋](#)$\color{Brown}^{20}$ <!-- suffix -->
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-10-21&labelColor=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-10-22%2017%3A58%3A22&labelColor=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-10-21 17:54:25
toc_title: 'QA 合集'
top: true
draft: false
thorough: true
hidden_in_recent: false
section_number: false
omit_in_tag_toc: false
level: 0
tags: []
algo_tags: []
-->

<!--START_SECTION:keywords-->
> ***Keywords**: QA*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [RLHF · **策略梯度算法**](#rlhf--策略梯度算法)
- [Transformer · **位置编码**](#transformer--位置编码)
<!--END_SECTION:toc-->

---

<!--START_SECTION:sub_tocs-->
## RLHF · **策略梯度算法**

- [1. ✅ PPO 中的 **价值模型** 是怎么训练的?](../09/大模型微调/策略梯度算法.md#1--ppo-中的-价值模型-是怎么训练的)
- [2. 🚩 PPO 中的 **价值模型** 存在什么问题?](../09/大模型微调/策略梯度算法.md#2--ppo-中的-价值模型-存在什么问题)
- [3. 💡 在线策略 (On-Policy) 与离线策略 (Off-Policy) 的本质差异是什么?](../09/大模型微调/策略梯度算法.md#3--在线策略-on-policy-与离线策略-off-policy-的本质差异是什么)
    - [3.1. 💡 PPO 是典型的 在线策略 (On-Policy) 算法, 但为什么有人说 RLHF 中使用的 PPO 是 Off-Policy 的?](../09/大模型微调/策略梯度算法.md#31--ppo-是典型的-在线策略-on-policy-算法-但为什么有人说-rlhf-中使用的-ppo-是-off-policy-的)

## Transformer · **位置编码**

- [1. 🏷️ 位置编码基础](../09/Transformer_整理/位置编码.md#1-️-位置编码基础)
    - [1.1. ✅ **为什么需要位置编码?** (位置编码的必要性, 自注意力的缺陷)](../09/Transformer_整理/位置编码.md#11--为什么需要位置编码-位置编码的必要性-自注意力的缺陷)
    - [1.2. ✅ **什么是"置换不变性"?** (自注意力为何对置换不敏感?)](../09/Transformer_整理/位置编码.md#12--什么是置换不变性-自注意力为何对置换不敏感)
    - [1.3. ✅ **位置编码是如何引入到模型中的?** (常见的引入方式)](../09/Transformer_整理/位置编码.md#13--位置编码是如何引入到模型中的-常见的引入方式)
    - [1.4. ✅ 多头注意力中, 位置参数是共享的吗?](../09/Transformer_整理/位置编码.md#14--多头注意力中-位置参数是共享的吗)
- [2. 🏷️ 常见的位置编码](../09/Transformer_整理/位置编码.md#2-️-常见的位置编码)
    - [2.1. ✅ 介绍常见的位置编码 (除了正弦位置编码, 还有哪些位置编码方式?)](../09/Transformer_整理/位置编码.md#21--介绍常见的位置编码-除了正弦位置编码-还有哪些位置编码方式)
    - [2.2. ✅ 正弦位置编码有哪些优点?](../09/Transformer_整理/位置编码.md#22--正弦位置编码有哪些优点)
    - [2.3. ✅ 解释为何正弦位置编码蕴含了相对位置信息? (三角恒等式推导)](../09/Transformer_整理/位置编码.md#23--解释为何正弦位置编码蕴含了相对位置信息-三角恒等式推导)
    - [2.4. ✅ 正弦位置编码的 "波长" 是什么意思? 不同维度对应的波长有何不同?](../09/Transformer_整理/位置编码.md#24--正弦位置编码的-波长-是什么意思-不同维度对应的波长有何不同)
    - [2.5. ✅ 为什么正弦位置编码使用 **加法** 引入而不是 **拼接**?](../09/Transformer_整理/位置编码.md#25--为什么正弦位置编码使用-加法-引入而不是-拼接)
    - [2.6. ✅ **可学习位置编码** 有哪些应用场景? 优势?](../09/Transformer_整理/位置编码.md#26--可学习位置编码-有哪些应用场景-优势)
- [3. 🏷️ 相对位置编码](../09/Transformer_整理/位置编码.md#3-️-相对位置编码)
    - [3.1. ✅ 什么是相对位置编码? 与绝对位置编码的核心区别是什么?](../09/Transformer_整理/位置编码.md#31--什么是相对位置编码-与绝对位置编码的核心区别是什么)
    - [3.2. ✅ 位置编码中 **相对** 与 **绝对** 的含义](../09/Transformer_整理/位置编码.md#32--位置编码中-相对-与-绝对-的含义)
    - [3.3. ✅ 比较 **绝对位置编码** 与 **相对位置编码**](../09/Transformer_整理/位置编码.md#33--比较-绝对位置编码-与-相对位置编码)
<!--END_SECTION:sub_tocs-->