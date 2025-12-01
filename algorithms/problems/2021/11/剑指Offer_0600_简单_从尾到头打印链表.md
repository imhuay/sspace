## 从尾到头打印链表
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E6%A0%88/%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#栈队列)
[![](https://img.shields.io/static/v1?label=&message=%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2&color=blue&style=flat-square)](../../../README.md#深度优先搜索)
[![](https://img.shields.io/static/v1?label=&message=%E9%80%92%E5%BD%92&color=blue&style=flat-square)](../../../README.md#递归)
[![](https://img.shields.io/static/v1?label=&message=%E9%93%BE%E8%A1%A8&color=blue&style=flat-square)](../../../README.md#链表)
<!--END_SECTION:badge-->
<!--info
tags: [链表, 栈, DFS, 递归]
source: 剑指Offer
level: 简单
number: '0600'
name: 从尾到头打印链表
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
从尾到头打印链表 (用数组返回)
```

<details><summary><b>详细描述</b></summary>

```txt
输入一个链表的头节点, 从尾到头反过来返回每个节点的值 (用数组返回).

示例 1:
    输入: head = [1,3,2]
    输出: [2,3,1]

限制:
    0 <= 链表长度 <= 10000

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

</details>


<summary><b>思路</b></summary>

- 法1) 利用栈, 顺序入栈, 然后依次出栈即可
- 法2) 利用深度优先遍历思想 (二叉树的先序遍历)


<details><summary><b>Python: 栈</b></summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        # ret = []
        # for _ in range(len(stack)):  # 相当于逆序遍历
        #     ret.append(stack.pop())
        # return ret
        return stack[::-1]  # 与以上代码等价
```

</details>

<details><summary><b>Python: DFS、递归</b></summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None:
            return []

        ret = self.reversePrint(head.next)
        ret.append(head.val)

        return ret
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


<details><summary><b>栈/队列 (15)</b></summary>

> [[中等, 剑指Offer] 栈的压入、弹出序列 🔥](剑指Offer_3100_中等_栈的压入、弹出序列.md)  
> [[中等, 剑指Offer] 队列的最大值](../../2022/01/剑指Offer_5902_中等_队列的最大值.md)  
> [[中等, 牛客] 按之字形顺序打印二叉树](../../2022/01/牛客_0014_中等_按之字形顺序打印二叉树.md)  
> [[中等, 牛客] 栈和排序 🔥](../../2022/05/牛客_0115_中等_栈和排序.md)  
  > 
> [[困难, LeetCode] 最长有效括号 🔥](../../2022/10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, 牛客] 最长的括号子串](../../2022/03/牛客_0049_困难_最长的括号子串.md)  
  > 
> [[简单, LeetCode] 有效的括号 🔥](../../2022/03/LeetCode_0020_简单_有效的括号.md)  
> [[简单, 剑指Offer] 包含min函数的栈](剑指Offer_3000_简单_包含min函数的栈.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](剑指Offer_3201_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](剑指Offer_3202_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树 (之字形遍历)](剑指Offer_3203_简单_层序遍历二叉树(之字形遍历).md)  
> [[简单, 剑指Offer] 用两个栈实现队列](剑指Offer_0900_简单_用两个栈实现队列.md)  
> [[简单, 牛客] 包含min函数的栈](../../2022/04/牛客_0090_简单_包含min函数的栈.md)  
> [[简单, 牛客] 有效括号序列](../../2022/03/牛客_0052_简单_有效括号序列.md)  
> [[简单, 牛客] 用两个栈实现队列](../../2022/03/牛客_0076_简单_用两个栈实现队列.md)  
  > 

</details>

<details><summary><b>深度优先搜索 (19)</b></summary>

> [[中等, LeetCode] 括号生成 🔥](../../2022/10/LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](../../2022/10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 组合总和 🔥](../../2022/10/LeetCode_0039_中等_组合总和.md)  
> [[中等, LeetCode] 路径总和III](../../2022/06/LeetCode_0437_中等_路径总和III.md)  
> [[中等, 剑指Offer] 二叉树中和为某一值的路径](../12/剑指Offer_3400_中等_二叉树中和为某一值的路径.md)  
> [[中等, 剑指Offer] 字符串的排列 (全排列) 🔥](../12/剑指Offer_3800_中等_字符串的排列(全排列).md)  
> [[中等, 剑指Offer] 打印从1到最大的n位数 (N叉树的遍历)](剑指Offer_1700_中等_打印从1到最大的n位数(N叉树的遍历).md)  
> [[中等, 剑指Offer] 机器人的运动范围](剑指Offer_1300_中等_机器人的运动范围.md)  
> [[中等, 剑指Offer] 矩阵中的路径](剑指Offer_1200_中等_矩阵中的路径.md)  
> [[中等, 牛客] 二叉树中和为某一值的路径(二)](../../2022/01/牛客_0008_中等_二叉树中和为某一值的路径(二).md)  
> [[中等, 牛客] 二叉树根节点到叶子节点的所有路径和](../../2022/01/牛客_0005_中等_二叉树根节点到叶子节点的所有路径和.md)  
> [[中等, 牛客] 字符串的排列 🔥](../../2022/05/牛客_0121_中等_字符串的排列.md)  
> [[中等, 牛客] 实现二叉树先序、中序、后序遍历](../../2022/03/牛客_0045_中等_实现二叉树先序、中序、后序遍历.md)  
> [[中等, 牛客] 岛屿数量 🔥](../../2022/04/牛客_0109_中等_岛屿数量.md)  
> [[中等, 牛客] 数字字符串转化成IP地址](../../2022/01/牛客_0020_中等_数字字符串转化成IP地址.md)  
  > 
> [[困难, 牛客] 多叉树的直径](../../2022/04/牛客_0099_困难_多叉树的直径.md)  
  > 
> [[简单, LeetCode] 二叉树的最小深度](../../2022/07/LeetCode_0111_简单_二叉树的最小深度.md)  
> [[简单, 剑指Offer] 二叉搜索树的第k大节点](../../2022/01/剑指Offer_5400_简单_二叉搜索树的第k大节点.md)  
> [[简单, 牛客] 二叉树中和为某一值的路径(一)](../../2022/01/牛客_0009_简单_二叉树中和为某一值的路径(一).md)  
  > 

</details>

<details><summary><b>递归 (25)</b></summary>

> [[中等, LeetCode] 全排列 🔥](../../2022/10/LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](../../2022/10/LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 分割回文串](../../2025/11/LeetCode_0131_中等_分割回文串.md)  
> [[中等, LeetCode] 子集](../../2025/11/LeetCode_0078_中等_子集.md)  
> [[中等, LeetCode] 组合](../../2025/11/LeetCode_0077_中等_组合.md)  
> [[中等, LeetCode] 组合总和 II 🔥](../../2022/10/LeetCode_0040_中等_组合总和II.md)  
> [[中等, LeetCode] 组合总和 III](../../2025/11/LeetCode_0216_中等_组合总和III.md)  
> [[中等, LeetCode] 组合总和 🔥](../../2022/10/LeetCode_0039_中等_组合总和.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](../12/剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 剑指Offer] 树的子结构](剑指Offer_2600_中等_树的子结构.md)  
> [[中等, 剑指Offer] 求1~n的和](../../2022/01/剑指Offer_6400_中等_求1~n的和.md)  
> [[中等, 牛客] 加起来和为目标值的组合(二)](../../2022/03/牛客_0046_中等_加起来和为目标值的组合(二).md)  
> [[中等, 牛客] 括号生成](../../2022/02/牛客_0026_中等_括号生成.md)  
> [[中等, 牛客] 有重复项数字的全排列](../../2022/03/牛客_0042_中等_有重复项数字的全排列.md)  
> [[中等, 牛客] 汉诺塔问题 🔥](../../2022/03/牛客_0067_中等_汉诺塔问题.md)  
> [[中等, 牛客] 没有重复项数字的全排列](../../2022/03/牛客_0043_中等_没有重复项数字的全排列.md)  
> [[中等, 牛客] 集合的所有子集(一)](../../2022/02/牛客_0027_中等_集合的所有子集(一).md)  
  > 
> [[困难, LeetCode] 51](../../2025/11/LeetCode_N 皇后_困难_51.md)  
> [[困难, 剑指Offer] 正则表达式匹配](剑指Offer_1900_困难_正则表达式匹配.md)  
> [[困难, 牛客] N皇后问题](../../2022/03/牛客_0039_困难_N皇后问题.md)  
> [[困难, 牛客] 数独](../../2022/03/牛客_0047_困难_数独.md)  
  > 
> [[简单, LeetCode] 二叉树的最大深度 🔥](../../2022/07/LeetCode_0104_简单_二叉树的最大深度.md)  
> [[简单, 剑指Offer] 二叉树的镜像](剑指Offer_2700_简单_二叉树的镜像.md)  
> [[简单, 剑指Offer] 对称的二叉树](剑指Offer_2800_简单_对称的二叉树.md)  
  > 

</details>

<details><summary><b>链表 (30)</b></summary>

> [[中等, LeetCode] 两数相加 🔥](../10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 分隔链表](../10/LeetCode_0086_中等_分隔链表.md)  
> [[中等, LeetCode] 删除链表中的节点](../../2025/10/LeetCode_0237_中等_删除链表中的节点.md)  
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
> [[简单, 剑指Offer] 删除链表的节点](剑指Offer_1800_简单_删除链表的节点.md)  
> [[简单, 剑指Offer] 反转链表 🔥](剑指Offer_2400_简单_反转链表.md)  
> [[简单, 剑指Offer] 合并两个排序的链表](剑指Offer_2500_简单_合并两个排序的链表.md)  
> [[简单, 剑指Offer] 链表中倒数第k个节点](剑指Offer_2200_简单_链表中倒数第k个节点.md)  
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
