#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-09-14 16:24:15
Author:
    Copilot with huayang (imhuay@163.com)
Subject:
    Prompt Tuning 代码示例
References:
    None
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


class PromptTuning(nn.Module):
    """Prompt Tuning 模块

    维护可训练的软提示向量（soft prompt），
    在输入嵌入层后拼接到原始序列前端。
    """

    def __init__(self, prompt_len, embed_dim):
        super().__init__()
        # 可训练的软提示向量，形状 [1, P, C]；跨 batch 共享，按需 expand
        self.prompt = nn.Parameter(torch.randn(1, prompt_len, embed_dim))

    def expand(self, batch_size):
        return self.prompt.expand(batch_size, -1, -1)  # [B, P, C]


class PromptTransformer(nn.Module):
    """带 Prompt Tuning 的简化 Transformer 模型

    冻结主干 Transformer，仅训练软提示参数。
    """

    def __init__(self, vocab_size, embed_dim, num_heads, ff_dim, num_layers, prompt_len):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.prompt_tuning = PromptTuning(prompt_len, embed_dim)

        self.layers = nn.ModuleList([TransformerBlock(embed_dim, num_heads, ff_dim) for _ in range(num_layers)])
        self.ln_f = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, vocab_size, bias=False)

        # 冻结主干，仅训练软提示
        for p in self.embed.parameters():
            p.requires_grad = False
        for layer in self.layers:
            for p in layer.parameters():
                p.requires_grad = False
        for p in self.ln_f.parameters():
            p.requires_grad = False
        for p in self.head.parameters():
            p.requires_grad = False

    def forward(self, input_ids, attn_mask=None, labels=None):
        B, T = input_ids.size()
        x = self.embed(input_ids)  # [B, T, C]
        p = self.prompt_tuning.expand(B)  # [B, P, C]
        x = torch.cat([p, x], dim=1)  # [B, P+T, C]

        # 构造/扩展注意力 mask（这里简单用全可见；如需因果可自行替换）
        if attn_mask is None:
            attn_mask = torch.ones(B, 1, 1, T, device=input_ids.device)
        prefix_mask = torch.ones(B, 1, 1, p.size(1), device=input_ids.device)
        attn_mask = torch.cat([prefix_mask, attn_mask], dim=-1)  # [B,1,1,P+T]

        for layer in self.layers:
            x = layer(x, attn_mask)

        x = self.ln_f(x)
        logits = self.head(x)  # [B, P+T, V]

        loss = None
        if labels is not None:
            # 仅对原始 token 位置计算损失；软提示位置忽略
            P = p.size(1)
            ignore = torch.full((B, P), -100, device=labels.device, dtype=labels.dtype)  # -100 用于 ignore_index
            padded_labels = torch.cat([ignore, labels], dim=1)  # [B, P+T]
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), padded_labels.view(-1), ignore_index=-100)

        return logits, loss


class SelfAttention(nn.Module):
    """标准自注意力层

    实现多头自注意力机制（Multi-Head Self-Attention）。
    在 Prompt Tuning 中，这里不直接处理提示向量，
    提示向量会在输入层拼接到原始序列后统一进入注意力计算。
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

        q = self.q_proj(x).view(B, T, H, -1).transpose(1, 2)  # [B,H,T,D]
        k = self.k_proj(x).view(B, T, H, -1).transpose(1, 2)
        v = self.v_proj(x).view(B, T, H, -1).transpose(1, 2)

        attn_scores = torch.matmul(q, k.transpose(-2, -1)) / (self.head_dim**0.5)
        if attn_mask is not None:
            attn_scores = attn_scores.masked_fill(attn_mask == 0, float('-inf'))
        attn_weights = F.softmax(attn_scores, dim=-1)
        attn_output = torch.matmul(attn_weights, v)  # [B,H,T,D]

        out = attn_output.transpose(1, 2).contiguous().view(B, T, C)
        return self.out_proj(out)


class TransformerBlock(nn.Module):
    """Transformer 基本块

    包含：
    - 多头自注意力层
    - 前馈全连接网络
    - 残差连接与 LayerNorm
    """

    def __init__(self, embed_dim, num_heads, ff_dim):
        super().__init__()
        self.attn = SelfAttention(embed_dim, num_heads)
        self.ln1 = nn.LayerNorm(embed_dim)
        self.ff = nn.Sequential(nn.Linear(embed_dim, ff_dim), nn.ReLU(), nn.Linear(ff_dim, embed_dim))
        self.ln2 = nn.LayerNorm(embed_dim)

    def forward(self, x, attn_mask=None):
        x = x + self.attn(self.ln1(x), attn_mask)
        x = x + self.ff(self.ln2(x))
        return x


if __name__ == '__main__':
    """测试运行"""
    torch.manual_seed(0)
    vocab_size = 100
    model = PromptTransformer(
        vocab_size=vocab_size,
        embed_dim=32,
        num_heads=4,
        ff_dim=64,
        num_layers=2,
        prompt_len=10,  # 软提示长度 P
    )

    # 只优化软提示参数
    optimizer = torch.optim.Adam(model.prompt_tuning.parameters(), lr=1e-2)

    B, T = 4, 12
    input_ids = torch.randint(0, vocab_size, (B, T))
    labels = torch.randint(0, vocab_size, (B, T))
    attn_mask = torch.ones(B, 1, 1, T)  # 全可见；如需因果，请改造成因果 mask 并同步扩展 P

    for step in range(5):
        logits, loss = model(input_ids, attn_mask=attn_mask, labels=labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(f'Step {step} | Loss: {loss.item():.4f}')
