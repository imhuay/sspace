## <title - autoUpdate>
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [前缀和]
source: 'LeetCode'
level: '中等'
number: '560'
name: '和为K的子数组'
-->

> [560. 和为 K 的子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/subarray-sum-equals-k/)

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

<summary><b>思路: 前缀和+哈希表</b></summary>

- 构建前缀和 `p`
- 转化为查找问题
    - 如果 `p[j] - p[i] == k`, 说明子数组 `nums[i..j-1]` 的和为 k
    - 等价于：在遍历到前缀和 `p[j]` 时，查找是否存在 `p[i] = p[j] - k`

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
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
<!--END_SECTION:relate_problem-->