## 左旋转字符串
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&label_color=gray&color=yellow&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&label_color=gray&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%AD%97%E7%AC%A6%E4%B8%B2&label_color=gray&color=blue&style=flat-square)](../../../README.md#字符串)
<!--END_SECTION:badge-->
<!--info
tags: [字符串]
source: 剑指Offer
level: 简单
number: '5802'
name: 左旋转字符串
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
把字符串前面的 n 个字符转移到字符串的尾部.
```

<details><summary><b>详细描述</b></summary>

```txt
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部. 请定义一个函数实现字符串左旋转操作的功能. 比如, 输入字符串"abcdefg"和数字2, 该函数将返回左旋转两位得到的结果"cdefgab".

示例 1:
    输入: s = "abcdefg", k = 2
    输出: "cdefgab"
示例 2:
    输入: s = "lrloseumgh", k = 6
    输出: "umghlrlose"

限制:
    1 <= k < s.length <= 10000

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

> [左旋转字符串 (切片 / 列表 / 字符串, 清晰图解) ](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/solution/mian-shi-ti-58-ii-zuo-xuan-zhuan-zi-fu-chuan-qie-p/)

<details><summary><b>Python</b></summary>

```python
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:

        # 法1: 切片 (速度最快)
        def f1():
            return s[n:] + s[:n]

        # 法2: 列表 (面试推荐写法)
        def f2():
            ret = []
            # for i in range(n, len(s)):
            #     ret.append(s[i])
            # for i in range(n):
            #     ret.append(s[i])

            # 使用求余操作简化上述循环
            for i in range(len(s)):
                ret.append(s[(n + i) % len(s)])

            return ''.join(ret)

        return f2()

```

</details>


<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>字符串</b></summary>

> [[中等, LeetCode] 电话号码的字母组合 🔥](../10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, 剑指Offer] 把字符串转换成整数 🔥](剑指Offer_6700_中等_把字符串转换成整数.md)  
> [[中等, 剑指Offer] 表示数值的字符串](../../2021/11/剑指Offer_2000_中等_表示数值的字符串.md)  
> [[中等, 牛客] 大数乘法](牛客_0010_中等_大数乘法.md)  
> [[中等, 牛客] 大数加法](牛客_0001_中等_大数加法.md)  
> [[中等, 牛客] 把字符串转换成整数(atoi) 🔥](../04/牛客_0100_中等_把字符串转换成整数(atoi).md)  
> [[中等, 牛客] 比较版本号](../04/牛客_0104_中等_比较版本号.md)  
> [[中等, 牛客] 验证IP地址](../05/牛客_0113_中等_验证IP地址.md)  
  > 
> [[困难, 剑指Offer] 正则表达式匹配](../../2021/11/剑指Offer_1900_困难_正则表达式匹配.md)  
  > 
> [[简单, LeetCode] 亲密字符串](../../2021/11/LeetCode_0859_简单_亲密字符串.md)  
> [[简单, LeetCode] 字符串中的单词数](../07/LeetCode_0434_简单_字符串中的单词数.md)  
> [[简单, 剑指Offer] 替换空格](../../2021/11/剑指Offer_0500_简单_替换空格.md)  
> [[简单, 牛客] 压缩字符串(一)](../04/牛客_0101_简单_压缩字符串(一).md)  
> [[简单, 牛客] 反转字符串](../04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 旋转字符串](../05/牛客_0114_简单_旋转字符串.md)  
> [[简单, 牛客] 最长公共前缀](../03/牛客_0055_简单_最长公共前缀.md)  
  > 

</details>
<!--END_SECTION:relate-->