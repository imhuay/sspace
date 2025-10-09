## 在排序数组中查找数字
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=yellow&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE&color=blue&style=flat-square)](../../../README.md#二分查找)
<!--END_SECTION:badge-->
<!--info
tags: [二分]
source: 剑指Offer
level: 简单
number: '5302'
name: 在排序数组中查找数字
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
统计给定数字在排序数组中出现的次数.
```

<details><summary><b>详细描述</b></summary>

```txt
统计一个数字在排序数组中出现的次数.

示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: 2
示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: 0

提示:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums 是一个非递减数组
    -10^9 <= target <= 10^9

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 二分法分别查找目标值的左右边界;
- 小技巧: 如果二分查找的是右边界, 那么可以通过查找 `target - 1` 来获得左边界, 因为二分查找实际上找的是目标值的插入位置;

<details><summary><b>Python: 使用库函数</b></summary>

```python
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx_r, idx_l = bisect.bisect_right(nums, target), bisect.bisect_left(nums, target)
        # idx_r, idx_l = bisect.bisect_right(nums, target), bisect.bisect_right(nums, target - 1)
        return idx_r - idx_l
```

</details>

<details><summary><b>Python: 不使用库函数</b></summary>

```python
class Solution:
    def search(self, nums: [int], target: int) -> int:

        def bisect(tar):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= tar:
                    l = m + 1
                else:
                    r = m - 1
            return l

        return bisect(target) - bisect(target - 1)
```

</details>


<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>二分查找</b></summary>

> [[中等, LeetCode] 两数相除](../../2021/10/LeetCode_0029_中等_两数相除.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, 剑指Offer2] 整数除法 🔥](../09/剑指Offer2_001_中等_整数除法.md)  
> [[中等, 剑指Offer] 二维数组中的查找](../../2021/11/剑指Offer_0400_中等_二维数组中的查找.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../../2021/11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 牛客] 二分查找-II](../04/牛客_0105_中等_二分查找-II.md)  
> [[中等, 牛客] 二维数组中的查找](../02/牛客_0029_中等_二维数组中的查找.md)  
> [[中等, 牛客] 寻找峰值 🔥](../04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 矩阵元素查找](../04/牛客_0086_中等_矩阵元素查找.md)  
  > 
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 将数据流变为多个不相交区间](../../2021/10/LeetCode_0352_困难_将数据流变为多个不相交区间.md)  
> [[困难, 牛客] 在两个长度相等的排序数组中找到上中位数](../02/牛客_0036_困难_在两个长度相等的排序数组中找到上中位数.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](../10/LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 排列硬币](../../2021/10/LeetCode_0441_简单_排列硬币.md)  
> [[简单, 剑指Offer2] 山峰数组的顶部](../09/剑指Offer2_069_简单_山峰数组的顶部.md)  
> [[简单, 剑指Offer] 旋转数组的最小数字](../../2021/11/剑指Offer_1100_简单_旋转数组的最小数字.md)  
> [[简单, 剑指Offer] 求0～n-1中缺失的数字](剑指Offer_5301_简单_求0～n-1中缺失的数字.md)  
> [[简单, 牛客] 在旋转过的有序数组中寻找目标值](../03/牛客_0048_简单_在旋转过的有序数组中寻找目标值.md)  
> [[简单, 牛客] 数字在升序数组中出现的次数](../03/牛客_0074_简单_数字在升序数组中出现的次数.md)  
> [[简单, 牛客] 旋转数组的最小数字](../03/牛客_0071_简单_旋转数组的最小数字.md)  
> [[简单, 牛客] 求平方根 🔥](../02/牛客_0032_简单_求平方根.md)  
  > 

</details>
<!--END_SECTION:relate-->
