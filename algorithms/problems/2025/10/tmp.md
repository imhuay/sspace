## <title - autoUpdate>
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [前缀和, 数组]
source: LeetCode
level: 中等
number: '3147'
name: 从魔法师身上吸取的最大能量
companies: []
-->

> [3147. 从魔法师身上吸取的最大能量 - 力扣（LeetCode）](https://leetcode.cn/problems/taking-maximum-energy-from-the-mystic-dungeon)

<summary><b>问题简述</b></summary>

```txt
在神秘的地牢中，n 个魔法师站成一排。每个魔法师都拥有一个属性，这个属性可以给你提供能量。有些魔法师可能会给你负能量，即从你身上吸取能量。

你被施加了一种诅咒，当你从魔法师 i 处吸收能量后，你将被立即传送到魔法师 (i + k) 处。这一过程将重复进行，直到你到达一个不存在 (i + k) 的魔法师为止。

换句话说，你将选择一个起点，然后以 k 为间隔跳跃，直到到达魔法师序列的末端，在过程中吸收所有的能量。

给定一个数组 energy 和一个整数k，返回你能获得的 最大 能量。

示例 1：
    输入： energy = [5,2,-10,-5,1], k = 3
    输出： 3
    解释：可以从魔法师 1 开始，吸收能量 2 + 1 = 3。

示例 2：
    输入： energy = [-2,-3,-1], k = 2
    输出： -1
    解释：可以从魔法师 2 开始，吸收能量 -1。

提示：
    1 <= energy.length <= 10^5
    -1000 <= energy[i] <= 1000
    1 <= k <= energy.length - 1
```

<!-- 
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

<summary><b>思路</b></summary>

- 直观理解就是求下面这个公式的结果: <br>
    ```max([sum(energy[i::k]) for i in range(len(energy))])```
- 但是直接求会超时;
- **关键观察**:
    - 无轮从中间哪个节点开始遍历, 其终点只会落在 `[n-k, n-1]` 之间, 这启发我们可以逆序遍历.

<details><summary><b>Python</b></summary>

```python
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        ret = float('-inf')
        n = len(energy)
        for fin in range(n - k, n):
            tmp = 0
            cnt = 0
            while (idx := fin - cnt * k) >= 0:
                tmp += energy[idx]
                ret = max(ret, tmp)
                cnt += 1
        
        return ret
```

</details>


<!--START_SECTION:relate-->
<!--END_SECTION:relate-->