## 乘积最大子数组
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
number: '0152'
name: 乘积最大子数组
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定整型数组, 求乘积最大的非空连续子数组, 返回乘积;
```

<details><summary><b>详细描述</b></summary>

```txt
给你一个整数数组 nums, 请你找出数组中乘积最大的连续子数组 (该子数组中至少包含一个数字), 并返回该子数组所对应的乘积.

示例 1:
    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6.
示例 2:
    输入: [-2,0,-1]
    输出: 0
    解释: 结果不能为 2, 因为 [-2,-1] 不是子数组.

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路: 动态规划</b></summary>

- 延续连续子数组最大和的思路, 定义 `dp[i]` 表示以 `nums[i]` 结尾的连续最大乘积;
- 区别在于非0值乘以负数时, 最大值会变最小值, 最小值变最大值;
- 因此可以考虑定义两个 dp: `dp_max[i]` 和 `dp_min[i]` 分别表示最大和最小乘积 (详见代码);
- 本题同样可以使用 "滚动变量" 的方式降低空间复杂度;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ret = dp_max = dp_min = nums[0]
        for x in nums[1:]:
            tmp_mx = dp_max  # 临时变量
            dp_max = max(x, dp_max * x, dp_min * x)
            dp_min = min(x, dp_min * x, tmp_mx * x)
            ret = max(ret, dp_max)

        return ret
```

</details>


<!--START_SECTION:relate_problem-->
---

### 相关主题

<details><summary><b>动态规划</b></summary>

> [[中等, LeetCode] 一和零](LeetCode_0474_中等_一和零.md)  
> [[中等, LeetCode] 三角形最小路径和](LeetCode_0120_中等_三角形最小路径和.md)  
> [[中等, LeetCode] 不同的二叉搜索树](../03/LeetCode_0096_中等_不同的二叉搜索树.md)  
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
<!--END_SECTION:relate_problem-->
