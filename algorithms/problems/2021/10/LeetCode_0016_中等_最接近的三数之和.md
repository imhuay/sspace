## 最接近的三数之和
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%8F%8C%E6%8C%87%E9%92%88&color=blue&style=flat-square)](../../../README.md#双指针)
<!--END_SECTION:badge-->
<!--info
tags: [双指针]
source: LeetCode
level: 中等
number: '0016'
name: 最接近的三数之和
companies: []
-->

<summary><b>问题简述</b></summary>

```text
给定一个数组, 找出该数组中和最接近指定值的三元组.
```


<details><summary><b>详细描述</b></summary>

```text
给定一个包括 n 个整数的数组 nums 和 一个目标值 target. 找出 nums 中的三个整数, 使得它们的和与 target 最接近. 返回这三个数的和. 假定每组输入只存在唯一答案.

示例:
    输入: nums = [-1,2,1,-4], target = 1
    输出: 2
    解释: 与 target 最接近的和是 2 (-1 + 2 + 1 = 2).

提示:
    3 <= nums.length <= 10^3
    -10^3 <= nums[i] <= 10^3
    -10^4 <= target <= 10^4

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>


<summary><b>思路</b></summary>

- 思路跟三数之和基本一致;
- 当找到比当前更接近的结果时更新;


<details><summary><b>Python</b></summary>

```python
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """"""
        nums = sorted(nums)

        L = len(nums)
        ret = nums[0] + nums[1] + nums[2]  # 初始化, len(nums) >= 3
        for i in range(L - 2):

            # 跳过重复元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 利用单调性剪纸
            min_s = nums[i] + nums[i + 1] + nums[i + 2]  # 最小和
            if min_s > target:
                if abs(min_s - target) < abs(ret - target):
                    ret = min_s
                break

            max_s = nums[i] + nums[L - 2] + nums[L - 1]  # 最大和
            if max_s < target:
                ret = max_s
                continue

            # 初始化双指针
            l, r = i + 1, L - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(ret - target):
                    ret = s

                if s < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                elif s > target:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                else:  # ret == target
                    return ret
        return ret

```

</details>

<details><summary><b>利用单调性剪枝</b></summary>

- 在经过排序后, 每轮迭代时, 三数之和的最大值和最小值是确定的;
- 所以如果最小值比目标值大, 那么后面无论怎么移动双指针, 差值都只会越来越大; 最大值比目标值小时同理;
- 代码细节:

    ```python
    # 剪枝: 利用单调性
    min_s = nums[i] + nums[i + 1] + nums[i + 2]  # 最小和
    if min_s > target:  # 如果最小和也大于 target, 则剩余部分的差值肯定越来越大
        # 容易忽略的一步, 注意此时也是有可能出现答案的, 比如 ret < 0 < min_s 时
        if abs(min_s - target) < abs(ret - target):
            ret = min_s
        break

    max_s = nums[i] + nums[L - 2] + nums[L - 1]  # 最大和
    if max_s < target:  # 如果最大和也小于 target, 则剩余部分的差值肯定越来越大
        ret = max_s  # 此时 ret < max_s < target, 所以 max_s 必然比当前 ret 更接近目标值
        continue
    ```

</details>


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


<details><summary><b>双指针 (24)</b></summary>

> [[中等, LeetCode] 三数之和 🔥](LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../../2022/10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../../2022/01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 最长回文子串 🔥](LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 有效三角形的个数](LeetCode_0611_中等_有效三角形的个数.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 牛客] 三数之和 🔥](../../2022/03/牛客_0054_中等_三数之和.md)  
> [[中等, 牛客] 删除链表的倒数第n个节点](../../2022/03/牛客_0053_中等_删除链表的倒数第n个节点.md)  
> [[中等, 牛客] 合并两个有序的数组](../../2022/01/牛客_0022_中等_合并两个有序的数组.md)  
  > 
> [[困难, LeetCode] 接雨水 🔥](LeetCode_0042_困难_接雨水.md)  
> [[困难, 牛客] 接雨水问题 🔥](../../2022/05/牛客_0128_困难_接雨水问题.md)  
  > 
> [[简单, LeetCode] 两数之和II-输入有序数组](../../2022/07/LeetCode_0167_简单_两数之和II-输入有序数组.md)  
> [[简单, LeetCode] 链表的中间结点](../../2022/06/LeetCode_0876_简单_链表的中间结点.md)  
> [[简单, 剑指Offer] 两个链表的第一个公共节点](../../2022/01/剑指Offer_5200_简单_两个链表的第一个公共节点.md)  
> [[简单, 剑指Offer] 和为s的两个数字](../../2022/01/剑指Offer_5701_简单_和为s的两个数字.md)  
> [[简单, 剑指Offer] 和为s的连续正数序列](../../2022/01/剑指Offer_5702_简单_和为s的连续正数序列.md)  
> [[简单, 剑指Offer] 翻转单词顺序](../../2022/01/剑指Offer_5801_简单_翻转单词顺序.md)  
> [[简单, 剑指Offer] 调整数组顺序使奇数位于偶数前面](../11/剑指Offer_2100_简单_调整数组顺序使奇数位于偶数前面.md)  
> [[简单, 剑指Offer] 链表中倒数第k个节点](../11/剑指Offer_2200_简单_链表中倒数第k个节点.md)  
> [[简单, 牛客] 判断链表中是否有环](../../2022/01/牛客_0004_简单_判断链表中是否有环.md)  
> [[简单, 牛客] 反转字符串](../../2022/04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 链表中倒数最后k个结点](../../2022/03/牛客_0069_简单_链表中倒数最后k个结点.md)  
> [[简单, 牛客] 链表中环的入口结点](../../2022/01/牛客_0003_简单_链表中环的入口结点.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
