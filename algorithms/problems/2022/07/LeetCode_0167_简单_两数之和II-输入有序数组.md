## 两数之和II-输入有序数组
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=yellow&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%8F%8C%E6%8C%87%E9%92%88&color=blue&style=flat-square)](../../../README.md#双指针)
<!--END_SECTION:badge-->
<!--info
tags: [双指针]
source: LeetCode
level: 简单
number: '0167'
name: 两数之和II-输入有序数组
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
找出一个非递减数组中和等于 target 的两个数字, 输出它们的下标.

假定题目一定有一个解.
```

<details><summary><b>详细描述</b></summary>

```txt
给定一个已按照 非递减顺序排列 的整数数组 numbers , 请你从数组中找出两个数满足相加之和等于目标数 target .

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值. numbers 的下标 从 1 开始计数 , 所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length .

你可以假设每个输入 只对应唯一的答案 , 而且你 不可以 重复使用相同的元素.


示例 1:
    输入: numbers = [2,7,11,15], target = 9
    输出: [1,2]
    解释: 2 与 7 之和等于目标数 9 . 因此 index1 = 1, index2 = 2 .
示例 2:
    输入: numbers = [2,3,4], target = 6
    输出: [1,3]
示例 3:
    输入: numbers = [-1,0], target = -1
    输出: [1,2]


提示:
    2 <= numbers.length <= 3 * 10^4
    -1000 <= numbers[i] <= 1000
    numbers 按 非递减顺序 排列
    -1000 <= target <= 1000
    仅存在一个有效答案

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<summary><b>思路</b></summary>

<details><summary><b>Python: 双指针</b></summary>

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """"""
        lo, hi = 0, len(numbers) - 1

        while lo < hi:
            tmp = numbers[lo] + numbers[hi]

            if tmp < target:
                lo += 1
            elif tmp > target:
                hi -= 1
            else:
                return [lo + 1, hi + 1]
```

</details>

<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>双指针</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 最接近的三数之和](../../2021/10/LeetCode_0016_中等_最接近的三数之和.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 有效三角形的个数](../../2021/10/LeetCode_0611_中等_有效三角形的个数.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../../2021/12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 牛客] 三数之和 🔥](../03/牛客_0054_中等_三数之和.md)  
> [[中等, 牛客] 删除链表的倒数第n个节点](../03/牛客_0053_中等_删除链表的倒数第n个节点.md)  
> [[中等, 牛客] 合并两个有序的数组](../01/牛客_0022_中等_合并两个有序的数组.md)  
  > 
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, 牛客] 接雨水问题 🔥](../05/牛客_0128_困难_接雨水问题.md)  
  > 
> [[简单, LeetCode] 链表的中间结点](../06/LeetCode_0876_简单_链表的中间结点.md)  
> [[简单, 剑指Offer] 两个链表的第一个公共节点](../01/剑指Offer_5200_简单_两个链表的第一个公共节点.md)  
> [[简单, 剑指Offer] 和为s的两个数字](../01/剑指Offer_5701_简单_和为s的两个数字.md)  
> [[简单, 剑指Offer] 和为s的连续正数序列](../01/剑指Offer_5702_简单_和为s的连续正数序列.md)  
> [[简单, 剑指Offer] 翻转单词顺序](../01/剑指Offer_5801_简单_翻转单词顺序.md)  
> [[简单, 剑指Offer] 调整数组顺序使奇数位于偶数前面](../../2021/11/剑指Offer_2100_简单_调整数组顺序使奇数位于偶数前面.md)  
> [[简单, 剑指Offer] 链表中倒数第k个节点](../../2021/11/剑指Offer_2200_简单_链表中倒数第k个节点.md)  
> [[简单, 牛客] 判断链表中是否有环](../01/牛客_0004_简单_判断链表中是否有环.md)  
> [[简单, 牛客] 反转字符串](../04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 链表中倒数最后k个结点](../03/牛客_0069_简单_链表中倒数最后k个结点.md)  
> [[简单, 牛客] 链表中环的入口结点](../01/牛客_0003_简单_链表中环的入口结点.md)  
  > 

</details>
<!--END_SECTION:relate-->