Transformer 面试问题整理
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-09-06&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-20%2000%3A18%3A00&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-09-06 13:48:27
toc_title: 面试问题整理
top: false
draft: false
hidden: true
section_number: true
level: -1
tags: [dl_transformer]
-->

<!--START_SECTION:keywords-->
> ***Keywords**: Transformer*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [1. **模型框架**](#1-模型框架)
    - [1.1. ✅ 简要阐述 Transformer 的核心思想](#11--简要阐述-transformer-的核心思想)
        - [1.1.1. 💡 Transformer 的归纳偏置是什么? 与 CNN/RNN 有何不同?](#111--transformer-的归纳偏置是什么-与-cnnrnn-有何不同)
        - [1.1.2. ✅ 为什么 Transformer 比 RNN/LSTM 更好](#112--为什么-transformer-比-rnnlstm-更好)
    - [1.2. ✅ 简述 Transformer 中 Encoder 和 Decoder 各自的作用和结构](#12--简述-transformer-中-encoder-和-decoder-各自的作用和结构)
        - [1.2.1. ✅ 为什么大多数通用大模型选择 Decoder-Only (CausalLM) 架构?](#121--为什么大多数通用大模型选择-decoder-only-causallm-架构)
    - [1.3. ✅ 说明自注意力机制的计算过程](#13--说明自注意力机制的计算过程)
        - [1.3.1. ✅ 为什么要对 QK 的点积进行缩放?](#131--为什么要对-qk-的点积进行缩放)
        - [1.3.2. ✅ 多头注意力中 "多头" 的动机是什么, 是如何实现的?](#132--多头注意力中-多头-的动机是什么-是如何实现的)
        - [1.3.3. ✅ 为什么 Decoder 中计算自注意力需要 "掩码"?](#133--为什么-decoder-中计算自注意力需要-掩码)
    - [1.4. ✅ Cross Attention 中的 Q, K, V 分别来自哪里?](#14--cross-attention-中的-q-k-v-分别来自哪里)
- [2. **位置编码** (Position Encoding)](#2-位置编码-position-encoding)
- [3. **训练与推理**](#3-训练与推理)
    - [3.1. ✅ 说明 Decoder 在训练与推理阶段的差异](#31--说明-decoder-在训练与推理阶段的差异)
        - [3.1.1. 推理阶段, 怎么优化随着输出序列越来越长带来的开销?](#311-推理阶段-怎么优化随着输出序列越来越长带来的开销)
        - [3.1.2. 描述 KV Cache 的动机, 方法, 效果](#312-描述-kv-cache-的动机-方法-效果)
        - [3.1.3. 解释 "曝光偏差", 怎么引起的, 怎么缓解?](#313-解释-曝光偏差-怎么引起的-怎么缓解)
    - [3.2. 介绍常见的序列生成策略](#32-介绍常见的序列生成策略)
        - [3.2.1. 对比 BeamSearch 和 贪心搜索 的优劣](#321-对比-beamsearch-和-贪心搜索-的优劣)
        - [3.2.2. 为什么 LLM 在文本创作中倾向于使用 Sampling, 而不是 BeamSearch?](#322-为什么-llm-在文本创作中倾向于使用-sampling-而不是-beamsearch)
    - [3.3. 如何控制生成序列的长度和终止?](#33-如何控制生成序列的长度和终止)
    - [3.4. 怎么抑制 LLM 生成过程中的 重复问题?](#34-怎么抑制-llm-生成过程中的-重复问题)
- [4. **拓展问题**](#4-拓展问题)
    - [4.1. 非自回归模型是如何解码的? 与自回归解码的优劣](#41-非自回归模型是如何解码的-与自回归解码的优劣)
<!--END_SECTION:toc-->

---

## 1. **模型框架**

### 1.1. ✅ 简要阐述 Transformer 的核心思想
> 多头自注意机制 → 全局依赖关系

#### 1.1.1. 💡 Transformer 的归纳偏置是什么? 与 CNN/RNN 有何不同?
> 思路: **什么是归纳偏置** → **Transformer (位置编码 + 全局依赖)** / **CNN (局部性 + 平移不变性)** / **RNN (顺序性 + 马尔可夫假设)**

<details><summary><b>详述</b></summary>

- **什么是归纳偏置**
    - 在机器学习中, 归纳偏置是指模型在学习之前**对数据分布或任务结构的先验假设**;
- **Transformer**
    - **最小结构假设**: 除位置编码, 无强结构先验;
    - **全局依赖**: 依赖自注意力机制学习任意位置间的关系;
- **差异**:
    - CNN/RNN: 有较强的结构先验 (局部性 或 顺序性);
        - **优点**: 数据量不大也能学到一定模式
        - **缺点**: 强先验限制了表达能力
    - Transformer: 弱先验, 几乎不假设输入的内在结构 (位置关系通过显式编码输入);
        - **优点**: 灵活, 可以学习更丰富的模式
        - **缺点**: 需要更多数据和计算

</details>

#### 1.1.2. ✅ 为什么 Transformer 比 RNN/LSTM 更好
> **思路**: Transformer 的优势: 1) 长程依赖/全局交互, 2) 并行计算/训练速度

### 1.2. ✅ 简述 Transformer 中 Encoder 和 Decoder 各自的作用和结构
> **Encoder**: (文本表示, 自注意力 → FFN);  
> **Decoder**: (自回归, 掩码自注意力 → 交叉注意力 → FFN)

<details><summary><b>详述</b></summary>

- **Encoder**:
    - **作用**: 对输入序列编码, 将其表示为 **富含上下文信息的隐状态序列**;  
    - **结构**: $N$ 个相同的层堆叠结构, 每个层包含 2 个子层:  
        1. **多头自注意力** → **残差** → **层归一化**;
        2. **前馈网络** → **残差** → **层归一化**;
    - **输入**: Token 嵌入 + 位置编码;
    - **输出**: 上下文表示序列 (维度同输入);
- **Decoder**:
    - **作用**: 以**自回归**方式, 根据 Encoder 输出和已生成前缀, **逐词**生成目标序列;
    - **结构**: $N$ 个相同的层堆叠结构, 每个层包含 3 个子层:  
        1. **掩码多头自注意力** → **残差** → **层归一化**;
        2. **交叉注意力** → **残差** → **层归一化**;
        3. **前馈网络** → **残差** → **层归一化**;
    - **输入**: 目标序列右移一位的嵌入 + 位置编码 + Encoder 输出;
    - **输出**: 对下一个 token 的概率分布;

</details>


#### 1.2.1. ✅ 为什么大多数通用大模型选择 Decoder-Only (CausalLM) 架构?
> 思路: **LLM 的核心能力** 是自回归生成, 与 Decoder 的的工作模式相匹配;

<details><summary><b>详述</b></summary>

<!-- - **开场白**: Decoder-Only 相较于 Encoder-Decoder 的优势主要来源于现实中的实践 -->
- **任务匹配**
    - LLM 的核心能力是 **"给定上下文, 预测下一个 token"**, 这与 Decoder 的工作模式匹配;
    - Encoder-Decoder 架构是为 **Seq2Seq** 任务设计的 —— **先对输入进行编码, 再解码到输出** —— 对于单纯的生成任务, Encoder 部分可能并非必要, 实践中这种更复杂的架构也没有表现出优势;
- **效率优势**:
    - **参数效率**
        - Decoder-Only 中所有参数专注于核心任务; Encoder-Decoder 中参数分散在编码和解码两部分;
        - **在给定参数量预算下**, 将所有参数都投入到 Decoder 的上限更高 —— 更符合 **Scaling Laws**;
        - 在海量数据上训练后, Decoder-Only 模型展现出强大的 **涌现能力**; 在零样本泛化上优于 Encoder-Decoder;
            > **Causal Decoder** 严格遵守从左到右, 只看历史, 不看未来 (包括 Prompt 部分)
    - **训练效率**
        - **Decoder-Only 的训练目标只有一个**: Next Token 预测;
        - Encoder-Decoder 往往是**多任务联合训练**, 更容易出现训练不稳定的情况, 需要平衡各任务的 Loss;
    - **工程优势**
        - 所有主流大模型 (GPT, LLaMA等) 都采用此架构, 整个软硬件生态都针对其进行了极度优化;
- **参考资料**
    - [解码器仅架构: 探究大语言模型 (LLM) 采用Decoder-only架构的原因-百度开发者中心](https://developer.baidu.com/article/detail.html?id=2145079)
    - [为什么当前的大型语言模型 (LLMs) 普遍采用 "仅解码器" (Decoder-only) 架构? _decoder-only自回归模型架构-CSDN博客](https://blog.csdn.net/Listennnn/article/details/147934482)
    - [面试官问我: 大模型为何都用 Decoder only 架构? _大模型为什么是基于decoder-CSDN博客](https://blog.csdn.net/2401_84033492/article/details/143260251)

</details>


### 1.3. ✅ 说明自注意力机制的计算过程
> Q/K/V 投影 → 计算注意力分数 → 缩放与归一化 → 加权求和
>> $Q, K, V = XW^Q, XW^K, XW^V → QK^\top → \text{softmax}(\frac{QK^\top}{\sqrt{d_k}}) → \text{softmax}(\frac{QK^\top}{\sqrt{d_k}})V$

#### 1.3.1. ✅ 为什么要对 QK 的点积进行缩放?
> 防止点击 ($QK^\top$) 的数值过大引发梯度消失; 缩放因子是 $\sqrt{d_k}$ (其中 $d_k$ 为输入向量 $K$ 的维度)
>> **数学解释**: **两个均值为 0、方差为 1 的 d 维向量, 其点积的均值为 0、方差为 d**; 直接 softmax 会出现数值极小的分量, 反向传播时这些分量的梯度会趋于零, 导致梯度消失;

#### 1.3.2. ✅ 多头注意力中 "多头" 的动机是什么, 是如何实现的?
> **动机**: 将特征空间切分成多个独立的低维子空间 → 学习不同的注意力分布/不同的依赖关系;  
> **实现**: 将 Q/K/V 投影到多个低维子空间 → 每个头独立执行 Attention → 将结果拼接后再整体投影;
>> 实际并不会真的独立执行多个 Attention, 而是利用 **张量操作和广播机制** 一次完成;

<details><summary><b>代码演示</b></summary>

```python
def attn(self, x, mask):
    """
    x: [B, L, d_model]
    mask: [B, 1, 1, L]  -  Padding Mask
       or [B, 1, L, L]  -  Causal Mask
    """
    # 1. 线性映射到 Q, K, V
    #    [B, L, d_model]
    Q, K, V = self.W_Q(x), self.W_K(x), self.W_V(x)
    d_k = K.size(-1) // self.num_head  # 每个头的维度: d_model // H
    # 2. 重排为多头形式:
    #    [B, L, H*d_k] → [B, H, L, d_k]
    Q = einops.rearrange(Q, 'B L (H d) -> B H L d', H=self.num_head)
    K = einops.rearrange(K, 'B L (H d) -> B H L d', H=self.num_head)
    V = einops.rearrange(V, 'B L (H d) -> B H L d', H=self.num_head)
    # 3. 计算注意力权重 (scale → mask → softmax):
    #    [B, H, L, d_k] @ [B, H, d_k, L] → [B, H, L, L]
    scores = Q @ K.transpose(-2, -1) / math.sqrt(d_k)
    A = torch.softmax(scores + mask, dim=-1)
    # 4. 合并多头 → 投影
    #    [B, H, L, d_k] → [B, L, H*d_k] = [B, L, d_model]
    O = einops.rearrange(A @ V, 'B H L d -> B L (H d)')
    O = self.W_O(O)
    return O
```

</details>

#### 1.3.3. ✅ 为什么 Decoder 中计算自注意力需要 "掩码"?
> 维持自回归特性, 防止数据泄露

<details><summary><b>详述</b></summary>

- **核心目的: 维持自回归特性, 防止数据泄露**;
    - Decoder 的任务是 **自回归生成 (auto-regressive generation)**, 即逐个预测下一个 token;
    - 在生成第 `t` 个 token 时, 模型只能依据 **已经生成的 `1` 到 `t-1` 个 token**;
    - 若不加掩码, 模型在训练时会在计算第 `t` 个位置的注意力时 **"看到" 整个目标序列** (包括未来的 `t+1, t+2, ...` token), 这相当于 **数据泄露 (data leakage)**;
    - 掩码通过遮蔽 (设为负无穷) 当前位置之后的所有未来 token, 确保注意力权重仅基于历史信息, 从而 **强制训练与推理的行为保持一致**;
- **实现方式: 前瞻掩码 (Look-ahead Mask)**;
    - 掩码通常是一个 **下三角矩阵 (lower triangular matrix)**, 其对角线及左侧元素为 `0` (允许参与计算), 右上角元素为 `-inf` (被遮蔽);
    - 经过 softmax 后, 被遮蔽位置的权重变为 `0`, 从而在计算加权和时忽略这些未来信息;
- **一句话总结**: 掩码通过遮蔽未来信息, 确保 Decoder 在训练时只能基于历史上下文进行预测, 从而模拟推理时的自回归生成过程, 防止作弊;

</details>

### 1.4. ✅ Cross Attention 中的 Q, K, V 分别来自哪里?
> Q 来自 Decoder 上一层的输出; K, V 来自 Encoder 最后一层的输出;
>> **作用**: Decoder 在生成当前 token 时, 根据 **Cross-Atternion** 获取与当前生成最相关的源序列信息;

## 2. **位置编码** (Position Encoding)
> [**位置编码**面试问题整理](./位置编码_QA.md)

## 3. **训练与推理**

### 3.1. ✅ 说明 Decoder 在训练与推理阶段的差异
> **核心差异**: 对 **目标序列** 的 **可见性** 不同;

<details><summary><b>详述</b></summary>

- **训练阶段**:
    - **模式**: **教师强制 (Teacher Forcing)**
    - **过程**:
        - 将完整的目标序列一次性输入 Decoder,
        - 在计算**第 i 个**位置的输出时, 模型可以看到**第 1 到 i-1 位**的真实标签;
    - **特点**:
        - **并行计算**;
        - 整个目标序列可以同时输入, 通过**掩码**确保**当前位置看不到未来信息**, 一次性计算出所有位置的输出;
    - **缺点**:
        - **曝光偏差** (Exposure Bias)
- **推理阶段**:
    - **模式**: **自回归 (Auto-regressive)**
    - **过程**:
        - 从仅包含一个起始符 `<sos>` 的序列开始,
        - 模型每预测出下一个 token, 就**将该 token 追加到输入序列末尾**, 作为生成下一个 token 的上下文,
        - 直到生成结束符 `<eos>` 或达到最大长度;
    - **缺点**:
        - **串行计算**, 效率低;
    - **优化**:
        - **KV Cache**

</details>

#### 3.1.1. 推理阶段, 怎么优化随着输出序列越来越长带来的开销?
> **方法**: KV Cache; **效果**: $O(n^2) → O(n)$

#### 3.1.2. 描述 KV Cache 的动机, 方法, 效果
> 思路: **动机** (重复计算) → **方法** (缓存历史 K/V, 增量计算) → **效果** (降低计算复杂度)

<details><summary><b>详述</b></summary>

- **背景/动机**
    - 在**自回归**生成中, 第 `i` 个 token 的注意力计算需基于前 `i` 个 token `K/V` (含开始符);
    - 其中前 `i-1` 个 token 的 `K/V` 在之前步骤中已计算过, 重复计算导致效率低下;
- **方法**
    - 每步仅计算当前 token 的 `Q/K/V`, 并将新的 `K/V` 追加至缓存 `K_cache/V_cache` 中;
    - 执行 `Attention(Q, K_cache, V_cache)` —— **节省计算量的核心步骤**;
    - 生成当前 token, 并循环此过程;
- **效果**
    - 时间复杂度由 $O(n^2)$ 降至 $O(n)$;
- **代码展开说明**:
    ```python
    # 初始化缓存
    K_cache = torch.empty(batch, 0, d_model)
    V_cache = torch.empty(batch, 0, d_model)

    # --- 第 i 步: 生成第 i 个 token ---
    # 输入: [B, 1, D]
    Xi = torch.randn(batch, 1, d_model)

    # 计算 Q, K, V (假设这是解码器自注意力层)
    Qi = linear_q(Xi)  # [B, 1, D]
    Ki = linear_k(Xi)  # [B, 1, D]  
    Vi = linear_v(Xi)  # [B, 1, D]

    # 更新缓存: 将 Ki, Vi 存入
    K_cache = torch.cat([K_cache, Ki], dim=1) # [B, prev_len + 1, D]
    V_cache = torch.cat([V_cache, Vi], dim=1) # [B, prev_len + 1, D]

    # 计算自注意力
    Ai = attention(Qi, K_cache, V_cache) # [B, 1, D]

    # 经过 FFN 等操作, 生成第 i 个token
    ...
    ```
</details>

#### 3.1.3. 解释 "曝光偏差", 怎么引起的, 怎么缓解?


### 3.2. 介绍常见的序列生成策略
> Greedy Search, Beam Search, Sampling

#### 3.2.1. 对比 BeamSearch 和 贪心搜索 的优劣


#### 3.2.2. 为什么 LLM 在文本创作中倾向于使用 Sampling, 而不是 BeamSearch?


### 3.3. 如何控制生成序列的长度和终止?


### 3.4. 怎么抑制 LLM 生成过程中的 重复问题?


## 4. **拓展问题**

### 4.1. 非自回归模型是如何解码的? 与自回归解码的优劣