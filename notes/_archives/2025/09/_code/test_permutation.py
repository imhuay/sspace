#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-09-09 15:00:23
Author:
    huayang (imhuay@163.com)
Subject:
    测试自注意力的 置换不变性 (Permutation Invariance)
References:
    [设计位置编码](https://huggingface.co/blog/zh/designing-positional-encoding)
"""

import torch
import torch.nn as nn

# 设置随机种子以确保结果可重现
torch.manual_seed(42)

# 使用随机向量代替下载模型
vocab_size = 10000  # 假设的词汇表大小
hdim = 512  # 隐藏层维度
seq_len = 6  # 序列长度, 对应 "The dog chased another dog" 的 6 个 token

# 创建随机 token IDs (模拟分词结果)
tokens = torch.tensor([[1, 42, 789, 123, 5, 42]])  # 两个 "dog" 的 token ID 都是 42
batch_size, seq_len = tokens.shape

# 创建随机词嵌入矩阵
embedding_matrix = torch.randn(vocab_size, hdim)
embeddings = embedding_matrix[tokens]  # 查找对应的嵌入向量

print(f"Token IDs: {tokens}")
# Token IDs: tensor([[  1,  42, 789, 123,   5,  42]])
print(f"Embeddings shape: {embeddings.shape}")
# Embeddings shape: torch.Size([1, 6, 512])

# 定义注意力权重矩阵
W_q = nn.Linear(hdim, hdim, bias=False)
W_k = nn.Linear(hdim, hdim, bias=False)
W_v = nn.Linear(hdim, hdim, bias=False)

# 初始化多头注意力层
mha = nn.MultiheadAttention(embed_dim=hdim, num_heads=4, batch_first=True)

# 初始化权重
# with torch.no_grad():
#     # 初始化查询、键、值权重
#     nn.init.normal_(W_q.weight, std=0.1)
#     nn.init.normal_(W_k.weight, std=0.1)
#     nn.init.normal_(W_v.weight, std=0.1)
    
#     # 初始化多头注意力层的权重
#     for param in mha.parameters():
#         nn.init.normal_(param, std=0.1)

# 进行前向传播
Q = W_q(embeddings)
K = W_k(embeddings)
V = W_v(embeddings)

output, attention_weights = mha(Q, K, V)

print(f"Output shape: {output.shape}")

# 检查两个"dog" token的输出是否相同
dog1_out = output[0, 1]  # 第二个token是第一个"dog" (索引1)
dog2_out = output[0, 5]  # 第六个token是第二个"dog" (索引5)

print(f"\n第一个 dog token 的嵌入向量: {embeddings[0, 1][:5]}...")
print(f"第二个 dog token 的嵌入向量: {embeddings[0, 5][:5]}...")
print(f"两个 dog token 的嵌入向量是否相同: {torch.allclose(embeddings[0, 1], embeddings[0, 5], atol=1e-6)}")
# True

print(f"\n第一个 dog token 的输出: {dog1_out[:5]}...")
print(f"第二个 dog token 的输出: {dog2_out[:5]}...")
print(f"两个 dog 的输出是否相同?: {torch.allclose(dog1_out, dog2_out, atol=1e-6)}")
# True

# 额外分析：查看注意力权重
print(f"\n注意力权重形状: {attention_weights.shape}")  # torch.Size([1, 6, 6])
print(f"第一个 dog token 的注意力分布: {attention_weights[0, :, 1].detach().numpy()}")
print(f"第二个 dog token 的注意力分布: {attention_weights[0, :, 5].detach().numpy()}")
print(f"两个 dog 的注意力分布是否相同?: {torch.allclose(attention_weights[0, :, 1], attention_weights[0, :, 5], atol=1e-6)}")
# True