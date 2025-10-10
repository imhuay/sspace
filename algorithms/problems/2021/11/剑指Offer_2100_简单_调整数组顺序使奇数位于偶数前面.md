## 调整数组顺序使奇数位于偶数前面
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=yellow&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E6%95%B0%E7%BB%84/%E7%9F%A9%E9%98%B5&color=blue&style=flat-square)](../../../README.md#数组矩阵)
[![](https://img.shields.io/static/v1?label=&message=%E5%8F%8C%E6%8C%87%E9%92%88&color=blue&style=flat-square)](../../../README.md#双指针)
<!--END_SECTION:badge-->
<!--info
tags: [数组, 双指针]
source: 剑指Offer
level: 简单
number: '2100'
name: 调整数组顺序使奇数位于偶数前面
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定整型数组, 调整其顺序, 使所有奇数在偶数之前 (不要求顺序).
```

<details><summary><b>详细描述</b></summary>

```txt
输入一个整数数组, 实现一个函数来调整该数组中数字的顺序, 使得所有奇数在数组的前半部分, 所有偶数在数组的后半部分.

示例:
    输入: nums = [1,2,3,4]
    输出: [1,3,2,4]
    注: [3,1,2,4] 也是正确的答案之一.
提示:
    0 <= nums.length <= 50000
    0 <= nums[i] <= 10000

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 头尾双指针, 当头指针指向偶数, 尾指针指向奇数时, 交换;
- **注意边界判断**;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:

        l, r = 0, len(nums) - 1
        while l < r:
            # 注意需要始终保持 l < r
            while l < r and nums[l] % 2 == 1:
                l += 1
            while l < r and nums[r] % 2 == 0:
                r -= 1

            nums[l], nums[r] = nums[r], nums[l]

        return nums
```

</details>


<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>数组/矩阵</b></summary>

> [[中等, LeetCode] 从魔法师身上吸取的最大能量](../../2025/10/LeetCode_3147_中等_从魔法师身上吸取的最大能量.md)  
> [[中等, LeetCode] 矩阵置零](../../2025/10/LeetCode_0073_中等_矩阵置零.md)  
> [[中等, 剑指Offer] 栈的压入、弹出序列 🔥](剑指Offer_3100_中等_栈的压入、弹出序列.md)  
> [[中等, 剑指Offer] 顺时针打印矩阵 (3种思路4个写法) 🔥](剑指Offer_2900_中等_顺时针打印矩阵(3种思路4个写法).md)  
> [[中等, 牛客] 旋转数组](../../2022/04/牛客_0110_中等_旋转数组.md)  
> [[中等, 牛客] 缺失的第一个正整数](../../2022/02/牛客_0030_中等_缺失的第一个正整数.md)  
> [[中等, 牛客] 螺旋矩阵](../../2022/03/牛客_0038_中等_螺旋矩阵.md)  
> [[中等, 牛客] 调整数组顺序使奇数位于偶数前面(一)](../../2022/03/牛客_0077_中等_调整数组顺序使奇数位于偶数前面(一).md)  
  > 
> [[简单, 剑指Offer] 包含min函数的栈](剑指Offer_3000_简单_包含min函数的栈.md)  
> [[简单, 牛客] 最长公共前缀](../../2022/03/牛客_0055_简单_最长公共前缀.md)  
> [[简单, 牛客] 顺时针旋转矩阵](../../2022/01/牛客_0018_简单_顺时针旋转矩阵.md)  
  > 

</details>
<details><summary><b>双指针</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../../2022/10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../../2022/01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 最接近的三数之和](../10/LeetCode_0016_中等_最接近的三数之和.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 有效三角形的个数](../10/LeetCode_0611_中等_有效三角形的个数.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 牛客] 三数之和 🔥](../../2022/03/牛客_0054_中等_三数之和.md)  
> [[中等, 牛客] 删除链表的倒数第n个节点](../../2022/03/牛客_0053_中等_删除链表的倒数第n个节点.md)  
> [[中等, 牛客] 合并两个有序的数组](../../2022/01/牛客_0022_中等_合并两个有序的数组.md)  
  > 
> [[困难, LeetCode] 接雨水 🔥](../10/LeetCode_0042_困难_接雨水.md)  
> [[困难, 牛客] 接雨水问题 🔥](../../2022/05/牛客_0128_困难_接雨水问题.md)  
  > 
> [[简单, LeetCode] 两数之和II-输入有序数组](../../2022/07/LeetCode_0167_简单_两数之和II-输入有序数组.md)  
> [[简单, LeetCode] 链表的中间结点](../../2022/06/LeetCode_0876_简单_链表的中间结点.md)  
> [[简单, 剑指Offer] 两个链表的第一个公共节点](../../2022/01/剑指Offer_5200_简单_两个链表的第一个公共节点.md)  
> [[简单, 剑指Offer] 和为s的两个数字](../../2022/01/剑指Offer_5701_简单_和为s的两个数字.md)  
> [[简单, 剑指Offer] 和为s的连续正数序列](../../2022/01/剑指Offer_5702_简单_和为s的连续正数序列.md)  
> [[简单, 剑指Offer] 翻转单词顺序](../../2022/01/剑指Offer_5801_简单_翻转单词顺序.md)  
> [[简单, 剑指Offer] 链表中倒数第k个节点](剑指Offer_2200_简单_链表中倒数第k个节点.md)  
> [[简单, 牛客] 判断链表中是否有环](../../2022/01/牛客_0004_简单_判断链表中是否有环.md)  
> [[简单, 牛客] 反转字符串](../../2022/04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 链表中倒数最后k个结点](../../2022/03/牛客_0069_简单_链表中倒数最后k个结点.md)  
> [[简单, 牛客] 链表中环的入口结点](../../2022/01/牛客_0003_简单_链表中环的入口结点.md)  
  > 

</details>
<!--END_SECTION:relate-->
