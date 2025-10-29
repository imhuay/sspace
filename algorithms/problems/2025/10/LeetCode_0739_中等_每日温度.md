## 每日温度
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-10-10%2001%3A15%3A17&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%8D%95%E8%B0%83%E6%A0%88/%E5%8D%95%E8%B0%83%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#单调栈单调队列)
<!--END_SECTION:badge-->
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

> [739. 每日温度 - 力扣 (LeetCode) ](https://leetcode.cn/problems/daily-temperatures)

<summary><b>问题简述</b></summary>

```txt
给定一个整数数组 temperatures, 表示每天的温度, 返回一个数组 answer, 
其中 answer[i] 是指对于第 i 天, 下一个更高温度出现在几天后. 
如果气温在这之后都不会升高, 请在该位置用 0 来代替. 
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

- 维护一个 **存储下标** 的单调栈, 从栈底到栈顶的下标对应的温度依次递减;
    > 存储下标永远是比存储值更好的方案, 无轮你是否会用到下标信息;
- 如果一个下标在单调栈里, 则表示尚未找到下一次温度更高的下标.
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


<details><summary><b>单调栈/单调队列 (4)</b></summary>

> [[困难, LeetCode] 柱状图中最大的矩形](LeetCode_0084_困难_柱状图中最大的矩形.md)  
> [[困难, 剑指Offer] 滑动窗口的最大值](../../2022/01/剑指Offer_5901_困难_滑动窗口的最大值.md)  
> [[困难, 牛客] 滑动窗口的最大值](../../2022/03/牛客_0082_困难_滑动窗口的最大值.md)  
  > 
> [[简单, LeetCode] 下一个更大元素](../../2021/11/LeetCode_0496_简单_下一个更大元素.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->


<!--START_SECTION:relate_problem-->
<!--END_SECTION:relate_problem-->
