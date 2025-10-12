## 亲密字符串
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=green&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%AD%97%E7%AC%A6%E4%B8%B2&color=blue&style=flat-square)](../../../README.md#字符串)
[![](https://img.shields.io/static/v1?label=&message=%E6%A8%A1%E6%8B%9F&color=blue&style=flat-square)](../../../README.md#模拟)
<!--END_SECTION:badge-->
<!--info
tags: [模拟, 字符串]
source: LeetCode
level: 简单
number: '0859'
name: 亲密字符串
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给你两个字符串 s 和 goal , 只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果, 就返回 true ; 否则返回 false.

例如, 在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad".
```

<details><summary><b>详细描述</b></summary>

```txt
给你两个字符串 s 和 goal , 只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果, 就返回 true ; 否则返回 false .

交换字母的定义是: 取两个下标 i 和 j (下标从 0 开始) 且满足 i != j , 接着交换 s[i] 和 s[j] 处的字符.

例如, 在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad".


示例 1:
    输入: s = "ab", goal = "ba"
    输出: true
    解释: 你可以交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba", 此时 s 和 goal 相等.
示例 2:
    输入: s = "ab", goal = "ab"
    输出: false
    解释: 你只能交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba", 此时 s 和 goal 不相等.
示例 3:
    输入: s = "aa", goal = "aa"
    输出: true
    解释: 你可以交换 s[0] = 'a' 和 s[1] = 'a' 生成 "aa", 此时 s 和 goal 相等.
示例 4:
    输入: s = "aaaaaaabc", goal = "aaaaaaacb"
    输出: true


提示:
    1 <= s.length, goal.length <= 2 * 10^4
    s 和 goal 由小写英文字母组成

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/buddy-strings
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

</details>



<summary><b>思路: 分情况讨论</b></summary>

- 当 `len(s)!= len(goal)` 时: False
- 当 `len(s) == len(goal)` 时:
    - 当 `s != goal` 时: 当且仅当不同的字符数量等于 2, 且交换后满足条件;
    - 当 `s == goal` 时: `s` 中存在出现至少 2 次的字符;

- `s == goal` 的情况比较容易被忽略;


<details><summary><b>Python: 模拟</b></summary>

```python
class Solution:

    def buddyStrings(self, s: str, goal: str) -> bool:
        """"""
        if len(s)!= len(goal):
            return False

        dif = []
        cs = set()
        for i, c in enumerate(s):
            cs.add(c)
            if s[i] != goal[i]:
                dif.append(i)

        # 存在字符出现过 2 次
        if s == goal and len(cs) < len(s):
            return True

        # 只存在两个位置字符不同, 且交换后满足条件
        if len(dif) == 2 and (s[dif[0]], s[dif[1]]) == (goal[dif[1]], goal[dif[0]]):
            return True

        return False
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
> [[简单, LeetCode] 字符串中的单词数](../../2022/07/LeetCode_0434_简单_字符串中的单词数.md)  
> [[简单, 剑指Offer] 左旋转字符串](../../2022/01/剑指Offer_5802_简单_左旋转字符串.md)  
> [[简单, 剑指Offer] 替换空格](剑指Offer_0500_简单_替换空格.md)  
> [[简单, 牛客] 压缩字符串(一)](../../2022/04/牛客_0101_简单_压缩字符串(一).md)  
> [[简单, 牛客] 反转字符串](../../2022/04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 旋转字符串](../../2022/05/牛客_0114_简单_旋转字符串.md)  
> [[简单, 牛客] 最长公共前缀](../../2022/03/牛客_0055_简单_最长公共前缀.md)  
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
> [[简单, 剑指Offer] 扑克牌中的顺子](../../2022/01/剑指Offer_6100_简单_扑克牌中的顺子.md)  
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](../12/剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
> [[简单, 牛客] 买卖股票的最好时机(一)](../../2022/01/牛客_0007_简单_买卖股票的最好时机(一).md)  
> [[简单, 牛客] 反转数字](../../2022/03/牛客_0057_简单_反转数字.md)  
> [[简单, 牛客] 字符串变形](../../2022/04/牛客_0089_简单_字符串变形.md)  
> [[简单, 牛客] 扑克牌顺子](../../2022/03/牛客_0063_简单_扑克牌顺子.md)  
> [[简单, 牛客] 数组中出现次数超过一半的数字](../../2022/03/牛客_0073_简单_数组中出现次数超过一半的数字.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
