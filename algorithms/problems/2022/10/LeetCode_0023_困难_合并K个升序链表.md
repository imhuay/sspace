## 合并K个升序链表
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&color=red&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
[![](https://img.shields.io/static/v1?label=&message=%E5%A0%86/%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#堆优先队列)
[![](https://img.shields.io/static/v1?label=&message=%E7%83%AD%E9%97%A8&color=blue&style=flat-square)](../../../README.md#热门)
[![](https://img.shields.io/static/v1?label=&message=%E9%93%BE%E8%A1%A8&color=blue&style=flat-square)](../../../README.md#链表)
<!--END_SECTION:badge-->
<!--info
tags: [链表, 堆, lc100, 热门]
source: LeetCode
level: 困难
number: '0023'
name: 合并K个升序链表
companies: []
-->

> [23. 合并K个升序链表 - 力扣 (LeetCode) ](https://leetcode.cn/problems/merge-k-sorted-lists)

<summary><b>问题简述</b></summary>

```txt
给你一个链表数组, 每个链表都已经按升序排列.

请你将所有链表合并到一个升序链表中, 返回合并后的链表.
```

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 维护一个优先队列 (最小堆), 队列中每个元素为各链表中的当前节点;
- 依次弹出队首元素, 如果当前队列还有元素就继续加入队列;
- 提示:
    - 优先队列的内部移动依赖于比较运算符;
    - Python 标准库提供了一个简单的堆队列实现 [`heapq`](https://docs.python.org/zh-cn/3/library/heapq.html);

<details><summary><b>Python (写法 1, 不重载运算符) </b></summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        import heapq

        h = []  # 模拟堆
        cnt = 0  # 节点计数, 防止对 node 排序, 因为 node 没有重载 __lt__ 运算符
        for node in lists:
            if node:
                heapq.heappush(h, (node.val, cnt, node))  # 如果没有 cnt, 那么当 val 相等时, 就会比较 node
                cnt += 1

        dummy = cur = ListNode()
        while h:
            _, _, node = heapq.heappop(h)  # 弹出堆顶节点 (当前最小
            cur.next = node
            cur = cur.next
            if (node := node.next):  # 如果该链表还有元素, 继续加入堆
                heapq.heappush(h, (node.val, cnt, node))
                cnt += 1

        return dummy.next
```

</details>


<details><summary><b>Python (写法 2, 重载运算符) </b></summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        import heapq

        # 重载 ListNode 的 < 运算符
        ListNode.__lt__ = lambda o1, o2: o1.val < o2.val

        h = []  # 模拟堆
        for node in lists:
            if node:
                heapq.heappush(h, node)  # 因为重载了 < 运算符, 直接加入节点

        dummy = cur = ListNode()
        while h:
            node = heapq.heappop(h)  # 弹出堆顶节点 (当前最小)
            cur.next = node
            cur = cur.next
            if (node := node.next):  # 如果该链表还有元素, 继续加入堆
                heapq.heappush(h, node)

        return dummy.next
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


<details><summary><b>LeetCode Hot 100 (32)</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 两数相加 🔥](../../2021/10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 全排列 🔥](LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 和为K的子数组 🔥](../../2025/11/LeetCode_0560_中等_和为K的子数组.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 字母异位词分组 🔥](LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 找到字符串中所有字母异位词 🔥](../../2025/11/LeetCode_0438_中等_找到字符串中所有字母异位词.md)  
> [[中等, LeetCode] 括号生成 🔥](LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, LeetCode] 无重复字符的最长子串 🔥](../02/LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 最长连续序列 🔥](../../2025/11/LeetCode_0128_中等_最长连续序列.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, LeetCode] 组合总和 II 🔥](LeetCode_0040_中等_组合总和II.md)  
> [[中等, LeetCode] 组合总和 🔥](LeetCode_0039_中等_组合总和.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 最小覆盖子串 🔥](../../2025/11/LeetCode_0076_困难_最小覆盖子串.md)  
> [[困难, LeetCode] 最长有效括号 🔥](LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, 牛客] 最小覆盖子串 🔥](../02/牛客_0028_困难_最小覆盖子串.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 有效的括号 🔥](../03/LeetCode_0020_简单_有效的括号.md)  
> [[简单, LeetCode] 移动零 🔥](../../2025/11/LeetCode_0283_简单_移动零.md)  
  > 

</details>

<details><summary><b>堆/优先队列 (8)</b></summary>

> [[中等, 剑指Offer2] 数组中的第K大的数字](../09/剑指Offer2_076_中等_数组中的第K大的数字.md)  
> [[中等, 牛客] 字符串出现次数的TopK问题](../04/牛客_0097_中等_字符串出现次数的TopK问题.md)  
  > 
> [[困难, LeetCode] 滑动窗口最大值 🔥](LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, 剑指Offer] 数据流中的中位数](../../2021/12/剑指Offer_4100_困难_数据流中的中位数.md)  
> [[困难, 牛客] 合并k个已排序的链表](../03/牛客_0051_困难_合并k个已排序的链表.md)  
> [[困难, 牛客] 滑动窗口的最大值](../03/牛客_0082_困难_滑动窗口的最大值.md)  
  > 
> [[简单, 剑指Offer] 最小的k个数 (partition操作) 🔥](../../2021/12/剑指Offer_4000_简单_最小的k个数(partition操作).md)  
> [[简单, 牛客] 三个数的最大乘积](../04/牛客_0106_简单_三个数的最大乘积.md)  
  > 

</details>

<details><summary><b>热门 (16)</b></summary>

> [[中等, LeetCode] 买卖股票的最佳时机 II 🔥](../06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
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
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 平衡二叉树 🔥](../09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, 牛客] 两个链表的第一个公共结点 🔥](../03/牛客_0066_简单_两个链表的第一个公共结点.md)  
  > 

</details>

<details><summary><b>链表 (30)</b></summary>

> [[中等, LeetCode] 两数相加 🔥](../../2021/10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 分隔链表](../../2021/10/LeetCode_0086_中等_分隔链表.md)  
> [[中等, LeetCode] 删除链表中的节点](../../2025/10/LeetCode_0237_中等_删除链表中的节点.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 重排链表 🔥](../06/LeetCode_0143_中等_重排链表.md)  
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
  > 
> [[简单, LeetCode] 反转链表 🔥](LeetCode_0206_简单_反转链表.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 链表的中间结点](../06/LeetCode_0876_简单_链表的中间结点.md)  
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
