## 有效的括号
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
[![](https://img.shields.io/static/v1?label=&message=%E6%A0%88/%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#栈队列)
<!--END_SECTION:badge-->
<!--info
tags: [栈, lc100]
source: LeetCode
level: 简单
number: '0020'
name: 有效的括号
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定一个只包括 '(', ')', '{', '}', '[', ']' 的字符串 s , 判断字符串是否有效.
有效字符串需满足:
    左括号必须用相同类型的右括号闭合.
    左括号必须以正确的顺序闭合.
```
> [20. 有效的括号 - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/valid-parentheses/)

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->


<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 利用栈, 遇到左括号就压栈, 遇到右括号就出栈;
- 无效的情况: 栈顶与当前遇到的右括号不匹配, 或栈为空;
- 当遍历完所有字符, 且栈为空时, 即有效;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []  # 模拟栈
        table = {')':'(', ']': '[', '}': '{'}

        for c in s:
            if c in '([{':
                stack.append(c)
            elif stack and table[c] == stack[-1]:
                stack.pop()
            else:  # 栈为空, 且遇到左括号, 一定无效
                return False

        return len(stack) == 0
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


<details><summary><b>LeetCode Hot 100 (25)</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 两数相加 🔥](../../2021/10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 全排列 🔥](../10/LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](../10/LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 字母异位词分组 🔥](../10/LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 括号生成 🔥](../10/LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](../10/LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, LeetCode] 无重复字符的最长子串 🔥](../02/LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](../10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, LeetCode] 组合总和 🔥](../10/LeetCode_0039_中等_组合总和.md)  
> [[中等, LeetCode] 组合总和II 🔥](../10/LeetCode_0040_中等_组合总和II.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](../10/LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
  > 

</details>

<details><summary><b>栈/队列 (15)</b></summary>

> [[中等, 剑指Offer] 栈的压入、弹出序列 🔥](../../2021/11/剑指Offer_3100_中等_栈的压入、弹出序列.md)  
> [[中等, 剑指Offer] 队列的最大值](../01/剑指Offer_5902_中等_队列的最大值.md)  
> [[中等, 牛客] 按之字形顺序打印二叉树](../01/牛客_0014_中等_按之字形顺序打印二叉树.md)  
> [[中等, 牛客] 栈和排序 🔥](../05/牛客_0115_中等_栈和排序.md)  
  > 
> [[困难, LeetCode] 最长有效括号 🔥](../10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, 牛客] 最长的括号子串](牛客_0049_困难_最长的括号子串.md)  
  > 
> [[简单, 剑指Offer] 从尾到头打印链表](../../2021/11/剑指Offer_0600_简单_从尾到头打印链表.md)  
> [[简单, 剑指Offer] 包含min函数的栈](../../2021/11/剑指Offer_3000_简单_包含min函数的栈.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](../../2021/11/剑指Offer_3201_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](../../2021/11/剑指Offer_3202_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树 (之字形遍历)](../../2021/11/剑指Offer_3203_简单_层序遍历二叉树(之字形遍历).md)  
> [[简单, 剑指Offer] 用两个栈实现队列](../../2021/11/剑指Offer_0900_简单_用两个栈实现队列.md)  
> [[简单, 牛客] 包含min函数的栈](../04/牛客_0090_简单_包含min函数的栈.md)  
> [[简单, 牛客] 有效括号序列](牛客_0052_简单_有效括号序列.md)  
> [[简单, 牛客] 用两个栈实现队列](牛客_0076_简单_用两个栈实现队列.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
