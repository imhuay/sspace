## 数组中数字出现的次数
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&label_color=gray&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&label_color=gray&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E4%BD%8D%E8%BF%90%E7%AE%97&label_color=gray&color=blue&style=flat-square)](../../../README.md#位运算)
<!--END_SECTION:badge-->
<!--info
tags: [位运算]
source: 剑指Offer
level: 中等
number: '5601'
name: 数组中数字出现的次数
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
一个整型数组中除两个数字外, 其他数字都出现了两次. 求这两个只出现一次的数字.
要求时间复杂度是O(n), 空间复杂度是O(1).
```

<details><summary><b>详细描述</b></summary>

```txt
一个整型数组 nums 里除两个数字之外, 其他数字都出现了两次. 请写程序找出这两个只出现一次的数字. 要求时间复杂度是O(n), 空间复杂度是O(1).

示例 1:
    输入: nums = [4,1,4,6]
    输出: [1,6] 或 [6,1]
示例 2:
    输入: nums = [1,2,10,4,1,4,3,3]
    输出: [2,10] 或 [10,2]

限制:
    2 <= nums.length <= 10000

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 异或运算的性质:
    ```
    性质1: 0^a = a
    性质2: a^a = 0
    性质3 (交换律) : a^b = b^a
    性质4 (结合律) : (a^b)^c = a^(b^c)
    ```
- 根据性质1 和性质2, 可以构造如下算法:
    ```
    定义 all_xor(arr) := arr[0] ^ arr[1] ^ .. ^ arr[-1]
    记这两个不同的数分别为 a 和 b
    则 ab = a ^ b = all_xor(arr)  # 存在两个相同数字的都被消去
    因为 a != b, 则 ab 的二进制表示中必然有一个为 1 (因为 0^1=1)
    根据这个位置的 1 将 nums 分为两组, 则 a 和 b 分别在这两组数字中, 分别求一次 all_xor 即可;
    ```

<details><summary><b>Python</b></summary>

```python
class Solution:
    def singleNumbers(self, arr: List[int]) -> List[int]:

        ab = 0  # 计算 a ^ b
        for x in arr:
            ab ^= x

        r = ab & (~ab + 1)  # 计算 ab 最右侧的 1

        a = b = 0
        for x in arr:  # 根据 r 位置是否为 1 将 arr 分为两组
            if r & x:
                a ^= x
            else:
                b ^= x

        return [a, b]
```

</details>


<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>位运算</b></summary>

> [[中等, LeetCode] 两数相除](../../2021/10/LeetCode_0029_中等_两数相除.md)  
> [[中等, LeetCode] 重复的DNA序列](../07/LeetCode_0187_中等_重复的DNA序列.md)  
> [[中等, 剑指Offer] 数组中数字出现的次数](剑指Offer_5602_中等_数组中数字出现的次数.md)  
> [[中等, 牛客] 数组中只出现一次的两个数字 🔥](../03/牛客_0075_中等_数组中只出现一次的两个数字.md)  
  > 
> [[困难, 牛客] N皇后问题](../03/牛客_0039_困难_N皇后问题.md)  
  > 
> [[简单, 剑指Offer] 不用加减乘除做加法](剑指Offer_6500_简单_不用加减乘除做加法.md)  
> [[简单, 剑指Offer] 二进制中1的个数](../../2021/11/剑指Offer_1500_简单_二进制中1的个数.md)  
> [[简单, 牛客] 二进制中1的个数 🔥](../05/牛客_0120_简单_二进制中1的个数.md)  
  > 

</details>
<!--END_SECTION:relate-->