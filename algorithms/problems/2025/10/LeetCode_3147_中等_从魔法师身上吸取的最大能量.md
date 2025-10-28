## 从魔法师身上吸取的最大能量
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-10-09%2016%3A38%3A01&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%8D%E7%BC%80%E5%92%8C&color=blue&style=flat-square)](../../../README.md#前缀和)
[![](https://img.shields.io/static/v1?label=&message=%E6%95%B0%E7%BB%84/%E7%9F%A9%E9%98%B5&color=blue&style=flat-square)](../../../README.md#数组矩阵)
<!--END_SECTION:badge-->
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

> [3147. 从魔法师身上吸取的最大能量 - 力扣 (LeetCode) ](https://leetcode.cn/problems/taking-maximum-energy-from-the-mystic-dungeon)

<summary><b>问题简述</b></summary>

```txt
在神秘的地牢中, n 个魔法师站成一排. 每个魔法师都拥有一个属性, 这个属性可以给你提供能量. 有些魔法师可能会给你负能量, 即从你身上吸取能量. 

你被施加了一种诅咒, 当你从魔法师 i 处吸收能量后, 你将被立即传送到魔法师 (i + k) 处. 这一过程将重复进行, 直到你到达一个不存在 (i + k) 的魔法师为止. 

换句话说, 你将选择一个起点, 然后以 k 为间隔跳跃, 直到到达魔法师序列的末端, 在过程中吸收所有的能量. 

给定一个数组 energy 和一个整数k, 返回你能获得的 最大 能量. 

示例 1: 
    输入: energy = [5,2,-10,-5,1], k = 3
    输出: 3
    解释: 可以从魔法师 1 开始, 吸收能量 2 + 1 = 3. 

示例 2: 
    输入: energy = [-2,-3,-1], k = 2
    输出: -1
    解释: 可以从魔法师 2 开始, 吸收能量 -1. 

提示: 
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


<!--START_SECTION:relate_note-->
---

### 算法笔记

> 🌧️ _暂无主题相关的笔记_


<details><summary><b>其他算法笔记</b></summary>

- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>前缀和 (3)</b></summary>

> [[中等, LeetCode] 路径总和III](../../2022/06/LeetCode_0437_中等_路径总和III.md)  
> [[中等, 剑指Offer] 构建乘积数组](../../2022/01/剑指Offer_6600_中等_构建乘积数组.md)  
> [[中等, 牛客] 和为K的连续子数组](../../2022/05/牛客_0125_中等_和为K的连续子数组.md)  
  > 

</details>

<details><summary><b>数组/矩阵 (11)</b></summary>

> [[中等, LeetCode] 矩阵置零](LeetCode_0073_中等_矩阵置零.md)  
> [[中等, 剑指Offer] 栈的压入、弹出序列 🔥](../../2021/11/剑指Offer_3100_中等_栈的压入、弹出序列.md)  
> [[中等, 剑指Offer] 顺时针打印矩阵 (3种思路4个写法) 🔥](../../2021/11/剑指Offer_2900_中等_顺时针打印矩阵(3种思路4个写法).md)  
> [[中等, 牛客] 旋转数组](../../2022/04/牛客_0110_中等_旋转数组.md)  
> [[中等, 牛客] 缺失的第一个正整数](../../2022/02/牛客_0030_中等_缺失的第一个正整数.md)  
> [[中等, 牛客] 螺旋矩阵](../../2022/03/牛客_0038_中等_螺旋矩阵.md)  
> [[中等, 牛客] 调整数组顺序使奇数位于偶数前面(一)](../../2022/03/牛客_0077_中等_调整数组顺序使奇数位于偶数前面(一).md)  
  > 
> [[简单, 剑指Offer] 包含min函数的栈](../../2021/11/剑指Offer_3000_简单_包含min函数的栈.md)  
> [[简单, 剑指Offer] 调整数组顺序使奇数位于偶数前面](../../2021/11/剑指Offer_2100_简单_调整数组顺序使奇数位于偶数前面.md)  
> [[简单, 牛客] 最长公共前缀](../../2022/03/牛客_0055_简单_最长公共前缀.md)  
> [[简单, 牛客] 顺时针旋转矩阵](../../2022/01/牛客_0018_简单_顺时针旋转矩阵.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->


<!--START_SECTION:relate_problem-->
<!--END_SECTION:relate_problem-->
