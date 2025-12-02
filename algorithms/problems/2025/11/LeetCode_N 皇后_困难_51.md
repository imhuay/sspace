## 51
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-12-01%2000%3A20%3A11&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&color=red&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E9%80%92%E5%BD%92&color=blue&style=flat-square)](../../../README.md#递归)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [回溯]
source: 'LeetCode'
level: '困难'
number: '51'
name: 'N 皇后'
-->

> [51. N 皇后 - 力扣 (LeetCode) ](https://leetcode.cn/problems/n-queens/)

<summary><b>问题简述</b></summary>

```md
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
```

<!-- 
<details><summary><b>详细描述</b></summary>

```md
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

---

<summary><b>思路: 全排列 + 斜线判断</b></summary>


<details><summary><b>Python (写法1: 多叉树模板)</b></summary>

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ans = []
        col = [0] * n  # (r, col[r]) 表示在该坐标有一个皇后
        
        def dfs(r, s: set):

            if r == n:
                ans.append(['.'*c + 'Q' + '.'*(n-c-1) for c in col])
                return
            
            for c in s:
                if all(r+c != R+col[R] and r-c != R-col[R] for R in range(r)):
                    col[r] = c
                    dfs(r + 1, s - {c})
            
        dfs(0, set(range(n)))
        return ans
```

</details>


<details><summary><b>Python (写法2: 判断优化)</b></summary>

- 使用两个数组标记左右两个 "斜线" 是否已经使用;

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ans = []
        col = [0] * n  # (r, col[r]) 表示在该坐标有一个皇后
        used = [0] * n
        diag1 = [0] * (2*n-1)   # r+c 取值范围 [0, 2n), 最后一行 (n,n) 生成结果
        diag2 = [0] * (2*n-1)   # r-c 取值范围 (-n, n], 最后一行 (0,n) 生成结果
        
        def dfs(r):

            if r == n:
                ans.append(['.'*c + 'Q' + '.'*(n-c-1) for c in col])
                return
            
            for c in range(n):
                if used[c] or diag1[r + c] or diag2[r - c]:
                    continue

                col[r] = c
                used[c] = diag1[r + c] = diag2[r - c] = 1   # python 支持负索引
                dfs(r + 1)
                used[c] = diag1[r + c] = diag2[r - c] = 0
            
        dfs(0)
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


<details><summary><b>递归 (25)</b></summary>

> [[中等, LeetCode] 全排列 🔥](../../2022/10/LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](../../2022/10/LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 分割回文串](LeetCode_0131_中等_分割回文串.md)  
> [[中等, LeetCode] 子集](LeetCode_0078_中等_子集.md)  
> [[中等, LeetCode] 组合](LeetCode_0077_中等_组合.md)  
> [[中等, LeetCode] 组合总和 II 🔥](../../2022/10/LeetCode_0040_中等_组合总和II.md)  
> [[中等, LeetCode] 组合总和 III](LeetCode_0216_中等_组合总和III.md)  
> [[中等, LeetCode] 组合总和 🔥](../../2022/10/LeetCode_0039_中等_组合总和.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](../../2021/12/剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../../2021/11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 剑指Offer] 树的子结构](../../2021/11/剑指Offer_2600_中等_树的子结构.md)  
> [[中等, 剑指Offer] 求1~n的和](../../2022/01/剑指Offer_6400_中等_求1~n的和.md)  
> [[中等, 牛客] 加起来和为目标值的组合(二)](../../2022/03/牛客_0046_中等_加起来和为目标值的组合(二).md)  
> [[中等, 牛客] 括号生成](../../2022/02/牛客_0026_中等_括号生成.md)  
> [[中等, 牛客] 有重复项数字的全排列](../../2022/03/牛客_0042_中等_有重复项数字的全排列.md)  
> [[中等, 牛客] 汉诺塔问题 🔥](../../2022/03/牛客_0067_中等_汉诺塔问题.md)  
> [[中等, 牛客] 没有重复项数字的全排列](../../2022/03/牛客_0043_中等_没有重复项数字的全排列.md)  
> [[中等, 牛客] 集合的所有子集(一)](../../2022/02/牛客_0027_中等_集合的所有子集(一).md)  
  > 
> [[困难, 剑指Offer] 正则表达式匹配](../../2021/11/剑指Offer_1900_困难_正则表达式匹配.md)  
> [[困难, 牛客] N皇后问题](../../2022/03/牛客_0039_困难_N皇后问题.md)  
> [[困难, 牛客] 数独](../../2022/03/牛客_0047_困难_数独.md)  
  > 
> [[简单, LeetCode] 二叉树的最大深度 🔥](../../2022/07/LeetCode_0104_简单_二叉树的最大深度.md)  
> [[简单, 剑指Offer] 二叉树的镜像](../../2021/11/剑指Offer_2700_简单_二叉树的镜像.md)  
> [[简单, 剑指Offer] 从尾到头打印链表](../../2021/11/剑指Offer_0600_简单_从尾到头打印链表.md)  
> [[简单, 剑指Offer] 对称的二叉树](../../2021/11/剑指Offer_2800_简单_对称的二叉树.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
