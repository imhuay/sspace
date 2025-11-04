import math

import einops
import torch
import torch.nn as nn


class GqaSelfAttn(nn.Module):
    def __init__(self, d_model: int, n_head_q: int, n_kv_head: int):
        super().__init__()
        assert n_head_q % n_kv_head == 0, "n_head_q 必须能被 n_kv_head 整除（GQA 分组）"
        self.d_model = d_model
        self.n_head_q = n_head_q
        self.n_kv_head = n_kv_head

        # 设定每头维度一致，简化实现
        self.d_k = d_model // n_head_q
        assert self.d_k * n_head_q == d_model, "d_model 必须能被 n_head_q 整除"

        # 线性投影
        self.Wq = nn.Linear(d_model, n_head_q * self.d_k, bias=False)
        self.Wk = nn.Linear(d_model, n_kv_head * self.d_k, bias=False)
        self.Wv = nn.Linear(d_model, n_kv_head * self.d_k, bias=False)
        self.Wo = nn.Linear(n_head_q * self.d_k, d_model, bias=False)

    def self_attn(self, x, mask=None):
        """
        x:      [B, L, d_model]
        mask:   [B, 1, 1, L]  - Padding/causal mask with `-inf`
        """
        B, L, _ = x.shape
        H = self.n_head_q
        G = self.n_kv_head
        d_k = self.d_k
        group_size = H // G

        # 1) 线性投影
        q = self.Wq(x)  # [B, L, H*d_k]
        k = self.Wk(x)  # [B, L, G*d_k]
        v = self.Wv(x)  # [B, L, G*d_k]

        # 2) 重排为多头形式
        q = einops.rearrange(q, 'B L (H d) -> B H L d', H=H, d=d_k)          # [B, H, L, d_k]
        k = einops.rearrange(k, 'B L (G d) -> B G d L', G=G, d=d_k)          # [B, G, d_k, L]
        v = einops.rearrange(v, 'B L (G d) -> B G L d', G=G, d=d_k)          # [B, G, L, d_k]

        # 3) 将 K/V 按分组复制到 Q 头数量 (GQA / MQA 核心)
        # 每个 KV 头服务 group_size 个 Q 头
        k = k.repeat_interleave(group_size, dim=1)                            # [B, H, d_k, L]
        v = v.repeat_interleave(group_size, dim=1)                            # [B, H, L, d_k]

        # 4) 注意力 logits：scale → mask → softmax
        attn_logits = (q @ k) / math.sqrt(d_k)                                # [B, H, L, L]
        if mask is not None:
            attn_logits = attn_logits + mask                                  # 广播到 [B, H, L, L]
        a = torch.softmax(attn_logits, dim=-1)

        # 5) 聚合并输出
        o = a @ v                                                             # [B, H, L, d_k]
        o = einops.rearrange(o, 'B H L d -> B L (H d)', d=d_k)                # [B, L, H*d_k]
        o = self.Wo(o)                                                        # [B, L, d_model]
        return o


def demo():
    # MHA: 8 头
    attn_mha = GqaSelfAttn(d_model=1024, n_head_q=8, n_kv_head=8)

    # MQA: 8 个 Q 头，共享 1 组 KV
    attn_mqa = GqaSelfAttn(d_model=1024, n_head_q=8, n_kv_head=1)

    # GQA: 8 个 Q 头，2 组 KV（每组服务 4 个 Q 头）
    attn_gqa = GqaSelfAttn(d_model=1024, n_head_q=8, n_kv_head=2)
