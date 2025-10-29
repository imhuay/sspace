## 旋转数组的最小数字
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE&color=blue&style=flat-square)](../../../README.md#二分查找)
<!--END_SECTION:badge-->
<!--info
tags: [二分查找]
source: 剑指Offer
level: 简单
number: '1100'
name: 旋转数组的最小数字
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
求旋转数组中的最小元素;
旋转数组: 将一个有序数组的前 N 个数组拼接到末尾;
例如, 数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转;
```

<details><summary><b>详细描述</b></summary>

```txt
把一个数组最开始的若干个元素搬到数组的末尾, 我们称之为数组的旋转. 输入一个递增排序的数组的一个旋转, 输出旋转数组的最小元素. 例如, 数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转, 该数组的最小值为1.

示例 1:
    输入: [3,4,5,1,2]
    输出: 1
示例 2:
    输入: [2,2,2,0,1]
    输出: 0

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

</details>

<summary><b>思路: 二分查找</b></summary>

- 本题的难点是比较基准的确定 (详见代码)
- 本题虽然是简单题, 但有很多需要注意的点;
  > [旋转数组的最小数字 (二分法, 清晰图解) ](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/)


<details><summary><b>Python</b></summary>

```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """"""
        if numbers[0] < numbers[-1]:  # 只有严格小于, 才说明没有发生旋转
            return numbers[0]

        l, r = -1, len(numbers) - 1  # 本题设置为左开右闭较合适, 即 (l, r]
        while l + 1 < r:
            mid = l + (r - l) // 2  # l <= mid < r
            if numbers[mid] > numbers[r]:  # 中值大于右边界, 说明最小值在右侧
                l = mid  # 因为设置 l 为开区间, 故不需要 l = mid + 1
            elif numbers[mid] < numbers[r]:  # 中值小于右边界, 说明最小值在左侧
                r = mid  # mid 本身就可能是最小值, 且 r 为闭区间, 故不需要 r = mid - 1
            else:
                r -= 1  # 关键步骤, 当 numbers[mid] == numbers[r] 时, 无法判断旋转点 x 是在 (l, m] 还是 (m, r] 区间中, 通过 r-=1 来缩小范围

        return numbers[r]  # 循环结束时, 应有 l+1 == r
```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

- [二分查找相关](../../../../notes/_archives/2025/10/二分查找备忘.md)  

<details><summary><b>其他算法笔记</b></summary>

- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>二分查找 (23)</b></summary>

> [[中等, LeetCode] 两数相除](../10/LeetCode_0029_中等_两数相除.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../../2022/10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../../2022/07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, 剑指Offer2] 整数除法 🔥](../../2022/09/剑指Offer2_001_中等_整数除法.md)  
> [[中等, 剑指Offer] 二维数组中的查找](剑指Offer_0400_中等_二维数组中的查找.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 牛客] 二分查找-II](../../2022/04/牛客_0105_中等_二分查找-II.md)  
> [[中等, 牛客] 二维数组中的查找](../../2022/02/牛客_0029_中等_二维数组中的查找.md)  
> [[中等, 牛客] 寻找峰值 🔥](../../2022/04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 矩阵元素查找](../../2022/04/牛客_0086_中等_矩阵元素查找.md)  
  > 
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../../2022/02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 将数据流变为多个不相交区间](../10/LeetCode_0352_困难_将数据流变为多个不相交区间.md)  
> [[困难, 牛客] 在两个长度相等的排序数组中找到上中位数](../../2022/02/牛客_0036_困难_在两个长度相等的排序数组中找到上中位数.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](../../2022/10/LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 排列硬币](../10/LeetCode_0441_简单_排列硬币.md)  
> [[简单, 剑指Offer2] 山峰数组的顶部](../../2022/09/剑指Offer2_069_简单_山峰数组的顶部.md)  
> [[简单, 剑指Offer] 在排序数组中查找数字](../../2022/01/剑指Offer_5302_简单_在排序数组中查找数字.md)  
> [[简单, 剑指Offer] 求0～n-1中缺失的数字](../../2022/01/剑指Offer_5301_简单_求0～n-1中缺失的数字.md)  
> [[简单, 牛客] 在旋转过的有序数组中寻找目标值](../../2022/03/牛客_0048_简单_在旋转过的有序数组中寻找目标值.md)  
> [[简单, 牛客] 数字在升序数组中出现的次数](../../2022/03/牛客_0074_简单_数字在升序数组中出现的次数.md)  
> [[简单, 牛客] 旋转数组的最小数字](../../2022/03/牛客_0071_简单_旋转数组的最小数字.md)  
> [[简单, 牛客] 求平方根 🔥](../../2022/02/牛客_0032_简单_求平方根.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
