Attention 备忘
===
<!--START_SECTION:badge-->

![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-05-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-03%2022%3A42%3A16&label_color=gray&color=thistle&style=flat-square)

<!--END_SECTION:badge-->
<!--info
top: false
draft: true
hidden: true
tag: [dl_model]
-->

> ***Keywords**: Attention*

<!--START_SECTION:toc-->
- [Multi-head Self Attention](#multi-head-self-attention)
    - [前向过程（PyTorch 实现）](#前向过程pytorch-实现)
<!--END_SECTION:toc-->

---

## Multi-head Self Attention

<!-- 
### 前向过程

$$
\begin{aligned}
    \text{Attention}(Q,K,V) &= \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V \\
    \text{head}_\text{i} &= \text{Attention}(QW_i^Q,KW_i^K,VW_i^V) \\
    \text{MultiHead}(Q,K,V) &= \text{Concat}(\text{head}_1,..,\text{head}_\text{h})W^O
\end{aligned}
$$
 -->

### 前向过程（PyTorch 实现）

```python
def forward(x, mask, H, D):
    q = k = v = x  # [B, L, N]
    B, L, N = x.shape

    # linear
    q = W_q(q).reshape([B, L, H, D]).transpose(1, 2)  # [B, H, T, D]
    k = W_k(k).reshape([B, L, H, D]).transpose(1, 2)  # [B, H, T, D]
    v = W_v(v).reshape([B, L, H, D]).transpose(1, 2)  # [B, H, T, D]

    # attention
    logits = matmul(q, k.transpose(-2, -1)) / sqrt(D) + mask
    a = softmax(logits)

    # output
    o = matmul(a, v)
    o = W_o(o).reshape([B, L, N])
    return o

```