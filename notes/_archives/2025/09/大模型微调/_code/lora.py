#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-09-14 16:28:45
Author:
    Copilot with huayang (imhuay@163.com)
Subject:
    LoRA 代码示例
References:
    None
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


class LoRALinear(nn.Module):
    """LoRA 线性层封装

    在原始 Linear 层旁增加一个低秩分解的旁路：
      ΔW = B @ A
    其中：
      - A: [in_features, r]
      - B: [r, out_features]
    训练时：
      - 冻结原始 Linear 权重 W
      - 仅训练 A 和 B
    推理时：
      - 输出 = 原始 W(x) + α * ΔW(x)
    """

    def __init__(self, in_features, out_features, r=4, alpha=1.0, bias=True):
        super().__init__()
        self.r = r
        self.alpha = alpha
        self.scaling = alpha / r

        # 原始全连接层 (冻结)
        self.weight = nn.Parameter(torch.randn(out_features, in_features))
        self.weight.requires_grad = False
        self.bias = nn.Parameter(torch.zeros(out_features)) if bias else None
        if self.bias is not None:
            self.bias.requires_grad = False

        # LoRA 分解参数
        self.A = nn.Parameter(torch.randn(in_features, r) * 0.01)
        self.B = nn.Parameter(torch.zeros(r, out_features))

    def forward(self, x):
        # 原始输出
        base_out = F.linear(x, self.weight, self.bias)
        # LoRA 输出 (低秩旁路)
        lora_out = (x @ self.A @ self.B) * self.scaling
        return base_out + lora_out


class LoRASelfAttention(nn.Module):
    """多头自注意力层 (Q/K/V 使用 LoRA 线性层)"""

    def __init__(self, embed_dim, num_heads, r=4, alpha=1.0):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        assert embed_dim % num_heads == 0

        self.q_proj = LoRALinear(embed_dim, embed_dim, r, alpha, bias=False)
        self.k_proj = LoRALinear(embed_dim, embed_dim, r, alpha, bias=False)
        self.v_proj = LoRALinear(embed_dim, embed_dim, r, alpha, bias=False)
        self.out_proj = nn.Linear(embed_dim, embed_dim)

    def forward(self, x, attn_mask=None):
        B, T, C = x.size()
        H = self.num_heads
        D = self.head_dim

        q = self.q_proj(x).view(B, T, H, D).transpose(1, 2)
        k = self.k_proj(x).view(B, T, H, D).transpose(1, 2)
        v = self.v_proj(x).view(B, T, H, D).transpose(1, 2)

        attn_scores = torch.matmul(q, k.transpose(-2, -1)) / (D**0.5)
        if attn_mask is not None:
            attn_scores = attn_scores.masked_fill(attn_mask == 0, float('-inf'))
        attn_weights = F.softmax(attn_scores, dim=-1)
        attn_output = torch.matmul(attn_weights, v)

        out = attn_output.transpose(1, 2).contiguous().view(B, T, C)
        return self.out_proj(out)


class TransformerBlock(nn.Module):
    """带 LoRA 的 Transformer Block"""

    def __init__(self, embed_dim, num_heads, ff_dim, r=4, alpha=1.0):
        super().__init__()
        self.ln1 = nn.LayerNorm(embed_dim)
        self.attn = LoRASelfAttention(embed_dim, num_heads, r, alpha)
        self.ln2 = nn.LayerNorm(embed_dim)
        self.ff = nn.Sequential(nn.Linear(embed_dim, ff_dim), nn.ReLU(), nn.Linear(ff_dim, embed_dim))

    def forward(self, x, attn_mask=None):
        x = x + self.attn(self.ln1(x), attn_mask)
        x = x + self.ff(self.ln2(x))
        return x


class LoRATransformer(nn.Module):
    """简化版 Transformer，Q/K/V 使用 LoRA"""

    def __init__(self, vocab_size, embed_dim, num_heads, ff_dim, num_layers, r=4, alpha=1.0):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.layers = nn.ModuleList(
            [TransformerBlock(embed_dim, num_heads, ff_dim, r, alpha) for _ in range(num_layers)]
        )
        self.ln_f = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, vocab_size)

        # ===== 冻结所有参数 =====
        for p in self.parameters():
            p.requires_grad = False

        # ===== 只解冻 LoRA 参数 =====
        for module in self.modules():
            if isinstance(module, LoRALinear):
                module.A.requires_grad = True
                module.B.requires_grad = True

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


if __name__ == '__main__':
    """测试运行"""
    torch.manual_seed(42)
    vocab_size = 100
    model = LoRATransformer(vocab_size=vocab_size, embed_dim=32, num_heads=4, ff_dim=64, num_layers=2, r=4, alpha=8)

    # 只训练 LoRA 参数
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
        print(f'Step {step} | Loss: {loss.item():.4f}')
