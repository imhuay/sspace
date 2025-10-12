## 替换空格
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%AD%97%E7%AC%A6%E4%B8%B2&color=blue&style=flat-square)](../../../README.md#字符串)
<!--END_SECTION:badge-->
<!--info
tags: [字符串]
source: 剑指Offer
level: 简单
number: '0500'
name: 替换空格
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
实现一个函数, 把字符串 s 中的每个空格替换成"%20".
```

<details><summary><b>详细描述</b></summary>

```txt
请实现一个函数, 把字符串 s 中的每个空格替换成"%20".

示例 1:
    输入: s = "We are happy."
    输出: "We%20are%20happy."

限制:
    0 <= s 的长度 <= 10000

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

</details>


<summary><b>思路</b></summary>

- Python、Java 中的字符串都是不可变类型, 所以始终要申请新的容器; 那么问题就很简单, 替换拼接即可;
- C++ 中 string 是可变类型, 因此可以尝试原地替换;


<details><summary><b>Python</b></summary>

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        buf = []
        for c in s:
            if c == ' ':
                buf.append('%20')
            else:
                buf.append(c)

        return ''.join(buf)
```

</details>

<details><summary><b>C++: 原地替换</b></summary>

```cpp
class Solution {
public:
    string replaceSpace(string s) {
        // 统计空格数量
        int space_cnt = 0;
        for (char c : s) {
            if (c == ' ') space_cnt++;
        }
        // 修改 s 长度
        int i = s.size() - 1;  // 原来的长度
        s.resize(s.size() + 2 * space_cnt);  
        int j = s.size() - 1;  // 新的长度
        // 倒序遍历修改
        while (i < j) {
            if (s[i] != ' ')
                s[j] = s[i];
            else {
                s[j - 2] = '%';
                s[j - 1] = '2';
                s[j] = '0';
                j -= 2;
            }
            i--;
            j--;
        }
        return s;
    }
};
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


<details><summary><b>字符串 (16)</b></summary>

> [[中等, LeetCode] 电话号码的字母组合 🔥](../../2022/10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, 剑指Offer] 把字符串转换成整数 🔥](../../2022/01/剑指Offer_6700_中等_把字符串转换成整数.md)  
> [[中等, 剑指Offer] 表示数值的字符串](剑指Offer_2000_中等_表示数值的字符串.md)  
> [[中等, 牛客] 大数乘法](../../2022/01/牛客_0010_中等_大数乘法.md)  
> [[中等, 牛客] 大数加法](../../2022/01/牛客_0001_中等_大数加法.md)  
> [[中等, 牛客] 把字符串转换成整数(atoi) 🔥](../../2022/04/牛客_0100_中等_把字符串转换成整数(atoi).md)  
> [[中等, 牛客] 比较版本号](../../2022/04/牛客_0104_中等_比较版本号.md)  
> [[中等, 牛客] 验证IP地址](../../2022/05/牛客_0113_中等_验证IP地址.md)  
  > 
> [[困难, 剑指Offer] 正则表达式匹配](剑指Offer_1900_困难_正则表达式匹配.md)  
  > 
> [[简单, LeetCode] 亲密字符串](LeetCode_0859_简单_亲密字符串.md)  
> [[简单, LeetCode] 字符串中的单词数](../../2022/07/LeetCode_0434_简单_字符串中的单词数.md)  
> [[简单, 剑指Offer] 左旋转字符串](../../2022/01/剑指Offer_5802_简单_左旋转字符串.md)  
> [[简单, 牛客] 压缩字符串(一)](../../2022/04/牛客_0101_简单_压缩字符串(一).md)  
> [[简单, 牛客] 反转字符串](../../2022/04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 旋转字符串](../../2022/05/牛客_0114_简单_旋转字符串.md)  
> [[简单, 牛客] 最长公共前缀](../../2022/03/牛客_0055_简单_最长公共前缀.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
