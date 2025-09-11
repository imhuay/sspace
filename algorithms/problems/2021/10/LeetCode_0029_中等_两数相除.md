## 两数相除
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&label_color=gray&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&label_color=gray&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E4%BD%8D%E8%BF%90%E7%AE%97&label_color=gray&color=blue&style=flat-square)](../../../README.md#位运算)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE&label_color=gray&color=blue&style=flat-square)](../../../README.md#二分查找)
<!--END_SECTION:badge-->
<!--info
tags: [位运算, 二分查找]
source: LeetCode
level: 中等
number: '0029'
name: 两数相除
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
不使用乘法、除法和 mod 运算符, 返回两数相除的整数部分, 如 10/3 返回 3.
```

<details><summary><b>详细描述</b></summary>

```txt
给定两个整数, 被除数 dividend 和除数 divisor. 将两数相除, 要求不使用乘法、除法和 mod 运算符.

返回被除数 dividend 除以除数 divisor 得到的商.

整数除法的结果应当截去 (truncate) 其小数部分, 例如: truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:
    输入: dividend = 10, divisor = 3
    输出: 3
    解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:
    输入: dividend = 7, divisor = -3
    输出: -2
    解释: 7/-3 = truncate(-2.33333..) = -2

提示:
    被除数和除数均为 32 位有符号整数.
    除数不为 0.
    假设我们的环境只能存储 32 位有符号整数, 其数值范围是 [−2^31,  2^31 − 1]. 本题中, 如果除法结果溢出, 则返回 2^31 − 1.

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>


<summary><b>思路</b></summary>

<details><summary><b>Python: 二分查找</b></summary>

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """"""
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # 按照题目要求, 只有一种情况会溢出
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

        # 核心操作
        def div(a, b):
            if a < b:
                return 0

            cnt = 1
            tb = b
            while (tb + tb) <= a:
                cnt += cnt
                tb += tb

            return cnt + div(a - tb, b)

        ret = div(abs(dividend), abs(divisor))
        return ret if sign else -ret
```

**核心操作说明**, 以 60 / 8 为例:
```txt
第一轮 div(60, 8): 8 -> 32 时停止, 因为 32 + 32 > 60, 返回 4
第二轮 div(28, 8): 8 -> 16 时停止, 因为 16 + 16 > 28, 返回 2
第三轮 div(8, 8):  8 -> 8  时停止, 因为 8  +  8 >  8, 返回 1
第三轮 div(0, 8):  因为 0 < 8, 返回 0

因此结果为 1 + 2 + 4 = 7
```

</details>

<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>位运算</b></summary>

> [[中等, LeetCode] 重复的DNA序列](../../2022/07/LeetCode_0187_中等_重复的DNA序列.md)  
> [[中等, 剑指Offer] 数组中数字出现的次数](../../2022/01/剑指Offer_5601_中等_数组中数字出现的次数.md)  
> [[中等, 剑指Offer] 数组中数字出现的次数](../../2022/01/剑指Offer_5602_中等_数组中数字出现的次数.md)  
> [[中等, 牛客] 数组中只出现一次的两个数字 🔥](../../2022/03/牛客_0075_中等_数组中只出现一次的两个数字.md)  
  > 
> [[困难, 牛客] N皇后问题](../../2022/03/牛客_0039_困难_N皇后问题.md)  
  > 
> [[简单, 剑指Offer] 不用加减乘除做加法](../../2022/01/剑指Offer_6500_简单_不用加减乘除做加法.md)  
> [[简单, 剑指Offer] 二进制中1的个数](../11/剑指Offer_1500_简单_二进制中1的个数.md)  
> [[简单, 牛客] 二进制中1的个数 🔥](../../2022/05/牛客_0120_简单_二进制中1的个数.md)  
  > 

</details>
<details><summary><b>二分查找</b></summary>

> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../../2022/10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../../2022/07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, 剑指Offer2] 整数除法 🔥](../../2022/09/剑指Offer2_001_中等_整数除法.md)  
> [[中等, 剑指Offer] 二维数组中的查找](../11/剑指Offer_0400_中等_二维数组中的查找.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 牛客] 二分查找-II](../../2022/04/牛客_0105_中等_二分查找-II.md)  
> [[中等, 牛客] 二维数组中的查找](../../2022/02/牛客_0029_中等_二维数组中的查找.md)  
> [[中等, 牛客] 寻找峰值 🔥](../../2022/04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 矩阵元素查找](../../2022/04/牛客_0086_中等_矩阵元素查找.md)  
  > 
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../../2022/02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 将数据流变为多个不相交区间](LeetCode_0352_困难_将数据流变为多个不相交区间.md)  
> [[困难, 牛客] 在两个长度相等的排序数组中找到上中位数](../../2022/02/牛客_0036_困难_在两个长度相等的排序数组中找到上中位数.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](../../2022/10/LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 排列硬币](LeetCode_0441_简单_排列硬币.md)  
> [[简单, 剑指Offer2] 山峰数组的顶部](../../2022/09/剑指Offer2_069_简单_山峰数组的顶部.md)  
> [[简单, 剑指Offer] 在排序数组中查找数字](../../2022/01/剑指Offer_5302_简单_在排序数组中查找数字.md)  
> [[简单, 剑指Offer] 旋转数组的最小数字](../11/剑指Offer_1100_简单_旋转数组的最小数字.md)  
> [[简单, 剑指Offer] 求0～n-1中缺失的数字](../../2022/01/剑指Offer_5301_简单_求0～n-1中缺失的数字.md)  
> [[简单, 牛客] 在旋转过的有序数组中寻找目标值](../../2022/03/牛客_0048_简单_在旋转过的有序数组中寻找目标值.md)  
> [[简单, 牛客] 数字在升序数组中出现的次数](../../2022/03/牛客_0074_简单_数字在升序数组中出现的次数.md)  
> [[简单, 牛客] 旋转数组的最小数字](../../2022/03/牛客_0071_简单_旋转数组的最小数字.md)  
> [[简单, 牛客] 求平方根 🔥](../../2022/02/牛客_0032_简单_求平方根.md)  
  > 

</details>
<!--END_SECTION:relate-->