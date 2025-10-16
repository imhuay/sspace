Attention 备忘
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-05-xx&labelColor=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-10-10%2001%3A15%3A17&labelColor=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden_in_recent: true
tags: [dl_model]
-->

> ***Keywords**: Attention*

<!--START_SECTION:toc-->
- [Multi-head Self Attention](#multi-head-self-attention)
    - [前向过程 (PyTorch 实现) ](#前向过程pytorch-实现)
<!--END_SECTION:toc-->

---

## Multi-head Self Attention

<!--
### 前向过程

<div align='center'><a href='_formulas/Attention/f_001.js.tex'><img src='_formulas/Attention/f_001.js.svg'/></a></div>
 -->

### 前向过程 (PyTorch 实现)

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