#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-09-10 16:20:29
Author:
    huayang (imhuay@163.com)
Subject:
    RoPE (旋转位置编码) 演示
References:
    None
"""

from __future__ import annotations

import numpy as np

np.random.seed(42)


class RoPEDemo:
    """RoPE (选装) 演示类"""

    def __init__(self, base=10000.0):
        """初始化 RoPE 演示

        Args:
            base: RoPE 基数, 默认 10000.0
        """
        self.base = base

    def rope(self, vec, pos):
        """对向量应用 RoPE 旋转

        Args:
            vec: 输入向量, shape (D,), D 必须是偶数
            pos: 位置索引 (整数)

        Returns:
            np.ndarray: 旋转后的向量
        """
        D = vec.shape[0]
        assert D % 2 == 0, '维度必须是偶数'

        # 预计算频率项: 不同维度对应不同的旋转频率
        i = np.arange(0, D // 2)  # [1, 2, ..., D/2]
        inv_freq = 1.0 / (self.base ** (2 * i / D))  # shape: (D/2,)

        # 计算每个维度对应的旋转角度
        angles = pos * inv_freq  # shape: (D/2,)

        # 向量化计算旋转矩阵, 避免循环
        cos_vals = np.cos(angles)  # 所有维度的 cos 值
        sin_vals = np.sin(angles)  # 所有维度的 sin 值

        # 重组向量为复数形式便于旋转操作
        vec_reshaped = vec.reshape(-1, 2)  # shape: (D/2, 2)
        x = vec_reshaped[:, 0]  # 实部
        y = vec_reshaped[:, 1]  # 虚部

        # 应用旋转公式: x' = x*cosθ - y*sinθ, y' = x*sinθ + y*cosθ
        rotated_x = cos_vals * x - sin_vals * y
        rotated_y = sin_vals * x + cos_vals * y

        # 将旋转后的结果重新组合成原始形状
        out = np.column_stack((rotated_x, rotated_y)).flatten()

        return out

    def demonstrate_relative_property(self, q, k, pos_pairs):
        """演示 RoPE 的相对位置编码特性

        Args:
            vec1: 第一个向量
            vec2: 第二个向量
            pos_pairs: 位置对列表 [(m, n), ...]
        """
        print('=== RoPE 相对性验证 ===')
        # print(f'q 向量: {q}')
        # print(f'k 向量: {k}')
        # print()

        print('m    n    m-n    dot_val     ro_dot_val')
        print('-' * 40)

        # ==== 测试不同位置 ====
        # (m, n) 表示查询位置和键位置
        for m, n in pos_pairs:
            # 计算 <RoPE(q, m), RoPE(k, n)>
            q_rotated = self.rope(q, m)
            k_rotated = self.rope(k, n)
            dot_val = np.dot(q_rotated, k_rotated)

            # 计算 <q, RoPE(k, m - n)>
            k_relative_rotated = self.rope(k, m - n)
            rop_val = np.dot(q, k_relative_rotated)

            # 验证: <RoPE(q, m), RoPE(k, n)> == <q, RoPE(k, m - n)>
            print(f'{m:<4} {n:<4} {m - n:<4} {dot_val:>11.6f} {rop_val:>11.6f}')

        print()

    def demonstrate_rope_step_by_step(self, vec, pos, limit=3):
        """逐步演示 RoPE 计算过程

        Args:
            vec: 输入向量
            pos: 位置索引
            limit: 显示限制数量
        """
        print('=== RoPE 计算步骤演示 ===')

        D = len(vec)
        assert D % 2 == 0, '维度必须是偶数'

        # 步骤 1: 对输入向量的分量两两分组
        vec_pairs = []
        for i in range(0, D, 2):
            vec_pairs.append([vec[i], vec[i + 1]])

        print('步骤 1: 向量两两分组')
        vec_pairs_display = []
        for pair in vec_pairs[:limit]:
            vec_pairs_display.append([round(float(x), 3) for x in pair])
        print(f'  {vec_pairs_display}{" ..." if len(vec_pairs) > limit else ""}')
        print()

        # 步骤 2: 计算旋转角度
        angles = []
        for i in range(D // 2):
            exponent = 2 * i / D
            inv_freq = 1.0 / (self.base**exponent)
            angle = pos * inv_freq
            angles.append(angle)

        print('步骤 2: 计算各组的旋转角度, 数量为 D/2')
        angles_display = [round(float(angle), 3) for angle in angles[:limit]]
        print(f'  {angles_display}{" ..." if len(angles) > limit else ""}')
        print()

        # 步骤 3: 对每组应用旋转, 然后还原向量
        out = np.zeros(D)
        for i in range(D // 2):
            x, y = vec_pairs[i]
            cos_val = np.cos(angles[i])
            sin_val = np.sin(angles[i])

            # 应用旋转矩阵
            rotated_x = cos_val * x - sin_val * y
            rotated_y = sin_val * x + cos_val * y

            out[2 * i] = rotated_x
            out[2 * i + 1] = rotated_y

        print('步骤 3: 分组应用旋转')
        out_formatted = [round(float(x), 3) for x in out[: limit * 2]]
        pair_out = []
        for i in range(0, len(out_formatted), 2):
            pair_out.append([out_formatted[i], out_formatted[i + 1]])
        print(f'  原始向量 (分组): {vec_pairs_display}{" ..." if len(vec_pairs) > limit else ""}')
        print(f'  旋转后向量 (分组): {pair_out}{" ..." if len(vec_pairs) > limit else ""}')
        print(f'  旋转后向量 (展开): {out_formatted}{" ..." if len(out) > limit * 2 else ""}')
        print()

        print('范数比较')
        vec_norm = round(np.linalg.norm(vec), 8)
        out_norm = round(np.linalg.norm(out), 8)
        print(f'  原始范数: {vec_norm}')
        print(f'  旋转后范数: {out_norm}')
        print()


if __name__ == '__main__':
    """"""
    # 创建演示实例
    demo = RoPEDemo(base=10000.0)

    # ==== 参数设置 ====
    D = 8  # 向量维度, 必须为偶数
    q = np.random.randn(D)  # 随机查询向量
    k = np.random.randn(D)  # 随机键向量
    pos_pairs = [(0, 0), (4, 4), (10, 0), (15, 5), (18, 8), (6, 16), (16, 26), (3, 13)]

    # ==== 演示 RoPE 的相对位置编码特性 ====
    demo.demonstrate_relative_property(q, k, pos_pairs)
    """
    可以看到, 所有 m-n 相同的行, dot_val 和 rop_val 计算结果是一样的, 
    验证了经过 RoPE 编码的向量, 其点击结果只与相对位置 m-n 有关, 与绝对位置 m 和 n 无关.

    m   n   m-n    dot_val     rop_val
    0   0   0      -1.866203   -1.866203
    4   4   0      -1.866203   -1.866203
    10  0   10      1.942387   -0.996847
    15  5   10      1.942387   -0.996847
    18  8   10      1.942387   -0.996847
    6   16  -10    -0.996847    1.942387
    16  26  -10    -0.996847    1.942387
    3   13  -10    -0.996847    1.942387
    """

    # ==== 逐步演示 RoPE 旋转 ====
    demo.demonstrate_rope_step_by_step(q, 3)
