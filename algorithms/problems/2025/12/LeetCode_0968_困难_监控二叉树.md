## 监控二叉树
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-12-02%2013%3A39%3A41&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&color=red&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E6%A0%91%E5%BD%A2%E9%80%92%E5%BD%92&color=blue&style=flat-square)](../../../README.md#树形递归)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [树形DP]
source: 'LeetCode'
level: '困难'
number: '968'
name: '监控二叉树'
-->

> [968. 监控二叉树 - 力扣 (LeetCode) ](https://leetcode.cn/problems/binary-tree-cameras/description/)

<summary><b>问题简述</b></summary>

```md
给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。
```

<!-- 
<details><summary><b>详细描述</b></summary>

```md
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

---

<summary><b>思路</b></summary>

> [一个思路解决两种变形: 一般树 / 点权树 - 灵茶山艾府 - 力扣 (LeetCode) ](https://leetcode.cn/problems/binary-tree-cameras/solutions/2452795/shi-pin-ru-he-si-kao-shu-xing-dpgai-chen-uqsf/)

<details><summary><b>Python</b></summary>

```python
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        def dfs(n):
            if not n:
                return inf, 0, 0
            
            l_i, l_p, l_c = dfs(n.left)
            r_i, r_p, r_c = dfs(n.right)

            i = min(l_i, l_p, l_c) + min(r_i, r_p, r_c) + 1
            p = min(l_i, l_c) + min(r_i, r_c)
            c = min(l_i + r_c, r_i + l_c, l_i + r_i)
            return i, p, c
        
        i, _, c = dfs(root)
        return min(i, c)
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


<details><summary><b>树形递归 (7)</b></summary>

> [[中等, LeetCode] 打家劫舍III](../../2022/06/LeetCode_0337_中等_打家劫舍III.md)  
> [[中等, LeetCode] 路径总和III](../../2022/06/LeetCode_0437_中等_路径总和III.md)  
> [[中等, 牛客] 判断一棵二叉树是否为搜索二叉树和完全二叉树](../../2022/03/牛客_0060_中等_判断一棵二叉树是否为搜索二叉树和完全二叉树.md)  
  > 
> [[困难, LeetCode] 二叉树中的最大路径和](../../2022/02/LeetCode_0124_困难_二叉树中的最大路径和.md)  
  > 
> [[简单, LeetCode] 二叉树的直径](../11/LeetCode_0543_简单_二叉树的直径.md)  
> [[简单, LeetCode] 平衡二叉树 🔥](../../2022/09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, 剑指Offer] 二叉树的最近公共祖先](../../2022/01/剑指Offer_6802_简单_二叉树的最近公共祖先.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
