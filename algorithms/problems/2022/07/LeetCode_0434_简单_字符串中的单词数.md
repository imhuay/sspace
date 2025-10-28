## 字符串中的单词数
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%AD%97%E7%AC%A6%E4%B8%B2&color=blue&style=flat-square)](../../../README.md#字符串)
<!--END_SECTION:badge-->
<!--info
tags: [字符串]
source: LeetCode
level: 简单
number: '0434'
name: 字符串中的单词数
companies: []
-->

<summary><b>问题描述</b></summary>

```txt
统计字符串中的单词个数, 这里的单词指的是连续的不是空格的字符.

请注意, 你可以假定字符串里不包括任何不可打印的字符.

示例:
    输入: "Hello, my name is John"
    输出: 5
    解释: 这里的单词是指连续的不是空格的字符, 所以 "Hello," 算作 1 个单词.

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/number-of-segments-in-a-string
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<summary><b>思路</b></summary>

<details><summary><b>Python3</b></summary>

```python
class Solution:
    def countSegments(self, s):

        # 针对第一个字符初始化, 注意处理空串
        ans = 0 if s == '' or s[0] == ' ' else 1

        for i in range(1, len(s)):
            if s[i] != ' ' and s[i - 1] == ' ':
                ans += 1

        return ans

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


<details><summary><b>字符串 (16)</b></summary>

> [[中等, LeetCode] 电话号码的字母组合 🔥](../10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, 剑指Offer] 把字符串转换成整数 🔥](../01/剑指Offer_6700_中等_把字符串转换成整数.md)  
> [[中等, 剑指Offer] 表示数值的字符串](../../2021/11/剑指Offer_2000_中等_表示数值的字符串.md)  
> [[中等, 牛客] 大数乘法](../01/牛客_0010_中等_大数乘法.md)  
> [[中等, 牛客] 大数加法](../01/牛客_0001_中等_大数加法.md)  
> [[中等, 牛客] 把字符串转换成整数(atoi) 🔥](../04/牛客_0100_中等_把字符串转换成整数(atoi).md)  
> [[中等, 牛客] 比较版本号](../04/牛客_0104_中等_比较版本号.md)  
> [[中等, 牛客] 验证IP地址](../05/牛客_0113_中等_验证IP地址.md)  
  > 
> [[困难, 剑指Offer] 正则表达式匹配](../../2021/11/剑指Offer_1900_困难_正则表达式匹配.md)  
  > 
> [[简单, LeetCode] 亲密字符串](../../2021/11/LeetCode_0859_简单_亲密字符串.md)  
> [[简单, 剑指Offer] 左旋转字符串](../01/剑指Offer_5802_简单_左旋转字符串.md)  
> [[简单, 剑指Offer] 替换空格](../../2021/11/剑指Offer_0500_简单_替换空格.md)  
> [[简单, 牛客] 压缩字符串(一)](../04/牛客_0101_简单_压缩字符串(一).md)  
> [[简单, 牛客] 反转字符串](../04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 旋转字符串](../05/牛客_0114_简单_旋转字符串.md)  
> [[简单, 牛客] 最长公共前缀](../03/牛客_0055_简单_最长公共前缀.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
