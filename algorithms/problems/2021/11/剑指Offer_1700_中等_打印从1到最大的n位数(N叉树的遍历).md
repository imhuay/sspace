## 打印从1到最大的n位数 (N叉树的遍历)
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-23%2002%3A03%3A22&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2&color=blue&style=flat-square)](../../../README.md#深度优先搜索)
<!--END_SECTION:badge-->
<!--info
tags: [DFS]
source: 剑指Offer
level: 中等
number: '1700'
name: 打印从1到最大的n位数 (N叉树的遍历)
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
输入数字 n, 按顺序打印出从 1 到最大的 n 位十进制数 (考虑大数情况);
比如输入 3, 则打印出 1~999
```

<details><summary><b>详细描述</b></summary>

```txt
输入数字 n, 按顺序打印出从 1 到最大的 n 位十进制数. 比如输入 3, 则打印出 1、2、3 一直到最大的 3 位数 999.

示例 1:
    输入: n = 1
    输出: [1,2,3,4,5,6,7,8,9]

说明:
    用返回一个整数列表来代替打印
    n 为正整数

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<summary><b>思路</b></summary>

- 考虑大数情况下, 直接遍历会存在越界问题;
- 本题实际上是一个 N 叉树 (N=9) 的遍历问题;

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<details><summary><b>Python: 不考虑大数</b></summary>

```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10 ** n):
            res.append(i)
        return res
```

</details>

<details><summary><b>Python: 考虑大数</b></summary>

```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:

        ret = []
        dig = '0123456789'
        buf = [''] * n

        def process(buf):
            """去除前置0"""
            start = 0
            while start < n - 1 and buf[start] == '0':  # 保留至少一个 0
                start += 1
            return int(''.join(buf[start:]))  # LeetCode要求返回 int

        def dfs(k):
            """DFS全排列"""
            if k == n:
                ret.append(process(buf))
                return

            for i in dig:  # 每一位都有 0-9 10种取法
                buf[k] = i
                dfs(k+1)

        dfs(0)
        return ret[1:]  # 要求从 1 开始, 故移除第一位
```

</details>


<!--START_SECTION:relate_problem-->
---

### 相关主题

<details><summary><b>深度优先搜索</b></summary>

> [[中等, LeetCode] 括号生成 🔥](../../2022/10/LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](../../2022/10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 组合总和 🔥](../../2022/10/LeetCode_0039_中等_组合总和.md)  
> [[中等, LeetCode] 路径总和III](../../2022/06/LeetCode_0437_中等_路径总和III.md)  
> [[中等, 剑指Offer] 二叉树中和为某一值的路径](../12/剑指Offer_3400_中等_二叉树中和为某一值的路径.md)  
> [[中等, 剑指Offer] 字符串的排列 (全排列) 🔥](../12/剑指Offer_3800_中等_字符串的排列(全排列).md)  
> [[中等, 剑指Offer] 机器人的运动范围](剑指Offer_1300_中等_机器人的运动范围.md)  
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
