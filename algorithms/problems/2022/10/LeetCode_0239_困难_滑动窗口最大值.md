## 滑动窗口最大值
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-11-11%2013%3A04%3A08&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&color=red&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
[![](https://img.shields.io/static/v1?label=&message=%E5%8D%95%E8%B0%83%E6%A0%88/%E5%8D%95%E8%B0%83%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#单调栈单调队列)
[![](https://img.shields.io/static/v1?label=&message=%E5%A0%86/%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#堆优先队列)
[![](https://img.shields.io/static/v1?label=&message=%E7%83%AD%E9%97%A8&color=blue&style=flat-square)](../../../README.md#热门)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [堆, 单调队列, 热门, lc100]
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

示例
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

---

<summary><b>思路 1: 堆/优先队列</b></summary>

- 维护一个最大堆保存窗口内的值;
- 难点是如何保证堆内 (主要是堆顶) 的值正好在窗口内;
    - 方法是同时保存值的索引, 利用索引判断当前堆顶值是否在窗口内, 详见代码;

<details><summary><b>Python</b></summary>

```python
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

    import heapq

    h = []                                  # 初始化前 k 个元素入堆
    for i in range(k):                      # Python 的 heapq 是最小堆, 所以用 -nums[i] 模拟最大堆
        heapq.heappush(h, (-nums[i], i))    # 堆元素是 (值, 下标), 下标用于判断元素是否还在窗口内

    ret = [-h[0][0]]
    for i in range(k, len(nums)):           # 从第 k 个元素开始滑动窗口
        while h and h[0][1] <= i - k:       # 移除已经不在窗口内元素
            heapq.heappop(h)
        heapq.heappush(h, (-nums[i], i))
        ret.append(-h[0][0])

    return ret
```

</details>

---

<summary><b>思路 2: 单调队列 (略)</b></summary>

> [滑动窗口最大值 (方法二) - 力扣官方题解](https://leetcode.cn/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/)

<!--
<summary><b>相关问题</b></summary>

-->


<!--START_SECTION:relate_note-->
---

### 算法笔记

> 🌧️ _暂无主题相关的笔记_


<details><summary><b>其他算法笔记</b></summary>

- [二分查找相关](../../../../notes/_archives/2025/10/二分查找备忘.md)  
- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

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
> [[困难, LeetCode] 合并K个升序链表 🔥](LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 最小覆盖子串 🔥](../../2025/11/LeetCode_0076_困难_最小覆盖子串.md)  
> [[困难, LeetCode] 最长有效括号 🔥](LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, 牛客] 最小覆盖子串 🔥](../02/牛客_0028_困难_最小覆盖子串.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 有效的括号 🔥](../03/LeetCode_0020_简单_有效的括号.md)  
> [[简单, LeetCode] 移动零 🔥](../../2025/11/LeetCode_0283_简单_移动零.md)  
  > 

</details>

<details><summary><b>单调栈/单调队列 (5)</b></summary>

> [[中等, LeetCode] 每日温度](../../2025/10/LeetCode_0739_中等_每日温度.md)  
  > 
> [[困难, LeetCode] 柱状图中最大的矩形](../../2025/10/LeetCode_0084_困难_柱状图中最大的矩形.md)  
> [[困难, 剑指Offer] 滑动窗口的最大值](../01/剑指Offer_5901_困难_滑动窗口的最大值.md)  
> [[困难, 牛客] 滑动窗口的最大值](../03/牛客_0082_困难_滑动窗口的最大值.md)  
  > 
> [[简单, LeetCode] 下一个更大元素](../../2021/11/LeetCode_0496_简单_下一个更大元素.md)  
  > 

</details>

<details><summary><b>堆/优先队列 (8)</b></summary>

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

<details><summary><b>热门 (16)</b></summary>

> [[中等, LeetCode] 买卖股票的最佳时机 II (不限交易次数) 🔥](../06/LeetCode_0122_中等_买卖股票的最佳时机II(不限交易次数).md)  
> [[中等, LeetCode] 全排列 🔥](LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_中等_编辑距离.md)  
> [[中等, LeetCode] 重排链表 🔥](../06/LeetCode_0143_中等_重排链表.md)  
> [[中等, 剑指Offer] 把字符串转换成整数 🔥](../01/剑指Offer_6700_中等_把字符串转换成整数.md)  
> [[中等, 牛客] 三数之和 🔥](../03/牛客_0054_中等_三数之和.md)  
> [[中等, 牛客] 把二叉树打印成多行 🔥](../03/牛客_0080_中等_把二叉树打印成多行.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 平衡二叉树 🔥](../09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, 牛客] 两个链表的第一个公共结点 🔥](../03/牛客_0066_简单_两个链表的第一个公共结点.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
