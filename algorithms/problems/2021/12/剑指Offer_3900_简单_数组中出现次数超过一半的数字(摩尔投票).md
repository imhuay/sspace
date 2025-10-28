## 数组中出现次数超过一半的数字 (摩尔投票)
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-23%2002%3A03%3A22&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%88%86%E6%B2%BB&color=blue&style=flat-square)](../../../README.md#分治)
[![](https://img.shields.io/static/v1?label=&message=%E6%8E%92%E5%BA%8F&color=blue&style=flat-square)](../../../README.md#排序)
[![](https://img.shields.io/static/v1?label=&message=%E6%A8%A1%E6%8B%9F&color=blue&style=flat-square)](../../../README.md#模拟)
[![](https://img.shields.io/static/v1?label=&message=%E7%BB%8F%E5%85%B8&color=blue&style=flat-square)](../../../README.md#经典)
<!--END_SECTION:badge-->
<!--info
tags: [排序, 模拟, 分治, 经典]
source: 剑指Offer
level: 简单
number: '3900'
name: 数组中出现次数超过一半的数字 (摩尔投票)
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
数组中有一个数字出现的次数超过数组长度的一半, 请找出这个数字.
```

<details><summary><b>详细描述</b></summary>

```txt
数组中有一个数字出现的次数超过数组长度的一半, 请找出这个数字.

你可以假设数组是非空的, 并且给定的数组总是存在多数元素.

示例 1:
    输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
    输出: 2
限制:
    1 <= 数组长度 <= 50000

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1: 排序</b></summary>

- 排序后, 数组中间位置的数一定满足题意;
- 时间复杂度 `O(NlogN)`;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
```

</details>


<summary><b>思路2: 计数</b></summary>

- 一次遍历, 记录每个数出现的次数;
- 空间复杂度 `O(N)`;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict

        cnt = defaultdict(int)

        for x in nums:
            cnt[x] += 1
            if cnt[x] > len(nums) // 2:
                return x

        # return -1
```

</details>


<summary><b>思路3: "摩尔投票法" </b></summary>

> [数组中出现次数超过一半的数字 (摩尔投票法, 清晰图解) ](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/)

- "摩尔投票法" 的核心思想是**一一抵消**;
- 假设已知目标数为 x, 遍历时若出现一次 x 记 `+1` 票, 否则为 `-1` 票;
    - 推论1: 最终票数和必大于 0;
    - 推论2: 若前 n 个数的票数和为 0, 那么剩余部分依然满足推论1, 即目标数字依然为 x;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        cnt = 0
        for x in nums:
            if cnt == 0:  # 当票数和为 0 时, 假设当前值为目标值
                ret = x   # 如果这个数不是目标值, 那么它迟早会因为不断 -1, 被替换掉

            if x == ret:
                cnt += 1
            else:
                cnt -= 1

        return ret
```

</details>


<summary><b>思路4: 分治</b></summary>

> [数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-pvh8/)

- 本题使用分治在时间和空间上都不是最优, 仅用于理解分治的思想;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        def recur(lo, hi):  # [lo, hi] 闭区间
            if lo == hi:  # 当数组中只有一个元素时, 这个数就是目标值
                return nums[lo]

            # 分治
            mid = (hi - lo) // 2 + lo
            l = recur(lo, mid)
            r = recur(mid + 1, hi)

            # 如果左右返回值相同时, 显然这个值就是目标值
            if l == r:
                return l

            # 否则需要判断哪个出现的次数更多
            lc = sum(1 for i in range(lo, hi + 1) if nums[i] == l)
            rc = sum(1 for i in range(lo, hi + 1) if nums[i] == r)
            return l if lc > rc else r

        return recur(0, len(nums) - 1)
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
- [链表操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>分治 (3)</b></summary>

> [[中等, 剑指Offer2] 数组中的第K大的数字](../../2022/09/剑指Offer2_076_中等_数组中的第K大的数字.md)  
> [[中等, 剑指Offer] 重建二叉树 🔥](../11/剑指Offer_0700_中等_重建二叉树.md)  
  > 
> [[困难, 剑指Offer] 数组中的逆序对 🔥](../../2022/01/剑指Offer_5100_困难_数组中的逆序对.md)  
  > 

</details>

<details><summary><b>排序 (15)</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](../../2022/10/LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, 剑指Offer2] 数组中的第K大的数字](../../2022/09/剑指Offer2_076_中等_数组中的第K大的数字.md)  
> [[中等, 剑指Offer] 把数组排成最小的数](剑指Offer_4500_中等_把数组排成最小的数.md)  
> [[中等, 牛客] 合并区间](../../2022/02/牛客_0037_中等_合并区间.md)  
> [[中等, 牛客] 字符串出现次数的TopK问题](../../2022/04/牛客_0097_中等_字符串出现次数的TopK问题.md)  
> [[中等, 牛客] 寻找第K大](../../2022/04/牛客_0088_中等_寻找第K大.md)  
> [[中等, 牛客] 拼接所有的字符串产生字典序最小的字符串](../../2022/04/牛客_0085_中等_拼接所有的字符串产生字典序最小的字符串.md)  
> [[中等, 牛客] 数组中的逆序对](../../2022/05/牛客_0118_中等_数组中的逆序对.md)  
> [[中等, 牛客] 最大数](../../2022/04/牛客_0111_中等_最大数.md)  
> [[中等, 牛客] 最小的K个数](../../2022/05/牛客_0119_中等_最小的K个数.md)  
  > 
> [[简单, 剑指Offer] 扑克牌中的顺子](../../2022/01/剑指Offer_6100_简单_扑克牌中的顺子.md)  
> [[简单, 剑指Offer] 最小的k个数 (partition操作) 🔥](剑指Offer_4000_简单_最小的k个数(partition操作).md)  
> [[简单, 牛客] 三个数的最大乘积](../../2022/04/牛客_0106_简单_三个数的最大乘积.md)  
> [[简单, 程序员面试金典] 判定字符是否唯一](../../2022/09/程序员面试金典_0101_简单_判定字符是否唯一.md)  
  > 

</details>

<details><summary><b>模拟 (15)</b></summary>

> [[中等, LeetCode] 分割数组](../../2022/06/LeetCode_0915_中等_分割数组.md)  
> [[中等, 剑指Offer] 买卖股票的最佳时机](../../2022/01/剑指Offer_6300_中等_买卖股票的最佳时机.md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](../../2022/01/剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 牛客] 大数乘法](../../2022/01/牛客_0010_中等_大数乘法.md)  
> [[中等, 牛客] 大数加法](../../2022/01/牛客_0001_中等_大数加法.md)  
> [[中等, 牛客] 最长回文子串](../../2022/01/牛客_0017_中等_最长回文子串.md)  
> [[中等, 牛客] 螺旋矩阵](../../2022/03/牛客_0038_中等_螺旋矩阵.md)  
  > 
> [[困难, LeetCode] 将数据流变为多个不相交区间](../10/LeetCode_0352_困难_将数据流变为多个不相交区间.md)  
  > 
> [[简单, LeetCode] 亲密字符串](../11/LeetCode_0859_简单_亲密字符串.md)  
> [[简单, 剑指Offer] 扑克牌中的顺子](../../2022/01/剑指Offer_6100_简单_扑克牌中的顺子.md)  
> [[简单, 牛客] 买卖股票的最好时机(一)](../../2022/01/牛客_0007_简单_买卖股票的最好时机(一).md)  
> [[简单, 牛客] 反转数字](../../2022/03/牛客_0057_简单_反转数字.md)  
> [[简单, 牛客] 字符串变形](../../2022/04/牛客_0089_简单_字符串变形.md)  
> [[简单, 牛客] 扑克牌顺子](../../2022/03/牛客_0063_简单_扑克牌顺子.md)  
> [[简单, 牛客] 数组中出现次数超过一半的数字](../../2022/03/牛客_0073_简单_数组中出现次数超过一半的数字.md)  
  > 

</details>

<details><summary><b>经典 (37)</b></summary>

> [[中等, LeetCode] 下一个排列 🔥](../../2022/10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 二叉树的完全性检验 🔥](../../2022/03/LeetCode_0958_中等_二叉树的完全性检验.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../../2022/06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, 剑指Offer2] 整数除法 🔥](../../2022/09/剑指Offer2_001_中等_整数除法.md)  
> [[中等, 剑指Offer] 丑数 🔥](剑指Offer_4900_中等_丑数.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](../../2022/01/剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 剑指Offer] 复杂链表的复制 (深拷贝) 🔥](剑指Offer_3500_中等_复杂链表的复制(深拷贝).md)  
> [[中等, 剑指Offer] 字符串的排列 (全排列) 🔥](剑指Offer_3800_中等_字符串的排列(全排列).md)  
> [[中等, 剑指Offer] 把字符串转换成整数 🔥](../../2022/01/剑指Offer_6700_中等_把字符串转换成整数.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 剑指Offer] 栈的压入、弹出序列 🔥](../11/剑指Offer_3100_中等_栈的压入、弹出序列.md)  
> [[中等, 剑指Offer] 重建二叉树 🔥](../11/剑指Offer_0700_中等_重建二叉树.md)  
> [[中等, 剑指Offer] 顺时针打印矩阵 (3种思路4个写法) 🔥](../11/剑指Offer_2900_中等_顺时针打印矩阵(3种思路4个写法).md)  
> [[中等, 牛客] 01背包 🔥](../../2022/05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 丢棋子问题 (鹰蛋问题) 🔥](../../2022/04/牛客_0087_中等_丢棋子问题(鹰蛋问题).md)  
> [[中等, 牛客] 字符串的排列 🔥](../../2022/05/牛客_0121_中等_字符串的排列.md)  
> [[中等, 牛客] 寻找峰值 🔥](../../2022/04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 岛屿数量 🔥](../../2022/04/牛客_0109_中等_岛屿数量.md)  
> [[中等, 牛客] 把字符串转换成整数(atoi) 🔥](../../2022/04/牛客_0100_中等_把字符串转换成整数(atoi).md)  
> [[中等, 牛客] 数组中只出现一次的两个数字 🔥](../../2022/03/牛客_0075_中等_数组中只出现一次的两个数字.md)  
> [[中等, 牛客] 最长公共子序列(二) 🔥](../../2022/04/牛客_0092_中等_最长公共子序列(二).md)  
> [[中等, 牛客] 栈和排序 🔥](../../2022/05/牛客_0115_中等_栈和排序.md)  
> [[中等, 牛客] 汉诺塔问题 🔥](../../2022/03/牛客_0067_中等_汉诺塔问题.md)  
  > 
> [[困难, LeetCode] 编辑距离 🔥](../../2022/06/LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 数组中的逆序对 🔥](../../2022/01/剑指Offer_5100_困难_数组中的逆序对.md)  
> [[困难, 牛客] 接雨水问题 🔥](../../2022/05/牛客_0128_困难_接雨水问题.md)  
> [[困难, 牛客] 设计LFU缓存结构 🔥](../../2022/04/牛客_0094_困难_设计LFU缓存结构.md)  
> [[困难, 牛客] 设计LRU缓存结构 🔥](../../2022/04/牛客_0093_困难_设计LRU缓存结构.md)  
  > 
> [[简单, LeetCode] 二叉树的最大深度 🔥](../../2022/07/LeetCode_0104_简单_二叉树的最大深度.md)  
> [[简单, LeetCode] 反转链表 🔥](../../2022/10/LeetCode_0206_简单_反转链表.md)  
> [[简单, 剑指Offer] 二叉搜索树的最近公共祖先 🔥](../../2022/01/剑指Offer_6801_简单_二叉搜索树的最近公共祖先.md)  
> [[简单, 剑指Offer] 反转链表 🔥](../11/剑指Offer_2400_简单_反转链表.md)  
> [[简单, 剑指Offer] 最小的k个数 (partition操作) 🔥](剑指Offer_4000_简单_最小的k个数(partition操作).md)  
> [[简单, 牛客] 二进制中1的个数 🔥](../../2022/05/牛客_0120_简单_二进制中1的个数.md)  
> [[简单, 牛客] 单链表的排序 🔥](../../2022/03/牛客_0070_简单_单链表的排序.md)  
> [[简单, 牛客] 求平方根 🔥](../../2022/02/牛客_0032_简单_求平方根.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
