## 验证二叉搜索树
<!--START_SECTION:badge-->

![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&label_color=gray&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&label_color=gray&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%8F%89%E6%A0%91/%E6%A0%91&label_color=gray&color=blue&style=flat-square)](../../../README.md#二叉树树)

<!--END_SECTION:badge-->
<!--info
tags: [二叉树]
source: LeetCode
level: 中等
number: '0098'
name: 验证二叉搜索树
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给你一个二叉树的根节点 root , 判断其是否是一个有效的二叉搜索树。
```
> [98. 验证二叉搜索树 - 力扣（LeetCode）](https://leetcode-cn.com/problems/validate-binary-search-tree/)

<!-- 
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->


<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 二叉搜索树定义的定义:
    - 节点的左子树只包含 小于 当前节点的数;
    - 节点的右子树只包含 大于 当前节点的数;
    - 所有左子树和右子树自身必须也是二叉搜索树;
    - 空树是二叉搜索树
- 可以看到, 要判断是否为二叉树, 需要**先得到左右子树的信息**, 故采用**后序遍历**;

<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        from dataclasses import dataclass

        @dataclass
        class Info:
            is_bst: bool = False        # 当前子树是否为 BST
            max_v: int = float('-inf')     # 当前子树中的最大值
            min_v: int = float('inf')      # 当前子树中的最小值

        def dfs(x):
            if not x:  # 空树是二叉搜索树
                return Info(True)

            # 后序遍历: 先访问左右子树, 这里访问顺序不影响结果
            l, r = dfs(x.left), dfs(x.right)  # 得到左右子树的 info

            max_v = max(x.val, r.max_v)
            min_v = min(x.val, l.min_v)
            is_bst = l.is_bst and r.is_bst and l.max_v < x.val < r.min_v

            return Info(is_bst, max_v, min_v)

        return dfs(root).is_bst
```

</details>

