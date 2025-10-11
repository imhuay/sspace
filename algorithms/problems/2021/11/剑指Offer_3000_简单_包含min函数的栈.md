## 包含min函数的栈
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E6%95%B0%E7%BB%84/%E7%9F%A9%E9%98%B5&color=blue&style=flat-square)](../../../README.md#数组矩阵)
[![](https://img.shields.io/static/v1?label=&message=%E6%A0%88/%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#栈队列)
[![](https://img.shields.io/static/v1?label=&message=%E8%AE%BE%E8%AE%A1&color=blue&style=flat-square)](../../../README.md#设计)
<!--END_SECTION:badge-->
<!--info
tags: [栈, 数组, 设计]
source: 剑指Offer
level: 简单
number: '3000'
name: 包含min函数的栈
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
实现栈的 pop 和 push 方法, 同时实现一个 min 方法, 返回栈中的最小值, min、push 及 pop 的时间复杂度都是 O(1).
```

<details><summary><b>详细描述</b></summary>

```txt
定义栈的数据结构, 请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中, 调用 min、push 及 pop 的时间复杂度都是 O(1).

示例:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.min();     --> 返回 -3.
    minStack.pop();
    minStack.top();     --> 返回 0.
    minStack.min();     --> 返回 -2.

提示:
    - 各函数的调用总次数不超过 20000 次
    - pop、top 和 min 操作总是在 非空栈 上调用.

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 使用两个 list: Buf 和 Min; 其中 Buf 正常模拟栈, Min 也是一个栈, 但是它只会将**小于等于栈顶**的元素入栈;
- 当 Buf 的出栈元素等于 Min 的栈顶元素时, Min 也出栈;
- Python 中 list 自带的 `append` 和 `pop` 方法默认行为就是栈的 `push` 和 `pop`, `top` 方法返回 `Buf[-1]` 即可;

<details><summary><b>Python</b></summary>

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Buf = []
        self.Min = []

    def push(self, x: int) -> None:
        self.Buf.append(x)
        if not self.Min or x <= self.Min[-1]:  # 注意这里是小于等于
            self.Min.append(x)

    def pop(self) -> None:
        x = self.Buf.pop()
        if x == self.Min[-1]:
            self.Min.pop()

    def top(self) -> int:
        return self.Buf[-1]

    def min(self) -> int:
        return self.Min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

> 🌧️ _暂无主题相关的笔记_


<details><summary><b>其他算法笔记</b></summary>

- [从暴力递归到动态规划](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表常用操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>数组/矩阵 (11)</b></summary>

> [[中等, LeetCode] 从魔法师身上吸取的最大能量](../../2025/10/LeetCode_3147_中等_从魔法师身上吸取的最大能量.md)  
> [[中等, LeetCode] 矩阵置零](../../2025/10/LeetCode_0073_中等_矩阵置零.md)  
> [[中等, 剑指Offer] 栈的压入、弹出序列 🔥](剑指Offer_3100_中等_栈的压入、弹出序列.md)  
> [[中等, 剑指Offer] 顺时针打印矩阵 (3种思路4个写法) 🔥](剑指Offer_2900_中等_顺时针打印矩阵(3种思路4个写法).md)  
> [[中等, 牛客] 旋转数组](../../2022/04/牛客_0110_中等_旋转数组.md)  
> [[中等, 牛客] 缺失的第一个正整数](../../2022/02/牛客_0030_中等_缺失的第一个正整数.md)  
> [[中等, 牛客] 螺旋矩阵](../../2022/03/牛客_0038_中等_螺旋矩阵.md)  
> [[中等, 牛客] 调整数组顺序使奇数位于偶数前面(一)](../../2022/03/牛客_0077_中等_调整数组顺序使奇数位于偶数前面(一).md)  
  > 
> [[简单, 剑指Offer] 调整数组顺序使奇数位于偶数前面](剑指Offer_2100_简单_调整数组顺序使奇数位于偶数前面.md)  
> [[简单, 牛客] 最长公共前缀](../../2022/03/牛客_0055_简单_最长公共前缀.md)  
> [[简单, 牛客] 顺时针旋转矩阵](../../2022/01/牛客_0018_简单_顺时针旋转矩阵.md)  
  > 

</details>

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
> [[简单, 剑指Offer] 从尾到头打印链表](剑指Offer_0600_简单_从尾到头打印链表.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](剑指Offer_3201_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](剑指Offer_3202_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树 (之字形遍历)](剑指Offer_3203_简单_层序遍历二叉树(之字形遍历).md)  
> [[简单, 剑指Offer] 用两个栈实现队列](剑指Offer_0900_简单_用两个栈实现队列.md)  
> [[简单, 牛客] 包含min函数的栈](../../2022/04/牛客_0090_简单_包含min函数的栈.md)  
> [[简单, 牛客] 有效括号序列](../../2022/03/牛客_0052_简单_有效括号序列.md)  
> [[简单, 牛客] 用两个栈实现队列](../../2022/03/牛客_0076_简单_用两个栈实现队列.md)  
  > 

</details>

<details><summary><b>设计 (6)</b></summary>

> [[中等, 剑指Offer] 队列的最大值](../../2022/01/剑指Offer_5902_中等_队列的最大值.md)  
> [[中等, 牛客] 字典树的实现](../../2022/05/牛客_0124_中等_字典树的实现.md)  
  > 
> [[困难, 剑指Offer] 数据流中的中位数](../12/剑指Offer_4100_困难_数据流中的中位数.md)  
> [[困难, 牛客] 设计LFU缓存结构 🔥](../../2022/04/牛客_0094_困难_设计LFU缓存结构.md)  
> [[困难, 牛客] 设计LRU缓存结构 🔥](../../2022/04/牛客_0093_困难_设计LRU缓存结构.md)  
  > 
> [[简单, 剑指Offer] 用两个栈实现队列](剑指Offer_0900_简单_用两个栈实现队列.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
