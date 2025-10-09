## <title - autoUpdate>
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [单调栈]
source: LeetCode
level: 中等
number: '739'
name: '每日温度'
companies: []
-->

> [739. 每日温度 - 力扣（LeetCode）](https://leetcode.cn/problems/daily-temperatures)

<summary><b>问题简述</b></summary>

```txt
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
如果气温在这之后都不会升高，请在该位置用 0 来代替。
```

<!-- 
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

<summary><b>思路 1: 暴力 (超时)</b></summary>

- 参考 **选择排序** 模板, 双循环, 外层固定 `i`, 内层找 `[i+1, n)` 中第一个更大的元素;
- 该方法会超时;
- [官方题解 (方法一)](https://leetcode.cn/problems/daily-temperatures/solutions/283196/mei-ri-wen-du-by-leetcode-solution) 给出了一个 **基于逆序遍历** 的不超时暴力方法.

<details><summary><b>Python</b></summary>

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        ret = [0] * n
        s = []

        for i in range(n):
            ret[i] = 0
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    ret[i] = j - i
                    break

        return ret
```

</details>

<summary><b>思路 2: 单调栈</b></summary>

- 维护一个 **存储下标** 的单调栈，从栈底到栈顶的下标对应的温度依次递减;
    > 存储下标永远是比存储值更好的方案, 无轮你是否会用到下标信息;
- 如果一个下标在单调栈里，则表示尚未找到下一次温度更高的下标.
- 只要当前温度 `i` 大于栈顶 `idx`, 就出栈, 否则就入栈;
    - 每次出栈时, `i - idx` 就是 `idx` 对应的等待天数;
> [官方题解 (方法二)](https://leetcode.cn/problems/daily-temperatures/solutions/283196/mei-ri-wen-du-by-leetcode-solution)

<details><summary><b>Python</b></summary>

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        ret = [0] * n
        s = []

        for i in range(n):
            while s and temperatures[i] > temperatures[s[-1]]:
                idx = s.pop()
                ret[idx] = i - idx
            
            s.append(i)
            
        return ret
```

</details>


<!--START_SECTION:relate-->
<!--END_SECTION:relate-->