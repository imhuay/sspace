## 数组中重复的数字
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%93%88%E5%B8%8C%E8%A1%A8%28Hash%29&color=blue&style=flat-square)](../../../README.md#哈希表hash)
<!--END_SECTION:badge-->
<!--info
tags: [哈希表]
source: 剑指Offer
level: 简单
number: '0300'
name: 数组中重复的数字
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
找出数组中任意一个重复的数字.
```

<details><summary><b>详细描述</b></summary>

```txt
找出数组中重复的数字.

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内. 数组中某些数字是重复的, 但不知道有几个数字重复了, 也不知道每个数字重复了几次. 请找出数组中任意一个重复的数字.

示例 1:
    输入:
    [2, 3, 1, 0, 2, 5, 3]
    输出: 2 或 3

限制:
    2 <= n <= 100000

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

</details>

<summary><b>思路</b></summary>

- 遍历数组, 保存见过的数字, 当遇到出现过的数字即返回


<details><summary><b>Python</b></summary>

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        tb = set()
        for i in nums:
            if i in tb:
                return i
            tb.add(i)
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
- [链表常用操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>哈希表(Hash) (11)</b></summary>

> [[中等, LeetCode] 字母异位词分组 🔥](../../2022/10/LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 重复的DNA序列](../../2022/07/LeetCode_0187_中等_重复的DNA序列.md)  
> [[中等, 剑指Offer] 复杂链表的复制 (深拷贝) 🔥](../12/剑指Offer_3500_中等_复杂链表的复制(深拷贝).md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 牛客] 和为K的连续子数组](../../2022/05/牛客_0125_中等_和为K的连续子数组.md)  
  > 
> [[困难, 牛客] 数组中的最长连续子序列](../../2022/04/牛客_0095_困难_数组中的最长连续子序列.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../10/LeetCode_0001_简单_两数之和.md)  
> [[简单, 剑指Offer] 第一个只出现一次的字符](../12/剑指Offer_5000_简单_第一个只出现一次的字符.md)  
> [[简单, 牛客] 两数之和](../../2022/03/牛客_0061_简单_两数之和.md)  
> [[简单, 牛客] 第一个只出现一次的字符](../../2022/02/牛客_0031_简单_第一个只出现一次的字符.md)  
> [[简单, 程序员面试金典] 判定是否互为字符重排](../../2022/09/程序员面试金典_0102_简单_判定是否互为字符重排.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
