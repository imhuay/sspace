## 重排链表
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E7%83%AD%E9%97%A8&color=blue&style=flat-square)](../../../README.md#热门)
[![](https://img.shields.io/static/v1?label=&message=%E9%93%BE%E8%A1%A8&color=blue&style=flat-square)](../../../README.md#链表)
<!--END_SECTION:badge-->
<!--info
tags: [链表, 热门]
source: LeetCode
level: 中等
number: '0143'
name: 重排链表
companies: [字节, 度小满, 拼多多]
-->

> [143. 重排链表 - 力扣 (LeetCode) ](https://leetcode.cn/problems/reorder-list/)

<summary><b>问题简述</b></summary>

```txt
给定一个单链表 L 的头节点 head , 单链表 L 表示为:
    L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为:
    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
不能只是单纯的改变节点内部的值, 而是需要实际的进行节点交换.
```

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1</b></summary>

1. 找中间节点;
2. 将第二段链表反转;
3. 然后合并两段链表;
- 细节:
    - 因为需要截断, 所以实际上找的是中间节点的前一个节点(偶数情况下)

<details><summary><b>Python</b></summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse(h):
            pre, cur = None, h
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        def get_mid(h):
            slow, fast = h, h.next  # 找中间节点的前一个节点
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        mid = get_mid(head)
        tmp = mid.next
        mid.next = None  # 截断
        mid = reverse(tmp)

        l, r = head, mid
        while r:  # len(l) >= len(r)
            l_nxt, r_nxt = l.next, r.next
            l.next, r.next = r, l_nxt  # 关键步骤: 将 r 接入 l
            l, r = l_nxt, r_nxt
```

</details>


<summary><b>思路2</b></summary>

1. 把节点存入列表;
2. 通过索引拼接节点;
- 细节:
    - 把节点存入数组后, 可以使用下标访问节点, 形如 `arr[i].next = ...`
    - 拼接节点时注意边界位置的操作;
    - 尾节点的截断;

<details><summary><b>Python</b></summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tmp = []
        cur = head
        while cur:
            tmp.append(cur)
            cur = cur.next

        l, r = 0, len(tmp) - 1
        while l < r:  # 退出循环时 l == r
            tmp[l].next = tmp[r]
            l += 1
            if l == r: break  # 易错点
            tmp[r].next = tmp[l]
            r -= 1

        # 退出循环时 l 刚好指在中间节点(奇数时), 或中间位置的下一个节点(偶数时)
        tmp[l].next = None  # 易错点
```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

- [链表操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

<details><summary><b>其他算法笔记</b></summary>

- [二分查找相关](../../../../notes/_archives/2025/10/二分查找备忘.md)  
- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>热门 (16)</b></summary>

> [[中等, LeetCode] 买卖股票的最佳时机 II 🔥](LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 全排列 🔥](../10/LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](../10/LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, 剑指Offer] 把字符串转换成整数 🔥](../01/剑指Offer_6700_中等_把字符串转换成整数.md)  
> [[中等, 牛客] 三数之和 🔥](../03/牛客_0054_中等_三数之和.md)  
> [[中等, 牛客] 把二叉树打印成多行 🔥](../03/牛客_0080_中等_把二叉树打印成多行.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](../10/LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](../10/LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, LeetCode] 编辑距离 🔥](LeetCode_0072_困难_编辑距离.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](../10/LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 平衡二叉树 🔥](../09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, 牛客] 两个链表的第一个公共结点 🔥](../03/牛客_0066_简单_两个链表的第一个公共结点.md)  
  > 

</details>

<details><summary><b>链表 (30)</b></summary>

> [[中等, LeetCode] 两数相加 🔥](../../2021/10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 分隔链表](../../2021/10/LeetCode_0086_中等_分隔链表.md)  
> [[中等, LeetCode] 删除链表中的节点](../../2025/10/LeetCode_0237_中等_删除链表中的节点.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, 剑指Offer] 复杂链表的复制 (深拷贝) 🔥](../../2021/12/剑指Offer_3500_中等_复杂链表的复制(深拷贝).md)  
> [[中等, 牛客] 划分链表](../01/牛客_0023_中等_划分链表.md)  
> [[中等, 牛客] 删除有序链表中重复的元素-I](../01/牛客_0025_中等_删除有序链表中重复的元素-I.md)  
> [[中等, 牛客] 删除有序链表中重复的元素-II](../01/牛客_0024_中等_删除有序链表中重复的元素-II.md)  
> [[中等, 牛客] 重排链表](../01/牛客_0002_中等_重排链表.md)  
> [[中等, 牛客] 链表中的节点每k个一组翻转](../03/牛客_0050_中等_链表中的节点每k个一组翻转.md)  
> [[中等, 牛客] 链表内指定区间反转](../01/牛客_0021_中等_链表内指定区间反转.md)  
> [[中等, 牛客] 链表相加(二)](../03/牛客_0040_中等_链表相加(二).md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](../10/LeetCode_0023_困难_合并K个升序链表.md)  
  > 
> [[简单, LeetCode] 反转链表 🔥](../10/LeetCode_0206_简单_反转链表.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 链表的中间结点](LeetCode_0876_简单_链表的中间结点.md)  
> [[简单, 剑指Offer] 两个链表的第一个公共节点](../01/剑指Offer_5200_简单_两个链表的第一个公共节点.md)  
> [[简单, 剑指Offer] 从尾到头打印链表](../../2021/11/剑指Offer_0600_简单_从尾到头打印链表.md)  
> [[简单, 剑指Offer] 删除链表的节点](../../2021/11/剑指Offer_1800_简单_删除链表的节点.md)  
> [[简单, 剑指Offer] 反转链表 🔥](../../2021/11/剑指Offer_2400_简单_反转链表.md)  
> [[简单, 剑指Offer] 合并两个排序的链表](../../2021/11/剑指Offer_2500_简单_合并两个排序的链表.md)  
> [[简单, 剑指Offer] 链表中倒数第k个节点](../../2021/11/剑指Offer_2200_简单_链表中倒数第k个节点.md)  
> [[简单, 牛客] 两个链表的第一个公共结点 🔥](../03/牛客_0066_简单_两个链表的第一个公共结点.md)  
> [[简单, 牛客] 判断一个链表是否为回文结构](../04/牛客_0096_简单_判断一个链表是否为回文结构.md)  
> [[简单, 牛客] 判断链表中是否有环](../01/牛客_0004_简单_判断链表中是否有环.md)  
> [[简单, 牛客] 单链表的排序 🔥](../03/牛客_0070_简单_单链表的排序.md)  
> [[简单, 牛客] 反转链表](../03/牛客_0078_简单_反转链表.md)  
> [[简单, 牛客] 合并两个排序的链表](../02/牛客_0033_简单_合并两个排序的链表.md)  
> [[简单, 牛客] 链表中环的入口结点](../01/牛客_0003_简单_链表中环的入口结点.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
