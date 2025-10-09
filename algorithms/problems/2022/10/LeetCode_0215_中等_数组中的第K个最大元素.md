## 数组中的第K个最大元素
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E6%8E%92%E5%BA%8F&color=blue&style=flat-square)](../../../README.md#排序)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [排序, lc100]
source: LeetCode
level: 中等
number: '0215'
name: 数组中的第K个最大元素
companies: []
-->

> [215. 数组中的第K个最大元素 - 力扣 (LeetCode) ](https://leetcode.cn/problems/kth-largest-element-in-an-array/?favorite=2cktkvj)

<summary><b>问题简述</b></summary>

```txt
给定整数数组 nums 和整数 k, 请返回数组中第 k 个最大的元素.
请注意, 你需要找的是数组排序后的第 k 个最大的元素, 而不是第 k 个不同的元素.
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题.
```

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 利用快排的 partition 操作;
- 技巧: 利用 "三数取中" 或者随机选择 pivot 避免最坏情况;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def reset(l, r):

            # 三数取中
            # m = (l + r) // 2
            # if nums[l] < nums[m] < nums[r] or nums[r] < nums[m] < nums[l]:
            #     nums[m], nums[l] = nums[l], nums[m]
            # elif nums[l] < nums[r] < nums[m] or nums[m] < nums[r] < nums[l]:
            #     nums[r], nums[l] = nums[l], nums[r]

            # 随机
            i = random.randint(l, r)
            nums[l], nums[i] = nums[i], nums[l]

        def dfs(lo, hi):
            if lo >= hi: return

            reset(lo, hi - 1)  # 加速, 避免最坏情况
            p = nums[lo]
            l, r = lo, hi - 1
            while l < r:
                while l < r and nums[r] <= p: r -= 1
                while l < r and nums[l] >= p: l += 1
                nums[l], nums[r] = nums[r], nums[l]
            nums[l], nums[lo] = nums[lo], nums[l]

            if l > k - 1: dfs(lo, l)
            if l < k - 1: dfs(l + 1, hi)

        dfs(0, len(nums))
        return nums[k - 1]
```

</details>

<!--
<summary><b>相关问题</b></summary>

-->

<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>排序</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, 剑指Offer2] 数组中的第K大的数字](../09/剑指Offer2_076_中等_数组中的第K大的数字.md)  
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
> [[简单, 程序员面试金典] 判定字符是否唯一](../09/程序员面试金典_0101_简单_判定字符是否唯一.md)  
  > 

</details>
<details><summary><b>LeetCode Hot 100</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 两数相加 🔥](../../2021/10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 全排列 🔥](LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 字母异位词分组 🔥](LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 括号生成 🔥](LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 无重复字符的最长子串 🔥](../02/LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, LeetCode] 组合总和 🔥](LeetCode_0039_中等_组合总和.md)  
> [[中等, LeetCode] 组合总和II 🔥](LeetCode_0040_中等_组合总和II.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 最长有效括号 🔥](LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 有效的括号 🔥](../03/LeetCode_0020_简单_有效的括号.md)  
  > 

</details>
<!--END_SECTION:relate-->
