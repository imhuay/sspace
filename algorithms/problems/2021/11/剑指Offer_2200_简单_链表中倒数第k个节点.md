## 链表中倒数第k个节点
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%8F%8C%E6%8C%87%E9%92%88&color=blue&style=flat-square)](../../../README.md#双指针)
[![](https://img.shields.io/static/v1?label=&message=%E9%93%BE%E8%A1%A8&color=blue&style=flat-square)](../../../README.md#链表)
<!--END_SECTION:badge-->
<!--info
tags: [链表, 快慢指针]
source: 剑指Offer
level: 简单
number: '2200'
name: 链表中倒数第k个节点
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
输入一个链表, 输出该链表中倒数第k个节点.
```

<details><summary><b>详细描述</b></summary>

```txt
输入一个链表, 输出该链表中倒数第k个节点. 为了符合大多数人的习惯, 本题从1开始计数, 即链表的尾节点是倒数第1个节点.

例如, 一个链表有 6 个节点, 从头节点开始, 它们的值依次是 1、2、3、4、5、6. 这个链表的倒数第 3 个节点是值为 4 的节点.

示例:
    给定一个链表: 1->2->3->4->5, 和 k = 2.
    返回链表 4->5.

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 前后双指针, 保持两个指针相距 k 个节点, 当前指针达到链表尾时, 返回后指针;

<details><summary><b>Python</b></summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None or k < 1:
            return head

        cur = head
        ret = head

        while k:
            cur = cur.next
            k -= 1

        while cur:
            ret = ret.next
            cur = cur.next

        # 更简洁的写法, 合并两个循环
        # while cur:
        #     if k <= 0:
        #         ret = ret.next
        #     cur = cur.next
        #     k -= 1

        return ret
```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

- [链表常用操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

<details><summary><b>其他算法笔记</b></summary>

- [从暴力递归到动态规划](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>双指针 (24)</b></summary>

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
> [[简单, 剑指Offer] 调整数组顺序使奇数位于偶数前面](剑指Offer_2100_简单_调整数组顺序使奇数位于偶数前面.md)  
> [[简单, 牛客] 判断链表中是否有环](../../2022/01/牛客_0004_简单_判断链表中是否有环.md)  
> [[简单, 牛客] 反转字符串](../../2022/04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 链表中倒数最后k个结点](../../2022/03/牛客_0069_简单_链表中倒数最后k个结点.md)  
> [[简单, 牛客] 链表中环的入口结点](../../2022/01/牛客_0003_简单_链表中环的入口结点.md)  
  > 

</details>

<details><summary><b>链表 (29)</b></summary>

> [[中等, LeetCode] 两数相加 🔥](../10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 分隔链表](../10/LeetCode_0086_中等_分隔链表.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../../2022/01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 重排链表 🔥](../../2022/06/LeetCode_0143_中等_重排链表.md)  
> [[中等, 剑指Offer] 复杂链表的复制 (深拷贝) 🔥](../12/剑指Offer_3500_中等_复杂链表的复制(深拷贝).md)  
> [[中等, 牛客] 划分链表](../../2022/01/牛客_0023_中等_划分链表.md)  
> [[中等, 牛客] 删除有序链表中重复的元素-I](../../2022/01/牛客_0025_中等_删除有序链表中重复的元素-I.md)  
> [[中等, 牛客] 删除有序链表中重复的元素-II](../../2022/01/牛客_0024_中等_删除有序链表中重复的元素-II.md)  
> [[中等, 牛客] 重排链表](../../2022/01/牛客_0002_中等_重排链表.md)  
> [[中等, 牛客] 链表中的节点每k个一组翻转](../../2022/03/牛客_0050_中等_链表中的节点每k个一组翻转.md)  
> [[中等, 牛客] 链表内指定区间反转](../../2022/01/牛客_0021_中等_链表内指定区间反转.md)  
> [[中等, 牛客] 链表相加(二)](../../2022/03/牛客_0040_中等_链表相加(二).md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../../2022/02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](../../2022/10/LeetCode_0023_困难_合并K个升序链表.md)  
  > 
> [[简单, LeetCode] 反转链表 🔥](../../2022/10/LeetCode_0206_简单_反转链表.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 链表的中间结点](../../2022/06/LeetCode_0876_简单_链表的中间结点.md)  
> [[简单, 剑指Offer] 两个链表的第一个公共节点](../../2022/01/剑指Offer_5200_简单_两个链表的第一个公共节点.md)  
> [[简单, 剑指Offer] 从尾到头打印链表](剑指Offer_0600_简单_从尾到头打印链表.md)  
> [[简单, 剑指Offer] 删除链表的节点](剑指Offer_1800_简单_删除链表的节点.md)  
> [[简单, 剑指Offer] 反转链表 🔥](剑指Offer_2400_简单_反转链表.md)  
> [[简单, 剑指Offer] 合并两个排序的链表](剑指Offer_2500_简单_合并两个排序的链表.md)  
> [[简单, 牛客] 两个链表的第一个公共结点 🔥](../../2022/03/牛客_0066_简单_两个链表的第一个公共结点.md)  
> [[简单, 牛客] 判断一个链表是否为回文结构](../../2022/04/牛客_0096_简单_判断一个链表是否为回文结构.md)  
> [[简单, 牛客] 判断链表中是否有环](../../2022/01/牛客_0004_简单_判断链表中是否有环.md)  
> [[简单, 牛客] 单链表的排序 🔥](../../2022/03/牛客_0070_简单_单链表的排序.md)  
> [[简单, 牛客] 反转链表](../../2022/03/牛客_0078_简单_反转链表.md)  
> [[简单, 牛客] 合并两个排序的链表](../../2022/02/牛客_0033_简单_合并两个排序的链表.md)  
> [[简单, 牛客] 链表中环的入口结点](../../2022/01/牛客_0003_简单_链表中环的入口结点.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
