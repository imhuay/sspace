LLM 基座模型
===
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
date: 2025-11-04 23:51:12
toc_title: 'LLM 基座模型'
top: false
star: true
draft: false
thorough: false
hidden_in_recent: true
section_number: false
omit_in_tag_toc: false
level: 0
tags: [transformer]
algo_tags: []
-->

<!--START_SECTION:keywords-->
> ***Keywords**: LLM 基座模型*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [LLaMA 系列](#llama-系列)
- [DeepSeek](#deepseek)
- [Q\&A](#qa)
<!--END_SECTION:toc-->

---

<!--START_SECTION:keyword-->
<!--keyword_info
name: 'LLaMA'
extra_url: false
with_keywords: false
-->
## LLaMA 系列
<!--END_SECTION:keyword-->
> 将原版 Transformer 的 Post‑LN + 绝对位置 + ReLU/GeLU, 替换为 Pre‑LN + RMSNorm + RoPE + SwiGLU, 并使用 GQA 代替 MHA

- **优化重点**:
    - 稳定深层训练
    - 优化长序列建模, 提升外推能力
    - 降低计算成本, 提升推理效率

<!-- omit in toc -->
### LLaMA 模型结构要点 (vs Transformer)

| 组件 | 原版 Transformer (Vaswani 2017) | LLaMA 家族 (典型做法) | 目的 |
|---|---|---|---|
| 网络结构 | Encoder–Decoder | Decoder‑only | 结构更简洁 🔸 专注自回归生成 🔸 提升参数与计算效率 |
| `Attn` 位置编码 | 正弦位置编码 (绝对位置编码) | **RoPE** (相对位置编码) | 优化长序列建模 🔸 保留相对位置信息 🔸 **提升外推能力** |
| `Attn` 注意力头映射 | **MHA**: Q/K/V 头数一致 | **GQA/MQA**: Q 头多, K/V 头减少 (分组共享) | 降低 KV 存储与计算成本 🔸 提升推理吞吐与显存效率 |
| `FFN` 归一化位置 | **Post‑LN** (残差后归一化) | **Pre‑LN** (残差前归一化) | 改善深层训练稳定性 🔸 避免梯度消失/爆炸 🔸 支持更深层堆叠 |
| `FFN` 归一化方法 | **LayerNorm** (层归一化) | **RMSNorm** (均方根层归一化) | 计算更轻量 🔸 数值更稳定 🔸 减少均值偏移的影响 |
| `FFN` MLP 激活函数 | ReLU / GeLU | **SwiGLU** (门控激活) | 提升表示能力 🔸 改善训练稳定性 🔸 更高效的梯度流动 |

- #### **SwiGLU** vs **ReLU**
    $$\begin{align*}
        \text{FFN}(x) &= \text{ReLU}(xW_1){\cdot}W_2 &&\scriptstyle\text{// ReLU} \\
        \text{FFN}(x) &= \big( \text{Swish}(xW_1) \otimes (xW_2) \big){\cdot}W_3 &&\scriptstyle\text{// SwiGLU}
    \end{align*}$$

    > $\otimes$ 表示逐元素相乘, 用来实现门控机制

- #### **GQA/MQA 核心代码**
    - $H$ 个 Query 头, $G$ 个 K/V 头
    - $H > G$, 且 $H \bmod G = 0$
    ```python
    # 1) 线性投影, 
    q = self.Wq(x)  # [B, L, H*d_k], H*d_k == d_model
    k = self.Wk(x)  # [B, L, G*d_k]
    v = self.Wv(x)  # [B, L, G*d_k]

    # 2) 重排为多头形式
    q = einops.rearrange(q, 'B L (H d) -> B H L d', H=H, d=d_k)          # [B, H, L, d_k]
    k = einops.rearrange(k, 'B L (G d) -> B G d L', G=G, d=d_k)          # [B, G, d_k, L]
    v = einops.rearrange(v, 'B L (G d) -> B G L d', G=G, d=d_k)          # [B, G, L, d_k]

    # 3) 将 K/V 按分组复制到 Q 头数量 (GQA / MQA 核心)
    group_size = H // G
    # 每个 KV 头服务 group_size 个 Q 头
    k = k.repeat_interleave(group_size, dim=1)                            # [B, H, d_k, L]
    v = v.repeat_interleave(group_size, dim=1)                            # [B, H, L, d_k]
    ```
    > [transformer_gqa.py](../09/_code/transformer_gqa.py)

---

## DeepSeek
> ##### TODO

---

<!--## 相关问题-->
<!--START_SECTION:related_problems-->
<!--END_SECTION:related_problems-->

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
### 🏷️ LLaMA 相关

<!-- omit in toc -->
#### ✅ LLaMA 属于哪类架构？与原版 Transformer 的差异？改进的目的/效果
> • **架构**: Decoder‑only / Causal LM <br>
> • **差异**: 归一化 (Pre‑LN + RMSNorm) 🔸 激活函数(SwiGLU) 🔸 位置编码 (RoPE) 🔸 多头形式 (GQA) <br>
> • **效果**: 稳定深层训练 🔸 优化长序列建模, 提升外推能力 🔸 降低计算成本, 提升推理效率

-   <details><summary><b> 展开详情 ⬇️ </b></summary>
    
    > [LLaMA 模型结构要点 (vs Transformer)](#llama-模型结构要点-vs-transformer)

    - 为什么主流开源系选择 Decoder‑only? 与 Encoder‑Decoder 相比, 训练/推理的复杂度与生态权衡
    
    </details>

<!-- omit in toc -->
#### ✅ LLaMA 系列为何偏向 Pre‑Norm 与 RMSNorm? 与 LayerNorm 的数值与性能差异
> • **目的**: 为了在超深层网络中获得 **更稳定的梯度传播**, **更低的计算开销** 和 **更好的数值鲁棒性** <br>


<!-- omit in toc -->
#### ✅ SwiGLU 取代 ReLU 的动机是什么, 如何做到的?
> • **动机**: 提升模型的表达能力与训练稳定性 <br>
> • **ReLU 的局限性**: **稀疏性过强**, 导致梯度流动受限和信息丢失 <br>
> • **做法**: 通过 **门控机制 (GLU)** 引入额外的非线性与特征选择能力, 使前馈层更灵活, 避免 ReLU 的 **"死区"** 问题


<!-- omit in toc -->
#### ✅ LLaMA 为何采用 RoPE (旋转位置编码)？与正弦编码相比的优势
> • **优势**: RoPE 可以同时编码绝对与相对位置, 在 **长上下文外推** 与 **远程依赖建模** 上显著优于正弦编码/绝对位置编码. <br>


<!-- omit in toc -->
#### ✅ GQA/MQA 的动机是什么, 如何做的?
> • **动机**: 减少 KV Cache 的显存占用, 提高推理吞吐 🔸 在原始 MHA 中, $h$ 个头需要存储 $h$ 份 K/V, 显存和带宽的开销巨大; <br>
> • **GQA**: 将多个 Q 头分为若干组, 每组共享一份 K/V 🔸 特别的, **MQA** 中所有 Query 头共享同一组 K/V;

-   <details><summary><b> 展开详情 ⬇️ </b></summary>
    
    > [GQA/MQA 核心代码](#gqamqa-核心代码)
    
    </details>








<!--END_SECTION:qa-->