## 无重复字符的最长子串
<!--START_SECTION:badge-->

![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&label_color=gray&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&label_color=gray&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3&label_color=gray&color=blue&style=flat-square)](../../../README.md#滑动窗口)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&label_color=gray&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)

<!--END_SECTION:badge-->
<!--info
tags: [滑动窗口, lc100]
source: LeetCode
level: 中等
number: '0003'
name: 无重复字符的最长子串
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
```
> [3. 无重复字符的最长子串 - 力扣（LeetCode）](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

<!-- 
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->


<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路：滑动窗口</b></summary>

- 维护一个已经出现过的字符集合；

<details><summary><b>Python 写法1 （滑动窗口模板，推荐写法）</b></summary>

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        used = set()
        l = r = 0  # 窗口边界
        ret = 0
        while r < len(s):
            while s[r] in used:  # 滑动左边界
                # 判断的是右边界，移动的是左边界
                used.remove(s[l])
                l += 1
            ret = max(ret, r - l + 1)
            used.add(s[r])
            r += 1
        return ret
```

</details>


<details><summary><b>Python 写法2 （优化）</b></summary>

- **优化**：直接移动 l 指针到重复字符的下一个位置，减少 l 指针移动；
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = dict()
        l = r = 0  # [l, r] 闭区间
        ret = 0
        while r < len(s):
            if s[r] in used and l <= used[s[r]]:  # l <= used[s[r]] 的意思是重复字符出现在窗口内；
                l = used[s[r]] + 1
            ret = max(ret, r - l + 1)
            used[s[r]] = r
            r += 1
        return ret
```

</details>
<!--START_SECTION:relate-->

---

### 相关主题

<details><summary><b>滑动窗口</b></summary>

> [[中等, 牛客] 最长无重复子数组](../03/牛客_0041_中等_最长无重复子数组.md)  
  > 
> [[困难, 剑指Offer] 滑动窗口的最大值](../01/剑指Offer_5901_困难_滑动窗口的最大值.md)  
> [[困难, 牛客] 数组中的最长连续子序列](../04/牛客_0095_困难_数组中的最长连续子序列.md)  
> [[困难, 牛客] 最小覆盖子串](牛客_0028_困难_最小覆盖子串.md)  
  > 
> [[简单, 牛客] 压缩字符串(一)](../04/牛客_0101_简单_压缩字符串(一).md)  
  > 

</details>
<details><summary><b>LeetCode Hot 100</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 两数相加 🔥](../../2021/10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 全排列 🔥](../10/LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](../10/LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 字母异位词分组 🔥](../10/LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 括号生成 🔥](../10/LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](../10/LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](../10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, LeetCode] 组合总和 🔥](../10/LeetCode_0039_中等_组合总和.md)  
> [[中等, LeetCode] 组合总和II 🔥](../10/LeetCode_0040_中等_组合总和II.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](../10/LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 有效的括号 🔥](../03/LeetCode_0020_简单_有效的括号.md)  
  > 

</details>

<!--END_SECTION:relate-->