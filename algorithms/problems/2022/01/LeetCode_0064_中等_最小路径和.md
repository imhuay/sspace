## 最小路径和
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#动态规划)
<!--END_SECTION:badge-->
<!--info
tags: [动态规划]
source: LeetCode
level: 中等
number: '0064'
name: 最小路径和
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定一个非负整数的 m x n 网格 grid, 请找出一条从左上角到右下角的路径, 使得路径上的数字总和为最小.

说明: 每次只能向下或者向右移动一步.
```
> [64. 最小路径和 - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/minimum-path-sum/)

<details><summary><b>详细描述</b></summary>

```txt
给定一个包含非负整数的 m x n 网格 grid , 请找出一条从左上角到右下角的路径, 使得路径上的数字总和为最小.

说明: 每次只能向下或者向右移动一步.

示例 1:
    输入: grid = [[1,3,1],[1,5,1],[4,2,1]]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小.
示例 2:
    输入: grid = [[1,2,3],[4,5,6]]
    输出: 12

提示:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路: 动态规划</b></summary>

<details><summary><b>Python</b></summary>

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        # 初始化
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]
```

</details>

**空间优化**: 展开循环可以发现, 内循环每次遍历实际只会用到上一层的和当前层左边的结果 (详见代码);

<details><summary><b>Python</b></summary>

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        m, n = len(grid), len(grid[0])
        dp = [0] * n

        # 初始化
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]

        # print(dp)
        for i in range(1, m):
            dp[0] = dp[0] + grid[i][0]  # 初始化每一层最左边的结果
            for j in range(1, n):
                # dp[j - 1] + grid[i][j] 表示从左边移动
                # dp[j] + grid[i][j] 表示从上方移动
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]

        return dp[-1]

```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  

<details><summary><b>其他算法笔记</b></summary>

- [二分查找相关](../../../../notes/_archives/2025/10/二分查找备忘.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>动态规划 (59)</b></summary>

> [[中等, LeetCode] 一和零](../06/LeetCode_0474_中等_一和零.md)  
> [[中等, LeetCode] 三角形最小路径和](../06/LeetCode_0120_中等_三角形最小路径和.md)  
> [[中等, LeetCode] 不同的二叉搜索树](../03/LeetCode_0096_中等_不同的二叉搜索树.md)  
> [[中等, LeetCode] 乘积最大子数组](../06/LeetCode_0152_中等_乘积最大子数组.md)  
> [[中等, LeetCode] 买卖股票的最佳时机 (含冷冻期)](../../2025/11/LeetCode_0309_中等_买卖股票的最佳时机(含冷冻期).md)  
> [[中等, LeetCode] 买卖股票的最佳时机 II (不限交易次数) 🔥](../06/LeetCode_0122_中等_买卖股票的最佳时机II(不限交易次数).md)  
> [[中等, LeetCode] 多边形三角剖分的最低得分](../../2025/11/LeetCode_1039_中等_多边形三角剖分的最低得分.md)  
> [[中等, LeetCode] 完全平方数](../02/LeetCode_0279_中等_完全平方数.md)  
> [[中等, LeetCode] 打家劫舍](../06/LeetCode_0198_中等_打家劫舍.md)  
> [[中等, LeetCode] 打家劫舍II](../06/LeetCode_0213_中等_打家劫舍II.md)  
> [[中等, LeetCode] 整数拆分](../../2021/12/LeetCode_0343_中等_整数拆分.md)  
> [[中等, LeetCode] 施咒的最大总伤害](../../2025/10/LeetCode_3186_中等_施咒的最大总伤害.md)  
> [[中等, LeetCode] 最长公共子序列](../../2025/11/LeetCode_1143_中等_最长公共子序列.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 最长回文子序列](../../2025/11/LeetCode_0516_中等_最长回文子序列.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, LeetCode] 目标和](../../2025/12/LeetCode_0494_中等_目标和.md)  
> [[中等, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_中等_编辑距离.md)  
> [[中等, LeetCode] 解码方法](../02/LeetCode_0091_中等_解码方法.md)  
> [[中等, LeetCode] 零钱兑换 (完全背包)](../06/LeetCode_0322_中等_零钱兑换(完全背包).md)  
> [[中等, LeetCode] 零钱兑换II](../06/LeetCode_0518_中等_零钱兑换II.md)  
> [[中等, 剑指Offer] n个骰子的点数](剑指Offer_6000_中等_n个骰子的点数.md)  
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
> [[困难, LeetCode] 买卖股票的最佳时机 IV (至多交易 K 次)](../../2025/11/LeetCode_0188_困难_买卖股票的最佳时机IV(至多交易K次).md)  
> [[困难, LeetCode] 买卖股票的最佳时机III](../06/LeetCode_0123_困难_买卖股票的最佳时机III.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](LeetCode_0010_困难_正则表达式匹配.md)  
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
<!--END_SECTION:relate_problem-->
