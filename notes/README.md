Notes
===

<table>
<tr>
<td valign="top" width="1000">

<!-- omit in toc -->
## Index 📑

<!-- TOC -->
- [Researches](#researches)
    - [Transformer 🪄 LLM 🚀](#transformer--llm-)
        - [大模型微调 🔥](#大模型微调-)
    - [Machine Learning 🤖](#machine-learning-)
    - [Deep Learning 🧠](#deep-learning-)
    - [NLP 🔤](#nlp-)
    - [Algorithms 🧩](#algorithms-)
    - [Reading List 🔖](#reading-list-)
    - [Paper Notes 📝](#paper-notes-)
- [Engineerings](#engineerings)
    - [Python 🐍](#python-)
    - [Big Data 📊](#big-data-)
    - [Tools 🛠️](#tools-️)
    - [Design Pattern 🏗️](#design-pattern-️)
- [Wiki](#wiki)
- [Drafts](#drafts)
<!-- TOC -->

</td>
<td valign="top" width="2000">

<!-- omit in toc -->
## Recent 📖
<!--START_SECTION:recent-->
- [`2025-07-08` Markdown 简历工具](_archives/2022/06/Markdown_简历工具.md) 📌
- [`2025-10-03` 策略梯度定理及其推导](_archives/2025/09/大模型微调/策略梯度定理及其推导.md) 🧣
- [`2025-09-09` 位置编码 (Position Encoding)](_archives/2025/09/Transformer_整理/位置编码.md) 
- [`2025-09-05` Transformer 模型架构](_archives/2025/09/Transformer_整理/README.md) 
- [`2025-09-18` RLHF (基于人类反馈的强化学习)](_archives/2025/09/大模型微调/RLHF.md) ✒️🧣
- [`2025-08-22` AutoPhrase 备忘](_archives/2025/08/AutoPhrase备忘.md) 
- [`2025-08-21` 复合词检测](_archives/2025/08/复合词检测.md) 
- [`2025-08-08` VSCode 备忘](_archives/2025/08/VSCode备忘.md) 
- [`2025-08-06` 开发环境配置 (基于 WSL)](_archives/2025/08/WSL开发环境配置.md) 
- [`2025-08-05` `uv` 备忘](_archives/2025/08/python-uv备忘.md) 
- [`2025-08-02` 批量删除历史已提交文件](_archives/2025/08/git-删除历史已提交文件.md) 
- [`2025-07-08` 链表常用操作备忘](_archives/2022/10/链表模板.md) 
- [`2025-07-08` 过拟合与正则化](_archives/2022/05/过拟合与正则化.md) ✒️
- [`2025-07-08` 设计模式 Wiki](_archives/2022/09/设计模式.md) 
- [`2025-07-08` 论文-2022-YiboYang](_archives/2022/05/论文-2022-YiboYang.md) 
- [`2025-07-08` 综述-2019-Johnson](_archives/2022/05/综述-2019-Johnson.md) 

<!--END_SECTION:recent-->

</td>
</tr>
</table>


<!--START_SECTION:notes-->

## Researches

<table>
<!-- row 1 -->
<tr>
<td rowspan="1" valign="top" width="1000">

### Transformer 🪄 LLM 🚀

- [模型架构](_archives/2025/09/Transformer_整理/README.md) 
- [位置编码 ( PE )](_archives/2025/09/Transformer_整理/位置编码.md) 
  > _[QA](_archives/2025/09/Transformer_整理/位置编码_QA.md)_<br>
- [面试问题整理](_archives/2025/09/Transformer_整理/Transformer_QA.md) 
- [MoE 备忘](_archives/2025/09/MoE_备忘/README.md) 
- [LLM 训练稳定性](_archives/2025/09/大模型微调/训练稳定性.md) <a href="#"><img src="https://custom-icon-badges.demolab.com/static/v1?label=&message=1&labelColor=important&color=important&style=flat-square&logoSource=feather&logo=edit&logoColor=white" height="16"/></a>

<!-- omit in toc -->
#### BERT

- [Transformer 常见面试问题](_archives/2022/05/Transformer常见问题.md) 
- [Transformer Wiki](_archives/2022/05/TransformerWiki.md) 
- [BERT + CRF 备忘](_archives/2022/04/bert_crf备忘.md) 

#### 大模型微调 🔥

- [基础概念](_archives/2025/09/大模型微调/README.md) 
- [SFT 数据构建](_archives/2025/09/大模型微调/构建高质量_SFT_数据.md) ✒️
- [**RLHF** ( 偏好学习, 对齐学习 )](_archives/2025/09/大模型微调/RLHF.md) ✒️🧣
  > _[**快速回顾**](_archives/2025/09/大模型微调/RLHF.md#快速回顾-) • [奖励模型](_archives/2025/09/大模型微调/RLHF.md#奖励模型训练流程) • [BT 模型](_archives/2025/09/大模型微调/RLHF.md#bradleyterry-模型介绍) • [RL 基础](_archives/2025/09/大模型微调/强化学习基础_RLHF.md) • [QA](_archives/2025/09/大模型微调/偏好学习_RLHF_QA.md)_<br>
  - [强化学习基础 ( **LLM-based** )](_archives/2025/09/大模型微调/强化学习基础_RLHF.md) 
    > _[基础术语](_archives/2025/09/大模型微调/强化学习基础_RLHF.md#核心术语) • [价值函数 ↝ 优势函数](_archives/2025/09/大模型微调/强化学习基础_RLHF.md#4️⃣-价值函数--优势函数) • [策略优化](_archives/2025/09/大模型微调/强化学习基础_RLHF.md#策略优化) • [贝尔曼方程](_archives/2025/09/大模型微调/强化学习基础_RLHF.md#贝尔曼方程-bellman-equation) • [时序差分算法](_archives/2025/09/大模型微调/强化学习基础_RLHF.md#时序差分算法-temporal-difference-td) • [广义优势估计](_archives/2025/09/大模型微调/强化学习基础_RLHF.md#广义优势估计-gae)_<br>
  - [策略梯度定理及其推导](_archives/2025/09/大模型微调/策略梯度定理及其推导.md) 🧣
    > _[基本形式](_archives/2025/09/大模型微调/策略梯度定理及其推导.md#基本形式) • [Q函数形式](_archives/2025/09/大模型微调/策略梯度定理及其推导.md#q-函数形式) • [A函数形式](_archives/2025/09/大模型微调/策略梯度定理及其推导.md#a-函数形式) • [Score Function 恒等式](_archives/2025/09/大模型微调/策略梯度定理及其推导.md#score-function-恒等式) • [基线不变性](_archives/2025/09/大模型微调/策略梯度定理及其推导.md#基线不变性)_<br>
  - [**策略梯度算法**](_archives/2025/09/大模型微调/策略梯度算法.md) ✒️🧣<a href="#"><img src="https://custom-icon-badges.demolab.com/static/v1?label=&message=4&labelColor=important&color=important&style=flat-square&logoSource=feather&logo=edit&logoColor=white" height="16"/></a>
    > _[PPO](_archives/2025/09/大模型微调/策略梯度算法.md#ppo) • [DPO](_archives/2025/09/大模型微调/策略梯度算法.md#dpo-direct-preference-optimization) • [GRPO](_archives/2025/09/大模型微调/策略梯度算法.md#grpo-group-relative-policy-optimization)_<br>
- [参数高效微调 ( **PEFT** )](_archives/2025/09/大模型微调/PEFT.md) 
  > _[**LoRA**](_archives/2025/09/大模型微调/LoRA.md) • [QA](_archives/2025/09/大模型微调/PEFT_QA.md)_<br>
- [面试问题整理](_archives/2025/09/大模型微调/大模型微调_QA.md) 

<!-- omit in toc -->
#### Prompt Engineering

- [常用 prompt 备忘](_archives/2025/09/Prompt_记录/常用_prompt_备忘.md) 
- [反思 ( Reflection )](_archives/2025/08/Prompt_工程-自反思.md) 

<!-- omit in toc -->
<!-- #### Reinforcement Learning -->

</td>
<td rowspan="1" valign="top" width="1000">

### Machine Learning 🤖

- [概率论基础](_archives/2025/09/概率论基础.md) 
  > _[期望](_archives/2025/09/概率论基础.md#期望相关) • [全期望公式](_archives/2025/09/概率论基础.md#全期望公式-law-of-total-expectation)_<br>
- [机器学习基本概念](_archives/2025/09/机器学习基本概念.md) <a href="#"><img src="https://custom-icon-badges.demolab.com/static/v1?label=&message=1&labelColor=important&color=important&style=flat-square&logoSource=feather&logo=edit&logoColor=white" height="16"/></a>
  > _[归纳偏置](_archives/2025/09/机器学习基本概念.md#归纳偏置-inductive-bias) • [似然](_archives/2025/09/机器学习基本概念.md#似然-likelihood) • [正则化](_archives/2025/09/机器学习基本概念.md#正则化-regularization)_<br>
- [XGBoost 学习笔记](_archives/2022/05/XGBoost.md) ✒️
  - [GBDT/XGBoost 备忘](_archives/2022/10/XGBoost备忘.md) 

### Deep Learning 🧠

- [过拟合与正则化](_archives/2022/05/过拟合与正则化.md) ✒️
- [激活函数](_archives/2022/05/激活函数.md) 
- [损失函数](_archives/2022/05/损失函数.md) 

<!-- omit in toc -->
#### 模型

- [RNN 备忘](_archives/2022/05/RNN.md) 
- [CNN 备忘](_archives/2022/05/CNN.md) 
- [Attention 备忘](_archives/2022/05/Attention.md) ✒️

<!-- omit in toc -->
#### 框架

- [爱因斯坦标记法](_archives/2022/05/爱因斯坦标记法.md) 
- [HuggingFace 离线使用](_archives/2022/06/HuggingFace离线使用.md) 

<!-- omit in toc -->
#### 表示学习

- [基于对比学习的表示学习训练框架](_archives/2022/05/基于对比学习的表示学习训练框架.md) 
- [基于互信息的表示学习](_archives/2022/05/基于互信息的表示学习.md) 
- [向后兼容 ( Backward-Compatible ) 的表示学习](_archives/2022/05/向后兼容的表示学习.md) 
- [Sentence-BERT 论文笔记](_archives/2022/05/Sentence-BERT论文笔记.md) 

<!-- omit in toc -->
#### 迁移学习/SFT

- [预训练模型的轻量化微调](_archives/2022/05/预训练模型的轻量化微调.md) 

<!-- omit in toc -->
#### 不平衡学习

- [不平衡学习概述](_archives/2022/05/不平衡学习概述.md) 
- [论文-2022-YiboYang](_archives/2022/05/论文-2022-YiboYang.md) 
- [综述-2019-Johnson](_archives/2022/05/综述-2019-Johnson.md) 

</td>
</tr>

<!-- row 2; 跳过偶数灰色行 -->
<tr></tr>

<!-- row 3 -->
<tr>
<td rowspan="4" valign="top" width="1000">

### NLP 🔤
- [统一视角下的 NLP 任务](_archives/2025/09/统一视角下的NLP任务.md) 
- [语言模型](_archives/2022/10/语言模型.md) 
- [NLP 任务与应用](_archives/2022/06/NLP任务与应用.map.md) 

<!-- omit in toc -->
#### NER

- [NER Wiki](_archives/2022/12/NER.md) 
- [商品 NER 标签设计](_archives/2022/12/商品NER标签设计.md) 
- [GLiNER 阅读笔记](_archives/2024/06/ner.2023.arxiv.01/README.md) 

<!-- omit in toc -->
#### 知识图谱

- [知识图谱备忘](_archives/2022/07/知识图谱概述.md) 
- [短语挖掘](_archives/2025/07/短语挖掘.md) 
  - [AutoPhrase 备忘](_archives/2025/08/AutoPhrase备忘.md) 
  - [复合词检测](_archives/2025/08/复合词检测.md) 
  - [利用搜索引擎做短语质量评估](_archives/2025/08/利用搜索引擎做短语质量评估.md) 
- [实体链接](_archives/2022/04/实体链接/README.md) 
- [关系挖掘备忘](_archives/2022/10/关系挖掘.md) 
  - [同义词挖掘](_archives/2022/12/同义词挖掘.md) 
  - [上下位挖掘](_archives/2022/12/上下位挖掘.md) 

<!-- omit in toc -->
#### 搜索

- [搜索与 NLP](_archives/2022/12/搜索与NLP.md) 

<!-- omit in toc -->
#### 工具

- [NLP 标注工具](_archives/2022/12/NLP标注工具.md) 

<!-- omit in toc -->
#### 数据

- [印尼语 NLP](_archives/2022/07/印尼语NLP.md) 

</td>
<td rowspan="2" valign="top" width="1000">

### Algorithms 🧩



**技巧**

- [树形递归技巧](_archives/2022/10/树形递归技巧.md) 
- [从递归到递推 ( 动态规划 )](_archives/2022/10/从暴力递归到动态规划.md) 

**模板**

- [链表常用操作备忘](_archives/2022/10/链表模板.md) 
- [滑动窗口模板](_archives/2022/10/滑动窗口模板.md) 

</td>
</tr>

<!-- row 4; 跳过偶数灰色行 -->
<tr></tr>

<!-- row 5 -->
<tr>
<td rowspan="2" valign="top" width="1000">

### Reading List 🔖

- [强化学习相关](_archives/2025/08/强化学习相关资料.md) 
- [HuggingFace ( 博客 & 代码 )](_archives/2025/08/HuggingFace阅读列表.md) 
- [GitHub ( 仓库 )](_archives/2025/08/GitHub阅读列表.md) 

</td>
</tr>

<!-- row 6; 跳过偶数灰色行 -->
<tr></tr>

<!-- row 7 -->
<tr>
<td rowspan="1" colspan="6" valign="top" width="1000">

### Paper Notes 📝

- [[synonym.2012.KDD.01] A framework for robust discovery of entity synonyms | 基于统计方法的通用同义词挖掘框架 ⏳](_archives/2022/12/synonym.2012.KDD.01/README.md)
- [[el.2015.WSDM.01] Fast and Space-Efficient Entity Linking for Queries | 高效的 Query 实体链接](_archives/2022/04/实体链接/2015.wsdm.el.01.md)

</td>
</tr>
</table>


## Engineerings
<table>
<!-- row 1 -->
<tr>
<td rowspan='4' valign="top" width="1000">

### Python 🐍

- [类方法中 `self` 的含义](_archives/2022/06/python类方法中self的含义.md) 
- [python 装饰器的本质](_archives/2022/05/python装饰器的本质.md) 
- [python 类变量和成员变量的最佳实践](_archives/2022/07/python类变量和成员变量的最佳实践.md) 
- [`dataclass` 使用记录](_archives/2022/09/python-dataclass使用记录.md) 
- [Python 容器基类的使用](_archives/2022/08/Python容器基类的使用.md) 
- [Python 函数声明中单独的正斜杠 ( / ) 和星号 ( * ) 是什么意思](_archives/2022/07/python函数声明中单独的正斜杠和星号是什么意思.md) 

<!-- omit in toc -->
#### 工具

- [python 国内镜像源](_archives/2022/06/python国内镜像源.md) 
- [`uv` 备忘](_archives/2025/08/python-uv备忘.md) 
- [VSCode 配置 for Python](_archives/2025/08/VSCode配置-Python.md) 
- [PyCharm 配置](_archives/2022/07/PyCharm配置.md) 

<!-- omit in toc -->
#### 第三方库



</td>
<td rowspan='2' valign="top" width="1000">

### Big Data 📊



<!-- omit in toc -->
#### SQL

- [SQL 字符串处理](_archives/2022/08/SQL字符串处理.md) 
- [PySpark SQL 备忘](_archives/2022/07/pyspark_sql备忘.md) 
- [HiveSQL 常用操作](_archives/2022/04/HiveSQL常用操作.md) 

</td>
</tr>

<!-- row 2 -->
<tr></tr>

<!-- row 3 -->
<tr>
<td rowspan='4' valign="top" width="1000">

### Tools 🛠️

- [开发环境配置 ( 基于 WSL )](_archives/2025/08/WSL开发环境配置.md) 
- [VSCode 备忘](_archives/2025/08/VSCode备忘.md) 
- [Markdown 备忘](_archives/2022/04/Markdown_备忘.md) 
  - [Markdown 简历工具](_archives/2022/06/Markdown_简历工具.md) 
  - [LaTeX in Markdown 备忘](_archives/2022/04/LaTeX_备忘.md) 
- [Github Action 备忘](_archives/2022/08/GithubAction备忘.md) 
- [Docker 备忘](_archives/2022/08/Docker备忘.md) 

**Git**

- [`git` 备忘](_archives/2022/06/git备忘.md) 
- [批量删除历史已提交文件](_archives/2025/08/git-删除历史已提交文件.md) 
- [`git-subtree` 的基本用法](_archives/2022/06/git-subtree的基本用法.md) 

**Linux**

- [后台运行](_archives/2022/06/Linux后台运行.md) 
- [`glob` 备忘](_archives/2022/08/glob语法备忘.md) 
- [`awk` 备忘](_archives/2022/06/awk基本用法.md) 
- [WSL2 使用记录](_archives/2022/09/WSL使用记录.md) 
- [Shell 脚本备忘](_archives/2022/07/Shell脚本使用记录.md) 
- [Linux 解压缩](_archives/2022/06/Linux解压缩.md) 

</td>
</tr>

<!-- row 4 -->
<tr></tr>

<!-- row 5 -->
<tr>
<td rowspan='2' valign="top" width="1000">

### Design Pattern 🏗️

- [设计模式 Wiki](_archives/2022/09/设计模式.md) 
- [建造者模式 ( Python 实现 )](_archives/2022/09/设计模式-建造者模式.md) 
- [工厂模式 ( Python 实现 )](_archives/2022/09/设计模式-工厂模式.md) 

</td>
</tr>

</table>


## Wiki

- [C](999-WIKI.md#c)
    - [C++](999-WIKI.md#c-1)
- [D](999-WIKI.md#d)
    - [Docker](999-WIKI.md#docker)
- [G](999-WIKI.md#g)
    - [git](999-WIKI.md#git)
    - [gitbook](999-WIKI.md#gitbook)
        - [(1)](999-WIKI.md#1)
        - [(2)](999-WIKI.md#2)
    - [GitHub Action](999-WIKI.md#github-action)
    - [glob](999-WIKI.md#glob)
- [H](999-WIKI.md#h)
    - [Hive](999-WIKI.md#hive)
    - [HuggingFace](999-WIKI.md#huggingface)
- [J](999-WIKI.md#j)
    - [Jupyter](999-WIKI.md#jupyter)
        - [Jupyter Lab](999-WIKI.md#jupyter-lab)
        - [IPython](999-WIKI.md#ipython)
- [K](999-WIKI.md#k)
    - [开发环境](999-WIKI.md#开发环境)
        - [Mac](999-WIKI.md#mac)
        - [深度学习](999-WIKI.md#深度学习)
- [L](999-WIKI.md#l)
    - [LaTeX](999-WIKI.md#latex)
    - [LLM](999-WIKI.md#llm)
    - [领域短语挖掘](999-WIKI.md#领域短语挖掘)
- [M](999-WIKI.md#m)
    - [Markdown](999-WIKI.md#markdown)
- [N](999-WIKI.md#n)
    - [NLP](999-WIKI.md#nlp)
    - [Node.js](999-WIKI.md#nodejs)
- [O](999-WIKI.md#o)
    - [Obsidian](999-WIKI.md#obsidian)
- [P](999-WIKI.md#p)
    - [PyCharm](999-WIKI.md#pycharm)
    - [PySpark](999-WIKI.md#pyspark)
    - [Python](999-WIKI.md#python)
- [Q](999-WIKI.md#q)
    - [Query 理解](999-WIKI.md#query-理解)
- [S](999-WIKI.md#s)
    - [SQL](999-WIKI.md#sql)
    - [STAR 法则](999-WIKI.md#star-法则)
- [T](999-WIKI.md#t)
    - [Transformer 模型](999-WIKI.md#transformer-模型)
- [W](999-WIKI.md#w)
    - [Windows](999-WIKI.md#windows)
    - [WSL](999-WIKI.md#wsl)
- [Y](999-WIKI.md#y)
    - [yaml](999-WIKI.md#yaml)
    - [语言模型](999-WIKI.md#语言模型)


## Drafts

- [Python Wiki](_archives/2025/08/python_wiki.md) 
- [算法面试问题收录](_archives/2025/09/算法面试问题收录.md) ✒️
  > _[Transformer](_archives/2025/09/算法面试问题收录.md#transformer) • [LLM](_archives/2025/09/算法面试问题收录.md#llm)_<br>
- [算法面试笔记](_archives/2022/10/算法面试笔记.md) 
- [简历书写技巧 ( 算法 )](_archives/2022/10/程序员简历技巧.md) 
- [电商领域的 NER](_archives/2022/12/电商NER.md) 
- [电商搜索](_archives/2022/12/电商搜索.md) 
- [深度学习环境配置](_archives/2022/07/深度学习环境配置.md) 
- [文件夹模式测试-b](_archives/2025/07/测试文件夹模式/b.md) 
- [文件夹模式测试-a](_archives/2025/07/测试文件夹模式/a.md) 
- [文件夹模式测试](_archives/2025/07/测试文件夹模式/README.md) 
- [数仓基础概念](_archives/2023/01/数仓基础.md) 
- [搜索相关阅读](_archives/2022/12/搜索相关阅读.md) 
- [搜索指标](_archives/2022/12/搜索指标.md) 
- [快捷键记录](_archives/2022/07/快捷键记录.md) 
- [常见面试问题 ( 非技术 )](_archives/2022/06/常见面试问题（非技术）.md) 
- [常见的文本相似度计算](_archives/2022/12/文本相似度计算.md) 
- [实验报告模板](_archives/2022/12/实验报告模板.md) 
- [实体链接相关概念](_archives/2022/04/实体链接/实体链接相关概念.md) 
- [大模型解码](_archives/2025/09/Transformer_整理/解码.md) ✒️
- [多轮MRC信息抽取的优缺点](_archives/2025/08/多轮MRC信息抽取的优缺点.md) 
- [基于用户行为数据的同义词挖掘方法 ( 英文 )](_archives/2022/12/基于用户行为数据的同义词挖掘方法.md) 
- [基于 SQL 计算信息熵与信息增益](_archives/2023/01/sql-计算信息熵与信息增益.md) 
- [基于 BERT/MLM 的查询扩展方法](_archives/2022/12/qe-mlm.md) 
- [同义词挖掘](_archives/2025/07/同义词挖掘/README.md) 
- [偏好学习-QA](_archives/2025/09/大模型微调/偏好学习_RLHF_QA.md) 
- [低资源训练](_archives/2022/12/低资源训练.md) 
- [requirements.txt 语法备忘](_archives/2022/09/python-requirements语法.md) 
- [query 理解参考资料](_archives/2022/12/query理解相关阅读.md) 
- [huggingface 套件使用备忘](_archives/2023/06/huggingface套件使用备忘.md) 
- [`split` 分割文件](_archives/2022/06/split分割文件.md) 
- [Windows 使用备忘](_archives/2023/01/Windows备忘.md) 
- [Transformer与长度外推性](_archives/2023/02/Transformer与长度外推性.md) 
- [Transformer/BERT 常见变体](_archives/2022/10/Transformer系列模型.md) 
- [Transformer 的优势与劣势](_archives/2023/02/Transformer的优势与劣势.md) 
- [SQL优化之暴力扫描](_archives/2023/02/SQL优化之暴力扫描.md) 
- [SMART Loss](_archives/2022/06/论文-2019-HaomingJiang.md) 
- [RLHF 及其实现 ( PPO, DPO, GRPO 等 )](_archives/2025/08/RLHF.md) 
- [Query 纠错](_archives/2022/12/query纠错.md) 
- [Query 扩展 ( 电商领域 )](_archives/2022/12/query扩展.md) 
- [Query 分析指南](_archives/2022/12/query分析.md) 
- [Python 标准项目实践](_archives/2022/09/python标准项目实践.md) 
- [PySpark 笔记](_archives/2023/01/PySpark笔记.md) 
- [PET ( Pattern-Exploiting Training ) 模型](_archives/2022/07/PET模型实践.md) 
- [Obsidian](_archives/2022/05/Obsidian.md) 
- [Node.js 环境搭建](_archives/2022/12/nodejs环境.md) 
- [NLP 领域术语 Wiki](_archives/2022/12/nlp_wiki.md) 
- [Mac 环境配置](_archives/2022/07/Mac环境配置.md) 
- [Label Studio 使用记录](_archives/2022/12/label-studio使用记录.md) 
- [LLM 训练方案整理](_archives/2023/06/llm训练方案整理.md) 
- [LLM 应用收集](_archives/2023/06/llm应用收集.md) 
- [KDD 2022](_archives/2022/06/KDD2022.md) 
- [Jupyter & IPython 使用备忘](_archives/2022/12/jupyter与ipython备忘.md) 
- [Hive/Spark/Presto SQL 备忘](_archives/2023/01/大数据SQL备忘.md) 
- [Hive/Spark SQL 常用查询记录](_archives/2023/01/sql-常用查询记录.md) 
- [Hive 常用 SQL 备忘](_archives/2023/03/Hive常用SQL备忘.md) 
- [GitBook 备忘](_archives/2022/04/Gitbook备忘.md) 
- [BERT 常见面试问题](_archives/2022/05/BERT常见面试问题.md) 
- [使用 LLM 阅读论文](_archives/2024/01/使用LLM阅读论文.md) 
- [使用 LLM 优化简历](_archives/2025/08/使用LLM优化简历.md) 

<!--END_SECTION:notes-->