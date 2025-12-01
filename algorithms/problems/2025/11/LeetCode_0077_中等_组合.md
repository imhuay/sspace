## 组合
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-12-01%2000%3A20%3A11&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E9%80%92%E5%BD%92&color=blue&style=flat-square)](../../../README.md#递归)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [回溯]
source: 'LeetCode'
level: '中等'
number: '77'
name: '组合'
-->

> [77. 组合 - 力扣 (LeetCode) ](https://leetcode.cn/problems/combinations/)

<summary><b>问题简述</b></summary>

```md
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

示例 1：
    输入：n = 4, k = 2
    输出：
    [
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
    ]
```

<!-- 
<details><summary><b>详细描述</b></summary>

```md
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

---

<summary><b>思路: 多叉树模板</b></summary>


<details><summary><b>Python</b></summary>

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans, path = [], []

        def dfs(i):
            c = len(path)               # 当前已经添加的个数
            if c == k:
                ans.append(path[:])
                return
            if n - i + 1 < k - c:       # 剩下的数不够组成 k 个
                return
            for j in range(i, n + 1):
                path.append(j)
                dfs(j + 1)
                path.pop()
        
        dfs(1)  # 从 1 到 n
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
> [[困难, LeetCode] 51](LeetCode_N 皇后_困难_51.md)  
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
