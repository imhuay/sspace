Transformer 面试题整理
===
<!--START_SECTION:badge-->

![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-09-06&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-05%2012%3A30%3A39&label_color=gray&color=thistle&style=flat-square)

<!--END_SECTION:badge-->
<!--info
date: 2025-09-06 13:48:27
top: false
draft: false
hidden: true
level: 0
tag: [dl_transformer]
-->

<!--START_SECTION:keywords-->
> ***Keywords**: [Transformer](./README.md)*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [基础概念](#基础概念)
    - [**一句话解释 Transformer 的核心思想**](#一句话解释-transformer-的核心思想)
    - [**为什么 Transformer 比 RNN/LSTM 更好**](#为什么-transformer-比-rnnlstm-更好)
    - [**简述 Transformer 的 Encoder 和 Decoder 各自的作用和结构**](#简述-transformer-的-encoder-和-decoder-各自的作用和结构)
    - [**解释自注意力机制的计算过程**](#解释自注意力机制的计算过程)
    - [**多头注意力的动机是什么, 它是如何实现的?**](#多头注意力的动机是什么-它是如何实现的)
    - [**为什么 Transformer 需要位置编码?**](#为什么-transformer-需要位置编码)
        - [**常见的位置编码** TODO](#常见的位置编码-todo)
    - [**Cross Attention 中的 Q, K, V 分别来自哪里?**](#cross-attention-中的-q-k-v-分别来自哪里)
    - [**Decoder 在训练阶段与推理阶段的差异**](#decoder-在训练阶段与推理阶段的差异)
<!--END_SECTION:toc-->

---

## 基础概念

### **一句话解释 Transformer 的核心思想**
> **思路**: Transformer 的核心 → Attention → 全局动态建模序列中各位置之间的依赖关系

### **为什么 Transformer 比 RNN/LSTM 更好**
> **思路**: Transformer 的优势: 1) 长程依赖/全局交互, 2) 并行计算/训练速度

### **简述 Transformer 的 Encoder 和 Decoder 各自的作用和结构**
- **Encoder**:
    - **作用**: 对输入序列编码, 将其表示为 **富含上下文信息的隐状态序列**;  
    - **结构**: $N$ 个相同的层堆叠结构, 每个层包含 2 个子层:  
        1. **多头自注意力** → 残差 → 层归一化;
        2. **前馈网络** → 残差 → 层归一化;
    - **输入**: Token 嵌入 + 位置编码;
    - **输出**: 上下文表示序列 (维度同输入);
- **Decoder**:
    - **作用**: 以**自回归**方式, 根据 Encoder 输出和已生成前缀, **逐词**生成目标序列;
    - **结构**: $N$ 个相同的层堆叠结构, 每个层包含 3 个子层:  
        1. **带因果掩码的多头自注意力** → 残差 → 层归一化;
        2. **跨注意力** → 残差 → 层归一化;
        3. **前馈网络** → 残差 → 层归一化;
    - **输入**: 目标序列右移一位的嵌入 + 位置编码 + Encoder 输出;
    - **输出**: 对下一个 token 的概率分布;


### **解释自注意力机制的计算过程**
> 投影 → 计算注意力分数 → 缩放与归一化 → 加权求和  
>> $Q, K, V = XW^Q, XW^K, XW^V → QK^\top → \text{softmax}(\frac{QK^\top}{\sqrt{d_k}}) → \text{softmax}(\frac{QK^\top}{\sqrt{d_k}})V$

- **为什么要缩放点积, 缩放因子是什么?**
    > 防止点击 ($QK^\top$) 的数值过大引发梯度消失; 缩放因子是 $\sqrt{d_k}$ (其中 $d_k$ 为输入向量 $K$ 的维度)
    >> **数学解释**: **两个均值为 0、方差为 1 的 d 维向量, 其点积的均值为 0、方差为 d**; 直接 softmax 会出现数值极小的分量, 反向传播时这些分量的梯度会趋于零, 导致梯度消失;

### **多头注意力的动机是什么, 它是如何实现的?**
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

### **为什么 Transformer 需要位置编码?**
> **思路**: 自注意力机制的核心/本质是 **加权求和** → **"置换不变性"** → 位置编码提供**顺序信息** → 模型理解**序列结构** (**谁在谁前面**, **相隔多远**);

#### **常见的位置编码** TODO


### **Cross Attention 中的 Q, K, V 分别来自哪里?**
> Q 来自 Decoder 上一层的输出; K, V 来自 Encoder 最后一层的输出;
>> **作用**: Decoder 在生成当前 token 时, 根据 **Cross-Atternion** 获取与当前生成最相关的源序列信息;

### **Decoder 在训练阶段与推理阶段的差异**
> **核心差异**: 对 **目标序列** 的可见性不同

<details><summary><b>详细论述</b></summary>
    

</details>

- **训练阶段**
    - 将目标序列右移一位 (shift right), 在最前面加上开始符 (记 `<BOS>`);
    - 第一个位置的输入 token 就是 `<BOS>`;
- **推理阶段**
    - 仅有一个 <BOS> 作为初始输入 (翻译)
    - 或由 prompt 的最后一个 token 作为起点 (LLM 生成)
- **差异**

    方面 | 训练阶段 (Training) | 推理阶段 (Inference)
    ---------|----------|---------
    生成模式 | **教师强制 (Teacher Forcing)** | **自回归 (Autoregressive)**
    解码方式 | **并行解码** | **串行解码**
    **KV Cache** | 不使用 | 使用


    - **教师强制 (Teacher Forcing)**: 
        - Decoder 的输入是**完整的真实目标序列**, 即使模型上一个预测错了, 下一步仍然输入正确的词; 
        - 输入 `"<bos> Hello World"` → 输出 `"Hello World <eos>"`
    - **自回归 (Autoregressive)**:
        - Decoder 将自己**上一步的预测结果**作为下一步的输入, 是一个循环迭代的过程; 
        - 输入 `<bos>` → 预测 `Hello` → 输入 `Hello` -> 预测下一个词;
    - **并行解码**:
        - 利用掩码, 一次前向传播即可计算出整个目标序列所有位置的输出;
    - **串行解码**:
        - 逐步进行 N 次前向传播来生成一个长度为 N 的序列;
    - **KV Cache**:
        - **作用**: 避免了大量重复计算, 极大提升推理速度;
        - **方法**: 需要缓存已生成 token 的 K/V