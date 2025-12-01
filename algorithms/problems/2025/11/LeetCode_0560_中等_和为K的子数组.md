## 和为K的子数组
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-11-11%2013%3A04%3A08&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%8D%E7%BC%80%E5%92%8C&color=blue&style=flat-square)](../../../README.md#前缀和)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [前缀和, lc100]
source: 'LeetCode'
level: '中等'
number: '560'
name: '和为K的子数组'
-->

> [560. 和为 K 的子数组 - 力扣 (LeetCode) ](https://leetcode.cn/problems/subarray-sum-equals-k/)

<summary><b>问题简述</b></summary>

```md
给你一个整数数组 nums (存在负数) 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。
```

<!-- 
<details><summary><b>详细描述</b></summary>

```md
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

---

<summary><b>思路: 前缀和 + 哈希表</b></summary>

- 构建前缀和 `p`
- 转化为查找问题
    - 如果 `p[j] - p[i] == k`, 说明子数组 `nums[i..j-1]` 的和为 k
    - 等价于: 在遍历到前缀和 `p[j]` 时, 查找是否存在 `p[i] = p[j] - k`

<details><summary><b>Python</b></summary>

```python
def subarraySum(self, nums: List[int], k: int) -> int:
    
    p = [0]                     # 构建前缀和
    for x in nums:
        p.append(x + p[-1])

    ans = 0
    cnt = defaultdict(int)      # 哈希表: 前缀和出现次数
    for s in p:
        ans += cnt[s - k]       # 如果存在前缀和 (s-k)，说明区间和为 k
        cnt[s] += 1             # 更新当前前缀和出现次数 (因为存在负数, 所以相同的前缀和是可能多个的)
    
    return ans
```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

> 🌧️ _暂无主题相关的笔记_


<details><summary><b>其他算法笔记</b></summary>

- [二分查找相关](../../../../notes/_archives/2025/10/二分查找备忘.md)  
- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
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
> [[困难, LeetCode] 最小覆盖子串 🔥](LeetCode_0076_困难_最小覆盖子串.md)  
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

<details><summary><b>前缀和 (5)</b></summary>

> [[中等, LeetCode] 从魔法师身上吸取的最大能量](../10/LeetCode_3147_中等_从魔法师身上吸取的最大能量.md)  
> [[中等, LeetCode] 路径总和III](../../2022/06/LeetCode_0437_中等_路径总和III.md)  
> [[中等, 剑指Offer] 构建乘积数组](../../2022/01/剑指Offer_6600_中等_构建乘积数组.md)  
> [[中等, 牛客] 和为K的连续子数组](../../2022/05/牛客_0125_中等_和为K的连续子数组.md)  
  > 
> [[简单, LeetCode] 区域和检索 - 数组不可变](LeetCode_0303_简单_区域和检索-数组不可变.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
