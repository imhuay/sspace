BERT 系列模型 (Encoder-only 架构)
===
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
date: 2025-11-04 01:02:50
toc_title: 'BERT 系列 (Encoder-only)'
top: false
draft: false
thorough: false
hidden_in_recent: true
section_number: false
omit_in_tag_toc: false
level: 1
tags: []
algo_tags: []
-->

<!--START_SECTION:keywords-->
> ***Keywords**: Transformer_BERT*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [背景](#背景)
- [表示学习](#表示学习)
- [改进模型](#改进模型)
    - [RoBERTa](#roberta)
    - [DeBERTa](#deberta)
- [Q\&A](#qa)
<!--END_SECTION:toc-->

---

## 背景


---

<!--START_SECTION:keyword-->
<!--keyword_info
name: ''
extra_url: false
with_keywords: false
-->
## 表示学习
<!--END_SECTION:keyword-->
> ##### TODO
> SentenceBERT, SimCSE, 句向量 等

---

## 改进模型

### RoBERTa
> 移除 NSP, **动态 Mask**, 更多训练数据


<!--START_SECTION:keyword-->
<!--keyword_info
name: 'DeBERTa'
extra_url: false
with_keywords: false
-->
### DeBERTa
<!--END_SECTION:keyword-->
> 解耦注意力机制 (Disentangled Attention) 🔸 相对位置编码 🔸 增强的 Mask 解码器 (Enhanced Mask Decoder, EMD)

<!-- omit in toc -->
#### 解耦注意力 (Disentangled Attention)

<!-- omit in toc -->
#### 增强 Mask 解码器 (EMD)

---

<!--START_SECTION:qa-->
<!--qa_info
subject: 'Transformer'
subject_level: 0
topic: 'BERT (Encoder-only)'
topic_level: 0
with_section_title: true
use_section_number: true
-->
## Q&A

<!--START_SECTION:qa_toc-->
<!--END_SECTION:qa_toc-->

---

<!-- omit in toc -->
### 🏷️ BERT 改进模型比较

<!-- omit in toc -->
#### ✅ 说明 RoBERTa 相比 BERT 的改进
> RoBERTa 在架构上与 BERT 基本一致，但在 **预训练方法** 上做了系统优化, 显著提升了模型性能与泛化能力 <br>
> • **主要改进**: 移除 NSP 任务 🔸 动态 Mask 🔸 更多训练数据; <br>

<!-- omit in toc -->
#### ✅ 比较 DeBERTa 和 BERT 在架构与预训练目标上的差异
> • BERT 使用静态 Mask + NSP <br>
> • DeBERTa 引入 **解耦注意力 (Disentangled Attention)** 与 **增强的 Mask 解码器 (EMD)** <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>
    
    
    
    </details>

<!-- omit in toc -->
#### ✅ 解释一下 DeBERTa 的优点及原因
> • **优点**: 语义理解更精细，长程依赖更好，预训练效率更高 (相比 BERT/RoBERTa) <br>
> • **原因**: 更精细的语义–位置建模, 更高效的预训练目标 <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>
    
    
    
    </details>


---

<!-- omit in toc -->
### 🏷️ 表示学习

<!-- omit in toc -->
#### ✅ 说明 SentenceBERT (SBERT) 与 SimCSE 的核心思想?
> • 引入 **对比学习**, 在 **语义相似任务** 上微调, 使语义相近的句子在向量空间中靠近, 语义不相关的句子远离; <br>
> • **SimCSE** 额外利用 batch 内其他句子作为负样本来提升学习效率, 同时利用 dropout 构造正样本带来 **无监督版本**. <br>

<!-- omit in toc -->
#### ✅ 为什么对比学习能提升句向量的判别力?
> • 通过 **正负样本约束** 显式地塑造了句向量空间: 语义相似的句子被拉近, 不相似的句子被推远 <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>
    
    - **显式几何约束**：对比学习直接优化“相似句子近, 不相似句子远”，使得向量空间更符合语义结构。  
    - **避免塌缩 (collapse)**：负样本的存在防止所有句子映射到同一向量。  
    - **增强鲁棒性**：通过 dropout 或数据增强生成的正样本对，迫使模型学习到语义不变性。  
    - **缓解各向异性**：对比学习能让句向量分布更均匀，提升余弦相似度的判别性。  
        
    </details>

<!-- omit in toc -->
#### ✅ 说明 SBERT 的双塔结构
> • SBERT 的双塔结构本质是 **参数共享** 的 Siamese/Triplet 网络; <br>
> • 两个完全相同且参数共享的 BERT 编码器分别处理两个句子, 得到各自的句向量后, 再通过相似度函数 (如余弦、曼哈顿、欧氏距离) 或拼接后接分类器来完成语义相似度/匹配等任务; <br>


<!-- omit in toc -->
#### ✅ 为什么拼接形式的双塔结构中, 通常还会加入 `|u-v|`?
> • $|u-v|$ 提供了对称、直观的差异特征, 增强了模型对相似度的判别力 <br>

-   <details><summary><b> 展开详情 ⬇️ </b></summary>
    
    - 余弦相似度、欧氏距离等常用度量, 本质上都依赖向量差异;
    - 加入 $|u-v|$ 等价于在输入层显式提供这些度量的近似特征;
    
    </details>







<!--END_SECTION:qa-->
