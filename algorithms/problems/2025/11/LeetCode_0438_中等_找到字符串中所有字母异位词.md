## <title - autoUpdate>
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

> [两种方法：定长滑窗/不定长滑窗 - 灵茶山艾府](https://leetcode.cn/problems/find-all-anagrams-in-a-string/solutions/2969498/liang-chong-fang-fa-ding-chang-hua-chuan-14pd)


<!--START_SECTION:relate_note-->
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
<!--END_SECTION:relate_problem-->