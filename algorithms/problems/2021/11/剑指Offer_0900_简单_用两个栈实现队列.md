## 用两个栈实现队列
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=yellow&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E6%A0%88/%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#栈队列)
[![](https://img.shields.io/static/v1?label=&message=%E8%AE%BE%E8%AE%A1&color=blue&style=flat-square)](../../../README.md#设计)
<!--END_SECTION:badge-->
<!--info
tags: [栈, 队列, 设计]
source: 剑指Offer
level: 简单
number: '0900'
name: 用两个栈实现队列
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
用两个栈实现一个队列.
队列包含两个函数 appendTail 和 deleteHead(若队列中没有元素, deleteHead 操作返回 -1 )
```

<details><summary><b>详细描述</b></summary>

```txt
用两个栈实现一个队列. 队列的声明如下, 请实现它的两个函数 appendTail 和 deleteHead , 分别完成在队列尾部插入整数和在队列头部删除整数的功能. (若队列中没有元素, deleteHead 操作返回 -1 )

示例 1:
    输入:
    ["CQueue","appendTail","deleteHead","deleteHead"]
    [[],[3],[],[]]
    输出: [null,null,3,-1]
示例 2:
    输入:
    ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
    [[],[],[5],[2],[],[]]
    输出: [null,-1,null,null,5,2]

提示:
    1 <= values <= 10000
    最多会对 appendTail、deleteHead 进行 10000 次调用

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

</details>


<summary><b>思路</b></summary>

- 栈: 先进后出; 队列: 先进先出; 换言之, 队列就是倒序输出的栈;
- 利用双栈可实现倒序输出: 维护两个栈 A 和 B, 将 A 中元素依次弹出并压入栈 B, 再依次弹出 B 中元素, 即实现了对栈 A 元素的倒序输出, 即实现了队列的性质;


<details><summary><b>Python</b></summary>

```python
class CQueue:
    def __init__(self):
        self.I = []  # 入栈
        self.O = []  # 出栈

    def appendTail(self, value: int) -> None:
        self.I.append(value)  # 新元素全部加到 I

    def deleteHead(self) -> int:
        if self.O:  # 如果 O 不为空
            return self.O.pop()  # 弹出栈顶元素

        if not self.I:  # 如果 I 为空, 说明队列为空
            return -1

        while self.I:  # 如果 I 不为空, 但 O 为空, 此时将 I 中元素依次加入 O  
            self.O.append(self.I.pop())
        return self.O.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

</details>


<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>栈/队列</b></summary>

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
> [[简单, 剑指Offer] 包含min函数的栈](剑指Offer_3000_简单_包含min函数的栈.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](剑指Offer_3201_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](剑指Offer_3202_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树 (之字形遍历)](剑指Offer_3203_简单_层序遍历二叉树(之字形遍历).md)  
> [[简单, 牛客] 包含min函数的栈](../../2022/04/牛客_0090_简单_包含min函数的栈.md)  
> [[简单, 牛客] 有效括号序列](../../2022/03/牛客_0052_简单_有效括号序列.md)  
> [[简单, 牛客] 用两个栈实现队列](../../2022/03/牛客_0076_简单_用两个栈实现队列.md)  
  > 

</details>
<details><summary><b>栈/队列</b></summary>

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
> [[简单, 剑指Offer] 包含min函数的栈](剑指Offer_3000_简单_包含min函数的栈.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](剑指Offer_3201_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](剑指Offer_3202_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树 (之字形遍历)](剑指Offer_3203_简单_层序遍历二叉树(之字形遍历).md)  
> [[简单, 牛客] 包含min函数的栈](../../2022/04/牛客_0090_简单_包含min函数的栈.md)  
> [[简单, 牛客] 有效括号序列](../../2022/03/牛客_0052_简单_有效括号序列.md)  
> [[简单, 牛客] 用两个栈实现队列](../../2022/03/牛客_0076_简单_用两个栈实现队列.md)  
  > 

</details>
<details><summary><b>设计</b></summary>

> [[中等, 剑指Offer] 队列的最大值](../../2022/01/剑指Offer_5902_中等_队列的最大值.md)  
> [[中等, 牛客] 字典树的实现](../../2022/05/牛客_0124_中等_字典树的实现.md)  
  > 
> [[困难, 剑指Offer] 数据流中的中位数](../12/剑指Offer_4100_困难_数据流中的中位数.md)  
> [[困难, 牛客] 设计LFU缓存结构 🔥](../../2022/04/牛客_0094_困难_设计LFU缓存结构.md)  
> [[困难, 牛客] 设计LRU缓存结构 🔥](../../2022/04/牛客_0093_困难_设计LRU缓存结构.md)  
  > 
> [[简单, 剑指Offer] 包含min函数的栈](剑指Offer_3000_简单_包含min函数的栈.md)  
  > 

</details>
<!--END_SECTION:relate-->