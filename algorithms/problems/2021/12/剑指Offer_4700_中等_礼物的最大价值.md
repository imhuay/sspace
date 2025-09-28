## 礼物的最大价值
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#动态规划)
<!--END_SECTION:badge-->
<!--info
tags: [动态规划]
source: 剑指Offer
level: 中等
number: '4700'
name: 礼物的最大价值
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定 m*n 的整型数组 grid, 求从左上角到右下角路线中和的最大值 (每次向下或向右移动一格)

示例输入:
    [1,3,1]
    [1,5,1]
    [4,2,1]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
```

<details><summary><b>详细描述</b></summary>

```txt
在一个 m*n 的棋盘的每一格都放有一个礼物, 每个礼物都有一定的价值 (价值大于 0). 你可以从棋盘的左上角开始拿格子里的礼物, 并每次向右或者向下移动一格、直到到达棋盘的右下角. 给定一个棋盘及其上面的礼物的价值, 请计算你最多能拿到多少价值的礼物?

示例 1:
    输入:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 12
    解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

提示:
    0 < grid.length <= 200
    0 < grid[0].length <= 200

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<summary><b>思路: 动态规划</b></summary>

**状态定义**
- 记 `dp[i][j] := 从左上角走至 (i,j) 位置时的最大值`

**转移方程**
- `dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]`

**初始状态**
- `dp[i][0] = sum(grid[:i][0])`
- `dp[0][j] = sum(grid[0][:j])`


<details><summary><b>Python: 本地修改</b></summary>

因为 `dp[i][j]` 只与 `dp[i-1][j]` 和 `dp[i][j-1]` 有关, 因此可以直接将 grid 作为 dp 矩阵, 原地修改;
> [题解: 礼物的最大价值 (动态规划, 清晰图解) ](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/solution/mian-shi-ti-47-li-wu-de-zui-da-jie-zhi-dong-tai-gu/)

```python
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 初始化
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])

        return grid[-1][-1]
```

</details>


<details><summary><b>Python: 非本地修改, 优化空间复杂度</b></summary>

<br/>因为不存在回溯 (每次只能向下或向右), 所以只需要保存上一行 (或上一列) 的结果即可;

**状态定义**
- 记 `dp[j] := 从左上角走至 (i,j) 位置时的最大值`

**转移方程**
- `dp[j] = max(dp[j-1], dp[j]) + grid[i][j]`

    ```
    dp[j-1] + grid[i][j] 表示路线为 grid[i-1][j-1] → grid[i-1][j] → grid[i][j], 即先往右再向下
    dp[j]   + grid[i][j] 表示路线为 grid[i-1][j-1] → grid[i][j-1] → grid[i][j], 即先向下再往右
    然后选择这两条路线中较大的更新 dp[j]
    ```

**初始状态**
- `dp[j] = sum(grid[0][:j])`

```python
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0

        m, n = len(grid), len(grid[0])

        # 初始化第一行的结果
        dp = [grid[0][0]] + [0] * (n - 1)
        for i in range(1, n):
            dp[i] = dp[i - 1] + grid[0][i]

        for i in range(1, m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                # dp[j-1] + grid[i][j] 表示 grid[i-1][j-1] → grid[i][j-1] → grid[i][j]
                # dp[j]   + grid[i][j] 表示 grid[i-1][j-1] → grid[i-1][j] → grid[i][j]
                # 然后选择这两条路线中较大的更新 dp[j]
                dp[j] = max(dp[j-1], dp[j]) + grid[i][j]

        return dp[n-1]
```

</details>
<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>动态规划</b></summary>

> [[中等, LeetCode] 一和零](../../2022/06/LeetCode_0474_中等_一和零.md)  
> [[中等, LeetCode] 三角形最小路径和](../../2022/06/LeetCode_0120_中等_三角形最小路径和.md)  
> [[中等, LeetCode] 不同的二叉搜索树](../../2022/03/LeetCode_0096_中等_不同的二叉搜索树.md)  
> [[中等, LeetCode] 乘积最大子数组](../../2022/06/LeetCode_0152_中等_乘积最大子数组.md)  
> [[中等, LeetCode] 买卖股票的最佳时机II 🔥](../../2022/06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 完全平方数](../../2022/02/LeetCode_0279_中等_完全平方数.md)  
> [[中等, LeetCode] 打家劫舍](../../2022/06/LeetCode_0198_中等_打家劫舍.md)  
> [[中等, LeetCode] 打家劫舍II](../../2022/06/LeetCode_0213_中等_打家劫舍II.md)  
> [[中等, LeetCode] 整数拆分](LeetCode_0343_中等_整数拆分.md)  
> [[中等, LeetCode] 最小路径和](../../2022/01/LeetCode_0064_中等_最小路径和.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../../2022/06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, LeetCode] 解码方法](../../2022/02/LeetCode_0091_中等_解码方法.md)  
> [[中等, LeetCode] 零钱兑换](../../2022/06/LeetCode_0322_中等_零钱兑换.md)  
> [[中等, LeetCode] 零钱兑换II](../../2022/06/LeetCode_0518_中等_零钱兑换II.md)  
> [[中等, 剑指Offer] n个骰子的点数](../../2022/01/剑指Offer_6000_中等_n个骰子的点数.md)  
> [[中等, 剑指Offer] 丑数 🔥](剑指Offer_4900_中等_丑数.md)  
> [[中等, 剑指Offer] 剪绳子 (整数拆分)](../11/剑指Offer_1401_中等_剪绳子(整数拆分).md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](../../2022/01/剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 剑指Offer] 斐波那契数列-3 (把数字翻译成字符串)](剑指Offer_4600_中等_斐波那契数列-3(把数字翻译成字符串).md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
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
> [[困难, 剑指Offer] 正则表达式匹配](../11/剑指Offer_1900_困难_正则表达式匹配.md)  
> [[困难, 牛客] 最长上升子序列(三)](../../2022/04/牛客_0091_困难_最长上升子序列(三).md)  
> [[困难, 牛客] 正则表达式匹配](../../2022/05/牛客_0122_困难_正则表达式匹配.md)  
> [[困难, 牛客] 编辑距离(二)](../../2022/02/牛客_0035_困难_编辑距离(二).md)  
> [[困难, 牛客] 通配符匹配](../../2022/03/牛客_0044_困难_通配符匹配.md)  
  > 
> [[简单, LeetCode] 买卖股票的最佳时机](../../2022/06/LeetCode_0121_简单_买卖股票的最佳时机.md)  
> [[简单, LeetCode] 最大子数组和](../../2022/01/LeetCode_0053_简单_最大子数组和.md)  
> [[简单, LeetCode] 爬楼梯](../../2022/01/LeetCode_0070_简单_爬楼梯.md)  
> [[简单, 剑指Offer] 斐波那契数列](../11/剑指Offer_1001_简单_斐波那契数列.md)  
> [[简单, 剑指Offer] 跳台阶](../11/剑指Offer_1002_简单_跳台阶.md)  
> [[简单, 剑指Offer] 连续子数组的最大和](剑指Offer_4200_简单_连续子数组的最大和.md)  
> [[简单, 华为机试] 放苹果](../../2022/05/华为机试_061_简单_放苹果.md)  
> [[简单, 牛客] 兑换零钱(一)](../../2022/05/牛客_0126_简单_兑换零钱(一).md)  
> [[简单, 牛客] 斐波那契数列](../../2022/03/牛客_0065_简单_斐波那契数列.md)  
> [[简单, 牛客] 求路径](../../2022/02/牛客_0034_简单_求路径.md)  
> [[简单, 牛客] 跳台阶](../../2022/03/牛客_0068_简单_跳台阶.md)  
> [[简单, 牛客] 连续子数组的最大和](../../2022/01/牛客_0019_简单_连续子数组的最大和.md)  
  > 

</details>
<!--END_SECTION:relate-->