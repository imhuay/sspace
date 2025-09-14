#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-09-14 16:23:14
Author:
    Copilot with huayang (imhuay@163.com)
Subject:
    P-Tuning v2 代码示例
References:
    None
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class DeepPrompt(nn.Module):
    """P-Tuning v2 的深层提示参数容器

    为每一层维护一段可训练的虚拟 token 向量:
      prompts[l]: [1, P, C]
    也可改为共享提示 + 小投影生成各层提示，以进一步降参。
    """

    def __init__(self, num_layers, prompt_len, embed_dim):
        super().__init__()
        self.num_layers = num_layers
        self.prompt_len = prompt_len
        self.embed_dim = embed_dim
        self.prompts = nn.ParameterList(
            [nn.Parameter(torch.randn(1, prompt_len, embed_dim)) for _ in range(num_layers)]
        )

    def get(self, layer_idx, batch_size):
        """取某层提示，并扩展到 batch 维度"""
        return self.prompts[layer_idx].expand(batch_size, -1, -1)  # [B, P, C]


class PTuningV2Transformer(nn.Module):
    """带 P-Tuning v2 的简化 Transformer（Decoder-only 风格）

    关键流程（每一层）:
      1) 在该层输入处拼接该层的 P 个深层提示: x' = concat(P_l, x)  -> [B, P+T, C]
      2) 将 attn_mask 在 key_len 上同步扩展 P 个可见位
      3) 正常执行 self-attn + FFN
      4) 剪掉前 P 个位置，仅保留原序列位置: x = x'[:, P:, :]

    训练:
      冻结主干（embedding/blocks/输出头），只训练 deep prompts。
    """

    def __init__(self, vocab_size, embed_dim, num_heads, ff_dim, num_layers, prompt_len):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.blocks = nn.ModuleList([TransformerBlock(embed_dim, num_heads, ff_dim) for _ in range(num_layers)])
        self.deep_prompt = DeepPrompt(num_layers, prompt_len, embed_dim)
        self.ln_f = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, vocab_size, bias=False)

        # 冻结主干，仅训练 deep prompts
        for name, p in self.named_parameters():
            if 'deep_prompt.prompts' in name:
                p.requires_grad = True
            else:
                p.requires_grad = False

    def forward(self, input_ids, attn_mask=None, labels=None):
        B, T = input_ids.size()
        x = self.embed(input_ids)  # [B,T,C]

        # 若未提供 mask，则默认全可见（演示用；真实生成任务可用因果掩码）
        if attn_mask is None:
            attn_mask = torch.ones(B, 1, 1, T, device=input_ids.device)

        # 逐层注入与剪切
        for idx, block in enumerate(self.blocks):
            P = self.deep_prompt.prompt_len
            p = self.deep_prompt.get(idx, B)  # [B,P,C]
            x_with_p = torch.cat([p, x], dim=1)  # [B,P+T,C]

            # 同步扩展 mask: 在 key_len 维前添 P 个可见位
            p_mask = torch.ones(B, 1, 1, P, device=x.device)
            attn_mask_layer = torch.cat([p_mask, attn_mask], dim=-1)  # [B,1,1,P+T]

            # 过该层
            y = block(x_with_p, attn_mask_layer)  # [B,P+T,C]

            # 剪掉提示，仅将原序列部分传给下一层
            x = y[:, P:, :]  # [B,T,C]
            # 对于下一层，原始 attn_mask 不变（仍对应 T 个原序列位）

        # 输出层（只有原序列位）
        x = self.ln_f(x)
        logits = self.head(x)  # [B,T,V]

        loss = None
        if labels is not None:
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), labels.view(-1))
        return logits, loss


class SelfAttention(nn.Module):
    """多头自注意力层（无特殊改动）

    输入:
      x: [B, L, C] 隐状态（可能已在前端拼接了 P 个虚拟 token）
      attn_mask: [B, 1, 1, L] 可广播的注意力掩码

    输出:
      y: [B, L, C]
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
        B, L, C = x.size()
        H = self.num_heads
        D = self.head_dim

        q = self.q_proj(x).view(B, L, H, D).transpose(1, 2)  # [B,H,L,D]
        k = self.k_proj(x).view(B, L, H, D).transpose(1, 2)
        v = self.v_proj(x).view(B, L, H, D).transpose(1, 2)

        attn_scores = torch.matmul(q, k.transpose(-2, -1)) / (D**0.5)  # [B,H,L,L]
        if attn_mask is not None:
            attn_scores = attn_scores.masked_fill(attn_mask == 0, float('-inf'))
        attn_weights = F.softmax(attn_scores, dim=-1)
        attn_output = torch.matmul(attn_weights, v)  # [B,H,L,D]

        out = attn_output.transpose(1, 2).contiguous().view(B, L, C)
        return self.out_proj(out)


class TransformerBlock(nn.Module):
    """Transformer 基本块（LayerNorm 前置）

    在 P-Tuning v2 框架中，提示的拼接/剪切由上层控制，该层正常处理给定的序列。
    """

    def __init__(self, embed_dim, num_heads, ff_dim):
        super().__init__()
        self.ln1 = nn.LayerNorm(embed_dim)
        self.attn = SelfAttention(embed_dim, num_heads)
        self.ln2 = nn.LayerNorm(embed_dim)
        self.ff = nn.Sequential(nn.Linear(embed_dim, ff_dim), nn.ReLU(), nn.Linear(ff_dim, embed_dim))

    def forward(self, x, attn_mask=None):
        x = x + self.attn(self.ln1(x), attn_mask)
        x = x + self.ff(self.ln2(x))
        return x


if __name__ == '__main__':
    """测试运行"""
    torch.manual_seed(7)
    vocab_size = 100
    model = PTuningV2Transformer(
        vocab_size=vocab_size,
        embed_dim=64,
        num_heads=4,
        ff_dim=128,
        num_layers=3,
        prompt_len=8,  # 每层深层提示长度 P
    )

    # 只训练 deep prompts
    optimizer = torch.optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=5e-3)

    B, T = 4, 12
    input_ids = torch.randint(0, vocab_size, (B, T))
    labels = torch.randint(0, vocab_size, (B, T))
    # 演示用全可见 mask；若做自回归建模，可构造因果掩码并在每层扩展
    attn_mask = torch.ones(B, 1, 1, T)

    for step in range(10):
        logits, loss = model(input_ids, attn_mask, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(f'Step {step} | Loss: {loss.item():.4f}')
