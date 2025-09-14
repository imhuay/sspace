#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-09-14 16:23:41
Author:
    Copilot with huayang (imhuay@163.com)
Subject:
    P-Tuning 代码示例
References:
    None
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


class PromptEncoder(nn.Module):
    """提示编码器（Prompt Encoder）

    将可训练的虚拟 token embedding 通过 LSTM + MLP 编码，
    生成最终注入到模型输入的连续提示向量;
    """

    def __init__(self, num_virtual_tokens, embed_dim, hidden_size):
        super().__init__()
        self.num_virtual_tokens = num_virtual_tokens
        self.embedding = nn.Embedding(num_virtual_tokens, embed_dim)
        self.lstm = nn.LSTM(
            input_size=embed_dim,
            hidden_size=hidden_size,
            num_layers=2,
            dropout=0.1,
            bidirectional=True,
            batch_first=True,
        )
        self.mlp = nn.Sequential(
            nn.Linear(hidden_size * 2, embed_dim),  # 双向 LSTM 输出 (* 2)
            nn.ReLU(),
            nn.Linear(embed_dim, embed_dim),
        )

    def forward(self, batch_size):
        # 虚拟 token id: [0, 1, ..., num_virtual_tokens-1]
        virtual_token_ids = (
            torch.arange(self.num_virtual_tokens, device=self.embedding.weight.device)
            .unsqueeze(0)
            .expand(batch_size, -1)
        )
        # [B, P, C]
        embedded = self.embedding(virtual_token_ids)
        lstm_out, _ = self.lstm(embedded)
        prompts = self.mlp(lstm_out)  # [B, P, C]
        return prompts


class PTuningTransformer(nn.Module):
    """带 P-Tuning 的简化 Transformer 模型"""

    def __init__(self, vocab_size, embed_dim, num_heads, ff_dim, num_layers, num_virtual_tokens, prompt_hidden_size):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.prompt_encoder = PromptEncoder(num_virtual_tokens, embed_dim, prompt_hidden_size)

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

    def forward(self, input_ids, attn_mask=None, labels=None):
        B, T = input_ids.size()
        x = self.embed(input_ids)  # [B, T, C]
        p = self.prompt_encoder(B)  # [B, P, C]
        x = torch.cat([p, x], dim=1)  # 拼接提示向量

        if attn_mask is None:
            attn_mask = torch.ones(B, 1, 1, T, device=input_ids.device)
        prefix_mask = torch.ones(B, 1, 1, p.size(1), device=input_ids.device)
        attn_mask = torch.cat([prefix_mask, attn_mask], dim=-1)

        for layer in self.layers:
            x = layer(x, attn_mask)

        x = self.ln_f(x)
        logits = self.head(x)

        loss = None
        if labels is not None:
            P = p.size(1)
            ignore = torch.full((B, P), -100, device=labels.device, dtype=labels.dtype)
            padded_labels = torch.cat([ignore, labels], dim=1)
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), padded_labels.view(-1), ignore_index=-100)

        return logits, loss


class SelfAttention(nn.Module):
    """多头自注意力层"""

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

        attn_scores = torch.matmul(q, k.transpose(-2, -1)) / (self.head_dim**0.5)
        if attn_mask is not None:
            attn_scores = attn_scores.masked_fill(attn_mask == 0, float('-inf'))
        attn_weights = F.softmax(attn_scores, dim=-1)
        attn_output = torch.matmul(attn_weights, v)

        out = attn_output.transpose(1, 2).contiguous().view(B, T, C)
        return self.out_proj(out)


class TransformerBlock(nn.Module):
    """Transformer 基本块"""

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
    torch.manual_seed(42)
    vocab_size = 100
    model = PTuningTransformer(
        vocab_size=vocab_size,
        embed_dim=32,
        num_heads=4,
        ff_dim=64,
        num_layers=2,
        num_virtual_tokens=5,
        prompt_hidden_size=16,
    )

    optimizer = torch.optim.Adam(model.prompt_encoder.parameters(), lr=1e-3)

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
