import torch
import torch.nn as nn
import torch.nn.functional as F


class BitFitTransformer(nn.Module):
    """带 BitFit 的简化 Transformer

    冻结所有参数，只训练 bias 项
    """

    def __init__(self, vocab_size, embed_dim, num_heads, ff_dim, num_layers):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.layers = nn.ModuleList([TransformerBlock(embed_dim, num_heads, ff_dim) for _ in range(num_layers)])
        self.ln_f = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, vocab_size)

        # 冻结所有参数
        for p in self.parameters():
            p.requires_grad = False

        # 只解冻 bias 参数
        for name, p in self.named_parameters():
            if 'bias' in name:
                p.requires_grad = True

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


class SimpleSelfAttention(nn.Module):
    """多头自注意力层（用于 BitFit 演示）

    结构：
    - Q/K/V 投影层
    - 输出投影层
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
    """Transformer 基本块（带前馈网络）"""

    def __init__(self, embed_dim, num_heads, ff_dim):
        super().__init__()
        self.ln1 = nn.LayerNorm(embed_dim)
        self.attn = SimpleSelfAttention(embed_dim, num_heads)
        self.ln2 = nn.LayerNorm(embed_dim)
        self.ff = nn.Sequential(nn.Linear(embed_dim, ff_dim), nn.ReLU(), nn.Linear(ff_dim, embed_dim))

    def forward(self, x, attn_mask=None):
        x = x + self.attn(self.ln1(x), attn_mask)
        x = x + self.ff(self.ln2(x))
        return x


if __name__ == '__main__':
    """测试运行"""
    torch.manual_seed(42)
    vocab_size = 100
    model = BitFitTransformer(vocab_size=vocab_size, embed_dim=32, num_heads=4, ff_dim=64, num_layers=2)

    # 只训练 bias 参数
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
