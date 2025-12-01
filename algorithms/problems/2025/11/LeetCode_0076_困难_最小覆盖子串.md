## 最小覆盖子串
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-11-11%2017%3A59%3A46&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&color=red&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
[![](https://img.shields.io/static/v1?label=&message=%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3&color=blue&style=flat-square)](../../../README.md#滑动窗口)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [滑动窗口, lc100]
source: 'LeetCode'
level: '困难'
number: '76'
name: '最小覆盖子串'
-->

> [76. 最小覆盖子串 - 力扣 (LeetCode) ](https://leetcode.cn/problems/minimum-window-substring/)

<summary><b>问题简述</b></summary>

```md
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
```

<!-- 
<details><summary><b>详细描述</b></summary>

```md
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

---

<summary><b>思路: 滑动窗口</b></summary>

- **核心目标**: 在字符串 S 中找到最短的子串, 使其包含字符串 T 的所有字符 (包括重复次数). 
- **滑动窗口法**: 用两个指针维护一个窗口; 右指针扩展窗口直到包含所有目标字符; 左指针收缩窗口以尽量缩短长度; 在过程中不断更新最优解. 
- **复杂度分析**: 每个字符最多被左右指针访问一次; 时间复杂度 O(n); 空间复杂度 O(m), 其中 m 为 T 的字符种类数. 

<details><summary><b>Python</b></summary>

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        from collections import Counter

        ret = ''
        need = Counter(t)                           # 需要满足的每种字符数
        book = Counter()                            # 记录出现过的字符数
        
        # def check():                                # 检验是否满足情况
        #     return all(book[k] >= need[k] for k in need)
        
        l, r = 0, 0
        while r < len(s):
            book[s[r]] += 1
            # while check():
            while book >= need:                     # Counter 可以直接比较大小
                if not ret or r - l < len(ret):     # 更新答案
                    ret = s[l: r + 1]
                book[s[l]] -= 1
                l += 1                              # 移动左边界
            r += 1                                  # 移动右边界
        
        return ret
```

</details>

> 优化版: [两种方法: 从 O(52m+n) 到 O(m+n) - 灵茶山艾府](https://leetcode.cn/problems/minimum-window-substring/solutions/2713911/liang-chong-fang-fa-cong-o52mn-dao-omnfu-3ezz/)


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


<details><summary><b>LeetCode Hot 100 (32)</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../../2022/10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 两数相加 🔥](../../2021/10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 全排列 🔥](../../2022/10/LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](../../2022/10/LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../../2022/01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 和为K的子数组 🔥](LeetCode_0560_中等_和为K的子数组.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../../2022/10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 字母异位词分组 🔥](../../2022/10/LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 找到字符串中所有字母异位词 🔥](LeetCode_0438_中等_找到字符串中所有字母异位词.md)  
> [[中等, LeetCode] 括号生成 🔥](../../2022/10/LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](../../2022/10/LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, LeetCode] 无重复字符的最长子串 🔥](../../2022/02/LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 最长连续序列 🔥](LeetCode_0128_中等_最长连续序列.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](../../2022/10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, LeetCode] 组合总和 II 🔥](../../2022/10/LeetCode_0040_中等_组合总和II.md)  
> [[中等, LeetCode] 组合总和 🔥](../../2022/10/LeetCode_0039_中等_组合总和.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../../2022/02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](../../2022/10/LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../../2022/02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../../2022/10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../../2022/01/LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](../../2022/10/LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, 牛客] 最小覆盖子串 🔥](../../2022/02/牛客_0028_困难_最小覆盖子串.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 有效的括号 🔥](../../2022/03/LeetCode_0020_简单_有效的括号.md)  
> [[简单, LeetCode] 移动零 🔥](LeetCode_0283_简单_移动零.md)  
  > 

</details>

<details><summary><b>滑动窗口 (7)</b></summary>

> [[中等, LeetCode] 找到字符串中所有字母异位词 🔥](LeetCode_0438_中等_找到字符串中所有字母异位词.md)  
> [[中等, LeetCode] 无重复字符的最长子串 🔥](../../2022/02/LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, 牛客] 最长无重复子数组](../../2022/03/牛客_0041_中等_最长无重复子数组.md)  
  > 
> [[困难, 剑指Offer] 滑动窗口的最大值](../../2022/01/剑指Offer_5901_困难_滑动窗口的最大值.md)  
> [[困难, 牛客] 数组中的最长连续子序列](../../2022/04/牛客_0095_困难_数组中的最长连续子序列.md)  
> [[困难, 牛客] 最小覆盖子串 🔥](../../2022/02/牛客_0028_困难_最小覆盖子串.md)  
  > 
> [[简单, 牛客] 压缩字符串(一)](../../2022/04/牛客_0101_简单_压缩字符串(一).md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
