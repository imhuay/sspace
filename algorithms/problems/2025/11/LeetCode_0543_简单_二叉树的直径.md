## 二叉树的直径
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-11-30%2001%3A14%3A52&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E6%A0%91%E5%BD%A2%E9%80%92%E5%BD%92&color=blue&style=flat-square)](../../../README.md#树形递归)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [树形DP]
source: 'LeetCode'
level: '简单'
number: '543'
name: '二叉树的直径'
-->

> [543. 二叉树的直径 - 力扣 (LeetCode) ](https://leetcode.cn/problems/diameter-of-binary-tree/description/)

<summary><b>问题简述</b></summary>

```md
给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。
```

<!-- 
<details><summary><b>详细描述</b></summary>

```md
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

---

<summary><b>思路: 树形 DP</b></summary>

- 对任一节点, **经过该节点** 的 "直径" = 左子树的深度 + 右子树的深度
- 所需信息:
    ```python
    @dataclass
    class Info:
        h: int = 0      # 该节点的深度
        d: int = 0      # 该节点的最大直径 (可能不经过该节点)
    ```

<details><summary><b>Python</b></summary>

```python
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        from dataclasses import dataclass

        @dataclass
        class Info:
            h: int = 0      # 该节点的深度
            d: int = 0      # 该节点的最大直径 (可能不经过该节点)

        def dfs(x):
            if not x:
                return Info()
            
            l, r = dfs(x.left), dfs(x.right)
            h = max(l.h, r.h) + 1
            d = max(l.d, r.d, l.h + r.h)
            return Info(h, d)

        return dfs(root).d
```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  

<details><summary><b>其他算法笔记</b></summary>

- [二分查找相关](../../../../notes/_archives/2025/10/二分查找备忘.md)  
- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>树形递归 (6)</b></summary>

> [[中等, LeetCode] 打家劫舍III](../../2022/06/LeetCode_0337_中等_打家劫舍III.md)  
> [[中等, LeetCode] 路径总和III](../../2022/06/LeetCode_0437_中等_路径总和III.md)  
> [[中等, 牛客] 判断一棵二叉树是否为搜索二叉树和完全二叉树](../../2022/03/牛客_0060_中等_判断一棵二叉树是否为搜索二叉树和完全二叉树.md)  
  > 
> [[困难, LeetCode] 二叉树中的最大路径和](../../2022/02/LeetCode_0124_困难_二叉树中的最大路径和.md)  
  > 
> [[简单, LeetCode] 平衡二叉树 🔥](../../2022/09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, 剑指Offer] 二叉树的最近公共祖先](../../2022/01/剑指Offer_6802_简单_二叉树的最近公共祖先.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
