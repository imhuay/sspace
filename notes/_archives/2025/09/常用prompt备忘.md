常用 prompt 备忘
===
<!--START_SECTION:badge-->

![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-09-03&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-10%2010%3A00%3A24&label_color=gray&color=thistle&style=flat-square)

<!--END_SECTION:badge-->
<!--info
date: 2025-09-03 10:26:05
top: false
draft: false
hidden: true
level: 0
tag: [llm_prompt]
-->

<!--START_SECTION:keywords-->
> ***Keywords**: LLM*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [背景](#背景)
- [改写](#改写)
- [知识整理](#知识整理)
    - [面试模拟](#面试模拟)
<!--END_SECTION:toc-->

---

## 背景

记录一些常用的 Prompt

## 改写

**单轮**
```md
说说你对这段内容的理解, 然后从逻辑性、准确性、表达性这三个维度指出其存在的问题, 先给出改进建议, 然后给出修改后的版本, 并遵循以下要求:

- 提纲式、笔记式
- 使用术语、符号 (破折号 -、等号 =、箭头 → 等), 省略非必要词汇 (如冠词、连词)
- 从二级标题 (##) 开始;
- 使用 bullet 排版;
- 对重点进行加粗但不要滥用;
- 不要使用 emoji;
- 一律使用**半角标点**;
- 在中文与英文间插入空格, 在括号左右插入空格, 在加粗文字左右插入空格;
- 用 分号(;) 代替 句号(.)

```

**多轮**
```md
说说你对这段内容的理解, 然后从逻辑性、准确性、表达性这三个维度指出其存在的问题, 并给出改进建议. 不用给出修改后的版本;

---

根据你指出的问题和改进建议, 对这段内容进行修改. 请遵循以下要求

- 提纲式、笔记式
- 使用术语、符号 (破折号 -、等号 =、箭头 → 等), 省略非必要词汇 (如冠词、连词)
- 从二级标题 (##) 开始;
- 使用 bullet 排版;
- 对重点进行加粗但不要滥用;
- 不要使用 emoji;
- 一律使用**半角标点**;
- 在中文与英文间插入空格, 在括号左右插入空格, 在加粗文字左右插入空格;
- 用 分号(;) 代替 句号(.)
```
> 其他 LLM 可能部分要求无法跟随, 比如 copilot 对 "使用半角标点" 就执行不好;


## 知识整理

**DeepSeek** / **Copilot**
> 推荐 Copilot, 默认不加其他 Prompt 的情况下, Copilot 倾向于 **提纲式、笔记式** 的风格;
```md
我正在准备有关 xxx 的面试, 请帮我尽可能详细的罗列相关知识点; 
然后准备一份尽可能全的面试问题清单, 注意清单中所有问题的答案要尽可能在知识点中直接找到或推理得到, 并附上可能得追问;
```

### 面试模拟

```md
### 面试官视角
下面我会以面试官的身份, 问你一些问题, 请从一个应聘者的角度回答问题. 如果没有问题, 请回复 "好的"

### 应聘者视角
你是一位 xxx 方面的专家, 下面我们会进行一场模拟面试: 我会给出一个问题, 以及我的回答;
请你对我的回答进行评价, 并给出改进建议;
```
> **DeepSeek**