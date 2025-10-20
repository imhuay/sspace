#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-09-14 16:23:56
Author:
    Copilot with huayang (imhuay@163.com)
Subject:
    Prefix Tuning 代码示例
References:
    None
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


class PrefixSelfAttention(nn.Module):
    """应用 prefix tuning 的自注意力模块"""

    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        assert embed_dim % num_heads == 0

        self.q_proj = nn.Linear(embed_dim, embed_dim)
        self.k_proj = nn.Linear(embed_dim, embed_dim)
        self.v_proj = nn.Linear(embed_dim, embed_dim)
        self.out_proj = nn.Linear(embed_dim, embed_dim)

    def forward(self, x, attn_mask=None, prefix_k=None, prefix_v=None):
        B, T, C = x.size()
        H = self.num_heads

        q = self.q_proj(x).view(B, T, H, -1).transpose(1, 2)  # [B, H, T, D]
        k = self.k_proj(x).view(B, T, H, -1).transpose(1, 2)
        v = self.v_proj(x).view(B, T, H, -1).transpose(1, 2)

        # ====== 核心：拼接 prefix K/V ======
        if prefix_k is not None and prefix_v is not None:
            k = torch.cat([prefix_k, k], dim=2)  # [B, H, k+T, D]
            v = torch.cat([prefix_v, v], dim=2)

            # mask 同步扩展
            if attn_mask is not None:
                prefix_mask = torch.ones(B, 1, 1, prefix_k.size(2), device=attn_mask.device)  # [B, 1, 1, k]
                attn_mask = torch.cat([prefix_mask, attn_mask], dim=-1)  # [B, 1, 1, k+T]

        attn_scores = torch.matmul(q, k.transpose(-2, -1)) / (self.head_dim**0.5)
        if attn_mask is not None:
            attn_scores = attn_scores.masked_fill(attn_mask == 0, float('-inf'))
        attn_weights = F.softmax(attn_scores, dim=-1)
        attn_output = torch.matmul(attn_weights, v)

        out = attn_output.transpose(1, 2).contiguous().view(B, T, C)
        return self.out_proj(out)


class TransformerBlock(nn.Module):
    """标准 Transformer Block, 集成了 Prefix Tuning"""

    def __init__(self, embed_dim, num_heads, ff_dim):
        super().__init__()
        self.attn = PrefixSelfAttention(embed_dim, num_heads)
        self.ln1 = nn.LayerNorm(embed_dim)
        self.ff = nn.Sequential(nn.Linear(embed_dim, ff_dim), nn.ReLU(), nn.Linear(ff_dim, embed_dim))
        self.ln2 = nn.LayerNorm(embed_dim)

    def forward(self, x, attn_mask=None, prefix_k=None, prefix_v=None):
        x = x + self.attn(self.ln1(x), attn_mask, prefix_k, prefix_v)
        x = x + self.ff(self.ln2(x))
        return x


class PrefixTuning(nn.Module):
    """Prefix Tuning 参数容器"""

    def __init__(self, num_layers, num_heads, head_dim, prefix_len):
        super().__init__()
        self.prefix_key = nn.ParameterList(
            [nn.Parameter(torch.randn(1, num_heads, prefix_len, head_dim)) for _ in range(num_layers)]
        )
        self.prefix_value = nn.ParameterList(
            [nn.Parameter(torch.randn(1, num_heads, prefix_len, head_dim)) for _ in range(num_layers)]
        )


class PrefixTransformer(nn.Module):
    """集成 Prefix Tuning 的 Transformer 模型"""

    def __init__(self, vocab_size, embed_dim, num_heads, ff_dim, num_layers, prefix_len):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.prefix_tuning = PrefixTuning(num_layers, num_heads, embed_dim // num_heads, prefix_len)

        self.layers = nn.ModuleList([TransformerBlock(embed_dim, num_heads, ff_dim) for _ in range(num_layers)])
        self.ln_f = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, vocab_size, bias=False)

        # 冻结主干
        for p in self.embed.parameters():
            p.requires_grad = False
        for layer in self.layers:
            for p in layer.parameters():
                p.requires_grad = False
        for p in self.ln_f.parameters():
            p.requires_grad = False
        for p in self.head.parameters():
            p.requires_grad = False

    def forward(self, idx, attn_mask=None):
        x = self.embed(idx)
        B = idx.size(0)
        for i, layer in enumerate(self.layers):
            pk = self.prefix_tuning.prefix_key[i].expand(B, -1, -1, -1)
            pv = self.prefix_tuning.prefix_value[i].expand(B, -1, -1, -1)
            x = layer(x, attn_mask, pk, pv)
        x = self.ln_f(x)
        logits = self.head(x)
        return logits


if __name__ == '__main__':
    """测试运行"""
    torch.manual_seed(42)
    vocab_size = 100
    model = PrefixTransformer(vocab_size=vocab_size, embed_dim=32, num_heads=4, ff_dim=64, num_layers=2, prefix_len=5)

    optimizer = torch.optim.Adam(model.prefix_tuning.parameters(), lr=1e-3)

    input_ids = torch.randint(0, vocab_size, (4, 10))
    target_ids = torch.randint(0, vocab_size, (4, 10))
    attn_mask = torch.ones(4, 1, 1, 10)  # 全可见

    for step in range(5):
        logits = model(input_ids, attn_mask)
        loss = F.cross_entropy(logits.view(-1, vocab_size), target_ids.view(-1))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(f'Step {step} | Loss: {loss.item():.4f}')
