## 不同的二叉搜索树
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#动态规划)
<!--END_SECTION:badge-->
<!--info
tags: [动态规划]
source: LeetCode
level: 中等
number: '0096'
name: 不同的二叉搜索树
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给你一个整数 n , 求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种? 返回满足题意的二叉搜索树的种数.
```
> [96. 不同的二叉搜索树 - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/unique-binary-search-trees/)

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->


<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路: 动态规划</b></summary>

- 对一个有序数组, 无论值是多少, 它能构成的方法数都是一样的;
- 对一个长度为 `n` 的有序数组, 取第 `i` 个值作为根节点, 分成左右两个规模分别为 `l=i-1` 和 `r=n-i` 的子问题;
    - 则选择该节点作为根节点的方法数 `=` 左子树的方法数 `*` 右子树的方法数;
    - 得递推公式: `dp(n) = sum( dp(i-1) * dp(n-i) )`, 其中 `i in [1, n+1)`;
- 实际上本题就是一个卡特兰数的实例;

<details><summary><b>Python: 递归写法</b></summary>

```python
class Solution:
    def numTrees(self, n: int) -> int:

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(n):
            if n in (0, 1): return 1

            ret = 0
            for i in range(1, n + 1):   # 选择第 i 个数字作为根节点
                l, r = i - 1, n - i     # 此时左右子树的节点个数
                ret += dp(l) * dp(r)    # 左边 l 个节点的方法数 * 右边 r 个节点的方法数
            return ret

        return dp(n)
```

</details>


<details><summary><b>Python: 迭代写法 (略) </b></summary>

```python
```

</details>


<!--START_SECTION:relate_problem-->
---

### 相关主题

<details><summary><b>动态规划</b></summary>

> [[中等, LeetCode] 一和零](../06/LeetCode_0474_中等_一和零.md)  
> [[中等, LeetCode] 三角形最小路径和](../06/LeetCode_0120_中等_三角形最小路径和.md)  
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
> [[中等, 牛客] 丑数](牛客_0079_中等_丑数.md)  
> [[中等, 牛客] 丢棋子问题 (鹰蛋问题) 🔥](../04/牛客_0087_中等_丢棋子问题(鹰蛋问题).md)  
> [[中等, 牛客] 把数字翻译成字符串](../05/牛客_0116_中等_把数字翻译成字符串.md)  
> [[中等, 牛客] 最大正方形](../04/牛客_0108_中等_最大正方形.md)  
> [[中等, 牛客] 最长公共子串](../05/牛客_0127_中等_最长公共子串.md)  
> [[中等, 牛客] 最长公共子序列(二) 🔥](../04/牛客_0092_中等_最长公共子序列(二).md)  
> [[中等, 牛客] 最长回文子串](../01/牛客_0017_中等_最长回文子串.md)  
> [[中等, 牛客] 矩阵的最小路径和](牛客_0059_中等_矩阵的最小路径和.md)  
> [[中等, 牛客] 连续子数组的最大乘积](../04/牛客_0083_中等_连续子数组的最大乘积.md)  
  > 
> [[困难, LeetCode] 买卖股票的最佳时机III](../06/LeetCode_0123_困难_买卖股票的最佳时机III.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 正则表达式匹配](../../2021/11/剑指Offer_1900_困难_正则表达式匹配.md)  
> [[困难, 牛客] 最长上升子序列(三)](../04/牛客_0091_困难_最长上升子序列(三).md)  
> [[困难, 牛客] 正则表达式匹配](../05/牛客_0122_困难_正则表达式匹配.md)  
> [[困难, 牛客] 编辑距离(二)](../02/牛客_0035_困难_编辑距离(二).md)  
> [[困难, 牛客] 通配符匹配](牛客_0044_困难_通配符匹配.md)  
  > 
> [[简单, LeetCode] 买卖股票的最佳时机](../06/LeetCode_0121_简单_买卖股票的最佳时机.md)  
> [[简单, LeetCode] 最大子数组和](../01/LeetCode_0053_简单_最大子数组和.md)  
> [[简单, LeetCode] 爬楼梯](../01/LeetCode_0070_简单_爬楼梯.md)  
> [[简单, 剑指Offer] 斐波那契数列](../../2021/11/剑指Offer_1001_简单_斐波那契数列.md)  
> [[简单, 剑指Offer] 跳台阶](../../2021/11/剑指Offer_1002_简单_跳台阶.md)  
> [[简单, 剑指Offer] 连续子数组的最大和](../../2021/12/剑指Offer_4200_简单_连续子数组的最大和.md)  
> [[简单, 华为机试] 放苹果](../05/华为机试_061_简单_放苹果.md)  
> [[简单, 牛客] 兑换零钱(一)](../05/牛客_0126_简单_兑换零钱(一).md)  
> [[简单, 牛客] 斐波那契数列](牛客_0065_简单_斐波那契数列.md)  
> [[简单, 牛客] 求路径](../02/牛客_0034_简单_求路径.md)  
> [[简单, 牛客] 跳台阶](牛客_0068_简单_跳台阶.md)  
> [[简单, 牛客] 连续子数组的最大和](../01/牛客_0019_简单_连续子数组的最大和.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
