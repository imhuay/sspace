## <title - autoUpdate>
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [链表]
source: LeetCode
level: 中等
number: '237'
name: 删除链表中的节点
companies: []
-->

> [237. 删除链表中的节点 - 力扣（LeetCode）](https://leetcode.cn/problems/delete-node-in-a-linked-list/)

<summary><b>问题简述</b></summary>

```txt
删除给定节点, 但无法访问头结点.
```

<!-- 
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

<summary><b>思路</b></summary>

- **没有什么特殊的方法**: 和下一个节点交换值, 然后删除下一个节点.

<details><summary><b>Python</b></summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```

</details>


<!--START_SECTION:relate_note-->
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
<!--END_SECTION:relate_problem-->