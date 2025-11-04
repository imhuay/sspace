import math
from typing import Literal

import einops
import torch
import torch.nn as nn
import torch.nn.functional as F


class TransformerEncoderBlock(nn.Module):
    def __init__(self, n_head, d_model, d_ff, act=F.gelu):
        super().__init__()

        self.n_head = n_head
        self.d_model = d_model

        # Attention
        self.Wq = nn.Linear(d_model, d_model)
        self.Wk = nn.Linear(d_model, d_model)
        self.Wv = nn.Linear(d_model, d_model)
        self.Wo = nn.Linear(d_model, d_model)

        # LN
        self.LN1 = nn.LayerNorm(d_model)
        self.LN2 = nn.LayerNorm(d_model)

        # FFN
        self.W1 = nn.Linear(d_model, d_ff)
        self.W2 = nn.Linear(d_ff, d_model)
        self.act = act

        # Dropout
        self.dropout = nn.Dropout(0.1)

    def self_attn(self, x, mask=None):
        """
        x:      [B, L, d_model]
        mask:   [B, 1, 1, L]  - Padding Mask with `-inf`
        """
        # 1. 线性投影 (维度不变)
        #    [B, L, d_model] → [B, L, d_model]
        q, k, v = self.Wq(x), self.Wk(x), self.Wv(x)

        # 2. 重排为多头形式
        #    [B, L, d_model] → [B, L, H*d_k] → [B, H, L, d_k]
        q = einops.rearrange(q, 'B L (H d) -> B H L d', H=self.n_head)
        k = einops.rearrange(k, 'B L (H d) -> B H d L', H=self.n_head)
        v = einops.rearrange(v, 'B L (H d) -> B H L d', H=self.n_head)

        # 3. 计算注意力权重 (scale → mask → softmax)
        #    [B, H, L, d_k] @ [B, H, d_k, L] → [B, H, L, L]
        d_k = self.d_model // self.n_head
        attn_logits = q @ k / math.sqrt(d_k)
        if mask is not None:
            attn_logits = attn_logits + mask  # Padding Mask with `-inf`
        a = torch.softmax(attn_logits, dim=-1)

        # 4. 合并多头
        #    [B, H, L, L] @ [B, H, L, d_k] → [B, H, L, d_k] → [B, L, H*d_k] → [B, L, d_model]
        o = einops.rearrange(a @ v, 'B H L d -> B L (H d)')
        o = self.Wo(o)
        return o

    def ffn(self, x):
        """
        x: [B, L, d_model]
        """
        x = self.dropout(self.act(self.W1(x)))
        x = self.dropout(self.W2(x))
        return x

    def forward(self, x, mask, mode: Literal['post_ln', 'pre_ln'] = 'post_ln'):
        if mode == 'post_ln':
            # ln 在最后 (原版)
            #    Sublayer → 残差 → LN
            x = self.LN1(x + self.self_attn(x, mask))
            x = self.LN2(x + self.ffn(x))
        elif mode == 'pre_ln':
            # ln 在最前
            #    LN → Sublayer → 残差
            x = x + self.self_attn(self.LN1(x), mask)
            x = x + self.ffn(self.LN2(x))
        else:
            raise ValueError(f'Unsupported mode: {mode}')
        return x


class TransformerDecoderBlock(nn.Module):
    def __init__(self, n_head, d_model, d_ff, act=F.gelu):
        super().__init__()

        self.n_head = n_head
        self.d_model = d_model

        # Self-Attention
        self.Wq_self = nn.Linear(d_model, d_model)
        self.Wk_self = nn.Linear(d_model, d_model)
        self.Wv_self = nn.Linear(d_model, d_model)
        self.Wo_self = nn.Linear(d_model, d_model)

        # Cross-Attention
        self.Wq_cross = nn.Linear(d_model, d_model)
        self.Wk_cross = nn.Linear(d_model, d_model)
        self.Wv_cross = nn.Linear(d_model, d_model)
        self.Wo_cross = nn.Linear(d_model, d_model)

        # LN
        self.LN1 = nn.LayerNorm(d_model)  # for self-attn
        self.LN2 = nn.LayerNorm(d_model)  # for cross-attn
        self.LN3 = nn.LayerNorm(d_model)  # for ffn

        # FFN
        self.W1 = nn.Linear(d_model, d_ff)
        self.W2 = nn.Linear(d_ff, d_model)
        self.act = act

        # Dropout
        self.dropout = nn.Dropout(0.1)

    def masked_self_attn(self, x, mask=None):
        """
        x:    [B, L, d_model]
        mask: [B, 1, L, L]
            - Padding Mask ([B,1,1,L]) + Causal Mask ([1,1,L,L])
        """
        q, k, v = self.Wq_self(x), self.Wk_self(x), self.Wv_self(x)
        q = einops.rearrange(q, 'B L (H d) -> B H L d', H=self.n_head)
        k = einops.rearrange(k, 'B L (H d) -> B H d L', H=self.n_head)
        v = einops.rearrange(v, 'B L (H d) -> B H L d', H=self.n_head)

        d_k = self.d_model // self.n_head
        attn_logits = q @ k / math.sqrt(d_k)
        if mask is not None:
            attn_logits = attn_logits + mask  # Causal Mask with `-inf`
        a = torch.softmax(attn_logits, dim=-1)

        o = einops.rearrange(a @ v, 'B H L d -> B L (H d)')
        o = self.Wo_self(o)
        return o

    def cross_attn(self, x, memory, mask=None):
        """
        x:      [B, L_dec, d_model]
        memory: [B, L_enc, d_model]
        mask:   [B, 1, L_dec, L_enc] - Encoder-Decoder Attention Mask
        """
        q = self.Wq_cross(x)
        k, v = self.Wk_cross(memory), self.Wv_cross(memory)

        q = einops.rearrange(q, 'B L (H d) -> B H L d', H=self.n_head)
        k = einops.rearrange(k, 'B L (H d) -> B H d L', H=self.n_head)
        v = einops.rearrange(v, 'B L (H d) -> B H L d', H=self.n_head)

        d_k = self.d_model // self.n_head
        attn_logits = q @ k / math.sqrt(d_k)
        if mask is not None:
            attn_logits = attn_logits + mask
        a = torch.softmax(attn_logits, dim=-1)

        o = einops.rearrange(a @ v, 'B H L d -> B L (H d)')
        o = self.Wo_cross(o)
        return o

    def ffn(self, x):
        x = self.dropout(self.act(self.W1(x)))
        x = self.dropout(self.W2(x))
        return x

    def forward(self, x, memory, self_mask, cross_mask, mode: Literal['post_ln', 'pre_ln'] = 'post_ln'):
        if mode == 'post_ln':
            # Self-Attn
            x = self.LN1(x + self.masked_self_attn(x, self_mask))
            # Cross-Attn
            x = self.LN2(x + self.cross_attn(x, memory, cross_mask))
            # FFN
            x = self.LN3(x + self.ffn(x))
        elif mode == 'pre_ln':
            # Self-Attn
            x = x + self.masked_self_attn(self.LN1(x), self_mask)
            # Cross-Attn
            x = x + self.cross_attn(self.LN2(x), memory, cross_mask)
            # FFN
            x = x + self.ffn(self.LN3(x))
        else:
            raise ValueError(f'Unsupported mode: {mode}')
        return x


class TransformerEncoder(nn.Module):
    def __init__(self, n_layer, n_head, d_model, d_ff, act=F.gelu):
        super().__init__()
        self.layers = nn.ModuleList([TransformerEncoderBlock(n_head, d_model, d_ff, act) for _ in range(n_layer)])

    def forward(self, x, mask, mode='post_ln'):
        for layer in self.layers:
            x = layer(x, mask, mode=mode)
        return x


class TransformerDecoder(nn.Module):
    def __init__(self, n_layer, n_head, d_model, d_ff, act=F.gelu):
        super().__init__()
        self.layers = nn.ModuleList([TransformerDecoderBlock(n_head, d_model, d_ff, act) for _ in range(n_layer)])

    def forward(self, x, memory, self_mask, cross_mask, mode='post_ln'):
        for layer in self.layers:
            x = layer(x, memory, self_mask, cross_mask, mode=mode)
        return x


def make_padding_mask(ids, pad_idx=0):
    """
    ids:    [B, L]
    return: [B, 1, 1, L] with 0 at non-pad, -inf at pad
    """
    is_pad = ids == pad_idx  # [B, L] boolean
    mask = is_pad.unsqueeze(1).unsqueeze(2)  # [B, 1, 1, L]
    return mask.masked_fill(mask, float('-inf')).masked_fill(~mask, 0.0)


def make_causal_mask(L, device=None):
    """
    return: [1, 1, L, L] upper-triangular -inf mask
    """
    m = torch.triu(torch.ones(L, L, device=device) * float('-inf'), diagonal=1)
    return m.unsqueeze(0).unsqueeze(0)


def make_cross_mask(enc_pad_mask, L_dec):
    """
    enc_pad_mask: [B, 1, 1, L_enc]
    return: [B, 1, L_dec, L_enc] (屏蔽 encoder 的 padding 列)
    """
    return enc_pad_mask.expand(enc_pad_mask.size(0), 1, L_dec, enc_pad_mask.size(-1))


# model = TransformerEncoderBlock(2, 4, 8)
# x = torch.randn(2, 3, 4)
# mask = torch.randn(1, 1, 3, 3)
# o = model(x, mask)


def demo():
    """"""
    # 参数配置
    d_model = 512
    d_ff = 2048
    B = 4
    L_enc = 20
    L_dec = 15
    pad_idx = 0
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # 输入张量
    #   伪造 token ids, 包含 padding
    src_ids = torch.randint(1, 1000, (B, L_enc), device=device)
    tgt_ids = torch.randint(1, 1000, (B, L_dec), device=device)
    # 在末尾制造 padding
    src_ids[:, -3:] = pad_idx
    tgt_ids[:, -2:] = pad_idx

    # 以下 mask 均使用 *自动广播*, 实践时推荐手动处理, 增加可读性
    # encoder padding_mask: [B, 1, 1, L_enc]
    enc_pad_mask = make_padding_mask(src_ids, pad_idx=pad_idx)  # .expand(B, 1, L_enc, L_enc)

    # decoder padding_mask: [B, 1, 1, L_dec]
    dec_pad_mask = make_padding_mask(tgt_ids, pad_idx=pad_idx)  # .expand(B, 1, L_dec, L_dec)
    # decoder causal_mask: [1, 1, L_dec, L_dec]
    dec_causal_mask = make_causal_mask(L_dec, device=device)    # .expand(B, 1, L_dec, L_dec)
    # decoder 自注意力需要同时屏蔽未来与 padding (把两者相加): [B, 1, L_dec, L_dec]
    dec_self_mask = dec_causal_mask + dec_pad_mask

    # decoder cross_mask: [B, 1, L_dec, L_enc]
    cross_mask = make_cross_mask(enc_pad_mask, L_dec=L_dec)

    # 随机嵌入作为输入
    src = torch.randn(B, L_enc, d_model, device=device)
    tgt = torch.randn(B, L_dec, d_model, device=device)

    # Encoder-Decoder
    encoder = TransformerEncoder(n_layer=6, n_head=8, d_model=d_model, d_ff=d_ff).to(device)
    decoder = TransformerDecoder(n_layer=6, n_head=8, d_model=d_model, d_ff=d_ff).to(device)
    memory = encoder(src, mask=enc_pad_mask, mode='post_ln')  # [B, L_enc, d_model]
    out = decoder(tgt, memory, self_mask=dec_self_mask, cross_mask=cross_mask, mode='post_ln')  # [B, L_dec, d_model]
    print(memory.shape, out.shape)


if __name__ == '__main__':
    """"""
    demo()
