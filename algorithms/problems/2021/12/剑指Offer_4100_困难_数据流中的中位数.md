## 数据流中的中位数
<!--START_SECTION:badge-->

![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&label_color=gray&color=yellow&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&label_color=gray&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E8%AE%BE%E8%AE%A1&label_color=gray&color=blue&style=flat-square)](../../../README.md#设计)
[![](https://img.shields.io/static/v1?label=&message=%E5%A0%86/%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97&label_color=gray&color=blue&style=flat-square)](../../../README.md#堆优先队列)

<!--END_SECTION:badge-->
<!--info
tags: [设计, 堆]
source: 剑指Offer
level: 困难
number: '4100'
name: 数据流中的中位数
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
设计一个支持以下两种操作的数据结构：
    void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    double findMedian() - 返回目前所有元素的中位数。
```

<details><summary><b>详细描述</b></summary>

```txt
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
    void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    double findMedian() - 返回目前所有元素的中位数。
示例 1：
    输入：
    ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
    [[],[1],[2],[],[3],[]]
    输出：[null,null,null,1.50000,null,2.00000]
示例 2：
    输入：
    ["MedianFinder","addNum","findMedian","addNum","findMedian"]
    [[],[2],[],[3],[]]
    输出：[null,null,2.00000,null,2.50000]
 
限制：
    最多会对 addNum、findMedian 进行 50000 次调用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 分别使用一个大顶堆存放较小的一半（堆顶为其中的最大值），和一个小顶堆存放较大的一半（堆顶为其中的最小值）；
- 动态保持两个堆的元素数量相等或差1（为了减少判断，可以始终保持固定的堆数量多1）

<details><summary><b>Python：优化前</b></summary>

- 这份代码的逻辑非常直白，看上起也比较啰嗦；

```python
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []  # 大顶堆，维护小于中位数的部分
        self.hi = []  # 小顶堆，维护大于中位数的部分
        self.cnt = 0  # 计数

    def addNum(self, num: int) -> None:
        if self.cnt == 0:  # 初始化
            heapq.heappush(self.hi, num)
            self.cnt += 1
            return

        if num > self.findMedian():  # to hi
            if self.cnt % 2:
                heapq.heappush(self.hi, num)
                tmp = heapq.heappop(self.hi)
                heapq.heappush(self.lo, -tmp)
            else:
                heapq.heappush(self.hi, num)
        else:  # to lo
            if self.cnt % 2:
                heapq.heappush(self.lo, -num)
            else:
                heapq.heappush(self.lo, -num)
                tmp = heapq.heappop(self.lo)
                heapq.heappush(self.hi, -tmp)

        self.cnt += 1

    def findMedian(self) -> float:
        if self.cnt % 2:
            return self.hi[0]
        else:
            return (-self.lo[0] + self.hi[0]) / 2

```

</details>


<details><summary><b>Python：优化后</b></summary>

> [数据流中的中位数（优先队列 / 堆，清晰图解）](https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/mian-shi-ti-41-shu-ju-liu-zhong-de-zhong-wei-shu-y/)

```python
from heapq import *

class MedianFinder:
    def __init__(self):
        self.hi = []  # 小顶堆，保存较大的一半
        self.lo = []  # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        # 开始时，都为 0，先存入 self.lo，在转移到 self.hi
        if len(self.hi) == len(self.lo):
            heappush(self.lo, -num)
            heappush(self.hi, -heappop(self.lo))
        else:
            heappush(self.hi, num)
            heappush(self.lo, -heappop(self.hi))            


    def findMedian(self) -> float:
        if len(self.hi) != len(self.lo):
            return self.hi[0]
        else:
            return (-self.lo[0] + self.hi[0]) / 2

```

</details>
<!--START_SECTION:relate-->

---

### 相关主题

<details><summary><b>设计</b></summary>

> [[中等, 剑指Offer] 队列的最大值](../../2022/01/剑指Offer_5902_中等_队列的最大值.md)  
> [[中等, 牛客] 字典树的实现](../../2022/05/牛客_0124_中等_字典树的实现.md)  
  > 
> [[困难, 牛客] 设计LFU缓存结构 🔥](../../2022/04/牛客_0094_困难_设计LFU缓存结构.md)  
> [[困难, 牛客] 设计LRU缓存结构 🔥](../../2022/04/牛客_0093_困难_设计LRU缓存结构.md)  
  > 
> [[简单, 剑指Offer] 包含min函数的栈](../11/剑指Offer_3000_简单_包含min函数的栈.md)  
> [[简单, 剑指Offer] 用两个栈实现队列](../11/剑指Offer_0900_简单_用两个栈实现队列.md)  
  > 

</details>
<details><summary><b>堆/优先队列</b></summary>

> [[中等, 剑指Offer2] 数组中的第K大的数字](../../2022/09/剑指Offer2_076_中等_数组中的第K大的数字.md)  
> [[中等, 牛客] 字符串出现次数的TopK问题](../../2022/04/牛客_0097_中等_字符串出现次数的TopK问题.md)  
  > 
> [[困难, LeetCode] 合并K个升序链表 🔥](../../2022/10/LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](../../2022/10/LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, 牛客] 合并k个已排序的链表](../../2022/03/牛客_0051_困难_合并k个已排序的链表.md)  
> [[困难, 牛客] 滑动窗口的最大值](../../2022/03/牛客_0082_困难_滑动窗口的最大值.md)  
  > 
> [[简单, 剑指Offer] 最小的k个数（partition操作） 🔥](剑指Offer_4000_简单_最小的k个数（partition操作）.md)  
> [[简单, 牛客] 三个数的最大乘积](../../2022/04/牛客_0106_简单_三个数的最大乘积.md)  
  > 

</details>

<!--END_SECTION:relate-->