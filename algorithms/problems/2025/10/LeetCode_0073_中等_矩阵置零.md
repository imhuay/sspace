## <title - autoUpdate>
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
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
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
- 使用两个标记变量分别记录第一行和第一列是否原本包含 0。

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


<!--START_SECTION:relate-->
<!--END_SECTION:relate-->