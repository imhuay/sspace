GBDT/XGBoost 备忘
===
<!--START_SECTION:badge-->

![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-10-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-03%2022%3A42%3A16&label_color=gray&color=thistle&style=flat-square)

<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden: false
tag: [ml]
-->

> ***Keywords**: XGBoost*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [概述](#概述)
- [常见面试问题](#常见面试问题)
    - [GBDT 为什么用 CART 回归树做基学习器? ](#gbdt-为什么用-cart-回归树做基学习器)
    - [XGBoost 和 GBDT 的区别](#xgboost-和-gbdt-的区别)
- [参考](#参考)
<!--END_SECTION:toc-->

---

## 概述
- 演进路线: `Boosting` -> `Gradient Boosting` -> `GDBDT` -> `XGBoost`


## 常见面试问题

### GBDT 为什么用 CART 回归树做基学习器?
> 回归树的优点

- 决策树可以认为是 if-then 规则的集合, 可解释性强, 计算速度快;
- 更少的特征工程: 不用做特征标准化, 可以很好的处理字段缺失的数据, 不用关心特征间是否相互依赖等;
- 能够自动组合多个特征 (非参数化的处理特征间的交互关系);
    - 不用担心异常值或者数据是否线性可分;
- 回归树的缺点:
    - 容易过拟合;
    - 解决方法: 抑制决策树的复杂性, 降低单决策树的拟合能力, 再通过梯度提升的方法集成多个决策树;
        - 限制树的个数;
        - 限制树的最大深度;
        - 限制叶子节点的最少样本数量;
        - 限制节点分裂时的最少样本数量;
        - 吸收 bagging 思想对训练样本采样;
        - 在学习单颗决策树时只使用一部分训练样本;
        - 借鉴随机森林的思路在学习单颗决策树时只采样一部分特征;
        - 在目标函数中添加正则项惩罚复杂的树结构等.

### XGBoost 和 GBDT 的区别
TODO


## 参考
- [GBDT/XGBOOST面试总结 - 知乎](https://zhuanlan.zhihu.com/p/412630287)
