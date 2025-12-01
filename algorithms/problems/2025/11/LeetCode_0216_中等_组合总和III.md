## 组合总和 III
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
number: '216'
name: '组合总和 III'
-->

> [216. 组合总和 III - 力扣 (LeetCode) ](https://leetcode.cn/problems/combination-sum-iii/description/)

<summary><b>问题简述</b></summary>

```md
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

只使用数字1到9
每个数字 最多使用一次 
返回 **所有可能的有效组合的列表** 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

示例 1:
    输入: k = 3, n = 7
    输出: [[1,2,4]]
    解释:
        1 + 2 + 4 = 7
    没有其他符合的组合了。
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

> 更多剪枝优化: [回溯+剪枝优化 - 灵茶山艾府 - 力扣 (LeetCode) ](https://leetcode.cn/problems/combination-sum-iii/solutions/2071013/hui-su-bu-hui-xie-tao-lu-zai-ci-pythonja-feme/)

<details><summary><b>Python</b></summary>

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans, path = [], []

        def dfs(i, s):
            if s < 0 :   # 剪枝
                return
            if len(path) == k and s == 0:
                ans.append(path[:])
                return
            
            for j in range(i, 10):
                path.append(j)
                dfs(j + 1, s - j)
                path.pop()
        
        dfs(1, n)
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
