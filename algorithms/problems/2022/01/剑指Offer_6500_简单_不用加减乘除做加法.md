## 不用加减乘除做加法
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&label_color=gray&color=yellow&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&label_color=gray&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E4%BD%8D%E8%BF%90%E7%AE%97&label_color=gray&color=blue&style=flat-square)](../../../README.md#位运算)
<!--END_SECTION:badge-->
<!--info
tags: [位运算]
source: 剑指Offer
level: 简单
number: '6500'
name: 不用加减乘除做加法
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
求两个整数之和，要求不能使用 “+”、“-”、“*”、“/” 运算符号。
```

<details><summary><b>详细描述</b></summary>

```txt
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:
    输入: a = 1, b = 1
    输出: 2

提示：
    a, b 均可能是负数或 0
    结果不会溢出 32 位整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

<div align="center"><img src="../../../_assets/剑指Offer_065_简单_不用加减乘除做加法.png" height="300" /></div>

> [不用加减乘除做加法（位运算，清晰图解）](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/)

- 不用编程语言之间略有区别；

<details><summary><b>Java（推荐）</b></summary>

```java
class Solution {
    public int add(int a, int b) {
        while(b != 0) { // 当进位为 0 时跳出
            int c = (a & b) << 1;  // c = 进位
            a ^= b; // a = 非进位和
            b = c; // b = 进位
        }
        return a;
    }
}
```

</details>

<details><summary><b>Python</b></summary>

- Python 中

```python
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x  # 转为补码形式
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)  # 还原
```

</details>

<details><summary><b>C++</b></summary>

> [不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/dian-zan-yao-wo-zhi-dao-ni-xiang-kan-dia-ovxy/)

```cpp
class Solution {
public:
    int add(int a, int b) {
        while (b) {
            int carry = a & b; // 计算 进位
            a = a ^ b; // 计算 本位
            b = (unsigned)carry << 1;  // C++中负数不支持左位移
        }
        return a;
    }
};
```

</details>


<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>位运算</b></summary>

> [[中等, LeetCode] 两数相除](../../2021/10/LeetCode_0029_中等_两数相除.md)  
> [[中等, LeetCode] 重复的DNA序列](../07/LeetCode_0187_中等_重复的DNA序列.md)  
> [[中等, 剑指Offer] 数组中数字出现的次数](剑指Offer_5601_中等_数组中数字出现的次数.md)  
> [[中等, 剑指Offer] 数组中数字出现的次数](剑指Offer_5602_中等_数组中数字出现的次数.md)  
> [[中等, 牛客] 数组中只出现一次的两个数字 🔥](../03/牛客_0075_中等_数组中只出现一次的两个数字.md)  
  > 
> [[困难, 牛客] N皇后问题](../03/牛客_0039_困难_N皇后问题.md)  
  > 
> [[简单, 剑指Offer] 二进制中1的个数](../../2021/11/剑指Offer_1500_简单_二进制中1的个数.md)  
> [[简单, 牛客] 二进制中1的个数 🔥](../05/牛客_0120_简单_二进制中1的个数.md)  
  > 

</details>
<!--END_SECTION:relate-->