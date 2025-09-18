多轮MRC信息抽取的优缺点
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-08-23&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-24%2017%3A30%3A57&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-08-23 23:05:36
top: false
draft: true
hidden: true
level: 0
tags: []
-->

<!--START_SECTION:keywords-->
> ***Keywords**: 多轮MRC信息抽取的优缺点*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [对比](#对比)
<!--END_SECTION:toc-->

---

## 对比

| 维度 | 多轮 MRC (链式) | 一次性 MRC / 生成式抽取 |
|------|-----------------|------------------------|
| **抽取精度** | 高, 因每步针对单一子任务, 可单独优化; 但存在误差传播 | 依赖一次前向推理, 避免误差累积; 在稳定数据集上可能略优 |
| **标注成本** | 低~中, 可分阶段标注 (属性→观点→情感) | 高, 一次性三元组标注难度大、易漏标或错标 |
| **可解释性** | 强, 每步结果可单独审查、Debug | 弱, 难定位错误源头 |
| **维护成本** | 低, 模块可独立替换、升级或迁移到新场景 | 高, 需求变动需重新训练整个模型 |
| **推理延迟** | 高, 每轮独立推理累加延迟 | 低, 一次推理完成 |
| **鲁棒性** | 更能适应长尾、噪声场景, 易做规则兜底 | 易受复杂文本或多属性干扰导致整体结果失真 |
| **业务适配性** | 高, 可按需插入或调整环节 (如属性分类) | 低, 结构紧耦合, 灵活性差 |
| **工业界采纳度** | 主流方案, 尤其在数据异质、场景变化频繁的行业 | 较少落地, 更多见于研究或场景极稳的业务 |
| **代表性方案** | 美团到餐 ABSA Pipeline、阿里多阶段情感抽取 | [A Unified Generative Framework for ABSA](https://arxiv.org/abs/2106.04300) 等生成式框架 |