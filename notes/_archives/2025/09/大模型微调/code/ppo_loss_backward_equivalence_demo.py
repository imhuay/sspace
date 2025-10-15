import torch
import torch.nn as nn
import torch.nn.functional as F

# 固定随机数种子，保证可复现
torch.manual_seed(42)

# 定义两个独立的线性层，分别模拟 policy head 和 value head
policy = nn.Linear(5, 1, bias=False)
value  = nn.Linear(5, 1, bias=False)

x = torch.randn(3, 5)  # 输入

# ===== 方法一：合并 loss 一次 backward =====
pg_loss = policy(x).mean()              # policy loss
vf_loss = F.mse_loss(value(x), torch.ones(3, 1))  # value loss

loss = pg_loss + vf_loss
policy.zero_grad()
value.zero_grad()
loss.backward()

grad_policy_1 = policy.weight.grad.clone()
grad_value_1  = value.weight.grad.clone()

# ===== 方法二：分别 backward 两次 =====
policy.zero_grad()
value.zero_grad()
pg_loss = policy(x).mean()
vf_loss = F.mse_loss(value(x), torch.ones(3, 1))

pg_loss.backward(retain_graph=True)  # 保留计算图，才能继续反传
vf_loss.backward()

grad_policy_2 = policy.weight.grad.clone()
grad_value_2  = value.weight.grad.clone()

# ===== 打印对比 =====
print("Grad policy (合并):\n", grad_policy_1)
print("Grad policy (分开):\n", grad_policy_2)
print("是否相等:", torch.allclose(grad_policy_1, grad_policy_2))

print("\nGrad value (合并):\n", grad_value_1)
print("Grad value (分开):\n", grad_value_2)
print("是否相等:", torch.allclose(grad_value_1, grad_value_2))
