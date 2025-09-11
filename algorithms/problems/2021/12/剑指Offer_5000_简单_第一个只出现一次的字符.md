## 第一个只出现一次的字符
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&label_color=gray&color=yellow&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&label_color=gray&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%93%88%E5%B8%8C%E8%A1%A8%28Hash%29&label_color=gray&color=blue&style=flat-square)](../../../README.md#哈希表hash)
<!--END_SECTION:badge-->
<!--info
tags: [哈希表]
source: 剑指Offer
level: 简单
number: '5000'
name: 第一个只出现一次的字符
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。
```

<details><summary><b>详细描述</b></summary>

```txt
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:
    输入：s = "abaccdeff"
    输出：'b'
示例 2:
    输入：s = "" 
    输出：' '

限制：
    0 <= s 的长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->


<summary><b>思路1：哈希表</b></summary>

<details><summary><b>Python</b></summary>

```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = defaultdict(int)  # python 3.6 之后 dict 默认就是有序的

        for c in s:
            dic[c] += 1

        for c in s:
            if dic[c] == 1: 
                return c

        return ' '
```

</details>


<summary><b>思路1：有序哈希表</b></summary>

<details><summary><b>Python</b></summary>

- python 3.6 之后 dict 默认就是有序的；
    > [为什么 Python 3.6 以后字典有序并且效率更高？](https://www.cnblogs.com/xieqiankun/p/python_dict.html)

```python
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = defaultdict(int)  # python 3.6 之后 dict 默认就是有序的

        for c in s:
            dic[c] += 1

        for c, v in dic.items():
            if v == 1: 
                return c

        return ' '
```

</details>
<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>哈希表(Hash)</b></summary>

> [[中等, LeetCode] 字母异位词分组 🔥](../../2022/10/LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 重复的DNA序列](../../2022/07/LeetCode_0187_中等_重复的DNA序列.md)  
> [[中等, 剑指Offer] 复杂链表的复制（深拷贝） 🔥](剑指Offer_3500_中等_复杂链表的复制（深拷贝）.md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 牛客] 和为K的连续子数组](../../2022/05/牛客_0125_中等_和为K的连续子数组.md)  
  > 
> [[困难, 牛客] 数组中的最长连续子序列](../../2022/04/牛客_0095_困难_数组中的最长连续子序列.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../10/LeetCode_0001_简单_两数之和.md)  
> [[简单, 剑指Offer] 数组中重复的数字](../11/剑指Offer_0300_简单_数组中重复的数字.md)  
> [[简单, 牛客] 两数之和](../../2022/03/牛客_0061_简单_两数之和.md)  
> [[简单, 牛客] 第一个只出现一次的字符](../../2022/02/牛客_0031_简单_第一个只出现一次的字符.md)  
> [[简单, 程序员面试金典] 判定是否互为字符重排](../../2022/09/程序员面试金典_0102_简单_判定是否互为字符重排.md)  
  > 

</details>
<!--END_SECTION:relate-->