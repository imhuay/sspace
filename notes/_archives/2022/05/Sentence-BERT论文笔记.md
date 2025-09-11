Sentence-BERT 论文笔记
===
<!--START_SECTION:badge-->

![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-05-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-15%2022%3A16%3A49&label_color=gray&color=thistle&style=flat-square)

<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden: false
tag: [dl_embed]
-->

> ***Keywords**: Sentence-BERT*

<!--START_SECTION:toc-->
- [相关资料](#相关资料)
    - [相关阅读](#相关阅读)
- [模型结构](#模型结构)
- [关键结构](#关键结构)
    - [Pooling 层](#pooling-层)
- [常见问题](#常见问题)
    - [为什么 SBERT 中训练与预测不一致的方法会有效? ](#为什么-sbert-中训练与预测不一致的方法会有效)
    - [为什么通过分类任务后, 就能直接使用模型输出向量的 cosine 值来表示相似度? ](#为什么通过分类任务后就能直接使用模型输出向量的-cosine-值来表示相似度)
    - [为什么加入一个线性层后比直接学习距离的效果更好? ](#为什么加入一个线性层后比直接学习距离的效果更好)
    - [为什么采用 `(u, v, |u-v|)` 的方式进行特征组合? ](#为什么采用-u-v-u-v-的方式进行特征组合)
- [TODO 关键词](#todo-关键词)
<!--END_SECTION:toc-->

---

## 相关资料
- 【GitHub】[UKPLab/sentence-transformers: Multilingual Sentence & Image Embeddings with BERT](https://github.com/UKPLab/sentence-transformers)
- [[EMNLP 2019] Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084)

### 相关阅读
- [[EMNLP 2017] Supervised Learning of Universal Sentence Representations from Natural Language Inference Data](https://arxiv.org/abs/1705.02364)


## 模型结构

<div align="center"><img src="../../../_assets/imgs/Sentence-BERT模型图.png" height="300" /></div>

<!-- > [CoSENT (一) : 比Sentence-BERT更有效的句向量方案 - 科学空间|Scientific Spaces](https://kexue.fm/archives/8847) -->


## 关键结构

### Pooling 层
TODO

```python
```


## 常见问题

### 为什么 SBERT 中训练与预测不一致的方法会有效?

**【训练和预测不一致的情况在预训练任务中很常见】**
- 首先, 训练和预测不一致的情况很常见, 几乎所有的预训练任务都存在这个问题, 因为训练和预测的**目标**不同; 训练时会采用各种不同的代理任务来训练模型, 而预测时一般会使用基模型输出的 Embedding 作为后续模型的输入;
- 其次, Sentence-BERT 中训练与预测不一致的情况只在**分类任务**中出现; 对于**回归任务**, 即标签是浮点值的场景, SBERT 在训练和预测时是一致的, 此时使用 MSE Loss (均方误差损失) 作为目标函数;
- SBERT 中的问题是**为什么通过分类代理任务后, 不需要微调就能直接使用输出向量的 cosine 值作为相似度?** 这是与其他预训练任务不同的地方;

### 为什么通过分类任务后, 就能直接使用模型输出向量的 cosine 值来表示相似度?
- 首先, 不是任何分类任务都可以的, 而是需要进行**相似性判断**的分类任务;
- 其次, 不光可以使用 cosine 距离, SBERT 库还提供了曼哈顿距离、欧几里得距离等度量方式, 都可以用来衡量相似度, 且效果差异不大;
- 这表明模型学到的并不是单一的 cosine 相似度, 而是学到了**通过向量刻画相似**的方法, 所以即使是不同的相似度计算方法都可以得到类似的结果;
- 而产生这个结果是显然的, 因为目标任务虽然没有直接使用距离作为目标函数, 但依然需要通过模型输出的向量来表达 "相似" 这一概念, 因此期待输出的向量能够表达相似也是合理的;
    - 另一个回答的方向是从 `|u-v|` 这个特征组合入手 (详见后面的问题) ; 但即使不使用这个特征依然可以使用 cosine, 它的加入只是提升了效果;

### 为什么加入一个线性层后比直接学习距离的效果更好?
> 为什么在分类任务中不建议直接使用 cosine 距离 (或其他距离) 作为训练目标?
- 在分类场景下, label 通常是 `0/1` 这样的离散值, 其真实含义为 "**是否**" , 而不是 "相似度" ; 可想而知, 如果将其作为相似度进行训练, 会有极大的可能出现**过拟合**;
- 一个可能的原因是 `0/1` 标签的先验假设太强, 导致过度学习; 简单来说, 一般训练集中的负样本通常是 "**困难样本**" , 虽然语义不同, 但也不至于完全不相似 (label 为 `0`) ; 如此训练的结果通常是**过拟合**, 甚至无法收敛;
- 而加入一个线性层 (不带激活函数) , 可以一定程度上弱化这个先验, 提升模型的泛化能力, 避免过拟合;
    > 一个例子是, 对比学习中的 SimCLR 模型, 他在训练时会加入一个**非线性投影层**来对特征向量降维, 以避免过拟合; 该操作在之后的对比学习任务中被广泛采用;
- 除了加入全连接层, 下面给出其他改进方案:
    > [CoSENT (一) : 比Sentence-BERT更有效的句向量方案 - 科学空间|Scientific Spaces](https://kexue.fm/archives/8847)
    - 法1) 增加 "困难负例" 的得分 (如 0.5、0.7 等) , 同时采样一些完全无关的句子作为纯负样本, 避免过度学习; 该方法的问题是如何选择这个阈值;
    - 法2) 学习相似度的相对差异, 而不是绝对差异; 即只保证正例的相似度大于负例, 至于大多少由模型来决定; 具体来说, 使用排序 loss 代替交叉熵或均方差损失;


### 为什么采用 `(u, v, |u-v|)` 的方式进行特征组合?
- 首先特征组合是机器学习中常见的做法; 一般经验是采用**拼接**的方式能够最大程度保留原始特征, 并激发神经网络的拟合能力;
- 其次 `(u, v, |u-v|)` 的组合方式是消融实验的结果, 结果表明这样进行特征组合的效果最好;
- 一个可能的解释是, 无论采用哪种距离度量方式, 都有当 `u == v` 时, `|u-v| = 0`, 即 `|u-v|` 也能刻画两个向量的相似程度; 这相当于为模型提供了一个如何刻画两个向量相似的学习方向; 当模型学习到两个相似向量的 `|u-v| = 0` 时, 也就能使用向量的 cosine 值来刻画相似度了;
    > [用开源的人工标注数据来增强RoFormer-Sim - 科学空间|Scientific Spaces](https://kexue.fm/archives/8541#%E9%97%AD%E9%97%A8%E9%80%A0%E8%BD%A6)


## TODO 关键词
- 各向同性、各向异性
- 白化 whitening
- BERT-Flow
- WhiteningBERT