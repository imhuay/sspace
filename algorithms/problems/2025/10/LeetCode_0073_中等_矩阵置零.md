## 矩阵置零
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-10-10%2001%3A15%3A17&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E6%95%B0%E7%BB%84/%E7%9F%A9%E9%98%B5&color=blue&style=flat-square)](../../../README.md#数组矩阵)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [矩阵]
source: LeetCode
level: 中等
number: '73'
name: '矩阵置零'
companies: []
-->

> [title](#a-url)

<summary><b>问题简述</b></summary>

```txt
给定一个 m x n 的矩阵, 如果一个元素为 0, 则将其所在行和列的所有元素都设为 0. 请使用 原地 算法. 
```

<!-- 
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

<summary><b>思路</b></summary>

- 用矩阵的第一行和第一列记录每一行和每一列是否有零出现;
- 使用两个标记变量分别记录第一行和第一列是否原本包含 0. 

<details><summary><b>Python</b></summary>

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_has_0 = any(it == 0 for it in matrix[0])
        col_has_0 = any(it[0] == 0 for it in matrix)

        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if col_has_0:
            for i in range(m):
                matrix[i][0] = 0

        if row_has_0:
            for j in range(n):
                matrix[0][j] = 0
```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

> 🌧️ _暂无主题相关的笔记_


<details><summary><b>其他算法笔记</b></summary>

- [从暴力递归到动态规划](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表常用操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>数组/矩阵 (11)</b></summary>

> [[中等, LeetCode] 从魔法师身上吸取的最大能量](LeetCode_3147_中等_从魔法师身上吸取的最大能量.md)  
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
