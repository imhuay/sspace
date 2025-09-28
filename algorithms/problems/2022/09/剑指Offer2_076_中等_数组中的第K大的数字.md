## 数组中的第K大的数字
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer2&color=green&style=flat-square)](../../../README.md#剑指offer2)
[![](https://img.shields.io/static/v1?label=&message=%E5%A0%86/%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#堆优先队列)
[![](https://img.shields.io/static/v1?label=&message=%E5%88%86%E6%B2%BB&color=blue&style=flat-square)](../../../README.md#分治)
[![](https://img.shields.io/static/v1?label=&message=%E6%8E%92%E5%BA%8F&color=blue&style=flat-square)](../../../README.md#排序)
<!--END_SECTION:badge-->
<!--info
tags: [堆, 分治, 快排]
source: 剑指Offer2
level: 中等
number: '076'
name: 数组中的第K大的数字
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定整数数组 nums 和整数 k, 请返回数组中第 k 个最大的元素.
```

<details><summary><b>详细描述</b></summary>

```txt
给定整数数组 nums 和整数 k, 请返回数组中第 k 个最大的元素.

请注意, 你需要找的是数组排序后的第 k 个最大的元素, 而不是第 k 个不同的元素.

示例 1:
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5
示例 2:
    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4

提示:
    1 <= k <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/xx4gT2
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>


<summary><b>思路</b></summary>

<details><summary><b>思路1: partition操作 (分治) </b></summary>

- partition操作描述: 先随机确定一个锚点, 然后将数组划分为小于锚点和大于锚点的两部分呢;

```python
import random


class Solution:
    """"""

    def findKthLargest(self, nums: List[int], k: int) -> int:  # noqa
        """"""
        lo, hi = 0, len(nums) - 1

        while True:  # 第 k 大, 排序后期下标应该是 k - 1
            idx = self.partition(nums, lo, hi)
            if idx + 1 == k:
                return nums[idx]
            elif idx + 1 < k:
                lo = idx + 1
            else:
                hi = idx - 1

    def partition(self, nums: List[int], lo: int, hi: int) -> int:
        """"""
        # === 挑选锚点 ===
        # 方式1) 默认选 lo 作为锚点
        # pivot = nums[lo]

        # 方式2) 随机选择一个锚点, 并把锚点固定到首位或末位, 这里交换到首位
        flag = random.randint(lo, hi)
        pivot = nums[flag]
        nums[flag], nums[lo] = nums[lo], nums[flag]

        # === partition 操作 ===
        # 方式1) 单向遍历
        idx = lo  # 记录锚点在数组中的升序顺位
        for i in range(lo + 1, hi + 1):
            if nums[i] > pivot:  # 找到一个大于锚点的值
                idx += 1
                nums[idx], nums[i] = nums[i], nums[idx]

        nums[idx], nums[lo] = nums[lo], nums[idx]  # 把锚点交换到 idx 的位置

        return idx

        # 方式2) 左右交换
        # l, r = lo, hi
        # while l < r:
        #     while l < r and nums[r] <= pivot:
        #         r -= 1
        #     while l < r and nums[l] >= pivot:
        #         l += 1
        #     if l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        # nums[lo], nums[l] = nums[l], nums[lo]
        #
        # return l
```

</details>


<details><summary><b>思路2: 大顶堆 (Python, 调库) </b></summary>

```python
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """"""
        heap = []

        for x in nums:
            heapq.heappush(heap, -x)  # 默认是小顶堆, 这里传入 -x, 模拟大顶堆

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heap[0]
```

</details>



<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>堆/优先队列</b></summary>

> [[中等, 牛客] 字符串出现次数的TopK问题](../04/牛客_0097_中等_字符串出现次数的TopK问题.md)  
  > 
> [[困难, LeetCode] 合并K个升序链表 🔥](../10/LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](../10/LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, 剑指Offer] 数据流中的中位数](../../2021/12/剑指Offer_4100_困难_数据流中的中位数.md)  
> [[困难, 牛客] 合并k个已排序的链表](../03/牛客_0051_困难_合并k个已排序的链表.md)  
> [[困难, 牛客] 滑动窗口的最大值](../03/牛客_0082_困难_滑动窗口的最大值.md)  
  > 
> [[简单, 剑指Offer] 最小的k个数 (partition操作) 🔥](../../2021/12/剑指Offer_4000_简单_最小的k个数(partition操作).md)  
> [[简单, 牛客] 三个数的最大乘积](../04/牛客_0106_简单_三个数的最大乘积.md)  
  > 

</details>
<details><summary><b>分治</b></summary>

> [[中等, 剑指Offer] 重建二叉树 🔥](../../2021/11/剑指Offer_0700_中等_重建二叉树.md)  
  > 
> [[困难, 剑指Offer] 数组中的逆序对 🔥](../01/剑指Offer_5100_困难_数组中的逆序对.md)  
  > 
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](../../2021/12/剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
  > 

</details>
<details><summary><b>排序</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](../10/LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, 剑指Offer] 把数组排成最小的数](../../2021/12/剑指Offer_4500_中等_把数组排成最小的数.md)  
> [[中等, 牛客] 合并区间](../02/牛客_0037_中等_合并区间.md)  
> [[中等, 牛客] 字符串出现次数的TopK问题](../04/牛客_0097_中等_字符串出现次数的TopK问题.md)  
> [[中等, 牛客] 寻找第K大](../04/牛客_0088_中等_寻找第K大.md)  
> [[中等, 牛客] 拼接所有的字符串产生字典序最小的字符串](../04/牛客_0085_中等_拼接所有的字符串产生字典序最小的字符串.md)  
> [[中等, 牛客] 数组中的逆序对](../05/牛客_0118_中等_数组中的逆序对.md)  
> [[中等, 牛客] 最大数](../04/牛客_0111_中等_最大数.md)  
> [[中等, 牛客] 最小的K个数](../05/牛客_0119_中等_最小的K个数.md)  
  > 
> [[简单, 剑指Offer] 扑克牌中的顺子](../01/剑指Offer_6100_简单_扑克牌中的顺子.md)  
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](../../2021/12/剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
> [[简单, 剑指Offer] 最小的k个数 (partition操作) 🔥](../../2021/12/剑指Offer_4000_简单_最小的k个数(partition操作).md)  
> [[简单, 牛客] 三个数的最大乘积](../04/牛客_0106_简单_三个数的最大乘积.md)  
> [[简单, 程序员面试金典] 判定字符是否唯一](程序员面试金典_0101_简单_判定字符是否唯一.md)  
  > 

</details>
<!--END_SECTION:relate-->