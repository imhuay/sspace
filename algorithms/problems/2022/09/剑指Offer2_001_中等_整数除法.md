## 整数除法
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&label_color=gray&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer2&label_color=gray&color=green&style=flat-square)](../../../README.md#剑指offer2)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE&label_color=gray&color=blue&style=flat-square)](../../../README.md#二分查找)
[![](https://img.shields.io/static/v1?label=&message=%E7%BB%8F%E5%85%B8&label_color=gray&color=blue&style=flat-square)](../../../README.md#经典)
<!--END_SECTION:badge-->
<!--info
tags: [二分, 经典]
source: 剑指Offer2
level: 中等
number: '001'
name: 整数除法
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定两个整数 a 和 b ，求它们的除法的商 a/b。
要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%'。
```

<details><summary><b>详细描述</b></summary>

```txt
给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%'。

注意：
    整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31, 2^31−1]。本题中，如果除法结果溢出，则返回 2^31 − 1

示例 1：
    输入：a = 15, b = 2
    输出：7
    解释：15/2 = truncate(7.5) = 7
示例 2：
    输入：a = 7, b = -3
    输出：-2
    解释：7/-3 = truncate(-2.33333..) = -2
示例 3：
    输入：a = 0, b = 1
    输出：0
示例 4：
    输入：a = 1, b = 1
    输出：1
提示:
    -2^31 <= a, b <= 2^31 - 1
    b != 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xoh6Oh
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1：减法（超时）</b></summary>

- 用 a 循环减 b，直到为负；
- 越界讨论：因为是整数除法，实际的越界情况就一种，就是 `a=-2^31,b=-1`
- 极端情况：`a=2^31-1, b=1` 要循坏 `2^31-1` 次；

<details><summary><b>Python</b></summary>

```python
class Solution:
    def divide(self, a: int, b: int) -> int:
        assert b != 0
        
        MAX = 2 ** 31 - 1
        if a == 0: return 0
        if a == -2 ** 31 and b == -1: return MAX  # 越界
        
        # 转为两个整数操作
        sign = 1
        if a < 0:
            sign *= -1
            a = -a
        
        if b < 0:
            sign *= -1
            b = -b

        # 循坏减去 b
        ret = -1
        while a > 0:
            a -= b
            ret += 1

        if a == 0:  # 整除的情况
            ret += 1 
        
        return sign * ret
```

</details>


<summary><b>思路2：二分思想</b></summary>

1. 初始化返回值 `ret = 0`
2. `a > b` 时，不断将 `b` 翻倍（乘 2），直到再翻倍一次就大于 `a`，记翻倍后的数为 `tmp_b`，翻的倍数为 `tmp`，然后将 `ret` 加上 `tmp`、`a` 减去 `tmp_b`；
3. `a` 减去 `tmp_b` 后循环以上过程，直到 `a` 小于 `b`；

```
以 a = 32, b = 3 为例，模拟过程如下：

初始化 ret = 0
第一轮：
    32 / (3*2*2*2) = t1 / (1*2*2*2)  # 再乘一个 2 会大于 32
    32 / 24 = 1 = t1 / 8 -> t1 = 8
    (32 - 24) / 3 = 8 / 3
    ret += t1 -> 8
第二轮：
    8 / (3*2) = t2 / (1*2)
    8 / 6 = 1 = t2 / 2 -> t2 = 2
    (8 - 6) / 3 = 0
    ret += t2 -> 10
因为 2 < 3 退出循环
```

<details><summary><b>Python</b></summary>

```python
class Solution:
    def divide(self, a: int, b: int) -> int:
        assert b != 0
        if a == 0: return 0
        if a == -2**31 and b == -1: return 2 ** 31 - 1
        sign = 1 if (a > 0 and b > 0) or (a < 0 and b < 0) else -1
        a = a if a > 0 else -a
        b = b if b > 0 else -b
        
        # if a < b: return 0

        ret = 0
        while a >= b:
            tmp, tmp_b = 1, b
            while tmp_b * 2 < a:
                tmp_b *= 2
                tmp *= 2
            
            ret += tmp
            a -= tmp_b

        return ret * sign
```

</details>
<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>二分查找</b></summary>

> [[中等, LeetCode] 两数相除](../../2021/10/LeetCode_0029_中等_两数相除.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, 剑指Offer] 二维数组中的查找](../../2021/11/剑指Offer_0400_中等_二维数组中的查找.md)  
> [[中等, 剑指Offer] 数值的整数次方（快速幂） 🔥](../../2021/11/剑指Offer_1600_中等_数值的整数次方（快速幂）.md)  
> [[中等, 牛客] 二分查找-II](../04/牛客_0105_中等_二分查找-II.md)  
> [[中等, 牛客] 二维数组中的查找](../02/牛客_0029_中等_二维数组中的查找.md)  
> [[中等, 牛客] 寻找峰值 🔥](../04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 矩阵元素查找](../04/牛客_0086_中等_矩阵元素查找.md)  
  > 
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 将数据流变为多个不相交区间](../../2021/10/LeetCode_0352_困难_将数据流变为多个不相交区间.md)  
> [[困难, 牛客] 在两个长度相等的排序数组中找到上中位数](../02/牛客_0036_困难_在两个长度相等的排序数组中找到上中位数.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](../10/LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 排列硬币](../../2021/10/LeetCode_0441_简单_排列硬币.md)  
> [[简单, 剑指Offer2] 山峰数组的顶部](剑指Offer2_069_简单_山峰数组的顶部.md)  
> [[简单, 剑指Offer] 在排序数组中查找数字](../01/剑指Offer_5302_简单_在排序数组中查找数字.md)  
> [[简单, 剑指Offer] 旋转数组的最小数字](../../2021/11/剑指Offer_1100_简单_旋转数组的最小数字.md)  
> [[简单, 剑指Offer] 求0～n-1中缺失的数字](../01/剑指Offer_5301_简单_求0～n-1中缺失的数字.md)  
> [[简单, 牛客] 在旋转过的有序数组中寻找目标值](../03/牛客_0048_简单_在旋转过的有序数组中寻找目标值.md)  
> [[简单, 牛客] 数字在升序数组中出现的次数](../03/牛客_0074_简单_数字在升序数组中出现的次数.md)  
> [[简单, 牛客] 旋转数组的最小数字](../03/牛客_0071_简单_旋转数组的最小数字.md)  
> [[简单, 牛客] 求平方根 🔥](../02/牛客_0032_简单_求平方根.md)  
  > 

</details>
<details><summary><b>经典</b></summary>

> [[中等, LeetCode] 下一个排列 🔥](../10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 二叉树的完全性检验 🔥](../03/LeetCode_0958_中等_二叉树的完全性检验.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../06/LeetCode_0300_中等_最长递增子序列.md)  
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
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
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