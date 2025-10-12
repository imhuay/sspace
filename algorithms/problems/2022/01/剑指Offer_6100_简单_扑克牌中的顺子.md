## 扑克牌中的顺子
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E6%8E%92%E5%BA%8F&color=blue&style=flat-square)](../../../README.md#排序)
[![](https://img.shields.io/static/v1?label=&message=%E6%A8%A1%E6%8B%9F&color=blue&style=flat-square)](../../../README.md#模拟)
<!--END_SECTION:badge-->
<!--info
tags: [排序, 模拟]
source: 剑指Offer
level: 简单
number: '6100'
name: 扑克牌中的顺子
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
从若干副扑克牌中随机抽 5 张牌, 判断是不是一个顺子;
```

<details><summary><b>详细描述</b></summary>

```txt
从若干副扑克牌中随机抽 5 张牌, 判断是不是一个顺子, 即这5张牌是不是连续的. 2～10为数字本身, A为1, J为11, Q为12, K为13, 而大、小王为 0 , 可以看成任意数字. A 不能视为 14.

示例 1:
    输入: [1,2,3,4,5]
    输出: True
示例 2:
    输入: [0,0,1,2,5]
    输出: True

限制:
    数组长度为 5
    数组的数取值为 [0, 13] .

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 排序后, 统计 0 出现的次数, 以及数组中的 `max_x` 和 `min_x`;
- 当`最大值 - 最小值 < 5` 时即可组成顺子;
- 若出现相同牌则提前返回 False;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def isStraight(self, nums: List[int]) -> bool:

        nums.sort()  # 排序
        # 如果不想排序需的话, 就需要另外使用一些变量来记录最大、最小和已经出现过的牌

        cnt_0 = 0
        for i, x in enumerate(nums[:-1]):
            if x == 0:  # 记录 0 的个数
                cnt_0 += 1
            elif x == nums[i + 1]:
                return False

        # return nums[-1] - nums[cnt_0] == 4  # Error, 因为 0 也可以用来作为最大或最小的牌
        return nums[-1] - nums[cnt_0] < 5

```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

> 🌧️ _暂无主题相关的笔记_


<details><summary><b>其他算法笔记</b></summary>

- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表常用操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>排序 (15)</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](../10/LeetCode_0215_中等_数组中的第K个最大元素.md)  
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
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](../../2021/12/剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
> [[简单, 剑指Offer] 最小的k个数 (partition操作) 🔥](../../2021/12/剑指Offer_4000_简单_最小的k个数(partition操作).md)  
> [[简单, 牛客] 三个数的最大乘积](../04/牛客_0106_简单_三个数的最大乘积.md)  
> [[简单, 程序员面试金典] 判定字符是否唯一](../09/程序员面试金典_0101_简单_判定字符是否唯一.md)  
  > 

</details>

<details><summary><b>模拟 (15)</b></summary>

> [[中等, LeetCode] 分割数组](../06/LeetCode_0915_中等_分割数组.md)  
> [[中等, 剑指Offer] 买卖股票的最佳时机](剑指Offer_6300_中等_买卖股票的最佳时机.md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 牛客] 大数乘法](牛客_0010_中等_大数乘法.md)  
> [[中等, 牛客] 大数加法](牛客_0001_中等_大数加法.md)  
> [[中等, 牛客] 最长回文子串](牛客_0017_中等_最长回文子串.md)  
> [[中等, 牛客] 螺旋矩阵](../03/牛客_0038_中等_螺旋矩阵.md)  
  > 
> [[困难, LeetCode] 将数据流变为多个不相交区间](../../2021/10/LeetCode_0352_困难_将数据流变为多个不相交区间.md)  
  > 
> [[简单, LeetCode] 亲密字符串](../../2021/11/LeetCode_0859_简单_亲密字符串.md)  
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](../../2021/12/剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
> [[简单, 牛客] 买卖股票的最好时机(一)](牛客_0007_简单_买卖股票的最好时机(一).md)  
> [[简单, 牛客] 反转数字](../03/牛客_0057_简单_反转数字.md)  
> [[简单, 牛客] 字符串变形](../04/牛客_0089_简单_字符串变形.md)  
> [[简单, 牛客] 扑克牌顺子](../03/牛客_0063_简单_扑克牌顺子.md)  
> [[简单, 牛客] 数组中出现次数超过一半的数字](../03/牛客_0073_简单_数组中出现次数超过一半的数字.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
