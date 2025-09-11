## 把数组排成最小的数
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&label_color=gray&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&label_color=gray&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E6%8E%92%E5%BA%8F&label_color=gray&color=blue&style=flat-square)](../../../README.md#排序)
<!--END_SECTION:badge-->
<!--info
tags: [排序]
source: 剑指Offer
level: 中等
number: '4500'
name: 把数组排成最小的数
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
xxx
```

<details><summary><b>详细描述</b></summary>

```txt
输入一个非负整数数组, 把数组里所有数字拼接起来排成一个数, 打印能拼接出的所有数字中最小的一个.

示例 1:
    输入: [10,2]
    输出: "102"
示例 2:
    输入: [3,30,34,5,9]
    输出: "3033459"

提示:
    0 < nums.length <= 100
说明:
    输出结果可能非常大, 所以你需要返回一个字符串而不是整数
    拼接起来的数字可能会有前导 0, 最后结果不需要去掉前导 0

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 算法基于以下结论: 若 `x + y < y + x` 则 `x` 应该排在 `y` 前面/左边;
- 关于该结论的证明详见: [把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/mian-shi-ti-45-ba-shu-zu-pai-cheng-zui-xiao-de-s-4/)

- 根于该规则对 `nums` 排序后拼接即可;


<details><summary><b>Python: 使用库函数</b></summary>

```python
import functools

class Solution:
    def minNumber(self, nums: List[int]) -> str:

        def cmp(x1, x2):
            if x1 + x2 < x2 + x1:
                return -1
            elif x1 + x2 > x2 + x1:
                return 1
            else:
                return 0

        # Python3 的 sort 中取消了 cmp 参数, 需要通过 functools.cmp_to_key 转换
        nums = sorted([str(x) for x in nums], key=functools.cmp_to_key(cmp))
        # print(nums)
        return ''.join(nums)
```

</details>


<details><summary><b>Python: 手动实现排序 (快排) </b></summary>

```python
class Solution:
    def minNumber(self, nums: List[int]) -> str:

        nums = [str(x) for x in nums]

        def qsort(lo, hi):
            if lo >= hi: return

            i, j = lo, hi
            while i < j:
                while nums[j] + nums[lo] >= nums[lo] + nums[j] and i < j: j -= 1
                while nums[i] + nums[lo] <= nums[lo] + nums[i] and i < j: i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[lo] = nums[lo], nums[i]

            qsort(lo, i - 1)
            qsort(i + 1, hi)

        qsort(0, len(nums) - 1)
        return ''.join(nums)
```

</details>


<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>排序</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](../../2022/10/LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, 剑指Offer2] 数组中的第K大的数字](../../2022/09/剑指Offer2_076_中等_数组中的第K大的数字.md)  
> [[中等, 牛客] 合并区间](../../2022/02/牛客_0037_中等_合并区间.md)  
> [[中等, 牛客] 字符串出现次数的TopK问题](../../2022/04/牛客_0097_中等_字符串出现次数的TopK问题.md)  
> [[中等, 牛客] 寻找第K大](../../2022/04/牛客_0088_中等_寻找第K大.md)  
> [[中等, 牛客] 拼接所有的字符串产生字典序最小的字符串](../../2022/04/牛客_0085_中等_拼接所有的字符串产生字典序最小的字符串.md)  
> [[中等, 牛客] 数组中的逆序对](../../2022/05/牛客_0118_中等_数组中的逆序对.md)  
> [[中等, 牛客] 最大数](../../2022/04/牛客_0111_中等_最大数.md)  
> [[中等, 牛客] 最小的K个数](../../2022/05/牛客_0119_中等_最小的K个数.md)  
  > 
> [[简单, 剑指Offer] 扑克牌中的顺子](../../2022/01/剑指Offer_6100_简单_扑克牌中的顺子.md)  
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
> [[简单, 剑指Offer] 最小的k个数 (partition操作) 🔥](剑指Offer_4000_简单_最小的k个数(partition操作).md)  
> [[简单, 牛客] 三个数的最大乘积](../../2022/04/牛客_0106_简单_三个数的最大乘积.md)  
> [[简单, 程序员面试金典] 判定字符是否唯一](../../2022/09/程序员面试金典_0101_简单_判定字符是否唯一.md)  
  > 

</details>
<!--END_SECTION:relate-->