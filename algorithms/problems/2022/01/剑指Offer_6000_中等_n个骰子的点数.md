## n个骰子的点数
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#动态规划)
[![](https://img.shields.io/static/v1?label=&message=%E6%9A%B4%E5%8A%9B%E9%80%92%E5%BD%92%E4%B8%8E%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#暴力递归与动态规划)
<!--END_SECTION:badge-->
<!--info
tags: [动态规划, dfs2dp]
source: 剑指Offer
level: 中等
number: '6000'
name: n个骰子的点数
companies: []
-->

> [剑指 Offer 60. n个骰子的点数 - 力扣 (LeetCode) ](https://leetcode.cn/problems/nge-tou-zi-de-dian-shu-lcof/)

<summary><b>问题简述</b></summary>

```txt
把 n 个骰子扔在地上, 所有骰子朝上一面的点数之和为 s.
输入 n, 打印出 s 的所有可能的值出现的概率 (按 s 从小到大排列).
```

<details><summary><b>详细描述</b></summary>

```txt
把n个骰子扔在地上, 所有骰子朝上一面的点数之和为s. 输入n, 打印出s的所有可能的值出现的概率.

你需要用一个浮点数数组返回答案, 其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率.

示例 1:
    输入: 1
    输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:
    输入: 2
    输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

限制:
    1 <= n <= 11
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1: 从暴力递归到动态规划</b></summary>

- 定义 `dfs(k)` 返回 k 个骰子产生的可能性序列 `dp`, 其中 `dp[i]` 表示 k 个骰子掷出点数 i 的可能数;
- 【递归基】`k=1` 时, `dfs(1)` 返回 `dp = [_, 1, 1, 1, 1, 1, 1]` (为方便编码, `dp[:n]` 为占位符, 无实际意义)
- 递归过程即使用 `dfs(k-1)` 返回的 `dp_pre` 生成 `dfs(k)` 的 `dp`;
- 然后根据暴力递归过程直接写出动态规划的代码 (已经与原问题解耦);

<details><summary><b>Python: 暴力递归</b></summary>

```python
class Solution:
    def dicesProbability(self, n: int) -> List[float]:

        def dfs(k):
            if k == 1:
                return [1] * 7

            dp_pre = dfs(k - 1)
            dp = [0] * (k * 6 + 1)

            # 遍历方式 1 (推荐, 不需要判断范围):
            for i in range(1 * (k - 1), 6 * (k - 1) + 1):  # n - 1 个骰子的点数范围
                for d in range(1, 7):  # 当前骰子掷出的点数
                    dp[i + d] += dp_pre[i]

            # 遍历方式 2:
            # for i in range(1 * k, 6 * k + 1):  # n 个骰子的点数范围
            #     for d in range(1, 7):  # 当前骰子掷出的点数
            #         if 1 * (k - 1) <= i - d <= 6 * (k - 1):  # 边界判断
            #             dp[i] += dp_pre[i - d]

            return dp

        dp = dfs(n)
        return [x / (6 ** n) for x in dp[n:]]
```

</details>

<details><summary><b>Python: 动态规划</b></summary>

```python
class Solution:
    def dicesProbability(self, n: int) -> List[float]:

        dp = [1] * 7

        for k in range(2, n + 1):
            dp_pre = dp
            dp = [0] * (k * 6 + 1)
            for i in range(1 * k, 6 * k + 1):  # n 个骰子的点数范围
                for d in range(1, 7):  # 当前骰子掷出的点数
                    if 1 * (k - 1) <= i - d <= 6 * (k - 1):
                        dp[i] += dp_pre[i - d]

        return [x / (6 ** n) for x in dp[n:]]
```

</details>


<summary><b>思路2: 从 "跳台阶" 理解本题</b></summary>

- "跳台阶" 的递推公式为: `dp[i] = dp[i-1] + dp[i-2]`;
- 在本题中, 可以看做目标台阶数为 `i`, 每次可以跳 `1~6` 步; 对 `k` 个骰子, `i` 的范围为 `k ~ 6*k`, 每次都是从 `n-1` 个骰子的可能性出发;
- 因此本题的递推公式为: `dp[k][i] = dp[k-1][i-1] + dp[k-1][i-2] + .. + dp[k-1][i-6]`;
    - 同时因为每一轮只和上一轮相关, 可以使用两个数组滚动优化空间;
        > 也可以只是用一个数组, 参考: [n个骰子的点数 - 路漫漫我不畏](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/nge-tou-zi-de-dian-shu-dong-tai-gui-hua-ji-qi-yo-3/)
- 代码同上.


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


<details><summary><b>动态规划 (53)</b></summary>

> [[中等, LeetCode] 一和零](../06/LeetCode_0474_中等_一和零.md)  
> [[中等, LeetCode] 三角形最小路径和](../06/LeetCode_0120_中等_三角形最小路径和.md)  
> [[中等, LeetCode] 不同的二叉搜索树](../03/LeetCode_0096_中等_不同的二叉搜索树.md)  
> [[中等, LeetCode] 乘积最大子数组](../06/LeetCode_0152_中等_乘积最大子数组.md)  
> [[中等, LeetCode] 买卖股票的最佳时机II 🔥](../06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 完全平方数](../02/LeetCode_0279_中等_完全平方数.md)  
> [[中等, LeetCode] 打家劫舍](../06/LeetCode_0198_中等_打家劫舍.md)  
> [[中等, LeetCode] 打家劫舍II](../06/LeetCode_0213_中等_打家劫舍II.md)  
> [[中等, LeetCode] 整数拆分](../../2021/12/LeetCode_0343_中等_整数拆分.md)  
> [[中等, LeetCode] 施咒的最大总伤害](../../2025/10/LeetCode_3186_中等_施咒的最大总伤害.md)  
> [[中等, LeetCode] 最小路径和](LeetCode_0064_中等_最小路径和.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, LeetCode] 解码方法](../02/LeetCode_0091_中等_解码方法.md)  
> [[中等, LeetCode] 零钱兑换](../06/LeetCode_0322_中等_零钱兑换.md)  
> [[中等, LeetCode] 零钱兑换II](../06/LeetCode_0518_中等_零钱兑换II.md)  
> [[中等, 剑指Offer] 丑数 🔥](../../2021/12/剑指Offer_4900_中等_丑数.md)  
> [[中等, 剑指Offer] 剪绳子 (整数拆分)](../../2021/11/剑指Offer_1401_中等_剪绳子(整数拆分).md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
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
> [[中等, 牛客] 最长回文子串](牛客_0017_中等_最长回文子串.md)  
> [[中等, 牛客] 矩阵的最小路径和](../03/牛客_0059_中等_矩阵的最小路径和.md)  
> [[中等, 牛客] 连续子数组的最大乘积](../04/牛客_0083_中等_连续子数组的最大乘积.md)  
  > 
> [[困难, LeetCode] 买卖股票的最佳时机III](../06/LeetCode_0123_困难_买卖股票的最佳时机III.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 正则表达式匹配](../../2021/11/剑指Offer_1900_困难_正则表达式匹配.md)  
> [[困难, 牛客] 最长上升子序列(三)](../04/牛客_0091_困难_最长上升子序列(三).md)  
> [[困难, 牛客] 正则表达式匹配](../05/牛客_0122_困难_正则表达式匹配.md)  
> [[困难, 牛客] 编辑距离(二)](../02/牛客_0035_困难_编辑距离(二).md)  
> [[困难, 牛客] 通配符匹配](../03/牛客_0044_困难_通配符匹配.md)  
  > 
> [[简单, LeetCode] 买卖股票的最佳时机](../06/LeetCode_0121_简单_买卖股票的最佳时机.md)  
> [[简单, LeetCode] 最大子数组和](LeetCode_0053_简单_最大子数组和.md)  
> [[简单, LeetCode] 爬楼梯](LeetCode_0070_简单_爬楼梯.md)  
> [[简单, 剑指Offer] 斐波那契数列](../../2021/11/剑指Offer_1001_简单_斐波那契数列.md)  
> [[简单, 剑指Offer] 跳台阶](../../2021/11/剑指Offer_1002_简单_跳台阶.md)  
> [[简单, 剑指Offer] 连续子数组的最大和](../../2021/12/剑指Offer_4200_简单_连续子数组的最大和.md)  
> [[简单, 华为机试] 放苹果](../05/华为机试_061_简单_放苹果.md)  
> [[简单, 牛客] 兑换零钱(一)](../05/牛客_0126_简单_兑换零钱(一).md)  
> [[简单, 牛客] 斐波那契数列](../03/牛客_0065_简单_斐波那契数列.md)  
> [[简单, 牛客] 求路径](../02/牛客_0034_简单_求路径.md)  
> [[简单, 牛客] 跳台阶](../03/牛客_0068_简单_跳台阶.md)  
> [[简单, 牛客] 连续子数组的最大和](牛客_0019_简单_连续子数组的最大和.md)  
  > 

</details>

<details><summary><b>暴力递归与动态规划 (11)</b></summary>

> [[中等, LeetCode] 一和零](../06/LeetCode_0474_中等_一和零.md)  
> [[中等, LeetCode] 完全平方数](../02/LeetCode_0279_中等_完全平方数.md)  
> [[中等, LeetCode] 打家劫舍](../06/LeetCode_0198_中等_打家劫舍.md)  
> [[中等, LeetCode] 施咒的最大总伤害](../../2025/10/LeetCode_3186_中等_施咒的最大总伤害.md)  
> [[中等, LeetCode] 解码方法](../02/LeetCode_0091_中等_解码方法.md)  
> [[中等, LeetCode] 零钱兑换](../06/LeetCode_0322_中等_零钱兑换.md)  
> [[中等, 牛客] 01背包 🔥](../05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 最长公共子串](../05/牛客_0127_中等_最长公共子串.md)  
  > 
> [[困难, 牛客] 编辑距离(二)](../02/牛客_0035_困难_编辑距离(二).md)  
> [[困难, 牛客] 通配符匹配](../03/牛客_0044_困难_通配符匹配.md)  
  > 
> [[简单, LeetCode] 爬楼梯](LeetCode_0070_简单_爬楼梯.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
