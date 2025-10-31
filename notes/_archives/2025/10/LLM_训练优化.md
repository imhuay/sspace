LLM 训练优化
===
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
date: 2025-11-01 17:44:51
toc_title: 'LLM 训练优化'
top: false
draft: false
thorough: false
hidden_in_recent: false
section_number: false
omit_in_tag_toc: false
level: 0
tags: [transformer]
algo_tags: []
-->

<!--START_SECTION:keywords-->
> ***Keywords**: LLM_训练优化*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [背景](#背景)
- [正则化与泛化性](#正则化与泛化性)
    - [Dropout](#dropout)
    - [](#)
- [Q\&A](#qa)
<!--END_SECTION:toc-->

---

## 背景


## 正则化与泛化性

### Dropout

- **基本原理**:
    - 在训练过程中，以概率 $p$ 随机将部分神经元的输出置零。  
    - 等价于在每次迭代中训练一个 **子网络**，最终模型相当于这些子网络的 **集成 (Ensemble)**。  
- **作用**:
    - **防止过拟合**：避免神经元之间的过强共适应 (co-adaptation)。  
    - **提升泛化能力**：让模型学到更鲁棒的特征表示。  
    - **类似集成学习**：Dropout 相当于在训练时隐式训练了多个子模型。  

> [🚫 为什么现代 LLM 中一般不使用 Dropout?](#42--为什么现代-llm-中一般不使用-dropout)

### 



---

<!--START_SECTION:qa-->
<!--qa_info
subject: ''  # Transformer, RLHF, SFT, Other
subject_level: 0  # subject 间的排序信号; 对已经设置过的 subject, 取最大值
topic: ''  # 默认取文档的 toc_title, 如果有层级结构, 用 · 分隔, 如 'SFT · PEFT'
topic_level: 0  # 同一个 subject 下的排序信号
with_section_title: true  # 如果不需要 section_title
use_section_number: true
-->
## Q&A

<!--START_SECTION:qa_toc-->
<!--END_SECTION:qa_toc-->

---

<!-- omit in toc -->
### 🏷️ 数据层优化
> 提升数据质量与多样性

-   <details><summary><b> 大纲 ⬇️ </b></summary>
    
    - **数据清洗与预处理**：去噪、重复、异常样本。  
    - **数据标准化**: 归一化、正则化、token 处理。  
    - **数据增强**：图像 (旋转、裁剪)、文本 (同义替换、回译)、语音 (加噪、变速)。
    - **数据平衡**：过采样、欠采样、SMOTE。  
    - **难例挖掘 (Hard Negative Mining)**：提升模型判别力。 
    </details>



---

<!-- omit in toc -->
### 🏷️ 模型结构优化
> 提升表达能力与稳定性

-   <details><summary><b> 大纲 ⬇️ </b></summary>
    
    - **架构选择**：CNN、RNN、Transformer 等针对任务的合适结构。  
    - **激活函数选择**：ReLU、GELU、SiLU 等。  
    - **归一化层**：BatchNorm、LayerNorm、RMSNorm 提升稳定性。  
    - **残差连接与缩放**：缓解梯度消失/爆炸。  
    - **轻量化设计**：剪枝、蒸馏、量化，提升推理效率。  
    - **正交/低秩分解**：减少冗余参数。  
    
    </details>

---

<!-- omit in toc -->
### 🏷️ 优化算法与超参数优化
> 加快收敛, 提升性能

-   <details><summary><b> 大纲 ⬇️ </b></summary>
    
    - **权重初始化**：Xavier、He、μ-parameterization。  
    - **优化器选择**：SGD、Adam、AdamW、RMSProp 等。  
    - **学习率调度**：Warm-up、余弦退火、指数衰减、OneCycle。  
    - **批量大小 (Batch Size)**：影响收敛速度与泛化。  
    - **自动调参**：网格搜索、随机搜索、贝叶斯优化。  
    
    </details>

---

<!-- omit in toc -->
### 🏷️ 正则与泛化性优化
> 防止过拟合, 增强泛化

-   <details><summary><b> 大纲 ⬇️ </b></summary>
    
    - **权重衰减 (Weight Decay)**：抑制过拟合。  
    - **Dropout / Stochastic Depth**：随机丢弃神经元或层。  
    - **数据正则化**：Mixup、CutMix、Label Smoothing等。  
    - **早停 (Early Stopping)**：防止过拟合。  
    - **对抗训练 (Adversarial Training)**。  
    
    </details>

<!-- omit in toc -->
#### ✅ Dropout 的原理作用
> • 在训练时随机 **屏蔽** 部分神经元，迫使网络学到更鲁棒的特征，从而防止过拟合; <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>

    > [Dropout](#dropout)
    
    </details>

<!-- omit in toc -->
#### ✅ 为什么现代 LLM 中一般不使用 Dropout?
> • 过拟合风险低; 模型结构自带正则化; 训练稳定性问题; 计算与资源开销; 实证结果 <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>
    
    > [大模型面试题：为什么不用dropout技术 - 知乎](https://zhuanlan.zhihu.com/p/17365886727)
    
    1. **过拟合风险低**  
        - LLM 在 **数千亿 token** 级别的数据上训练，本身处于欠拟合状态；  
        - Dropout 的正则化作用不再显著。  

    2. **模型结构自带正则化**  
        - Transformer 内部已有 **LayerNorm、残差连接、多头注意力** 等机制；  
        - 这些天然提供了稳定性和一定的正则化效果。  

    3. **训练稳定性问题**  
        - Dropout 引入的随机噪声会导致 **梯度震荡**，在深层网络 + 混合精度 (FP16/BF16) 下尤其明显；  
        - 可能导致收敛变慢甚至不稳定。  

    4. **计算与资源开销**  
        - Dropout 需要生成随机掩码并在前向/反向传播中应用；  
        - 在超大规模模型中，这会显著增加 **显存占用与计算开销**。  

    5. **实证结果**  
        - 实验表明，在小模型上 Dropout 有效，但在 LLM 中效果不明显甚至更差；  
        - GPT、LLaMA、PaLM 等主流大模型均 **移除了 Dropout**，依赖数据规模和架构设计来保证泛化。  

    </details>




---

<!-- omit in toc -->
### 🏷️ 计算与系统层优化
> 提升训练效率与可扩展性

-   <details><summary><b> 大纲 ⬇️ </b></summary>
    
    - **混合精度训练 (FP16/BF16)**：加速训练，减少显存。  
    - **分布式训练**：数据并行、模型并行、流水线并行。  
    - **梯度裁剪**：防止梯度爆炸。  
    - **梯度累积**：解决显存不足。  
    - **缓存与高效 I/O**：提升数据加载效率。  
    
    </details>

<!--END_SECTION:qa-->