## 剪绳子 (整数拆分)
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-23%2002%3A03%3A22&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#动态规划)
[![](https://img.shields.io/static/v1?label=&message=%E6%95%B0%E5%AD%A6&color=blue&style=flat-square)](../../../README.md#数学)
[![](https://img.shields.io/static/v1?label=&message=%E8%B4%AA%E5%BF%83&color=blue&style=flat-square)](../../../README.md#贪心)
<!--END_SECTION:badge-->
<!--info
tags: [动态规划, 贪心, 数学]
source: 剑指Offer
level: 中等
number: '1401'
name: 剪绳子 (整数拆分)
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定一个正整数 n, 将其拆分为至少两个正整数的和, 使这些整数的乘积最大化. 返回最大乘积.
```

<details><summary><b>详细描述</b></summary>

```txt
给你一根长度为 n 的绳子, 请把绳子剪成整数长度的 m 段 (m、n都是整数, n>1并且m>1), 每段绳子的长度记为 k[0],k[1]...k[m-1] . 请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少? 例如, 当绳子的长度是8时, 我们把它剪成长度分别为2、3、3的三段, 此时得到的最大乘积是18.

示例 1:
    输入: 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:
    输入: 10
    输出: 36
    解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示:
    2 <= n <= 58

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<summary><b>思路1: 动态规划</b></summary>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

- 在不使用任何数学结论的前提下, 可以把本题当做纯 dp 来做:

<details><summary><b>Python (写法1) </b></summary>

> LeetCode 官方题解中的写法: [整数拆分](https://leetcode-cn.com/problems/integer-break/solution/zheng-shu-chai-fen-by-leetcode-solution/)

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            for j in range(1, i):
                # 状态定义: dp[i] 表示长度为 i 并拆分成至少两个正整数后的最大乘积 (i>=1)
                #   j * (i - j)   表示将 i 拆分成 j 和 i-j, 且 i-j 不再拆分
                #   j * dp[i - j] 表示将 i 拆分成 j 和 i-j, 且 i-j 会继续拆分, dp[i-j] 即为继续拆分的最优结果 (最优子结构)
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))

        return dp[n]
```

</details>

<details><summary><b>Python (写法2, 推荐) </b></summary>

> 《剑指Offer》中的写法

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        # 对于 n = 2、3 的情况, 直接硬编码
        if n == 2:
            return 1
        if n == 3:
            return 2

        # 状态定义: dp[i] 表示长度为 i 并拆分成至少两个正整数后的最大乘积 (i>3)
        #   当 i <= 3 时, 不满足该定义, 此时不拆效率最高
        #   初始状态 (dp[0] 仅用于占位)
        dp = [0,1,2,3] + [0] * (n - 3)

        for i in range(4, n + 1):
            for j in range(2, i):
                dp[i] = max(dp[i], dp[i-j] * dp[j])

        return dp[n]
```

</details>


<summary><b>思路2: 数学/贪心</b></summary>

- 数学上可证: 尽可能按长度为 3 切, 如果剩余 4, 则按 2、2 切;
  > 证明见: [剪绳子1 (数学推导 / 贪心思想, 清晰图解) ](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/)

- **简述**: 当 `x >= 4` 时, 有 `2(x-2) = 2x - 4 >= x`; 简言之, 对任意大于等于 4 的因子, 都可以拆成 2 和 x-2 而不损失性能; 因此只需考虑拆成 2 或 3 两种情况 (1除外); 而由于 `2*2 > 3*1` 和 `3*3 > 2*2*2`, 可知最多使用两个 2;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        import math
        if n <= 3:
            return n - 1

        a, b = n // 3, n % 3
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        elif b == 2:
            return int(math.pow(3, a) * 2)
        else:
            return int(math.pow(3, a))
```

</details>


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


<details><summary><b>动态规划 (52)</b></summary>

> [[中等, LeetCode] 一和零](../../2022/06/LeetCode_0474_中等_一和零.md)  
> [[中等, LeetCode] 三角形最小路径和](../../2022/06/LeetCode_0120_中等_三角形最小路径和.md)  
> [[中等, LeetCode] 不同的二叉搜索树](../../2022/03/LeetCode_0096_中等_不同的二叉搜索树.md)  
> [[中等, LeetCode] 乘积最大子数组](../../2022/06/LeetCode_0152_中等_乘积最大子数组.md)  
> [[中等, LeetCode] 买卖股票的最佳时机II 🔥](../../2022/06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 完全平方数](../../2022/02/LeetCode_0279_中等_完全平方数.md)  
> [[中等, LeetCode] 打家劫舍](../../2022/06/LeetCode_0198_中等_打家劫舍.md)  
> [[中等, LeetCode] 打家劫舍II](../../2022/06/LeetCode_0213_中等_打家劫舍II.md)  
> [[中等, LeetCode] 整数拆分](../12/LeetCode_0343_中等_整数拆分.md)  
> [[中等, LeetCode] 最小路径和](../../2022/01/LeetCode_0064_中等_最小路径和.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../../2022/06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, LeetCode] 解码方法](../../2022/02/LeetCode_0091_中等_解码方法.md)  
> [[中等, LeetCode] 零钱兑换](../../2022/06/LeetCode_0322_中等_零钱兑换.md)  
> [[中等, LeetCode] 零钱兑换II](../../2022/06/LeetCode_0518_中等_零钱兑换II.md)  
> [[中等, 剑指Offer] n个骰子的点数](../../2022/01/剑指Offer_6000_中等_n个骰子的点数.md)  
> [[中等, 剑指Offer] 丑数 🔥](../12/剑指Offer_4900_中等_丑数.md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](../../2022/01/剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 剑指Offer] 斐波那契数列-3 (把数字翻译成字符串)](../12/剑指Offer_4600_中等_斐波那契数列-3(把数字翻译成字符串).md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 剑指Offer] 礼物的最大价值](../12/剑指Offer_4700_中等_礼物的最大价值.md)  
> [[中等, 牛客] 01背包 🔥](../../2022/05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 丑数](../../2022/03/牛客_0079_中等_丑数.md)  
> [[中等, 牛客] 丢棋子问题 (鹰蛋问题) 🔥](../../2022/04/牛客_0087_中等_丢棋子问题(鹰蛋问题).md)  
> [[中等, 牛客] 把数字翻译成字符串](../../2022/05/牛客_0116_中等_把数字翻译成字符串.md)  
> [[中等, 牛客] 最大正方形](../../2022/04/牛客_0108_中等_最大正方形.md)  
> [[中等, 牛客] 最长公共子串](../../2022/05/牛客_0127_中等_最长公共子串.md)  
> [[中等, 牛客] 最长公共子序列(二) 🔥](../../2022/04/牛客_0092_中等_最长公共子序列(二).md)  
> [[中等, 牛客] 最长回文子串](../../2022/01/牛客_0017_中等_最长回文子串.md)  
> [[中等, 牛客] 矩阵的最小路径和](../../2022/03/牛客_0059_中等_矩阵的最小路径和.md)  
> [[中等, 牛客] 连续子数组的最大乘积](../../2022/04/牛客_0083_中等_连续子数组的最大乘积.md)  
  > 
> [[困难, LeetCode] 买卖股票的最佳时机III](../../2022/06/LeetCode_0123_困难_买卖股票的最佳时机III.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../../2022/10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../../2022/01/LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, LeetCode] 编辑距离 🔥](../../2022/06/LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 正则表达式匹配](剑指Offer_1900_困难_正则表达式匹配.md)  
> [[困难, 牛客] 最长上升子序列(三)](../../2022/04/牛客_0091_困难_最长上升子序列(三).md)  
> [[困难, 牛客] 正则表达式匹配](../../2022/05/牛客_0122_困难_正则表达式匹配.md)  
> [[困难, 牛客] 编辑距离(二)](../../2022/02/牛客_0035_困难_编辑距离(二).md)  
> [[困难, 牛客] 通配符匹配](../../2022/03/牛客_0044_困难_通配符匹配.md)  
  > 
> [[简单, LeetCode] 买卖股票的最佳时机](../../2022/06/LeetCode_0121_简单_买卖股票的最佳时机.md)  
> [[简单, LeetCode] 最大子数组和](../../2022/01/LeetCode_0053_简单_最大子数组和.md)  
> [[简单, LeetCode] 爬楼梯](../../2022/01/LeetCode_0070_简单_爬楼梯.md)  
> [[简单, 剑指Offer] 斐波那契数列](剑指Offer_1001_简单_斐波那契数列.md)  
> [[简单, 剑指Offer] 跳台阶](剑指Offer_1002_简单_跳台阶.md)  
> [[简单, 剑指Offer] 连续子数组的最大和](../12/剑指Offer_4200_简单_连续子数组的最大和.md)  
> [[简单, 华为机试] 放苹果](../../2022/05/华为机试_061_简单_放苹果.md)  
> [[简单, 牛客] 兑换零钱(一)](../../2022/05/牛客_0126_简单_兑换零钱(一).md)  
> [[简单, 牛客] 斐波那契数列](../../2022/03/牛客_0065_简单_斐波那契数列.md)  
> [[简单, 牛客] 求路径](../../2022/02/牛客_0034_简单_求路径.md)  
> [[简单, 牛客] 跳台阶](../../2022/03/牛客_0068_简单_跳台阶.md)  
> [[简单, 牛客] 连续子数组的最大和](../../2022/01/牛客_0019_简单_连续子数组的最大和.md)  
  > 

</details>

<details><summary><b>数学 (8)</b></summary>

> [[中等, Collection] 划分2N个点](../../2022/01/Collection_20220126_中等_划分2N个点.md)  
> [[中等, LeetCode] 整数拆分](../12/LeetCode_0343_中等_整数拆分.md)  
> [[中等, 剑指Offer] 剪绳子](剑指Offer_1402_中等_剪绳子.md)  
> [[中等, 牛客] 阶乘末尾0的数量](../../2022/05/牛客_0129_中等_阶乘末尾0的数量.md)  
  > 
> [[简单, LeetCode] 排列硬币](../10/LeetCode_0441_简单_排列硬币.md)  
> [[简单, 牛客] 三个数的最大乘积](../../2022/04/牛客_0106_简单_三个数的最大乘积.md)  
> [[简单, 牛客] 回文数字](../../2022/03/牛客_0056_简单_回文数字.md)  
> [[简单, 牛客] 进制转换](../../2022/04/牛客_0112_简单_进制转换.md)  
  > 

</details>

<details><summary><b>贪心 (4)</b></summary>

> [[中等, LeetCode] 买卖股票的最佳时机II 🔥](../../2022/06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../../2022/06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, 牛客] 分糖果问题](../../2022/05/牛客_0130_中等_分糖果问题.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
