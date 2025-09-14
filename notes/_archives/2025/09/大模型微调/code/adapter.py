#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-09-14 16:21:28
Author:
    Copilot with huayang (imhuay@163.com)
Subject:
    Adapter Tuning 代码示例
References:
    None
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


class Adapter(nn.Module):
    """Adapter 模块

    结构：
    - 下投影：将维度从 d_model 降到 bottleneck_dim
    - 激活函数（ReLU）
    - 上投影：将维度升回 d_model
    - 残差连接：输出与输入相加

    作用：
    - 在冻结主干的情况下，通过少量可训练参数实现任务适配
    """
    def __init__(self, d_model, bottleneck_dim):
        super().__init__()
        self.down_proj = nn.Linear(d_model, bottleneck_dim)
        self.up_proj = nn.Linear(bottleneck_dim, d_model)
        self.activation = nn.ReLU()

    def forward(self, x):
        return x + self.up_proj(self.activation(self.down_proj(x)))


class SimpleSelfAttention(nn.Module):
    """多头自注意力层（无 Adapter）

    用于演示 Adapter Tuning 时的主干注意力模块
    """
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        assert embed_dim % num_heads == 0

        self.q_proj = nn.Linear(embed_dim, embed_dim)
        self.k_proj = nn.Linear(embed_dim, embed_dim)
        self.v_proj = nn.Linear(embed_dim, embed_dim)
        self.out_proj = nn.Linear(embed_dim, embed_dim)

    def forward(self, x, attn_mask=None):
        B, T, C = x.size()
        H = self.num_heads

        q = self.q_proj(x).view(B, T, H, -1).transpose(1, 2)
        k = self.k_proj(x).view(B, T, H, -1).transpose(1, 2)
        v = self.v_proj(x).view(B, T, H, -1).transpose(1, 2)

        attn_scores = torch.matmul(q, k.transpose(-2, -1)) / (self.head_dim ** 0.5)
        if attn_mask is not None:
            attn_scores = attn_scores.masked_fill(attn_mask == 0, float('-inf'))
        attn_weights = F.softmax(attn_scores, dim=-1)
        attn_output = torch.matmul(attn_weights, v)

        out = attn_output.transpose(1, 2).contiguous().view(B, T, C)
        return self.out_proj(out)


class TransformerBlockWithAdapter(nn.Module):
    """带 Adapter 的 Transformer Block

    结构：
    - 多头自注意力 + 残差
    - 前馈网络 + Adapter + 残差
    """
    def __init__(self, embed_dim, num_heads, ff_dim, bottleneck_dim):
        super().__init__()
        self.attn = SimpleSelfAttention(embed_dim, num_heads)
        self.ln1 = nn.LayerNorm(embed_dim)

        self.ff = nn.Sequential(
            nn.Linear(embed_dim, ff_dim),
            nn.ReLU(),
            nn.Linear(ff_dim, embed_dim)
        )
        self.adapter = Adapter(embed_dim, bottleneck_dim)
        self.ln2 = nn.LayerNorm(embed_dim)

    def forward(self, x, attn_mask=None):
        x = x + self.attn(self.ln1(x), attn_mask)
        x = x + self.adapter(self.ff(self.ln2(x)))
        return x


class AdapterTransformer(nn.Module):
    """带 Adapter Tuning 的简化 Transformer 模型

    冻结主干参数，仅训练 Adapter 层
    """
    def __init__(self, vocab_size, embed_dim, num_heads, ff_dim, num_layers, bottleneck_dim):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.layers = nn.ModuleList([
            TransformerBlockWithAdapter(embed_dim, num_heads, ff_dim, bottleneck_dim)
            for _ in range(num_layers)
        ])
        self.ln_f = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, vocab_size, bias=False)

        # 冻结主干参数（除了 Adapter）
        for name, param in self.named_parameters():
            if "adapter" not in name:
                param.requires_grad = False

    def forward(self, input_ids, attn_mask=None, labels=None):
        x = self.embed(input_ids)
        for layer in self.layers:
            x = layer(x, attn_mask)
        x = self.ln_f(x)
        logits = self.head(x)

        loss = None
        if labels is not None:
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), labels.view(-1))
        return logits, loss


# ====== 测试运行 ======
if __name__ == "__main__":
    torch.manual_seed(42)
    vocab_size = 100
    model = AdapterTransformer(
        vocab_size=vocab_size,
        embed_dim=32,
        num_heads=4,
        ff_dim=64,
        num_layers=2,
        bottleneck_dim=8  # Adapter 瓶颈维度
    )

    optimizer = torch.optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=1e-3)

    B, T = 4, 10
    input_ids = torch.randint(0, vocab_size, (B, T))
    labels = torch.randint(0, vocab_size, (B, T))
    attn_mask = torch.ones(B, 1, 1, T)

    for step in range(5):
        logits, loss = model(input_ids, attn_mask, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(f"Step {step} | Loss: {loss.item():.4f}")
