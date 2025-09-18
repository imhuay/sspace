构建高质量大模型微调数据
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-09-17&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-19%2004%3A11%3A35&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-09-17 13:38:07
toc_title: SFT 数据构建
top: false
draft: true
hidden: true
section_number: false
level: 0
tags: [llm_sft]
-->

<!--START_SECTION:keywords-->
> ***Keywords**: 构建高质量SFT数据*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [背景](#背景)
- [覆盖率](#覆盖率)
    - [**构建数据类别体系**](#构建数据类别体系)
- [多样性/复杂性](#多样性复杂性)
- [一致性](#一致性)
- [复杂性](#复杂性)
<!--END_SECTION:toc-->

---

## 背景

- **高质量数据是决定模型微调性能上限的关键**
- **核心维度**: 覆盖率, 多样性/复杂性, 一致性;
- **其他维度**: 准确性, 流畅性, 安全性, 时效性;

## 覆盖率

- **一般流程**:
    1. 构建数据类别体系;
    2. 数据收集;
    3. 数据标注: 为数据打上一个或多个标签;
- **AI 辅助生成**:
    1. 构建数据类别体系;
    2. 给定一个或多个标签由 Agent 辅助生成对应数据数据;
- **覆盖率取决于 *类别体系* 构建的完整度**;

### **构建数据类别体系**

- 首先根据任务 **领域** 设计一个分类体系;
    - 分类体系可以是一个 **复杂的, 层次化** 的 **Taxonomy**;
    - 或者简单的一系列 **属性/标签**;
- **示例**:
    - <details><summary><b>编程</b></summary>

        ```md
        - **第一层**
            1. 代码生成
            2. 代码理解
            3. 语言转换
            4. ...
        - **第二层**
            1. 代码生成
                1.1 从零实现
                1.2 代码补全
                1.3 ...
            2. 代码理解
                2.1 代码解释
                2.2 错误定位
                2.3 ...
            3. ...
        - **第三层**: 属性/标签
            - **编程语言**: `Python`, `JavaScript`, `Java`, `C++`, `Go`, `SQL`, `Bash`, `HTML/CSS`...
            - **技术领域/框架**:
                - `Web`: React, Vue, Django, Spring
                - `Data Science`: Pandas, NumPy, PyTorch, TensorFlow
                - `System`: Linux, Docker, Kubernetes
                - `Mobile`: Android, SwiftUI
        ```

      </details>
    - <details><summary><b>电商客服</b></summary>

        ```md
        - **第一层**
            1. 商品咨询
            2. 订单服务
            3. 售后支持
            4. 平台规则
        - **第二层**
            1. 商品咨询
                1.1 商品信息
                1.2 库存物流
                1.3 ...
            2. 订单服务
                2.1 下单与支付
                2.2 修改与取消
                2.3 ...
            3. ...
        - **第三层**: **属性/标签**:
            - **商品品类**: `服装`, `数码`, `家居`, `美妆`, `食品`
            - **问题复杂度**: `简单`, `中等`, `复杂`
        ```

    </details>

## 多样性/复杂性

- **指令多样性**
    - 模板参数化;
    - 同义改写;
    - 风格变换;
    - 噪声与错别字扰动;
    - 多语言映射;
- **深度多样性**
    - 直接回答, 思维链, 深度思考;
- **风格多样性**
    - 角色, 语气, 文风;
- **难度多样性**
    - 基础, 中级, 高级;
- **上下文多样性**
    - 单轮/多轮;
    - 话题转换;
- **推理复杂度**
    - 逻辑推理, 数值计算;
- **任务复杂性**
    - 单一任务, 组合任务;


## 一致性

- **多源标注**
    - 多人标注
    - 多 Agent 标注
    - 多 Prompt 标注


## 复杂性

