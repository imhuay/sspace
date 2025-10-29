## 和为s的连续正数序列
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%8F%8C%E6%8C%87%E9%92%88&color=blue&style=flat-square)](../../../README.md#双指针)
<!--END_SECTION:badge-->
<!--info
tags: [双指针]
source: 剑指Offer
level: 简单
number: '5702'
name: 和为s的连续正数序列
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
输入一个正整数 target , 输出所有和为 target 的连续正整数序列 (至少含有两个数).
```

<details><summary><b>详细描述</b></summary>

```txt
输入一个正整数 target , 输出所有和为 target 的连续正整数序列 (至少含有两个数).

序列内的数字由小到大排列, 不同序列按照首个数字从小到大排列.

示例 1:
    输入: target = 9
    输出: [[2,3,4],[4,5]]
示例 2:
    输入: target = 15
    输出: [[1,2,3,4,5],[4,5,6],[7,8]]

限制:
    1 <= target <= 10^5

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1: 双指针</b></summary>

```
1 初始化 左边界 l = 1 , 右边界 r = 2, 结果列表 ret = [];
2 循环 当 l + r <= target 时:
    记 l 到 r 的连续和为 s
    当 s > target 时: 向右移动左边界 l += 1;
    当 s < target 时: 向右移动右边界 r += 1;
    当 s = target 时: 记录连续整数序列, 左右边界同时右移, l += 1, r += 1;
3 返回结果列表 ret;

```

- **Tips**: 求连续和可以在移动双指针的过程中同步加减, 并不需要每次用求和公式计算;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:

        l, r = 1, 2
        s = l + r

        ret = []
        while l + r <= target:
            if s > target:
                s -= l  # 先减
                l += 1
            elif s < target:
                r += 1
                s += r  # 后加
            else:
                ret.append(list(range(l, r + 1)))
                s -= l  # 先减
                l += 1
                r += 1
                s += r  # 后加

        return ret

```

</details>


<summary><b>思路2: 数学</b></summary>

> [和为 s 的连续正数序列 (求和公式 / 滑动窗口, 清晰图解) ](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/jian-zhi-offer-57-ii-he-wei-s-de-lian-xu-t85z/)

- 当确定左边界和 target 时, 可以通过求根公式得到右边界 (去掉负根);
- 当右边界为整数时得到一组解;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def findContinuousSequence(self, target: int):
        i, j, res = 1, 2, []
        while i < j:
            # 当确定左边界和 target 时, 可以通过求根公式得到右边界 (去掉负根)
            j = (-1 + (1 + 4 * (2 * target + i * i - i)) ** 0.5) / 2
            # 当 j 为整数时得到一组解
            if i < j and j == int(j):
                res.append(list(range(i, int(j) + 1)))
            i += 1
        return res
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

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 最接近的三数之和](../../2021/10/LeetCode_0016_中等_最接近的三数之和.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 有效三角形的个数](../../2021/10/LeetCode_0611_中等_有效三角形的个数.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../../2021/12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 牛客] 三数之和 🔥](../03/牛客_0054_中等_三数之和.md)  
> [[中等, 牛客] 删除链表的倒数第n个节点](../03/牛客_0053_中等_删除链表的倒数第n个节点.md)  
> [[中等, 牛客] 合并两个有序的数组](牛客_0022_中等_合并两个有序的数组.md)  
  > 
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, 牛客] 接雨水问题 🔥](../05/牛客_0128_困难_接雨水问题.md)  
  > 
> [[简单, LeetCode] 两数之和II-输入有序数组](../07/LeetCode_0167_简单_两数之和II-输入有序数组.md)  
> [[简单, LeetCode] 链表的中间结点](../06/LeetCode_0876_简单_链表的中间结点.md)  
> [[简单, 剑指Offer] 两个链表的第一个公共节点](剑指Offer_5200_简单_两个链表的第一个公共节点.md)  
> [[简单, 剑指Offer] 和为s的两个数字](剑指Offer_5701_简单_和为s的两个数字.md)  
> [[简单, 剑指Offer] 翻转单词顺序](剑指Offer_5801_简单_翻转单词顺序.md)  
> [[简单, 剑指Offer] 调整数组顺序使奇数位于偶数前面](../../2021/11/剑指Offer_2100_简单_调整数组顺序使奇数位于偶数前面.md)  
> [[简单, 剑指Offer] 链表中倒数第k个节点](../../2021/11/剑指Offer_2200_简单_链表中倒数第k个节点.md)  
> [[简单, 牛客] 判断链表中是否有环](牛客_0004_简单_判断链表中是否有环.md)  
> [[简单, 牛客] 反转字符串](../04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 链表中倒数最后k个结点](../03/牛客_0069_简单_链表中倒数最后k个结点.md)  
> [[简单, 牛客] 链表中环的入口结点](牛客_0003_简单_链表中环的入口结点.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
