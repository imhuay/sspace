## 寻找两个正序数组的中位数
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&color=red&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE&color=blue&style=flat-square)](../../../README.md#二分查找)
<!--END_SECTION:badge-->
<!--info
tags: [二分, lc100]
source: LeetCode
level: 困难
number: '0004'
name: 寻找两个正序数组的中位数
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定两个大小分别为 m 和 n 的正序 (从小到大) 数组 A 和 B. 请你找出并返回这两个正序数组的 中位数 .

算法的时间复杂度应该为 O(log (m+n)).
```
> [4. 寻找两个正序数组的中位数 - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->


<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 二分目标: 找到最大的 `i`, 使 `A[i - 1] <= B[j]`, 其中 `j = (m + n + 1) / 2 - i`, `m, n` 分别为 `A, B` 的长度;
- 思路简述: 将 `A, B` 分别分成如下两组, 且保证 `max(A_i-1, B_j-1) <= min(A_i, B_j)`, 根据中位数的性质, 目标值即 `max(A_i-1, B_j-1)`;
    - 可证, 该条件等价于找到最大的 `i`, 使 `A[i - 1] <= B[j]` (证明详见参考链接)
    > [寻找两个有序数组的中位数 - 力扣官方题解](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/)

    ```
        A_0, .., A_i-1 | A_i, .., A_m-1
        B_0, .., B_j-1 | B_j, .., B_n-1
    其中
        i + j == (m + n + 1) / 2
    这里使用 (m + n + 1) / 2 而不是 (m + n) / 2,
        是为了使当 m + n 为奇数时, 前一半比后一半多一个, 即 i + j == (m + n) - (i + j) + 1;
        偶数时不影响;
    ```

- 关于 `i == 0/m, j == 0/n` 的处理细节见代码;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)

        inf = 1e7
        m, n = len(A), len(B)
        # half 表示一半的数量; +1 是为了使奇数情况时, 左侧数量多一个, 偶数不影响;
        half = (m + n + 1) // 2
        l, r = 0, m  # [l, r) 左闭右开区间, 循环时要始终保持这个开闭原则

        while l < r:  # 因为是左闭右开区间, 所以 l 要始终小于 r
            # 这里 i 和 j 指的是数量, 而不是下标, 即 A 中的前 i 个数, B 中的前 j 个数;
            # i + j 共同组成了 "前一半" 的数
            i = (l + r + 1) // 2
            j = half - i
            # 因为 i 和 j 都是指的数量, 所以下标要 -1; 具体来说, i 和 j 分别把 A 和 B 划分成了如下两个区间
            # 前一半包括 A[0 .. i-1] 和 B[0 .. j-1]
            # 后一半包括 A[i .. m-1] 和 B[j .. n-1]

            # 二分的目标是找到最大的 i 使 A[i - 1] <= B[j] 成立
            if A[i - 1] <= B[j]:
                l = i  # [l, i-1] 区间满足要求, 下一轮在 [i, r) 中继续找更大的, 所以使 l = i
            else:
                r = i - 1  # [i-1, r) 区间不满足要求, 下一轮从 [l, i-1) 继续找符合的, 所以令 r = i - 1

        # 退出循环时 l == r
        i, j = l, half - l

        # 记 m1, m2 分别表示前半部分的最大值和后半部分的最小值, 根据定义
        #   m1, m2 = max(A[i-1],B[j-1]), min(A[i],B[j])
        # 这里要注意 i=0/i=m/j=0/j=n 的情况 (越界)
        #   i == 0 表示前一半从 A 中取 0 个数, 即前一半都从 B 中取;
        #   i == m 表示前一半取 A 中所有数, 剩下的再从 B 中取;
        #   j == 0, j == n 同理
        a_im1 = -inf if i == 0 else A[i - 1]
        a_i = inf if i == m else A[i]
        b_jm1 = -inf if j == 0 else B[j - 1]
        b_j = inf if j == n else B[j]
        m1, m2 = max(a_im1, b_jm1), min(a_i, b_j)

        return (m1 + m2) / 2 if (m + n) % 2 == 0 else m1
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


<details><summary><b>LeetCode Hot 100 (25)</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 两数相加 🔥](../../2021/10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 全排列 🔥](../10/LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](../10/LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 字母异位词分组 🔥](../10/LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 括号生成 🔥](../10/LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](../10/LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, LeetCode] 无重复字符的最长子串 🔥](LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](../10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, LeetCode] 组合总和 🔥](../10/LeetCode_0039_中等_组合总和.md)  
> [[中等, LeetCode] 组合总和II 🔥](../10/LeetCode_0040_中等_组合总和II.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](../10/LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 有效的括号 🔥](../03/LeetCode_0020_简单_有效的括号.md)  
  > 

</details>

<details><summary><b>二分查找 (23)</b></summary>

> [[中等, LeetCode] 两数相除](../../2021/10/LeetCode_0029_中等_两数相除.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, 剑指Offer2] 整数除法 🔥](../09/剑指Offer2_001_中等_整数除法.md)  
> [[中等, 剑指Offer] 二维数组中的查找](../../2021/11/剑指Offer_0400_中等_二维数组中的查找.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../../2021/11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 牛客] 二分查找-II](../04/牛客_0105_中等_二分查找-II.md)  
> [[中等, 牛客] 二维数组中的查找](牛客_0029_中等_二维数组中的查找.md)  
> [[中等, 牛客] 寻找峰值 🔥](../04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 矩阵元素查找](../04/牛客_0086_中等_矩阵元素查找.md)  
  > 
> [[困难, LeetCode] 将数据流变为多个不相交区间](../../2021/10/LeetCode_0352_困难_将数据流变为多个不相交区间.md)  
> [[困难, 牛客] 在两个长度相等的排序数组中找到上中位数](牛客_0036_困难_在两个长度相等的排序数组中找到上中位数.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](../10/LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 排列硬币](../../2021/10/LeetCode_0441_简单_排列硬币.md)  
> [[简单, 剑指Offer2] 山峰数组的顶部](../09/剑指Offer2_069_简单_山峰数组的顶部.md)  
> [[简单, 剑指Offer] 在排序数组中查找数字](../01/剑指Offer_5302_简单_在排序数组中查找数字.md)  
> [[简单, 剑指Offer] 旋转数组的最小数字](../../2021/11/剑指Offer_1100_简单_旋转数组的最小数字.md)  
> [[简单, 剑指Offer] 求0～n-1中缺失的数字](../01/剑指Offer_5301_简单_求0～n-1中缺失的数字.md)  
> [[简单, 牛客] 在旋转过的有序数组中寻找目标值](../03/牛客_0048_简单_在旋转过的有序数组中寻找目标值.md)  
> [[简单, 牛客] 数字在升序数组中出现的次数](../03/牛客_0074_简单_数字在升序数组中出现的次数.md)  
> [[简单, 牛客] 旋转数组的最小数字](../03/牛客_0071_简单_旋转数组的最小数字.md)  
> [[简单, 牛客] 求平方根 🔥](牛客_0032_简单_求平方根.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
