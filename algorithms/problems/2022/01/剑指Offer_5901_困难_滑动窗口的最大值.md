## 滑动窗口的最大值
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&color=red&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%8D%95%E8%B0%83%E6%A0%88/%E5%8D%95%E8%B0%83%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#单调栈单调队列)
[![](https://img.shields.io/static/v1?label=&message=%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3&color=blue&style=flat-square)](../../../README.md#滑动窗口)
<!--END_SECTION:badge-->
<!--info
tags: [滑动窗口, 单调队列]
source: 剑指Offer
level: 困难
number: '5901'
name: 滑动窗口的最大值
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定一个数组 nums 和滑动窗口的大小 k, 请找出所有滑动窗口里的最大值.
```

<details><summary><b>详细描述</b></summary>

```txt
给定一个数组 nums 和滑动窗口的大小 k, 请找出所有滑动窗口里的最大值.

示例:
    输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
    输出: [3,3,5,5,6,7]
    解释:
      滑动窗口的位置                最大值
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

提示:
    你可以假设 k 总是有效的, 在输入数组不为空的情况下, 1 ≤ k ≤ 输入数组的大小.

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 使用单调队列维护一个最大值序列, 每次滑动窗口前, 更新单调队列, 使队首元素为下一个窗口中的最大值, 详见参考链接或具体代码;
    > [滑动窗口的最大值 (单调队列, 清晰图解) ](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/mian-shi-ti-59-i-hua-dong-chuang-kou-de-zui-da-1-6/)

<details><summary><b>Python</b></summary>

- 跟[官方写法](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/hua-dong-chuang-kou-de-zui-da-zhi-by-lee-ymyo/)的区别:
    - 官方的单调队列维护的是数组下标, 通过判断下标位置来确定是否移除队首元素; 因此可以使用**严格单调队列**; 而下面的写法中使用值来判断是否移除队首, 因此使用的是非严格单调队列 (相关代码段: `if q[0] == nums[i - k]: q.popleft()`)

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        if not nums: return []

        # 初始化单调队列, 对任意 i > j, 有 q[i] >= q[j]
        q = deque()
        for x in nums[:k]:
            while q and q[-1] < x:  # 注意这里是非严格单调的
                q.pop()
            q.append(x)
        # print(q)

        ret = [q[0]]  #
        for i in range(k, len(nums)):
            if q[0] == nums[i - k]:  # 因为是通过值判断, 所以需要保留所有相同的最大值, 所以队列是非严格单调的
                q.popleft()
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            ret.append(q[0])
            # print(q)

        return ret
```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  

<details><summary><b>其他算法笔记</b></summary>

- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [链表常用操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>单调栈/单调队列 (4)</b></summary>

> [[中等, LeetCode] 每日温度](../../2025/10/LeetCode_0739_中等_每日温度.md)  
  > 
> [[困难, LeetCode] 柱状图中最大的矩形](../../2025/10/LeetCode_0084_困难_柱状图中最大的矩形.md)  
> [[困难, 牛客] 滑动窗口的最大值](../03/牛客_0082_困难_滑动窗口的最大值.md)  
  > 
> [[简单, LeetCode] 下一个更大元素](../../2021/11/LeetCode_0496_简单_下一个更大元素.md)  
  > 

</details>

<details><summary><b>滑动窗口 (5)</b></summary>

> [[中等, LeetCode] 无重复字符的最长子串 🔥](../02/LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, 牛客] 最长无重复子数组](../03/牛客_0041_中等_最长无重复子数组.md)  
  > 
> [[困难, 牛客] 数组中的最长连续子序列](../04/牛客_0095_困难_数组中的最长连续子序列.md)  
> [[困难, 牛客] 最小覆盖子串](../02/牛客_0028_困难_最小覆盖子串.md)  
  > 
> [[简单, 牛客] 压缩字符串(一)](../04/牛客_0101_简单_压缩字符串(一).md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
