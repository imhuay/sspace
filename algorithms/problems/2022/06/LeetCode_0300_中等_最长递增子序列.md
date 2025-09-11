## 最长递增子序列
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&label_color=gray&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&label_color=gray&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&label_color=gray&color=blue&style=flat-square)](../../../README.md#动态规划)
[![](https://img.shields.io/static/v1?label=&message=%E8%B4%AA%E5%BF%83&label_color=gray&color=blue&style=flat-square)](../../../README.md#贪心)
[![](https://img.shields.io/static/v1?label=&message=%E7%BB%8F%E5%85%B8&label_color=gray&color=blue&style=flat-square)](../../../README.md#经典)
<!--END_SECTION:badge-->
<!--info
tags: [动态规划, 贪心, 经典]
source: LeetCode
level: 中等
number: '0300'
name: 最长递增子序列
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定整数数组 nums, 返回最长严格递增子序列的长度;
进阶:
    你可以设计时间复杂度为 O(N^2) 的解决方案吗?
    你能把时间复杂度降到 O(NlogN) 吗?
```

<details><summary><b>详细描述</b></summary>

```txt
给你一个整数数组 nums , 找到其中最长严格递增子序列的长度.

子序列是由数组派生而来的序列, 删除 (或不删除) 数组中的元素而不改变其余元素的顺序. 例如, [3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列.

示例 1:
    输入: nums = [10,9,2,5,3,7,101,18]
    输出: 4
    解释: 最长递增子序列是 [2,3,7,101], 因此长度为 4 .
示例 2:
    输入: nums = [0,1,0,3,2,3]
    输出: 4
示例 3:
    输入: nums = [7,7,7,7,7,7,7]
    输出: 1

提示:
    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

进阶:
    你可以设计时间复杂度为 O(n2) 的解决方案吗?
    你能将算法的时间复杂度降低到 O(n log(n)) 吗?

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1: 动态规划</b></summary>

**状态定义**: `dp[i]` 表示以 `nums[i]` 结尾的最长递增子序列长度;
> 不能将 `dp[i]` 定义 `nums[:i]` 子数组中的最长递增子序列长度, 虽然这样定义很直观, 但它不满足**最优子结构**的条件, 简单来说, 就是你无法通过 `dp[i-1]` 得到 `dp[i]`.

<details><summary><b>Python</b></summary>

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        ret = 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:  # 如果要求非严格递增, 将 '>' 改为 '>=' 即可
                    dp[i] = max(dp[i], dp[j] + 1)

            ret = max(ret, dp[i])

        return ret
```

</details>

<summary><b>思路2: 优化 dp 的状态定义</b></summary>

- 考虑新的**状态定义**: `dp[i]` 表示长度为 `i + 1` 的最长递增子序列末尾的最小值;
    > `dp` 序列一定时单调递增的, 可用反证法证明, 详见: [最长递增子序列 (动态规划 + 二分查找, 清晰图解) - Krahets](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/)
    >> 该怎么想出这个定义? ——多看多做
- 是否满足**最优子结构**?
    - 即已知 `dp[i - 1]` 能否递推得到 `dp[i]` ; 显然是可以的, 当`nums[i] > dp[i - 1]`时, 长度 `+1`, 否则, 长度不变;
- 如何更新`dp`?
    - 当 `nums[i] > dp[i - 1]` 时, 直接添加到末尾;
    - 否则, 要看是否需要更新 `dp`. 根据 `dp` 递增的性质, 找到 `nums[i]` 在 `dp` 中应该插入的位置, 记 `idx`; 比较 `dp[idx]` 与 `nums[i]` 的大小, 如果 `dp[idx] > nums[i]` 根据定义, 更新 `dp[idx] = nums[i]`;

**从 "贪心" 角度来解释以上过程**: 如果我们要使上升子序列尽可能的长, 则应该让序列上升得尽可能慢, 即每次在上升子序列最后加上的那个数尽可能的小.
> [最长上升子序列 - 力扣官方题解](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/)


<details><summary><b>Python</b></summary>

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        # from bisect import bisect_left

        # 手写二分查找
        def bisect_left(ls, x):
            l, r = 0, len(ls)
            while l < r:
                m = (l + r) // 2
                if ls[m] < x:  # 注意这里要 <, 如果是 <= 就是 bisect_right 了, 不满足题意
                    l = m + 1
                else:
                    r = m
            return l

        dp = [nums[0]]  # dp[i] 表示长度为 (i+1) 的 LIS 的最后一个元素的最小值
        for x in nums[1:]:
            if x > dp[-1]:
                dp.append(x)
            else:
                idx = bisect_left(dp, x)  # 不能使用 bisect/bisect_right
                # if dp[idx] > x:
                #     dp[idx] = x
                dp[idx] = x  # 因为 bisect_left 返回的定义就是 dp[idx] <= x, 所以可以直接赋值

        return len(dp)
```

</details>

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
<details><summary><b>贪心</b></summary>

> [[中等, LeetCode] 买卖股票的最佳时机II 🔥](LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, 剑指Offer] 剪绳子（整数拆分）](../../2021/11/剑指Offer_1401_中等_剪绳子（整数拆分）.md)  
> [[中等, 牛客] 分糖果问题](../05/牛客_0130_中等_分糖果问题.md)  
  > 

</details>
<details><summary><b>经典</b></summary>

> [[中等, LeetCode] 下一个排列 🔥](../10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 二叉树的完全性检验 🔥](../03/LeetCode_0958_中等_二叉树的完全性检验.md)  
> [[中等, 剑指Offer2] 整数除法 🔥](../09/剑指Offer2_001_中等_整数除法.md)  
> [[中等, 剑指Offer] 丑数 🔥](../../2021/12/剑指Offer_4900_中等_丑数.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](../../2021/12/剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字（约瑟夫环问题） 🔥](../01/剑指Offer_6200_中等_圆圈中最后剩下的数字（约瑟夫环问题）.md)  
> [[中等, 剑指Offer] 复杂链表的复制（深拷贝） 🔥](../../2021/12/剑指Offer_3500_中等_复杂链表的复制（深拷贝）.md)  
> [[中等, 剑指Offer] 字符串的排列（全排列） 🔥](../../2021/12/剑指Offer_3800_中等_字符串的排列（全排列）.md)  
> [[中等, 剑指Offer] 把字符串转换成整数 🔥](../01/剑指Offer_6700_中等_把字符串转换成整数.md)  
> [[中等, 剑指Offer] 数值的整数次方（快速幂） 🔥](../../2021/11/剑指Offer_1600_中等_数值的整数次方（快速幂）.md)  
> [[中等, 剑指Offer] 栈的压入、弹出序列 🔥](../../2021/11/剑指Offer_3100_中等_栈的压入、弹出序列.md)  
> [[中等, 剑指Offer] 重建二叉树 🔥](../../2021/11/剑指Offer_0700_中等_重建二叉树.md)  
> [[中等, 剑指Offer] 顺时针打印矩阵（3种思路4个写法） 🔥](../../2021/11/剑指Offer_2900_中等_顺时针打印矩阵（3种思路4个写法）.md)  
> [[中等, 牛客] 01背包 🔥](../05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 丢棋子问题（鹰蛋问题） 🔥](../04/牛客_0087_中等_丢棋子问题（鹰蛋问题）.md)  
> [[中等, 牛客] 字符串的排列 🔥](../05/牛客_0121_中等_字符串的排列.md)  
> [[中等, 牛客] 寻找峰值 🔥](../04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 岛屿数量 🔥](../04/牛客_0109_中等_岛屿数量.md)  
> [[中等, 牛客] 把字符串转换成整数(atoi) 🔥](../04/牛客_0100_中等_把字符串转换成整数(atoi).md)  
> [[中等, 牛客] 数组中只出现一次的两个数字 🔥](../03/牛客_0075_中等_数组中只出现一次的两个数字.md)  
> [[中等, 牛客] 最长公共子序列(二) 🔥](../04/牛客_0092_中等_最长公共子序列(二).md)  
> [[中等, 牛客] 栈和排序 🔥](../05/牛客_0115_中等_栈和排序.md)  
> [[中等, 牛客] 汉诺塔问题 🔥](../03/牛客_0067_中等_汉诺塔问题.md)  
  > 
> [[困难, LeetCode] 编辑距离 🔥](LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 数组中的逆序对 🔥](../01/剑指Offer_5100_困难_数组中的逆序对.md)  
> [[困难, 牛客] 接雨水问题 🔥](../05/牛客_0128_困难_接雨水问题.md)  
> [[困难, 牛客] 设计LFU缓存结构 🔥](../04/牛客_0094_困难_设计LFU缓存结构.md)  
> [[困难, 牛客] 设计LRU缓存结构 🔥](../04/牛客_0093_困难_设计LRU缓存结构.md)  
  > 
> [[简单, LeetCode] 二叉树的最大深度 🔥](../07/LeetCode_0104_简单_二叉树的最大深度.md)  
> [[简单, LeetCode] 反转链表 🔥](../10/LeetCode_0206_简单_反转链表.md)  
> [[简单, 剑指Offer] 二叉搜索树的最近公共祖先 🔥](../01/剑指Offer_6801_简单_二叉搜索树的最近公共祖先.md)  
> [[简单, 剑指Offer] 反转链表 🔥](../../2021/11/剑指Offer_2400_简单_反转链表.md)  
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字（摩尔投票） 🔥](../../2021/12/剑指Offer_3900_简单_数组中出现次数超过一半的数字（摩尔投票）.md)  
> [[简单, 剑指Offer] 最小的k个数（partition操作） 🔥](../../2021/12/剑指Offer_4000_简单_最小的k个数（partition操作）.md)  
> [[简单, 牛客] 二进制中1的个数 🔥](../05/牛客_0120_简单_二进制中1的个数.md)  
> [[简单, 牛客] 单链表的排序 🔥](../03/牛客_0070_简单_单链表的排序.md)  
> [[简单, 牛客] 求平方根 🔥](../02/牛客_0032_简单_求平方根.md)  
  > 

</details>
<!--END_SECTION:relate-->