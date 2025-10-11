## <title - autoUpdate>
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [dfs2dp]
source: LeetCode
level: 中等
number: '3186'
name: '施咒的最大总伤害'
companies: []
-->

> [title](#a-url)

<summary><b>问题简述</b></summary>

```txt
一个魔法师有许多不同的咒语。
给你一个数组 power ，其中每个元素表示一个咒语的伤害值，可能会有多个咒语有相同的伤害值。

已知魔法师使用伤害值为 power[i] 的咒语时，他们就 不能 使用伤害为 power[i] - 2 ，power[i] - 1 ，power[i] + 1 或者 power[i] + 2 的咒语。

每个咒语最多只能被使用 一次 。

请你返回这个魔法师可以达到的伤害值之和的 最大值 。
```
- 简单翻译一下:
    - 从一个数组中取数, 当你取了某个数 `x` 后, 那么就不能取 `x±1` 和 `x±2` 了, 但是 `x` 本身可以取多次;
    - 返回能获得的最大值;

<!-- 
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

<summary><b>思路</b></summary>

- 比较典型的 **值域 DP** 问题, 
    - 因为状态不是按数组下标, 而是按数值大小排序后在值域上转移;
- 也称 "打家劫舍类 DP" (House Robber–type DP),
    - 特点: 相邻元素不能同时取 的 一维 DP;
- 如果值域稀疏，需要先离散化，再在离散后的序列上做 DP。

<details><summary><b>Python</b></summary>

```python
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        from collections import Counter
        from functools import cache

        cnt = Counter(power)
        a = sorted(cnt)
        n = len(a)

        @cache
        def dfs(i):  # a[i:n] 能获得的最大值
            if i >= n:
                return 0
            
            x = a[i]
            j = i + 1
            while j < n and a[j] <= x + 2:  # 找到 i 之后下一个位置 j, 要求 a[j] > x+2
                j += 1
            
            take = dfs(j) + x * cnt[x]  # 可能 1: 选了 a[i], 那么下一个位置必须从 j 开始, 因为 a[j] > x+2
            not_take = dfs(i + 1)       # 可能 2: 没选 a[i], 那么直接从下一个开始

            return max(take, not_take)
        
        return dfs(0)
```

</details>


<!--START_SECTION:relate_note-->
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
<!--END_SECTION:relate_problem-->