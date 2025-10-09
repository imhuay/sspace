## 滑动窗口最大值
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&color=yellow&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%A0%86/%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#堆优先队列)
[![](https://img.shields.io/static/v1?label=&message=%E7%83%AD%E9%97%A8&color=blue&style=flat-square)](../../../README.md#热门)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [堆, 热门]
source: LeetCode
level: 困难
number: '0239'
name: 滑动窗口最大值
companies: [Soul]
-->

> [239. 滑动窗口最大值 - 力扣 (LeetCode) ](https://leetcode.cn/problems/sliding-window-maximum/)

<summary><b>问题简述</b></summary>

```txt
给你一个整数数组 nums, 有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧.
你只可以看到在滑动窗口内的 k 个数字. 滑动窗口每次只向右移动一位.
返回 滑动窗口中的最大值.
```

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路 1: 堆/优先队列</b></summary>

- 维护一个最大堆保存窗口内的值;
- 难点是如何保证堆内 (主要是堆顶) 的值正好在窗口内;
    - 方法是同时保存值的索引, 利用索引判断当前堆顶值是否在窗口内, 详见代码;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        import heapq

        h = []
        for i in range(k):
            heapq.heappush(h, (-nums[i], i))

        ret = [-h[0][0]]
        for i in range(k, len(nums)):
            while h and h[0][1] <= i - k:
                heapq.heappop(h)
            heapq.heappush(h, (-nums[i], i))
            ret.append(-h[0][0])

        return ret
```

</details>


<summary><b>思路 2: 单调队列</b></summary>

> [滑动窗口最大值 (方法二) - 力扣官方题解](https://leetcode.cn/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/)

<!--
<summary><b>相关问题</b></summary>

-->

<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>堆/优先队列</b></summary>

> [[中等, 剑指Offer2] 数组中的第K大的数字](../09/剑指Offer2_076_中等_数组中的第K大的数字.md)  
> [[中等, 牛客] 字符串出现次数的TopK问题](../04/牛客_0097_中等_字符串出现次数的TopK问题.md)  
  > 
> [[困难, LeetCode] 合并K个升序链表 🔥](LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, 剑指Offer] 数据流中的中位数](../../2021/12/剑指Offer_4100_困难_数据流中的中位数.md)  
> [[困难, 牛客] 合并k个已排序的链表](../03/牛客_0051_困难_合并k个已排序的链表.md)  
> [[困难, 牛客] 滑动窗口的最大值](../03/牛客_0082_困难_滑动窗口的最大值.md)  
  > 
> [[简单, 剑指Offer] 最小的k个数 (partition操作) 🔥](../../2021/12/剑指Offer_4000_简单_最小的k个数(partition操作).md)  
> [[简单, 牛客] 三个数的最大乘积](../04/牛客_0106_简单_三个数的最大乘积.md)  
  > 

</details>
<details><summary><b>热门</b></summary>

> [[中等, LeetCode] 买卖股票的最佳时机II 🔥](../06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
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
> [[困难, LeetCode] 合并K个升序链表 🔥](LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 平衡二叉树 🔥](../09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, 牛客] 两个链表的第一个公共结点 🔥](../03/牛客_0066_简单_两个链表的第一个公共结点.md)  
  > 

</details>
<!--END_SECTION:relate-->
