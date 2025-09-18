AutoPhrase 备忘
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-08-22&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-19%2004%3A11%3A35&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-08-22 12:51:20
top: false
draft: false
hidden: false
level: 2
tags: [nlp_kg]
-->

<!--START_SECTION:keywords-->
> ***Keywords**: [短语挖掘](../07/短语挖掘.md)*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [背景](#背景)
    - [工程优势](#工程优势)
    - [参考资料](#参考资料)
- [核心流程](#核心流程)
    - [1. 候选短语生成](#1-候选短语生成)
    - [2. 短语质量评估](#2-短语质量评估)
    - [3. 远程监督训练](#3-远程监督训练)
    - [4. 短语切分优化 (可选)](#4-短语切分优化-可选)
- [PMI 计算](#pmi-计算)
    - [多词 PMI](#多词-pmi)
- [KL 散度计算](#kl-散度计算)
    - [AutoPhrase 中的 KL 散度](#autophrase-中的-kl-散度)
        - [示例](#示例)
- [IDF 计算](#idf-计算)
    - [示例](#示例-1)
<!--END_SECTION:toc-->

---

## 背景

AutoPhrase 是一种**半监督的短语挖掘算法/工具**, 由韩家炜团队提出, 专注于从原始文本中提取语义完整、信息量高的短语; 它的设计目标是:
- **领域无关**: 不依赖特定领域知识
- **语言适配强**: 支持多语言 (包括中文)
- **低人工成本**: 利用远程监督 (distant supervision) 自动构建训练数据

### 工程优势

- **轻量级部署**: C++ 实现, 效率高, 适合大规模语料处理;
- **可插拔词典**: 支持自定义种子短语, 适配特定业务场景;
- **语言扩展性强**: 通过编码/解码机制支持非英语语料;

### 参考资料
- 论文: [\[1702.04457\] Automated Phrase Mining from Massive Text Corpora](https://arxiv.org/abs/1702.04457)
- 代码: [shangjingbo1226/AutoPhrase: AutoPhrase: Automated Phrase Mining from Massive Text Corpora](https://github.com/shangjingbo1226/AutoPhrase)
- 解读: [AutoPhrase - 知乎](https://zhuanlan.zhihu.com/p/561578564)

## 核心流程

### 1. 候选短语生成
- 使用 n-gram 滑窗从语料中生成所有可能的短语;
- 设置最小支持度 (如频率 ≥ 30) 和最大长度 (如 ≤ 6);

### 2. 短语质量评估
- 构建短语质量评分器 $Q(·)$, 主要基于以下统计特征:
  - **PMI (点互信息) **: 衡量词与词之间的黏合度;
    > [PMI 计算](#pmi-计算)
  - **KL 散度**: 衡量短语与背景分布的差异;
    > [KL 计算](#kl-散度计算)
  - **IDF (逆文档频率) **: 衡量信息量;
    > [IDF 计算](#idf-计算)
- 对每个候选短语打分, 通过**设定阈值**来筛选高质量候选短语;
    > "候选短语"即第 1 步中通过滑窗生成的所有 n-gram 组合;

### 3. 远程监督训练
> 远程监督使用的语料与第 2 步中生成候选的语料, 两者在概念和功能上是解耦的, 可以将它们视为两个独立的语料, 各自服务不同目标, 不过有时也可根据需求复用同一原始文本;
- 从 Wikipedia 等通用知识库中提取高质量短语作为正样本池;
- 将剩余候选短语视为噪声负样本池;
- 使用集成模型 (如随机森林) 进行降噪训练, 提升分类器鲁棒性;
    - 使用的特征除了第 2 步中的之外, 还有其他统计特征, 比如"出现频率", "是否包含停用词", "Cohesion Score", 组合特征等等;

### 4. 短语切分优化 (可选)
> POS-Guided Phrasal Segmentation
- 对语料进行**词性标注**(POS tagging), 统计高置信短语的 POS 序列, 找出 Top-N 的常见模式;
- 对已有的高质量候选短语统计它们的词性序列模式, 保留命中常见模式的候选;
- 重新计算短语频率和质量, 提升完备性和准确率;


## PMI 计算
> PMI, 即"**点互信息**" (Pointwise Mutual Information)

**作用**: 衡量词与词的共现紧密程度

**公式**:

$$
    PMI(w_1, w_2) = \log_2 \frac{P(w_1, w_2)}{P(w_1) \cdot P(w_2)}
$$

其中
- $P(w_1, w_2)$ - 组合短语在语料中出现的概率;
- $P(w_1), P(w_2)$ - 各自单独出现的概率;


### 多词 PMI

<!-- omit in toc -->
#### 方案 1: **Pairwise PMI** (最常用)

- 把多词组合拆成若干相邻或成对的词, 然后对这些词对计算 PMI, 再用某种方式聚合
    - **最小值法**: 取组合里所有相邻词对 PMI 的最小值, 保证 "最弱的一环" 也达标;  
    - **均值法**: 取所有相邻词对 PMI 的平均值, 反映整体平均黏合度;  
    - **加权平均**: 权重按位置、频率或业务重要性分配, 比如头词和尾词的相关性可以给更高权重;  
- 示例
    ```txt
    短语: nasi goreng ayam
    pairwise: PMI(nasi, goreng), PMI(goreng, ayam)
    multi-PMI = min / mean / weighted_mean 之一
    ```
- 在实际语料里, **高阶 PMI 对低频组合不稳定**, 所以多用 pairwise 聚合而不是直接三元概率;

<!-- omit in toc -->
#### 方案 2: **多元 PMI** (二元版本的高阶扩展)
- 定义:
    $$
    PMI(w_1, w_2, w_3) = \log \frac{P(w_1,w_2,w_3)}{P(w_1) P(w_2) P(w_3)}
    $$
    更常见的条件式:
    $$
    PMI(w_1, w_2, w_3) = \log \frac{P(w_1,w_2,w_3)}{P(w_1,w_2) \cdot P(w_3)}
    $$
- 分母代表这三个词在"假设部分独立"条件下的期望共现概率, 分子是真实三元组概率;
- 缺点是**三元共现概率稀疏**, 低频组合噪声大, 需要设较高的频次下限;

<!-- omit in toc -->
#### 方案 3: **链式 PMI**
- 示例
    $$
    PMI(w_1,w_2,w_3) = PMI(w_1,w_2) + PMI((w_1,w_2),w_3)
    $$
- 这样可以直接复用二元统计逻辑, 并且对 (w1,w2) 先合并成"词块"再与 w3 计算 PMI, 相当于做了一次层次化评估;


## KL 散度计算

**KL 散度** (Kullback-Leibler Divergence) 作用: **衡量两个分布之间的差异**;

**公式**(离散型):
$$
    D_{KL}(P || Q) = \sum_{i} P(i) \log \frac{P(i)}{Q(i)}
$$

### AutoPhrase 中的 KL 散度

- 在 AutoPhrase 中, KL 散度被用来衡量一个候选短语的上下文分布与整个语料的背景分布之间的差异, 从而评估该短语是否具有 "**语义独立性**";
- 具体来说,
    - $i$ 为候选短语的上下文词 (即**这个短语周围出现的词**),
    - $P(i)$ 为 $i$ 在短语上下文中出现的概率,
    - $Q(i)$ 为 $i$ 在整个语料中的概率;


#### 示例

**Step 1: 定义上下文窗口**
- 定义上下文窗口长度为 1, 即左右各取 1 个词;
    ```txt
    ... saya suka makan [nasi goreng] enak dan pedas ...
                    ↑                  ↑
                    左1                右1
    ```
    - 从语料中找到所有 nasi goreng 的出现位置, 并统计它周围的词;

**Step 2: 统计上下文词频 (得到 $P(i)$) **
- 对所有 nasi goreng 的上下文词进行统计, 比如:
     词    | 出现次数 | 上下文总次数 | $P(i)$=次数/总数
     :---- | :------- | :----------- | :---------------
     makan | 30       | 1000         | 0.03  
     enak  | 20       | 1000         | 0.02  

**Step 3: 统计语料整体词频 (得到 $Q(i)$) **
- 对整个语料进行词频统计, 不考虑短语, 只统计所有词的出现频率:
     词    | 出现次数 | 语料总次数 | $Q(i)$=次数/总数
     :---- | :------- | :--------- | :---------------
     makan | 100      | 10000      | 0.01  
     enak  | 600      | 10000      | 0.06  

**Step 4: 计算 KL 散度**

- 带入公式:
$$
\begin{aligned}
    D_{KL}(P || Q) &= \sum_{i} P(i) \log \frac{P(i)}{Q(i)} \\
    &= 0.03\log\frac{0.03}{0.01} + 0.02\log\frac{0.02}{0.06}
\end{aligned}
$$
- 这个值越大, 说明 nasi goreng 的上下文分布越 "特殊", 越可能是一个语义独立的短语;


## IDF 计算

IDF (Inverse Document Frequency, 逆文档频率) 是衡量一个词在整个语料库中 "稀有程度" 的指标, 常用于信息检索、关键词提取、文本分类等任务中; 它的核心思想是:

> 一个词如果出现在很多文档中, 它的区分能力就低; 如果只出现在少数文档中, 它更可能是有信息价值的关键词;


**公式**:
$$
\text{IDF}(t) = \log \left( \frac{N}{df(t) + 1} \right)
$$
其中
- $t$: 目标词项 (term)
- $N$: 语料库中的总文档数
- $df(t)$: 包含词 \( t \) 的文档数量 (document frequency)
- 加 1 是为了避免分母为 0 (即词从未出现)


### 示例

假设语料库中总共有 $N = 1000$ 篇文档:

- 词 "机器学习" 出现在 50 篇文档中:
  $$
  \text{IDF}("机器学习") = \log \left( \frac{1000}{50 + 1} \right) \approx \log(19.6) \approx 1.29
  $$

- 词 "的" 出现在 950 篇文档中:
  $$
  \text{IDF}("的") = \log \left( \frac{1000}{950 + 1} \right) \approx \log(1.05) \approx 0.02
  $$

- 词 "深度学习" 只出现在 10 篇文档中:
  $$
  \text{IDF}("深度学习") = \log \left( \frac{1000}{10 + 1} \right) \approx \log(91) \approx 1.96
  $$

越稀有的词, IDF 值越高, 代表它在区分文档时更有价值.
