## 和为K的子数组
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-11-10%2003%3A02%3A25&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
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
