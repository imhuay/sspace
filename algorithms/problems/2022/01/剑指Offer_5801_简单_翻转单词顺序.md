## 翻转单词顺序
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=yellow&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%8F%8C%E6%8C%87%E9%92%88&color=blue&style=flat-square)](../../../README.md#双指针)
<!--END_SECTION:badge-->
<!--info
tags: [双指针]
source: 剑指Offer
level: 简单
number: '5801'
name: 翻转单词顺序
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
输入一个英文句子, 翻转句子中单词的顺序, 但单词内字符的顺序不变.
"  I  am a  student. " -> "student. a am I"
```

<details><summary><b>详细描述</b></summary>

```txt
输入一个英文句子, 翻转句子中单词的顺序, 但单词内字符的顺序不变. 为简单起见, 标点符号和普通字母一样处理. 例如输入字符串"I am a student. ", 则输出"student. a am I".

示例 1:
    输入: "the sky is blue"
    输出: "blue is sky the"
示例 2:
    输入: "  hello world!  "
    输出: "world! hello"
    解释: 输入字符串可以在前面或者后面包含多余的空格, 但是反转后的字符不能包括.
示例 3:
    输入: "a good   example"
    输出: "example good a"
    解释: 如果两个单词间有多余的空格, 将反转后单词间的空格减少到只含一个.

说明:
    无空格字符构成一个单词.
    输入字符串可以在前面或者后面包含多余的空格, 但是反转后的字符不能包括.
    如果两个单词间有多余的空格, 将反转后单词间的空格减少到只含一个.

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1: 双指针 (面试推荐写法) </b></summary>

- 手写 split 函数, 切分字符串, 再逆序拼接

<details><summary><b>Python</b></summary>

```python
class Solution:
    def reverseWords(self, s: str) -> str:

        ret = []
        l, r = 0, 0
        while r < len(s):
            while r < len(s) and s[r] == ' ':  # 跳过空格
                r += 1

            l = r  # 单词首位
            while r < len(s) and s[r] != ' ':  # 跳过字符
                r += 1

            if l < r:  # 如果存在字符
                ret.append(s[l: r])

        return ' '.join(ret[::-1])

```

</details>


<summary><b>思路2: 库函数</b></summary>

<details><summary><b>Python</b></summary>

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
```

</details>

<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>双指针</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 最接近的三数之和](../../2021/10/LeetCode_0016_中等_最接近的三数之和.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 有效三角形的个数](../../2021/10/LeetCode_0611_中等_有效三角形的个数.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../../2021/12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 牛客] 三数之和 🔥](../03/牛客_0054_中等_三数之和.md)  
> [[中等, 牛客] 删除链表的倒数第n个节点](../03/牛客_0053_中等_删除链表的倒数第n个节点.md)  
> [[中等, 牛客] 合并两个有序的数组](牛客_0022_中等_合并两个有序的数组.md)  
  > 
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, 牛客] 接雨水问题 🔥](../05/牛客_0128_困难_接雨水问题.md)  
  > 
> [[简单, LeetCode] 两数之和II-输入有序数组](../07/LeetCode_0167_简单_两数之和II-输入有序数组.md)  
> [[简单, LeetCode] 链表的中间结点](../06/LeetCode_0876_简单_链表的中间结点.md)  
> [[简单, 剑指Offer] 两个链表的第一个公共节点](剑指Offer_5200_简单_两个链表的第一个公共节点.md)  
> [[简单, 剑指Offer] 和为s的两个数字](剑指Offer_5701_简单_和为s的两个数字.md)  
> [[简单, 剑指Offer] 和为s的连续正数序列](剑指Offer_5702_简单_和为s的连续正数序列.md)  
> [[简单, 剑指Offer] 调整数组顺序使奇数位于偶数前面](../../2021/11/剑指Offer_2100_简单_调整数组顺序使奇数位于偶数前面.md)  
> [[简单, 剑指Offer] 链表中倒数第k个节点](../../2021/11/剑指Offer_2200_简单_链表中倒数第k个节点.md)  
> [[简单, 牛客] 判断链表中是否有环](牛客_0004_简单_判断链表中是否有环.md)  
> [[简单, 牛客] 反转字符串](../04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 链表中倒数最后k个结点](../03/牛客_0069_简单_链表中倒数最后k个结点.md)  
> [[简单, 牛客] 链表中环的入口结点](牛客_0003_简单_链表中环的入口结点.md)  
  > 

</details>
<!--END_SECTION:relate-->