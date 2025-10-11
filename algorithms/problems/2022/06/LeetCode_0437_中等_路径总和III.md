## 路径总和III
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%8F%89%E6%A0%91/%E6%A0%91&color=blue&style=flat-square)](../../../README.md#二叉树树)
[![](https://img.shields.io/static/v1?label=&message=%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2&color=blue&style=flat-square)](../../../README.md#深度优先搜索)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%8D%E7%BC%80%E5%92%8C&color=blue&style=flat-square)](../../../README.md#前缀和)
[![](https://img.shields.io/static/v1?label=&message=%E6%A0%91%E5%BD%A2%E9%80%92%E5%BD%92&color=blue&style=flat-square)](../../../README.md#树形递归)
<!--END_SECTION:badge-->
<!--info
tags: [二叉树, 深度优先搜索, 前缀和, TreeDP]
source: LeetCode
level: 中等
number: '0437'
name: 路径总和III
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定一个二叉树的根节点 root , 和一个整数 targetSum , 求该二叉树里节点值之和等于 targetSum 的 路径 的数目.

路径 不需要从根节点开始, 也不需要在叶子节点结束, 但是路径方向必须是向下的 (只能从父节点到子节点).
```
> [437. 路径总和 III - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/path-sum-iii/)

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->


<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1: 先序遍历</b></summary>

- 先序遍历每个节点, 每个节点再先序遍历找目标值;

<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:  # noqa
        """"""
        if root is None:
            return 0

        def dfs(x, rest):
            if not x:
                return 0

            ans = 0 if x.val != rest else 1  # 如果相等说明, 从头结点开始到该节点可以形成一条路径

            # 继续遍历左右子树
            rest -= x.val
            ans += dfs(x.left, rest)
            ans += dfs(x.right, rest)
            rest += x.val  # 回溯
            return ans

        # dfs 是一个先序遍历
        ret = dfs(root, targetSum)
        # pathSum 本身也是一个先序遍历, 相当于对每个点都做一次 dfs
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)

        return ret
```

</details>


<summary><b>思路2: 先序遍历+前缀和 (最优) </b></summary>

> [【宫水三叶】一题双解 :「DFS」&「前缀和」 - 路径总和 III - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/path-sum-iii/solution/gong-shui-san-xie-yi-ti-shuang-jie-dfs-q-usa7/)

<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        from collections import defaultdict
        self.prefix = defaultdict(int)  # 保存前缀和
        self.prefix[0] = 1
        self.targetSum = targetSum

        def dfs(x, preSum):
            if not x: return 0

            ret = 0
            preSum += x.val
            ret += self.prefix[preSum - targetSum]

            self.prefix[preSum] += 1
            ret += dfs(x.left, preSum)
            ret += dfs(x.right, preSum)
            self.prefix[preSum] -= 1

            return ret

        return dfs(root, 0)
```

</details>


<summary><b>思路3: 后序遍历 (推荐) </b></summary>

<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        from dataclasses import dataclass

        @dataclass
        class Info:
            cnt: int  # 题目要求的路径数目
            dp: list  # 保存所有可能的路径和

        def dfs(x):
            if not x:
                return Info(0, [])

            l, r = dfs(x.left), dfs(x.right)

            x_cnt = l.cnt + r.cnt
            x_dp = [x.val]
            if x.val == targetSum:
                x_cnt += 1
            for t in l.dp:
                x_dp.append(t + x.val)
                if t + x.val == targetSum:
                    x_cnt += 1
            for t in r.dp:
                x_dp.append(t + x.val)
                if t + x.val == targetSum:
                    x_cnt += 1

            return Info(x_cnt, x_dp)

        return dfs(root).cnt
```

</details>


<!--START_SECTION:relate_problem-->
---

### 相关主题

<details><summary><b>二叉树/树</b></summary>

> [[中等, LeetCode] 二叉树的完全性检验 🔥](../03/LeetCode_0958_中等_二叉树的完全性检验.md)  
> [[中等, LeetCode] 从叶结点开始的最小字符串](../07/LeetCode_0988_中等_从叶结点开始的最小字符串.md)  
> [[中等, LeetCode] 求根节点到叶节点数字之和](../07/LeetCode_0129_中等_求根节点到叶节点数字之和.md)  
> [[中等, LeetCode] 路径总和II](LeetCode_0113_中等_路径总和II.md)  
> [[中等, LeetCode] 验证二叉搜索树](../03/LeetCode_0098_中等_验证二叉搜索树.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](../../2021/12/剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 二叉搜索树的后序遍历序列](../../2021/12/剑指Offer_3300_中等_二叉搜索树的后序遍历序列.md)  
> [[中等, 剑指Offer] 二叉树中和为某一值的路径](../../2021/12/剑指Offer_3400_中等_二叉树中和为某一值的路径.md)  
> [[中等, 剑指Offer] 树的子结构](../../2021/11/剑指Offer_2600_中等_树的子结构.md)  
> [[中等, 剑指Offer] 重建二叉树 🔥](../../2021/11/剑指Offer_0700_中等_重建二叉树.md)  
> [[中等, 牛客] 二叉搜索树与双向链表](../03/牛客_0064_中等_二叉搜索树与双向链表.md)  
> [[中等, 牛客] 二叉搜索树的第k个节点](../03/牛客_0081_中等_二叉搜索树的第k个节点.md)  
> [[中等, 牛客] 二叉树中和为某一值的路径(二)](../01/牛客_0008_中等_二叉树中和为某一值的路径(二).md)  
> [[中等, 牛客] 二叉树根节点到叶子节点的所有路径和](../01/牛客_0005_中等_二叉树根节点到叶子节点的所有路径和.md)  
> [[中等, 牛客] 在二叉树中找到两个节点的最近公共祖先](../04/牛客_0102_中等_在二叉树中找到两个节点的最近公共祖先.md)  
> [[中等, 牛客] 完全二叉树结点数](../04/牛客_0084_中等_完全二叉树结点数.md)  
> [[中等, 牛客] 找到搜索二叉树中两个错误的节点](../03/牛客_0058_中等_找到搜索二叉树中两个错误的节点.md)  
> [[中等, 牛客] 把二叉树打印成多行 🔥](../03/牛客_0080_中等_把二叉树打印成多行.md)  
> [[中等, 牛客] 按之字形顺序打印二叉树](../01/牛客_0014_中等_按之字形顺序打印二叉树.md)  
> [[中等, 牛客] 求二叉树的层序遍历](../01/牛客_0015_中等_求二叉树的层序遍历.md)  
> [[中等, 牛客] 重建二叉树](../01/牛客_0012_中等_重建二叉树.md)  
  > 
> [[困难, 剑指Offer] 序列化二叉树](../../2021/12/剑指Offer_3700_困难_序列化二叉树.md)  
> [[困难, 牛客] 二叉树中的最大路径和](../01/牛客_0006_困难_二叉树中的最大路径和.md)  
> [[困难, 牛客] 序列化二叉树](../05/牛客_0123_困难_序列化二叉树.md)  
  > 
> [[简单, LeetCode] 二叉树的所有路径](../07/LeetCode_0257_简单_二叉树的所有路径.md)  
> [[简单, LeetCode] 二叉树的最大深度 🔥](../07/LeetCode_0104_简单_二叉树的最大深度.md)  
> [[简单, LeetCode] 二叉树的最小深度](../07/LeetCode_0111_简单_二叉树的最小深度.md)  
> [[简单, LeetCode] 平衡二叉树 🔥](../09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, LeetCode] 路径总和](LeetCode_0112_简单_路径总和.md)  
> [[简单, 剑指Offer] 二叉搜索树的最近公共祖先 🔥](../01/剑指Offer_6801_简单_二叉搜索树的最近公共祖先.md)  
> [[简单, 剑指Offer] 二叉搜索树的第k大节点](../01/剑指Offer_5400_简单_二叉搜索树的第k大节点.md)  
> [[简单, 剑指Offer] 二叉树的最近公共祖先](../01/剑指Offer_6802_简单_二叉树的最近公共祖先.md)  
> [[简单, 剑指Offer] 二叉树的镜像](../../2021/11/剑指Offer_2700_简单_二叉树的镜像.md)  
> [[简单, 剑指Offer] 判断是否为平衡二叉树](../01/剑指Offer_5502_简单_判断是否为平衡二叉树.md)  
> [[简单, 剑指Offer] 对称的二叉树](../../2021/11/剑指Offer_2800_简单_对称的二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](../../2021/11/剑指Offer_3201_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](../../2021/11/剑指Offer_3202_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树 (之字形遍历)](../../2021/11/剑指Offer_3203_简单_层序遍历二叉树(之字形遍历).md)  
> [[简单, 剑指Offer] 求二叉树的深度](../01/剑指Offer_5501_简单_求二叉树的深度.md)  
> [[简单, 牛客] 二叉树中和为某一值的路径(一)](../01/牛客_0009_简单_二叉树中和为某一值的路径(一).md)  
> [[简单, 牛客] 二叉树的最大深度](../01/牛客_0013_简单_二叉树的最大深度.md)  
> [[简单, 牛客] 二叉树的镜像](../03/牛客_0072_简单_二叉树的镜像.md)  
> [[简单, 牛客] 判断t1树中是否有与t2树完全相同的子树](../04/牛客_0098_简单_判断t1树中是否有与t2树完全相同的子树.md)  
> [[简单, 牛客] 判断是不是平衡二叉树](../03/牛客_0062_简单_判断是不是平衡二叉树.md)  
> [[简单, 牛客] 合并二叉树](../05/牛客_0117_简单_合并二叉树.md)  
> [[简单, 牛客] 对称的二叉树](../01/牛客_0016_简单_对称的二叉树.md)  
> [[简单, 牛客] 将升序数组转化为平衡二叉搜索树](../01/牛客_0011_简单_将升序数组转化为平衡二叉搜索树.md)  
  > 

</details>
<details><summary><b>深度优先搜索</b></summary>

> [[中等, LeetCode] 括号生成 🔥](../10/LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](../10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 组合总和 🔥](../10/LeetCode_0039_中等_组合总和.md)  
> [[中等, 剑指Offer] 二叉树中和为某一值的路径](../../2021/12/剑指Offer_3400_中等_二叉树中和为某一值的路径.md)  
> [[中等, 剑指Offer] 字符串的排列 (全排列) 🔥](../../2021/12/剑指Offer_3800_中等_字符串的排列(全排列).md)  
> [[中等, 剑指Offer] 打印从1到最大的n位数 (N叉树的遍历)](../../2021/11/剑指Offer_1700_中等_打印从1到最大的n位数(N叉树的遍历).md)  
> [[中等, 剑指Offer] 机器人的运动范围](../../2021/11/剑指Offer_1300_中等_机器人的运动范围.md)  
> [[中等, 剑指Offer] 矩阵中的路径](../../2021/11/剑指Offer_1200_中等_矩阵中的路径.md)  
> [[中等, 牛客] 二叉树中和为某一值的路径(二)](../01/牛客_0008_中等_二叉树中和为某一值的路径(二).md)  
> [[中等, 牛客] 二叉树根节点到叶子节点的所有路径和](../01/牛客_0005_中等_二叉树根节点到叶子节点的所有路径和.md)  
> [[中等, 牛客] 字符串的排列 🔥](../05/牛客_0121_中等_字符串的排列.md)  
> [[中等, 牛客] 实现二叉树先序、中序、后序遍历](../03/牛客_0045_中等_实现二叉树先序、中序、后序遍历.md)  
> [[中等, 牛客] 岛屿数量 🔥](../04/牛客_0109_中等_岛屿数量.md)  
> [[中等, 牛客] 数字字符串转化成IP地址](../01/牛客_0020_中等_数字字符串转化成IP地址.md)  
  > 
> [[困难, 牛客] 多叉树的直径](../04/牛客_0099_困难_多叉树的直径.md)  
  > 
> [[简单, LeetCode] 二叉树的最小深度](../07/LeetCode_0111_简单_二叉树的最小深度.md)  
> [[简单, 剑指Offer] 二叉搜索树的第k大节点](../01/剑指Offer_5400_简单_二叉搜索树的第k大节点.md)  
> [[简单, 剑指Offer] 从尾到头打印链表](../../2021/11/剑指Offer_0600_简单_从尾到头打印链表.md)  
> [[简单, 牛客] 二叉树中和为某一值的路径(一)](../01/牛客_0009_简单_二叉树中和为某一值的路径(一).md)  
  > 

</details>
<details><summary><b>前缀和</b></summary>

> [[中等, LeetCode] 从魔法师身上吸取的最大能量](../../2025/10/LeetCode_3147_中等_从魔法师身上吸取的最大能量.md)  
> [[中等, 剑指Offer] 构建乘积数组](../01/剑指Offer_6600_中等_构建乘积数组.md)  
> [[中等, 牛客] 和为K的连续子数组](../05/牛客_0125_中等_和为K的连续子数组.md)  
  > 

</details>
<details><summary><b>树形递归</b></summary>

> [[中等, LeetCode] 打家劫舍III](LeetCode_0337_中等_打家劫舍III.md)  
> [[中等, 牛客] 判断一棵二叉树是否为搜索二叉树和完全二叉树](../03/牛客_0060_中等_判断一棵二叉树是否为搜索二叉树和完全二叉树.md)  
  > 
> [[困难, LeetCode] 二叉树中的最大路径和](../02/LeetCode_0124_困难_二叉树中的最大路径和.md)  
  > 
> [[简单, LeetCode] 平衡二叉树 🔥](../09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, 剑指Offer] 二叉树的最近公共祖先](../01/剑指Offer_6802_简单_二叉树的最近公共祖先.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
