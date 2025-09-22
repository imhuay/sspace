反思 (Reflection)
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-08-29&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-23%2000%3A18%3A47&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-08-29 03:38:21
top: false
draft: false
hidden: true
level: 0
tags: [llm_prompt]
-->

<!--START_SECTION:keywords-->
> ***Keywords**: Prompt工程-自反思*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [参考](#参考)
- [实现](#实现)
<!--END_SECTION:toc-->

---

## 参考
- [自反思 (Self-Reflexion) | Prompt Engineering Guide](https://www.promptingguide.ai/zh/techniques/reflexion)
- [\[2406.10400\] Self-Reflection Makes Large Language Models Safer, Less Biased, and Ideologically Neutral](https://arxiv.org/abs/2406.10400)
  > - 自我反思 (Self-Reflection) 是指让大型语言模型 (LLMs) 对自己的输出进行审查和修正, 无需外部反馈.
  > - 虽然**对推理能力的提升效果有限**, 但在安全性、性别偏见和意识形态中立性方面表现显著.


## 实现
- [self_reflect.py](../../../../examples/llm/prompts/self_reflect.py)
    > 通过多轮对话实现自反思
- [Reflection — AutoGen](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/reflection.html)
    > 通过多 Agent 实现反思