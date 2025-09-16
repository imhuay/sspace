import torch
import torch.nn as nn


class GroupLoRA(nn.Module):
    def __init__(self, d_model, num_groups, r=8, alpha=16):
        """
        d_model: 总特征维度, 要求 d_model = num_groups * d_feat
        num_groups: 分组数 (例如 head 数)
        r: LoRA 秩
        alpha: 缩放系数
        说明: d_feat = d_model // num_groups 在初始化时直接确定
        """
        super().__init__()
        assert d_model % num_groups == 0, 'd_model 必须能被 num_groups 整除'
        self.d_model = d_model
        self.num_groups = num_groups
        self.d_feat = d_model // num_groups
        self.r = r
        self.scaling = alpha / r

        # 冻结主干线性映射 (与 PerHeadLoRA 对齐, 作用于合并后的 d_model 维)
        self.W = nn.Parameter(torch.empty(d_model, d_model))
        nn.init.xavier_uniform_(self.W)
        self.W.requires_grad_(False)

        # LoRA 参数 (始终作用于每组的最后一维 d_feat)
        # A: [G, R, D], B: [G, D, R]
        self.A = nn.Parameter(torch.randn(num_groups, r, self.d_feat) * 0.02)  # (G, R, D)
        self.B = nn.Parameter(torch.zeros(num_groups, self.d_feat, r))  # (G, D, R)

    def forward(self, x, group_axis):
        """
        x: 任意维张量, 要求:
           - x.shape[group_axis] == num_groups (分组轴大小)
           - x.shape[-1] == d_feat (最后一维是每组的特征维)
        group_axis: 在哪个维度上进行分组 (可为负索引)
        """
        assert x.shape[group_axis] == self.num_groups, '分组轴大小需等于 num_groups'
        assert x.shape[-1] == self.d_feat, '最后一维需等于 d_feat = d_model // num_groups'

        # 基线分支: 将 [..., G, D] 合并为 [..., d_model] 再线性映射
        x_flat = x.reshape(*x.shape[:-2], self.d_model)  # [..., d_model]
        base_out = torch.matmul(x_flat, self.W.T)  # [..., d_model]

        # LoRA 分支: 将分组轴移动到倒数第二维 [..., G, D]
        x_group_feat = torch.movedim(x, group_axis, -2)  # [..., G, D]
        proj_r = torch.einsum('...gd,grd->...gr', x_group_feat, self.A)  # [..., G, R]
        proj_d = torch.einsum('...gr,gdr->...gd', proj_r, self.B)  # [..., G, D]
        proj_d = torch.movedim(proj_d, -2, group_axis)  # 还原到原始 group_axis 位置

        # 合并为 [..., d_model]
        proj_d = proj_d.reshape(*proj_d.shape[:-2], self.d_model)
        return base_out + self.scaling * proj_d


class PerHeadLoRA(nn.Module):
    def __init__(self, d_model, num_heads, r=8, alpha=16):
        super().__init__()
        assert d_model % num_heads == 0
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_head = d_model // num_heads
        self.r = r
        self.scaling = alpha / r

        # 与 head 对齐的 LoRA 参数
        # A: [H, R, D], B: [H, D, R]
        self.A = nn.Parameter(torch.randn(num_heads, r, self.d_head) * 0.02)  # (H, R, D)
        self.B = nn.Parameter(torch.zeros(num_heads, self.d_head, r))  # (H, D, R)

        # 冻结主干线性映射
        self.W = nn.Parameter(torch.empty(d_model, d_model))
        nn.init.xavier_uniform_(self.W)
        self.W.requires_grad_(False)

    def forward(self, x):
        # x: [B, S, d_model]
        batch_size, seq_len, _ = x.shape
        base_out = x @ self.W.T  # [B, S, d_model]

        # 拆分为 head 维度
        x_heads = x.view(batch_size, seq_len, self.num_heads, self.d_head)  # [B, S, H, D]
        proj_r = torch.einsum('bshd,hrd->bshr', x_heads, self.A)  # [B, S, H, R]
        proj_d = torch.einsum('bshr,hdr->bshd', proj_r, self.B)  # [B, S, H, D]
        proj_d = proj_d.reshape(batch_size, seq_len, self.d_model)  # [B, S, d_model]
        return base_out + self.scaling * proj_d


def test():
    """"""
    # 配置
    d_model = 16
    num_heads = 4
    d_head = d_model // num_heads
    r = 2
    alpha = 4
    batch_size, seq_len = 2, 3

    # 输入
    x = torch.randn(batch_size, seq_len, d_model)  # [B, S, d_model]

    # 模型
    per_head = PerHeadLoRA(d_model, num_heads, r, alpha)
    group_lora = GroupLoRA(d_model, num_heads, r, alpha)

    # 同步参数
    with torch.no_grad():
        group_lora.W.copy_(per_head.W)
        group_lora.A.copy_(per_head.A)  # (H, R, D)
        group_lora.B.copy_(per_head.B)  # (H, D, R)

    # 前向对比
    x_heads = x.view(batch_size, seq_len, num_heads, d_head)  # [B, S, H, D]
    out1 = per_head(x)  # [B, S, d_model]
    out2 = group_lora(x_heads, group_axis=-2)  # head 轴是倒数第二维

    print('最大绝对误差:', (out1 - out2).abs().max().item())
    print('是否完全一致:', torch.allclose(out1, out2, atol=1e-6))


if __name__ == '__main__':
    """"""
    test()