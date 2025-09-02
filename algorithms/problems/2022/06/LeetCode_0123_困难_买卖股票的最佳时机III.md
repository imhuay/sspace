## 买卖股票的最佳时机III
<!--START_SECTION:badge-->

![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&label_color=gray&color=yellow&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&label_color=gray&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&label_color=gray&color=blue&style=flat-square)](../../../README.md#动态规划)

<!--END_SECTION:badge-->
<!--info
tags: [动态规划]
source: LeetCode
level: 困难
number: '0123'
name: 买卖股票的最佳时机III
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
```

<details><summary><b>详细描述</b></summary>

```txt
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
    输入：prices = [3,3,5,0,0,3,1,4]
    输出：6
    解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
        随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2：
    输入：prices = [1,2,3,4,5]
    输出：4
    解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
        注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
        因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3：
    输入：prices = [7,6,4,3,1] 
    输出：0 
    解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
示例 4：
    输入：prices = [1]
    输出：0

提示：
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路：动态规划</b></summary>

- 分别定义前向、后向两个dp，记 `dp_f` 和 `dp_b`，其中：
    - `dp_f[i]` 表示 `prices[:i]` 区间内的买卖一次的最大值；
    - `dp_b[i]` 表示 `prices[i:]` 区间内的买卖一次的最大值；
- 因为可以只交易一次，所以最终结果为 `max(dp_f[-1], max(dp_f[i] + dp_b[i + 1]))`

<details><summary><b>Python</b></summary>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        n = len(prices)
        dp_f = [0] * n
        dp_b = [0] * n

        min_p = prices[0]
        for i in range(1, n):
            dp_f[i] = max(dp_f[i-1], prices[i] - min_p)
            min_p = min(min_p, prices[i])
        
        max_b = 0
        max_p = prices[-1]
        for i in range(n - 2, -1, -1):
            dp_b[i] = max(dp_b[i+1], max_p - prices[i])
            max_p = max(max_p, prices[i])
        
        # print(dp_f, dp_b)
        return max(dp_f[-1], max(dp_f[i] + dp_b[i + 1] for i in range(0, n - 1)))
```

</details>

**空间优化**：官方提供了一种空间复杂度为 `O(1)` 的解法：
> [买卖股票的最佳时机 III - 力扣官方题解](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-iii-by-wrnt/)

<details><summary><b>Python</b></summary>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i] - buy1)
            buy2 = min(buy2, prices[i] - sell1)
            sell2 = max(sell2, prices[i] - buy2)
        return sell2
```

</details>

<!-- 
**空间优化**：通过合理的控制下标，可以用一个循环生成 `dp_f` 和 `dp_b`，这样同时也省去了需要保存历史状态的问题，可以将空间复杂度优化到 `O(1)`

<details><summary><b>Python</b></summary>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        n = len(prices)
        dp_f = [0] * n
        dp_b = [0] * n

        min_p = prices[0]
        for i in range(1, n):
            dp_f[i] = max(dp_f[i-1], prices[i] - min_p)
            min_p = min(min_p, prices[i])
        
        max_b = 0
        max_p = prices[-1]
        for i in range(n - 2, -1, -1):
            dp_b[i] = max(dp_b[i+1], max_p - prices[i])
            max_p = max(max_p, prices[i])
        
        # print(dp_f, dp_b)
        return max(dp_f[-1], max(dp_f[i] + dp_b[i + 1] for i in range(0, n - 1)))
```

</details>

 -->
<!--START_SECTION:relate-->

---

### 相关主题

<details><summary><b>动态规划</b></summary>

> [[中等, LeetCode] 一和零](LeetCode_0474_中等_一和零.md)  
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
> [[中等, 剑指Offer] 剪绳子（整数拆分）](../../2021/11/剑指Offer_1401_中等_剪绳子（整数拆分）.md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字（约瑟夫环问题） 🔥](../01/剑指Offer_6200_中等_圆圈中最后剩下的数字（约瑟夫环问题）.md)  
> [[中等, 剑指Offer] 斐波那契数列-3（把数字翻译成字符串）](../../2021/12/剑指Offer_4600_中等_斐波那契数列-3（把数字翻译成字符串）.md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../../2021/12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 剑指Offer] 礼物的最大价值](../../2021/12/剑指Offer_4700_中等_礼物的最大价值.md)  
> [[中等, 牛客] 01背包 🔥](../05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 丑数](../03/牛客_0079_中等_丑数.md)  
> [[中等, 牛客] 丢棋子问题（鹰蛋问题） 🔥](../04/牛客_0087_中等_丢棋子问题（鹰蛋问题）.md)  
> [[中等, 牛客] 把数字翻译成字符串](../05/牛客_0116_中等_把数字翻译成字符串.md)  
> [[中等, 牛客] 最大正方形](../04/牛客_0108_中等_最大正方形.md)  
> [[中等, 牛客] 最长公共子串](../05/牛客_0127_中等_最长公共子串.md)  
> [[中等, 牛客] 最长公共子序列(二) 🔥](../04/牛客_0092_中等_最长公共子序列(二).md)  
> [[中等, 牛客] 最长回文子串](../01/牛客_0017_中等_最长回文子串.md)  
> [[中等, 牛客] 矩阵的最小路径和](../03/牛客_0059_中等_矩阵的最小路径和.md)  
> [[中等, 牛客] 连续子数组的最大乘积](../04/牛客_0083_中等_连续子数组的最大乘积.md)  
  > 
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

<!--END_SECTION:relate-->