## x 的平方根
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE&color=blue&style=flat-square)](../../../README.md#二分查找)
[![](https://img.shields.io/static/v1?label=&message=%E7%83%AD%E9%97%A8&color=blue&style=flat-square)](../../../README.md#热门)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [二分查找, 热门]
source: LeetCode
level: 简单
number: '0069'
name: x 的平方根
companies: []
-->

> [69. x 的平方根 - 力扣 (LeetCode) ](https://leetcode.cn/problems/sqrtx/)

<summary><b>问题简述</b></summary>

```txt
给你一个非负整数 x , 计算并返回 x 的 算术平方根 (整数部分).
```

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路: 二分查找</b></summary>

<details><summary><b>Python</b></summary>

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0, 1): return x

        l, r = 0, x
        while l < r:
            m = (l + r) // 2
            if m ** 2 <= x < (m + 1) ** 2:
                break

            if m ** 2 < x:
                l = m
            else:
                r = m

        return m
```

</details>


<summary><b>进阶: 浮点数版本</b></summary>

- 定义 `mySqrt(x: float, e: int)`, 其中 `e` 为小数精度;
- 注: 代码未经过严格测试, 可能存在问题;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def mySqrt(self, x: float, e: int) -> int:
        if x in (0, 1): return x

        assert x > 0
        flag = False
        if x < 1:  # 小于 1 的情况
            x = 1 / x
            flag = True

        l, r = 0, x
        while l < r:
            m = (l + r) / 2
            if abs(m ** 2 - x) <= 0.1 ** e:
                break

            if m ** 2 < x:
                l = m
            else:
                r = m

        return 1 / m if flag else m
```

</details>

<!--
<summary><b>相关问题</b></summary>

-->


<!--START_SECTION:relate_note-->
---

### 算法笔记

> 🌧️ _暂无主题相关的笔记_


<details><summary><b>其他算法笔记</b></summary>

- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表常用操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>二分查找 (23)</b></summary>

> [[中等, LeetCode] 两数相除](../../2021/10/LeetCode_0029_中等_两数相除.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, 剑指Offer2] 整数除法 🔥](../09/剑指Offer2_001_中等_整数除法.md)  
> [[中等, 剑指Offer] 二维数组中的查找](../../2021/11/剑指Offer_0400_中等_二维数组中的查找.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../../2021/11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 牛客] 二分查找-II](../04/牛客_0105_中等_二分查找-II.md)  
> [[中等, 牛客] 二维数组中的查找](../02/牛客_0029_中等_二维数组中的查找.md)  
> [[中等, 牛客] 寻找峰值 🔥](../04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 矩阵元素查找](../04/牛客_0086_中等_矩阵元素查找.md)  
  > 
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 将数据流变为多个不相交区间](../../2021/10/LeetCode_0352_困难_将数据流变为多个不相交区间.md)  
> [[困难, 牛客] 在两个长度相等的排序数组中找到上中位数](../02/牛客_0036_困难_在两个长度相等的排序数组中找到上中位数.md)  
  > 
> [[简单, LeetCode] 排列硬币](../../2021/10/LeetCode_0441_简单_排列硬币.md)  
> [[简单, 剑指Offer2] 山峰数组的顶部](../09/剑指Offer2_069_简单_山峰数组的顶部.md)  
> [[简单, 剑指Offer] 在排序数组中查找数字](../01/剑指Offer_5302_简单_在排序数组中查找数字.md)  
> [[简单, 剑指Offer] 旋转数组的最小数字](../../2021/11/剑指Offer_1100_简单_旋转数组的最小数字.md)  
> [[简单, 剑指Offer] 求0～n-1中缺失的数字](../01/剑指Offer_5301_简单_求0～n-1中缺失的数字.md)  
> [[简单, 牛客] 在旋转过的有序数组中寻找目标值](../03/牛客_0048_简单_在旋转过的有序数组中寻找目标值.md)  
> [[简单, 牛客] 数字在升序数组中出现的次数](../03/牛客_0074_简单_数字在升序数组中出现的次数.md)  
> [[简单, 牛客] 旋转数组的最小数字](../03/牛客_0071_简单_旋转数组的最小数字.md)  
> [[简单, 牛客] 求平方根 🔥](../02/牛客_0032_简单_求平方根.md)  
  > 

</details>

<details><summary><b>热门 (16)</b></summary>

> [[中等, LeetCode] 买卖股票的最佳时机II 🔥](../06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 全排列 🔥](LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 重排链表 🔥](../06/LeetCode_0143_中等_重排链表.md)  
> [[中等, 剑指Offer] 把字符串转换成整数 🔥](../01/剑指Offer_6700_中等_把字符串转换成整数.md)  
> [[中等, 牛客] 三数之和 🔥](../03/牛客_0054_中等_三数之和.md)  
> [[中等, 牛客] 把二叉树打印成多行 🔥](../03/牛客_0080_中等_把二叉树打印成多行.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
  > 
> [[简单, LeetCode] 平衡二叉树 🔥](../09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, 牛客] 两个链表的第一个公共结点 🔥](../03/牛客_0066_简单_两个链表的第一个公共结点.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
