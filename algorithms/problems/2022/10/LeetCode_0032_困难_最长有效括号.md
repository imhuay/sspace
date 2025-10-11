## 最长有效括号
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&color=red&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
[![](https://img.shields.io/static/v1?label=&message=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#动态规划)
[![](https://img.shields.io/static/v1?label=&message=%E6%A0%88/%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#栈队列)
<!--END_SECTION:badge-->
<!--info
tags: [动态规划, 栈, lc100]
source: LeetCode
level: 困难
number: '0032'
name: 最长有效括号
companies: []
-->

>

<summary><b>问题简述</b></summary>

```txt
给你一个只包含 '(' 和 ')' 的字符串, 找出最长有效 (格式正确且连续) 括号子串的长度.
```

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路 1: 动态规划 (推荐) </b></summary>

- `dp[i] = 2 + dp[i−1] + dp[i−dp[i−1]−2]`, 说明见下图:

    <div align="center"><img src="../../../_assets/LeetCode_0032_最长有效括号.png" height="300" /></div>

    > 时刻注意数组下标的有效性, 即 `i-1 >= 0 and i−dp[i−1]−2 >= 0`

<details><summary><b>Python (迭代, 推荐) </b></summary>

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0

        dp = [0] * len(s)
        for i in range(len(s)):
            if i >= 1 and i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(' and s[i] == ')':
                dp[i] = 2 + dp[i-1] + dp[i - dp[i-1] - 2]

        return max(dp)
```

</details>

<details><summary><b>Python (递归) </b></summary>

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        from functools import lru_cache

        ret = [0]

        @lru_cache(maxsize=None)
        def dfs(i):  # s[i] 结尾的最长有效括号
            if i <= 0: return 0

            if i - dfs(i - 1) - 1 >= 0 and s[i - dfs(i - 1) - 1] == '(' and s[i] == ')':
                r = 2 + dfs(i - 1) + dfs(i - dfs(i - 1) - 2)
                ret[0] = max(ret[0], r)
                return r
            else:
                return 0

        dfs(len(s) - 1)
        return ret[0]
```

</details>

<summary><b>思路 2: 栈</b></summary>

- 技巧性很强的方法, 临场可能很难写出来, 详见: [最长有效括号 (方法 2) - 力扣官方题解](https://leetcode.cn/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/)


<!--START_SECTION:relate_note-->
---

### 算法笔记

- [从暴力递归到动态规划](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  

<details><summary><b>其他算法笔记</b></summary>

- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表常用操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>LeetCode Hot 100 (25)</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 两数相加 🔥](../../2021/10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 全排列 🔥](LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 字母异位词分组 🔥](LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 括号生成 🔥](LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, LeetCode] 无重复字符的最长子串 🔥](../02/LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, LeetCode] 组合总和 🔥](LeetCode_0039_中等_组合总和.md)  
> [[中等, LeetCode] 组合总和II 🔥](LeetCode_0040_中等_组合总和II.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 有效的括号 🔥](../03/LeetCode_0020_简单_有效的括号.md)  
  > 

</details>

<details><summary><b>动态规划 (52)</b></summary>

> [[中等, LeetCode] 一和零](../06/LeetCode_0474_中等_一和零.md)  
> [[中等, LeetCode] 三角形最小路径和](../06/LeetCode_0120_中等_三角形最小路径和.md)  
> [[中等, LeetCode] 不同的二叉搜索树](../03/LeetCode_0096_中等_不同的二叉搜索树.md)  
> [[中等, LeetCode] 乘积最大子数组](../06/LeetCode_0152_中等_乘积最大子数组.md)  
> [[中等, LeetCode] 买卖股票的最佳时机II 🔥](../06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 完全平方数](../02/LeetCode_0279_中等_完全平方数.md)  
> [[中等, LeetCode] 打家劫舍](../06/LeetCode_0198_中等_打家劫舍.md)  
> [[中等, LeetCode] 打家劫舍II](../06/LeetCode_0213_中等_打家劫舍II.md)  
> [[中等, LeetCode] 整数拆分](../../2021/12/LeetCode_0343_中等_整数拆分.md)  
> [[中等, LeetCode] 最小路径和](../01/LeetCode_0064_中等_最小路径和.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, LeetCode] 解码方法](../02/LeetCode_0091_中等_解码方法.md)  
> [[中等, LeetCode] 零钱兑换](../06/LeetCode_0322_中等_零钱兑换.md)  
> [[中等, LeetCode] 零钱兑换II](../06/LeetCode_0518_中等_零钱兑换II.md)  
> [[中等, 剑指Offer] n个骰子的点数](../01/剑指Offer_6000_中等_n个骰子的点数.md)  
> [[中等, 剑指Offer] 丑数 🔥](../../2021/12/剑指Offer_4900_中等_丑数.md)  
> [[中等, 剑指Offer] 剪绳子 (整数拆分)](../../2021/11/剑指Offer_1401_中等_剪绳子(整数拆分).md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](../01/剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 剑指Offer] 斐波那契数列-3 (把数字翻译成字符串)](../../2021/12/剑指Offer_4600_中等_斐波那契数列-3(把数字翻译成字符串).md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../../2021/12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 剑指Offer] 礼物的最大价值](../../2021/12/剑指Offer_4700_中等_礼物的最大价值.md)  
> [[中等, 牛客] 01背包 🔥](../05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 丑数](../03/牛客_0079_中等_丑数.md)  
> [[中等, 牛客] 丢棋子问题 (鹰蛋问题) 🔥](../04/牛客_0087_中等_丢棋子问题(鹰蛋问题).md)  
> [[中等, 牛客] 把数字翻译成字符串](../05/牛客_0116_中等_把数字翻译成字符串.md)  
> [[中等, 牛客] 最大正方形](../04/牛客_0108_中等_最大正方形.md)  
> [[中等, 牛客] 最长公共子串](../05/牛客_0127_中等_最长公共子串.md)  
> [[中等, 牛客] 最长公共子序列(二) 🔥](../04/牛客_0092_中等_最长公共子序列(二).md)  
> [[中等, 牛客] 最长回文子串](../01/牛客_0017_中等_最长回文子串.md)  
> [[中等, 牛客] 矩阵的最小路径和](../03/牛客_0059_中等_矩阵的最小路径和.md)  
> [[中等, 牛客] 连续子数组的最大乘积](../04/牛客_0083_中等_连续子数组的最大乘积.md)  
  > 
> [[困难, LeetCode] 买卖股票的最佳时机III](../06/LeetCode_0123_困难_买卖股票的最佳时机III.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 正则表达式匹配](../../2021/11/剑指Offer_1900_困难_正则表达式匹配.md)  
> [[困难, 牛客] 最长上升子序列(三)](../04/牛客_0091_困难_最长上升子序列(三).md)  
> [[困难, 牛客] 正则表达式匹配](../05/牛客_0122_困难_正则表达式匹配.md)  
> [[困难, 牛客] 编辑距离(二)](../02/牛客_0035_困难_编辑距离(二).md)  
> [[困难, 牛客] 通配符匹配](../03/牛客_0044_困难_通配符匹配.md)  
  > 
> [[简单, LeetCode] 买卖股票的最佳时机](../06/LeetCode_0121_简单_买卖股票的最佳时机.md)  
> [[简单, LeetCode] 最大子数组和](../01/LeetCode_0053_简单_最大子数组和.md)  
> [[简单, LeetCode] 爬楼梯](../01/LeetCode_0070_简单_爬楼梯.md)  
> [[简单, 剑指Offer] 斐波那契数列](../../2021/11/剑指Offer_1001_简单_斐波那契数列.md)  
> [[简单, 剑指Offer] 跳台阶](../../2021/11/剑指Offer_1002_简单_跳台阶.md)  
> [[简单, 剑指Offer] 连续子数组的最大和](../../2021/12/剑指Offer_4200_简单_连续子数组的最大和.md)  
> [[简单, 华为机试] 放苹果](../05/华为机试_061_简单_放苹果.md)  
> [[简单, 牛客] 兑换零钱(一)](../05/牛客_0126_简单_兑换零钱(一).md)  
> [[简单, 牛客] 斐波那契数列](../03/牛客_0065_简单_斐波那契数列.md)  
> [[简单, 牛客] 求路径](../02/牛客_0034_简单_求路径.md)  
> [[简单, 牛客] 跳台阶](../03/牛客_0068_简单_跳台阶.md)  
> [[简单, 牛客] 连续子数组的最大和](../01/牛客_0019_简单_连续子数组的最大和.md)  
  > 

</details>

<details><summary><b>栈/队列 (15)</b></summary>

> [[中等, 剑指Offer] 栈的压入、弹出序列 🔥](../../2021/11/剑指Offer_3100_中等_栈的压入、弹出序列.md)  
> [[中等, 剑指Offer] 队列的最大值](../01/剑指Offer_5902_中等_队列的最大值.md)  
> [[中等, 牛客] 按之字形顺序打印二叉树](../01/牛客_0014_中等_按之字形顺序打印二叉树.md)  
> [[中等, 牛客] 栈和排序 🔥](../05/牛客_0115_中等_栈和排序.md)  
  > 
> [[困难, 牛客] 最长的括号子串](../03/牛客_0049_困难_最长的括号子串.md)  
  > 
> [[简单, LeetCode] 有效的括号 🔥](../03/LeetCode_0020_简单_有效的括号.md)  
> [[简单, 剑指Offer] 从尾到头打印链表](../../2021/11/剑指Offer_0600_简单_从尾到头打印链表.md)  
> [[简单, 剑指Offer] 包含min函数的栈](../../2021/11/剑指Offer_3000_简单_包含min函数的栈.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](../../2021/11/剑指Offer_3201_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](../../2021/11/剑指Offer_3202_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树 (之字形遍历)](../../2021/11/剑指Offer_3203_简单_层序遍历二叉树(之字形遍历).md)  
> [[简单, 剑指Offer] 用两个栈实现队列](../../2021/11/剑指Offer_0900_简单_用两个栈实现队列.md)  
> [[简单, 牛客] 包含min函数的栈](../04/牛客_0090_简单_包含min函数的栈.md)  
> [[简单, 牛客] 有效括号序列](../03/牛客_0052_简单_有效括号序列.md)  
> [[简单, 牛客] 用两个栈实现队列](../03/牛客_0076_简单_用两个栈实现队列.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
