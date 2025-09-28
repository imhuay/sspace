## 一和零
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#动态规划)
[![](https://img.shields.io/static/v1?label=&message=%E6%9A%B4%E5%8A%9B%E9%80%92%E5%BD%92%E4%B8%8E%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#暴力递归与动态规划)
<!--END_SECTION:badge-->
<!--info
tags: [dfs2dp]
source: LeetCode
level: 中等
number: '0474'
name: 一和零
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给你一个二进制字符串数组 strs 和两个整数 m 和 n .
请你找出并返回 strs 的最大子集的长度, 该子集中 最多 有 m 个 0 和 n 个 1 .
如果 x 的所有元素也是 y 的元素, 集合 x 是集合 y 的 子集 .
```
> [474. 一和零 - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/ones-and-zeroes/)

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->


<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路: 自底向上递归+记忆化搜索</b></summary>

- 定义 `dfs(i, rest_z, rest_o)` 表示剩余容量为 `rest_z`, `rest_o` 情况下, 前 `i` 个元素的最大子集长度 (子问题);
- 【递归基】显然 `i=0` 时, 返回 `0`;
- 然后分是否加入当前元素, 返回其中的最大值;
- 记得预处理所有字符串;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        from functools import lru_cache

        def get_zo(s):
            z, o = 0, 0
            for c in s:
                if c == '0': z += 1
                else: o += 1
            return z, o

        # 预处理
        tb = dict()
        for s in strs:
            tb[s] = get_zo(s)

        @lru_cache(maxsize=None)
        def dfs(i, rest_z, rest_o):  # 剩余容量为 rest_z, rest_o 情况下, strs[:i] 下的最大子集长度
            if i == 0:
                return 0

            c1 = dfs(i - 1, rest_z, rest_o)  # 不要
            c2 = 0
            z, o = tb[strs[i - 1]]
            if rest_z >= z and rest_o >= o:  # 要
                c2 = dfs(i - 1, rest_z - z, rest_o - o) + 1

            return max(c1, c2)

        N = len(strs)
        return dfs(N, m, n)
```

</details>

**优化**: 通过递归转动态规划
> 实际上, 记忆化搜索的速度要更快;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        from functools import lru_cache

        def get_zo(s):
            z, o = 0, 0
            for c in s:
                if c == '0': z += 1
                else: o += 1
            return z, o

        N = len(strs)
        # 预处理
        tb = dict()
        for s in strs:
            tb[s] = get_zo(s)

        # dp[N][m][n]
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(N + 1)]

        for i in range(1, N + 1):
            for rest_z in range(m + 1):
                for rest_o in range(n + 1):
                    c1 = dp[i - 1][rest_z][rest_o]
                    c2 = 0
                    z, o = tb[strs[i - 1]]
                    if rest_z >= z and rest_o >= o:
                        c2 = dp[i - 1][rest_z - z][rest_o - o] + 1
                    dp[i][rest_z][rest_o] = max(c1, c2)

        return dp[N][m][n]
```

</details>


**空间优化** (略)
> [【宫水三叶】详解如何转换「背包问题」, 以及逐步空间优化 - 一和零 - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/ones-and-zeroes/solution/gong-shui-san-xie-xiang-jie-ru-he-zhuan-174wv/)

<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>动态规划</b></summary>

> [[中等, LeetCode] 三角形最小路径和](LeetCode_0120_中等_三角形最小路径和.md)  
> [[中等, LeetCode] 不同的二叉搜索树](../03/LeetCode_0096_中等_不同的二叉搜索树.md)  
> [[中等, LeetCode] 乘积最大子数组](LeetCode_0152_中等_乘积最大子数组.md)  
> [[中等, LeetCode] 买卖股票的最佳时机II 🔥](LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 完全平方数](../02/LeetCode_0279_中等_完全平方数.md)  
> [[中等, LeetCode] 打家劫舍](LeetCode_0198_中等_打家劫舍.md)  
> [[中等, LeetCode] 打家劫舍II](LeetCode_0213_中等_打家劫舍II.md)  
> [[中等, LeetCode] 整数拆分](../../2021/12/LeetCode_0343_中等_整数拆分.md)  
> [[中等, LeetCode] 最小路径和](../01/LeetCode_0064_中等_最小路径和.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, LeetCode] 解码方法](../02/LeetCode_0091_中等_解码方法.md)  
> [[中等, LeetCode] 零钱兑换](LeetCode_0322_中等_零钱兑换.md)  
> [[中等, LeetCode] 零钱兑换II](LeetCode_0518_中等_零钱兑换II.md)  
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
> [[困难, LeetCode] 买卖股票的最佳时机III](LeetCode_0123_困难_买卖股票的最佳时机III.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, LeetCode] 编辑距离 🔥](LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 正则表达式匹配](../../2021/11/剑指Offer_1900_困难_正则表达式匹配.md)  
> [[困难, 牛客] 最长上升子序列(三)](../04/牛客_0091_困难_最长上升子序列(三).md)  
> [[困难, 牛客] 正则表达式匹配](../05/牛客_0122_困难_正则表达式匹配.md)  
> [[困难, 牛客] 编辑距离(二)](../02/牛客_0035_困难_编辑距离(二).md)  
> [[困难, 牛客] 通配符匹配](../03/牛客_0044_困难_通配符匹配.md)  
  > 
> [[简单, LeetCode] 买卖股票的最佳时机](LeetCode_0121_简单_买卖股票的最佳时机.md)  
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
<details><summary><b>暴力递归与动态规划</b></summary>

> [[中等, LeetCode] 完全平方数](../02/LeetCode_0279_中等_完全平方数.md)  
> [[中等, LeetCode] 打家劫舍](LeetCode_0198_中等_打家劫舍.md)  
> [[中等, LeetCode] 解码方法](../02/LeetCode_0091_中等_解码方法.md)  
> [[中等, LeetCode] 零钱兑换](LeetCode_0322_中等_零钱兑换.md)  
> [[中等, 剑指Offer] n个骰子的点数](../01/剑指Offer_6000_中等_n个骰子的点数.md)  
> [[中等, 牛客] 01背包 🔥](../05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 最长公共子串](../05/牛客_0127_中等_最长公共子串.md)  
  > 
> [[困难, 牛客] 编辑距离(二)](../02/牛客_0035_困难_编辑距离(二).md)  
> [[困难, 牛客] 通配符匹配](../03/牛客_0044_困难_通配符匹配.md)  
  > 
> [[简单, LeetCode] 爬楼梯](../01/LeetCode_0070_简单_爬楼梯.md)  
  > 

</details>
<!--END_SECTION:relate-->