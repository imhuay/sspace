## 二叉搜索树的最近公共祖先
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%8F%89%E6%A0%91/%E6%A0%91&color=blue&style=flat-square)](../../../README.md#二叉树树)
[![](https://img.shields.io/static/v1?label=&message=%E7%BB%8F%E5%85%B8&color=blue&style=flat-square)](../../../README.md#经典)
<!--END_SECTION:badge-->
<!--info
tags: [二叉搜索树, 经典]
source: 剑指Offer
level: 简单
number: '6801'
name: 二叉搜索树的最近公共祖先
companies: []
-->

<summary><b>问题简述</b></summary>

> [剑指 Offer 68 - I. 二叉搜索树的最近公共祖先 - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

```txt
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先.

如果是普通二叉树呢?
```

<details><summary><b>详细描述</b></summary>

```txt
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先.

百度百科中最近公共祖先的定义为: "对于有根树 T 的两个结点 p、q, 最近公共祖先表示为一个结点 x, 满足 x 是 p、q 的祖先且 x 的深度尽可能大 (一个节点也可以是它自己的祖先)."

例如, 给定如下二叉搜索树

            6
          /   \
         2     8
        / \   / \
       0   4 7   9
          / \
         3   5

示例 1:
    输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    输出: 6
    解释: 节点 2 和节点 8 的最近公共祖先是 6.
示例 2:
    输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    输出: 2
    解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身.

说明:
    所有节点的值都是唯一的.
    p、q 为不同节点且均存在于给定的二叉搜索树中.

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1: 基于二叉搜索树</b></summary>

- 根据二叉搜索树的性质: 左子树都小于父节点, 右子树都大于父节点, 快速找出指定节点的父节点路径;
- 然后找出最近的公共祖先;

<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def foo(node, p):
            ret = []
            while p and p.val != node.val:
                ret.append(p)
                if p.val > node.val:
                    p = p.left
                else:
                    p = p.right
            ret.append(p)
            return ret

        P = foo(p, root)
        Q = foo(q, root)

        ret = None
        for l, r in zip(P, Q):
            if l.val == r.val:
                ret = l
            else:
                break

        return ret
```

</details>


**优化1**: 根据二叉搜索树的定义, 如果一个节点 node 是 p 和 q 的祖先, 则有 node 同时 >= 或 <= p 和 q; 因此可以优化为一次遍历;

<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        node = root
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                break

        return node
```

</details>

**优化2**: 若可保证 `p.val < q.val`, 则在循环中可减少判断条件.
> [二叉搜索树的最近公共祖先 (迭代 / 递归, 清晰图解) ](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-i-er-cha-sou-suo-shu-de-zui-jin-g-7/)

<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val > p.val:
            p, q = q, p

        node = root
        while node:
            if node.val > p.val:
                node = node.left
            elif node.val < q.val:
                node = node.right
            else:
                break

        return node
```

</details>


<summary><b>思路2: 普通二叉树</b></summary>

> [剑指 Offer 68 - II. 二叉树的最近公共祖先 - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

- 思路1 利用了二叉搜索树的性质快速获取祖先路径;
- 可以不利用二叉搜索树的性质来获取祖先路径 (对非二叉搜索树也适用);
- 因为必须先找到目标节点才能确定路线, 所以可以考虑后序遍历; 当找到目标节点时, 返回 flag, 指示上级节点是否为祖先节点;

<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # 后序遍历搜索历史祖先, 因为是后序遍历, 所以 trace 是倒序的
        def dfs(node, target, trace):
            if node is None:
                return False
            if node.val == target.val:
                trace.append(node)  # 根据定义, 自己也是自己的祖先节点
                return True

            if dfs(node.left, target, trace) or dfs(node.right, target, trace):
                trace.append(node)
                return True
            else:
                return False

        # 分别找出 p 和 q 的祖先路径
        trace_p = []
        dfs(root, p, trace_p)
        # print(trace_p)
        trace_q = []
        dfs(root, q, trace_q)
        # print(trace_q)

        # 遍历找出最后一个相同的祖先
        ret = None
        for l, r in zip(trace_p[::-1], trace_q[::-1]):
            if l.val == r.val:
                ret = l
            else:
                break

        return ret
```

</details>


**优化**: 不使用额外空间存储祖先路径, 即在遍历过程中判断;
> [二叉树的最近公共祖先 (DFS , 清晰图解) - Krahets](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-ii-er-cha-shu-de-zui-jin-gong-gon-7/)

- 如果 node 仅是 p 和 q 的公共祖先 (但不是最近公共祖先), 那么 node 的左右子树之一必也是 p 和 q 的公共祖先;
- 如果 node 是 p 和 q 的最近公共祖先, 那么 node 的左右子树都不是 p 和 q 的公共祖先;
- 根据以上两条性质, 可知, 如果 node 是 p、q 的**最近公共祖先**, 有:
    - node 是 p、q 的公共祖先, 且 p 和 q 分别在 node 的两侧;
    - node 是 p 或 q 之一, 且是另一个节点的祖先;


<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):
            # 下面两个判断条件可以写在一起, 为了使逻辑更清晰, 故分开写
            if node is None:  # 说明当前路径上没有 p 或 q
                return None
            if node == p or node == q:  # 说明当前路径上存在 p 或 q
                return node

            l = dfs(node.left)
            r = dfs(node.right)

            # 返回的非 None 节点都是 p 和 q 的公共祖先
            if l is None and r is not None:  # r 是 p 和 q 之一, 且是另一个节点的祖先
                return r
            elif r is None and l is not None:  # l 是 p 和 q 之一, 且是另一个节点的祖先
                return l
            elif l and r:  # p 和 q 分别在 node 的两侧
                return node
            else:
                return None

        return dfs(root)

```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

> 🌧️ _暂无主题相关的笔记_


<details><summary><b>其他算法笔记</b></summary>

- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表常用操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>二叉树/树 (47)</b></summary>

> [[中等, LeetCode] 二叉树的完全性检验 🔥](../03/LeetCode_0958_中等_二叉树的完全性检验.md)  
> [[中等, LeetCode] 从叶结点开始的最小字符串](../07/LeetCode_0988_中等_从叶结点开始的最小字符串.md)  
> [[中等, LeetCode] 求根节点到叶节点数字之和](../07/LeetCode_0129_中等_求根节点到叶节点数字之和.md)  
> [[中等, LeetCode] 路径总和II](../06/LeetCode_0113_中等_路径总和II.md)  
> [[中等, LeetCode] 路径总和III](../06/LeetCode_0437_中等_路径总和III.md)  
> [[中等, LeetCode] 验证二叉搜索树](../03/LeetCode_0098_中等_验证二叉搜索树.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](../../2021/12/剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 二叉搜索树的后序遍历序列](../../2021/12/剑指Offer_3300_中等_二叉搜索树的后序遍历序列.md)  
> [[中等, 剑指Offer] 二叉树中和为某一值的路径](../../2021/12/剑指Offer_3400_中等_二叉树中和为某一值的路径.md)  
> [[中等, 剑指Offer] 树的子结构](../../2021/11/剑指Offer_2600_中等_树的子结构.md)  
> [[中等, 剑指Offer] 重建二叉树 🔥](../../2021/11/剑指Offer_0700_中等_重建二叉树.md)  
> [[中等, 牛客] 二叉搜索树与双向链表](../03/牛客_0064_中等_二叉搜索树与双向链表.md)  
> [[中等, 牛客] 二叉搜索树的第k个节点](../03/牛客_0081_中等_二叉搜索树的第k个节点.md)  
> [[中等, 牛客] 二叉树中和为某一值的路径(二)](牛客_0008_中等_二叉树中和为某一值的路径(二).md)  
> [[中等, 牛客] 二叉树根节点到叶子节点的所有路径和](牛客_0005_中等_二叉树根节点到叶子节点的所有路径和.md)  
> [[中等, 牛客] 在二叉树中找到两个节点的最近公共祖先](../04/牛客_0102_中等_在二叉树中找到两个节点的最近公共祖先.md)  
> [[中等, 牛客] 完全二叉树结点数](../04/牛客_0084_中等_完全二叉树结点数.md)  
> [[中等, 牛客] 找到搜索二叉树中两个错误的节点](../03/牛客_0058_中等_找到搜索二叉树中两个错误的节点.md)  
> [[中等, 牛客] 把二叉树打印成多行 🔥](../03/牛客_0080_中等_把二叉树打印成多行.md)  
> [[中等, 牛客] 按之字形顺序打印二叉树](牛客_0014_中等_按之字形顺序打印二叉树.md)  
> [[中等, 牛客] 求二叉树的层序遍历](牛客_0015_中等_求二叉树的层序遍历.md)  
> [[中等, 牛客] 重建二叉树](牛客_0012_中等_重建二叉树.md)  
  > 
> [[困难, 剑指Offer] 序列化二叉树](../../2021/12/剑指Offer_3700_困难_序列化二叉树.md)  
> [[困难, 牛客] 二叉树中的最大路径和](牛客_0006_困难_二叉树中的最大路径和.md)  
> [[困难, 牛客] 序列化二叉树](../05/牛客_0123_困难_序列化二叉树.md)  
  > 
> [[简单, LeetCode] 二叉树的所有路径](../07/LeetCode_0257_简单_二叉树的所有路径.md)  
> [[简单, LeetCode] 二叉树的最大深度 🔥](../07/LeetCode_0104_简单_二叉树的最大深度.md)  
> [[简单, LeetCode] 二叉树的最小深度](../07/LeetCode_0111_简单_二叉树的最小深度.md)  
> [[简单, LeetCode] 平衡二叉树 🔥](../09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, LeetCode] 路径总和](../06/LeetCode_0112_简单_路径总和.md)  
> [[简单, 剑指Offer] 二叉搜索树的第k大节点](剑指Offer_5400_简单_二叉搜索树的第k大节点.md)  
> [[简单, 剑指Offer] 二叉树的最近公共祖先](剑指Offer_6802_简单_二叉树的最近公共祖先.md)  
> [[简单, 剑指Offer] 二叉树的镜像](../../2021/11/剑指Offer_2700_简单_二叉树的镜像.md)  
> [[简单, 剑指Offer] 判断是否为平衡二叉树](剑指Offer_5502_简单_判断是否为平衡二叉树.md)  
> [[简单, 剑指Offer] 对称的二叉树](../../2021/11/剑指Offer_2800_简单_对称的二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](../../2021/11/剑指Offer_3201_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](../../2021/11/剑指Offer_3202_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树 (之字形遍历)](../../2021/11/剑指Offer_3203_简单_层序遍历二叉树(之字形遍历).md)  
> [[简单, 剑指Offer] 求二叉树的深度](剑指Offer_5501_简单_求二叉树的深度.md)  
> [[简单, 牛客] 二叉树中和为某一值的路径(一)](牛客_0009_简单_二叉树中和为某一值的路径(一).md)  
> [[简单, 牛客] 二叉树的最大深度](牛客_0013_简单_二叉树的最大深度.md)  
> [[简单, 牛客] 二叉树的镜像](../03/牛客_0072_简单_二叉树的镜像.md)  
> [[简单, 牛客] 判断t1树中是否有与t2树完全相同的子树](../04/牛客_0098_简单_判断t1树中是否有与t2树完全相同的子树.md)  
> [[简单, 牛客] 判断是不是平衡二叉树](../03/牛客_0062_简单_判断是不是平衡二叉树.md)  
> [[简单, 牛客] 合并二叉树](../05/牛客_0117_简单_合并二叉树.md)  
> [[简单, 牛客] 对称的二叉树](牛客_0016_简单_对称的二叉树.md)  
> [[简单, 牛客] 将升序数组转化为平衡二叉搜索树](牛客_0011_简单_将升序数组转化为平衡二叉搜索树.md)  
  > 

</details>

<details><summary><b>经典 (37)</b></summary>

> [[中等, LeetCode] 下一个排列 🔥](../10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 二叉树的完全性检验 🔥](../03/LeetCode_0958_中等_二叉树的完全性检验.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, 剑指Offer2] 整数除法 🔥](../09/剑指Offer2_001_中等_整数除法.md)  
> [[中等, 剑指Offer] 丑数 🔥](../../2021/12/剑指Offer_4900_中等_丑数.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](../../2021/12/剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 剑指Offer] 复杂链表的复制 (深拷贝) 🔥](../../2021/12/剑指Offer_3500_中等_复杂链表的复制(深拷贝).md)  
> [[中等, 剑指Offer] 字符串的排列 (全排列) 🔥](../../2021/12/剑指Offer_3800_中等_字符串的排列(全排列).md)  
> [[中等, 剑指Offer] 把字符串转换成整数 🔥](剑指Offer_6700_中等_把字符串转换成整数.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../../2021/11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 剑指Offer] 栈的压入、弹出序列 🔥](../../2021/11/剑指Offer_3100_中等_栈的压入、弹出序列.md)  
> [[中等, 剑指Offer] 重建二叉树 🔥](../../2021/11/剑指Offer_0700_中等_重建二叉树.md)  
> [[中等, 剑指Offer] 顺时针打印矩阵 (3种思路4个写法) 🔥](../../2021/11/剑指Offer_2900_中等_顺时针打印矩阵(3种思路4个写法).md)  
> [[中等, 牛客] 01背包 🔥](../05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 丢棋子问题 (鹰蛋问题) 🔥](../04/牛客_0087_中等_丢棋子问题(鹰蛋问题).md)  
> [[中等, 牛客] 字符串的排列 🔥](../05/牛客_0121_中等_字符串的排列.md)  
> [[中等, 牛客] 寻找峰值 🔥](../04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 岛屿数量 🔥](../04/牛客_0109_中等_岛屿数量.md)  
> [[中等, 牛客] 把字符串转换成整数(atoi) 🔥](../04/牛客_0100_中等_把字符串转换成整数(atoi).md)  
> [[中等, 牛客] 数组中只出现一次的两个数字 🔥](../03/牛客_0075_中等_数组中只出现一次的两个数字.md)  
> [[中等, 牛客] 最长公共子序列(二) 🔥](../04/牛客_0092_中等_最长公共子序列(二).md)  
> [[中等, 牛客] 栈和排序 🔥](../05/牛客_0115_中等_栈和排序.md)  
> [[中等, 牛客] 汉诺塔问题 🔥](../03/牛客_0067_中等_汉诺塔问题.md)  
  > 
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 数组中的逆序对 🔥](剑指Offer_5100_困难_数组中的逆序对.md)  
> [[困难, 牛客] 接雨水问题 🔥](../05/牛客_0128_困难_接雨水问题.md)  
> [[困难, 牛客] 设计LFU缓存结构 🔥](../04/牛客_0094_困难_设计LFU缓存结构.md)  
> [[困难, 牛客] 设计LRU缓存结构 🔥](../04/牛客_0093_困难_设计LRU缓存结构.md)  
  > 
> [[简单, LeetCode] 二叉树的最大深度 🔥](../07/LeetCode_0104_简单_二叉树的最大深度.md)  
> [[简单, LeetCode] 反转链表 🔥](../10/LeetCode_0206_简单_反转链表.md)  
> [[简单, 剑指Offer] 反转链表 🔥](../../2021/11/剑指Offer_2400_简单_反转链表.md)  
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](../../2021/12/剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
> [[简单, 剑指Offer] 最小的k个数 (partition操作) 🔥](../../2021/12/剑指Offer_4000_简单_最小的k个数(partition操作).md)  
> [[简单, 牛客] 二进制中1的个数 🔥](../05/牛客_0120_简单_二进制中1的个数.md)  
> [[简单, 牛客] 单链表的排序 🔥](../03/牛客_0070_简单_单链表的排序.md)  
> [[简单, 牛客] 求平方根 🔥](../02/牛客_0032_简单_求平方根.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
