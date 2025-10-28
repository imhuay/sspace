## 排列硬币
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE&color=blue&style=flat-square)](../../../README.md#二分查找)
[![](https://img.shields.io/static/v1?label=&message=%E6%95%B0%E5%AD%A6&color=blue&style=flat-square)](../../../README.md#数学)
<!--END_SECTION:badge-->
<!--info
tags: [二分查找, 数学]
source: LeetCode
level: 简单
number: '0441'
name: 排列硬币
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
你总共有 n 枚硬币, 并计划将它们按阶梯状排列. 对于一个由 k 行组成的阶梯, 其第 i 行必须正好有 i 枚硬币. 阶梯的最后一行 可能 是不完整的.

给你一个数字 n , 计算并返回可形成 完整阶梯行 的总行数.

示例 1:
    输入: n = 5
    输出: 2
    解释: 因为第三行不完整, 所以返回 2 .

提示:
    1 <= n <= 2^31 - 1

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/arranging-coins
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<div align="center"><img src="../../../_assets/arrangecoins1-grid.jpeg" height="150" /></div>


<summary><b>思路</b></summary>

<details><summary><b>法1) Python: 二分查找</b></summary>

- 因为时间复杂度为 `O(logN)`, 所以直接在 `[1, n]` 的范围里找即可

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left

```

</details>


<details><summary><b>法2) Python: 数学公式</b></summary>

- 解方程 $(1+x)*x/2 = n$;
- 去掉小于 0 的解, 保留: $x=(-1+\sqrt{8n+1})/2$

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (8 * n + 1) ** 0.5) / 2)
```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

> 🌧️ _暂无主题相关的笔记_


<details><summary><b>其他算法笔记</b></summary>

- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>二分查找 (23)</b></summary>

> [[中等, LeetCode] 两数相除](LeetCode_0029_中等_两数相除.md)  
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

<details><summary><b>数学 (7)</b></summary>

> [[中等, LeetCode] 整数拆分](../12/LeetCode_0343_中等_整数拆分.md)  
> [[中等, 剑指Offer] 剪绳子](../11/剑指Offer_1402_中等_剪绳子.md)  
> [[中等, 剑指Offer] 剪绳子 (整数拆分)](../11/剑指Offer_1401_中等_剪绳子(整数拆分).md)  
> [[中等, 牛客] 阶乘末尾0的数量](../../2022/05/牛客_0129_中等_阶乘末尾0的数量.md)  
  > 
> [[简单, 牛客] 三个数的最大乘积](../../2022/04/牛客_0106_简单_三个数的最大乘积.md)  
> [[简单, 牛客] 回文数字](../../2022/03/牛客_0056_简单_回文数字.md)  
> [[简单, 牛客] 进制转换](../../2022/04/牛客_0112_简单_进制转换.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
