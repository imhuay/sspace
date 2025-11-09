## 找到字符串中所有字母异位词
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-11-10%2003%3A02%3A25&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%AE%9A%E9%95%BF%E6%BB%91%E7%AA%97&color=blue&style=flat-square)](../../../README.md#定长滑窗)
[![](https://img.shields.io/static/v1?label=&message=%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3&color=blue&style=flat-square)](../../../README.md#滑动窗口)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [滑动窗口, 定长滑窗]
source: 'LeetCode'
level: '中等'
number: '438'
name: '找到字符串中所有字母异位词'
-->

> <url/>

<summary><b>问题简述</b></summary>

```md
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
```

<!-- 
<details><summary><b>详细描述</b></summary>

```md
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

---

<summary><b>思路 1: 定长滑动窗口</b></summary>

- 简单来说, 就是在滑动窗口移动的过程中更新一个 **字符字典** 与 **p** 比较, 数量完全匹配的话就进行记录;
- 利用 `Counter` 简化统计代码

<details><summary><b>Python</b></summary>

```python
def findAnagrams(self, s: str, p: str) -> List[int]:
    
    from collections import Counter

    ans = []
    lp = len(p)
    cp = Counter(p)
    cs = Counter(s[:lp - 1])
    for r in range(lp - 1, len(s)):
        cs[s[r]] += 1
        l = r - lp + 1

        if cp == cs:
            ans.append(l)
            
        cs[s[l]] -= 1
        if cs[s[l]] == 0:
            del cs[s[l]]
    
    return ans
```

</details>

---

<summary><b>思路 2: 不定长滑动窗口</b></summary>

> [两种方法: 定长滑窗/不定长滑窗 - 灵茶山艾府](https://leetcode.cn/problems/find-all-anagrams-in-a-string/solutions/2969498/liang-chong-fang-fa-ding-chang-hua-chuan-14pd)


<!--START_SECTION:relate_note-->
---

### 算法笔记

- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  

<details><summary><b>其他算法笔记</b></summary>

- [二分查找相关](../../../../notes/_archives/2025/10/二分查找备忘.md)  
- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [链表操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>滑动窗口 (6)</b></summary>

> [[中等, LeetCode] 无重复字符的最长子串 🔥](../../2022/02/LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, 牛客] 最长无重复子数组](../../2022/03/牛客_0041_中等_最长无重复子数组.md)  
  > 
> [[困难, 剑指Offer] 滑动窗口的最大值](../../2022/01/剑指Offer_5901_困难_滑动窗口的最大值.md)  
> [[困难, 牛客] 数组中的最长连续子序列](../../2022/04/牛客_0095_困难_数组中的最长连续子序列.md)  
> [[困难, 牛客] 最小覆盖子串](../../2022/02/牛客_0028_困难_最小覆盖子串.md)  
  > 
> [[简单, 牛客] 压缩字符串(一)](../../2022/04/牛客_0101_简单_压缩字符串(一).md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
