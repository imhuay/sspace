## 机器人的运动范围
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2&color=blue&style=flat-square)](../../../README.md#深度优先搜索)
<!--END_SECTION:badge-->
<!--info
tags: [DFS]
source: 剑指Offer
level: 中等
number: '1300'
name: 机器人的运动范围
companies: []
-->

<summary><b>问题描述</b></summary>

```txt
地上有一个m行n列的方格, 从坐标 [0,0] 到坐标 [m-1,n-1] . 一个机器人从坐标 [0, 0] 的格子开始移动, 它每次可以向左、右、上、下移动一格 (不能移动到方格外), 也不能进入行坐标和列坐标的数位之和大于k的格子. 例如, 当k为18时, 机器人能够进入方格 [35, 37] , 因为3+5+3+7=18. 但它不能进入方格 [35, 38], 因为3+5+3+8=19. 请问该机器人能够到达多少个格子?

示例 1:
    输入: m = 2, n = 3, k = 1
    输出: 3
示例 2:
    输入: m = 3, n = 1, k = 0
    输出: 1

提示:
    1 <= n,m <= 100
    0 <= k <= 20

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<summary><b>思路</b></summary>

- 本题也可以使用广度优先搜索;
  > [机器人的运动范围 (回溯算法, DFS / BFS , 清晰图解) ](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/)

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<details><summary><b>Python: DFS+回溯</b></summary>

```python
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def dig_sum(x):  # 求数位之和
            s = 0
            while x != 0:
                s += x % 10
                x = x // 10
            return s

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or dig_sum(i) + dig_sum(j) > k:
                return 0

            if (i, j) in visited:  # 如果已经访问过
                return 0
            else:
                visited.add((i, j))  # 访问标记
                return 1 + dfs(i + 1, j) + dfs(i, j + 1)  # 因为只能往左或往右, 所以只需要搜索两个方向

        visited = set()
        return dfs(0, 0)
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


<details><summary><b>深度优先搜索 (19)</b></summary>

> [[中等, LeetCode] 括号生成 🔥](../../2022/10/LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](../../2022/10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 组合总和 🔥](../../2022/10/LeetCode_0039_中等_组合总和.md)  
> [[中等, LeetCode] 路径总和III](../../2022/06/LeetCode_0437_中等_路径总和III.md)  
> [[中等, 剑指Offer] 二叉树中和为某一值的路径](../12/剑指Offer_3400_中等_二叉树中和为某一值的路径.md)  
> [[中等, 剑指Offer] 字符串的排列 (全排列) 🔥](../12/剑指Offer_3800_中等_字符串的排列(全排列).md)  
> [[中等, 剑指Offer] 打印从1到最大的n位数 (N叉树的遍历)](剑指Offer_1700_中等_打印从1到最大的n位数(N叉树的遍历).md)  
> [[中等, 剑指Offer] 矩阵中的路径](剑指Offer_1200_中等_矩阵中的路径.md)  
> [[中等, 牛客] 二叉树中和为某一值的路径(二)](../../2022/01/牛客_0008_中等_二叉树中和为某一值的路径(二).md)  
> [[中等, 牛客] 二叉树根节点到叶子节点的所有路径和](../../2022/01/牛客_0005_中等_二叉树根节点到叶子节点的所有路径和.md)  
> [[中等, 牛客] 字符串的排列 🔥](../../2022/05/牛客_0121_中等_字符串的排列.md)  
> [[中等, 牛客] 实现二叉树先序、中序、后序遍历](../../2022/03/牛客_0045_中等_实现二叉树先序、中序、后序遍历.md)  
> [[中等, 牛客] 岛屿数量 🔥](../../2022/04/牛客_0109_中等_岛屿数量.md)  
> [[中等, 牛客] 数字字符串转化成IP地址](../../2022/01/牛客_0020_中等_数字字符串转化成IP地址.md)  
  > 
> [[困难, 牛客] 多叉树的直径](../../2022/04/牛客_0099_困难_多叉树的直径.md)  
  > 
> [[简单, LeetCode] 二叉树的最小深度](../../2022/07/LeetCode_0111_简单_二叉树的最小深度.md)  
> [[简单, 剑指Offer] 二叉搜索树的第k大节点](../../2022/01/剑指Offer_5400_简单_二叉搜索树的第k大节点.md)  
> [[简单, 剑指Offer] 从尾到头打印链表](剑指Offer_0600_简单_从尾到头打印链表.md)  
> [[简单, 牛客] 二叉树中和为某一值的路径(一)](../../2022/01/牛客_0009_简单_二叉树中和为某一值的路径(一).md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
