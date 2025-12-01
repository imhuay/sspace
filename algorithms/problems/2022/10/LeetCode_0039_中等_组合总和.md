## 组合总和
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
[![](https://img.shields.io/static/v1?label=&message=%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2&color=blue&style=flat-square)](../../../README.md#深度优先搜索)
[![](https://img.shields.io/static/v1?label=&message=%E9%80%92%E5%BD%92&color=blue&style=flat-square)](../../../README.md#递归)
<!--END_SECTION:badge-->
<!--info
tags: [dfs, 回溯, lc100]
source: LeetCode
level: 中等
number: '0039'
name: 组合总和
companies: []
-->

>

<summary><b>问题简述</b></summary>

```txt
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target,
找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合,
并以列表形式返回. 你可以按 任意顺序 返回这些组合.

candidates 中的 同一个 数字可以 无限制重复被选取.
如果至少一个数字的被选数量不同, 则两种组合是不同的.
```

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路: 递归回溯</b></summary>

<details><summary><b>Python: 写法1 (标准写法, 推荐) </b></summary>

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ret = []

        def dfs(s, start, tmp):
            if s >= target:
                if s == target:
                    ret.append(tmp[:])
                return

            for i in range(start, len(candidates)):
                c = candidates[i]
                tmp.append(c)
                dfs(s + c, i, tmp)  
                # 这里传入 i 表示从 candidates 第 i 个开始取, 因此可以重复
                # 组合总和II 中不能重复取, 相应的要传入 i+1
                tmp.pop()

        dfs(0, 0, [])
        return ret
```

</details>

<details><summary><b>Python: 写法2 (好记) </b></summary>

- 本写法不保证在其他相关问题上适用;

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ret = []

        def dfs(s, tmp):
            if s >= target:
                if s == target:
                    ret.append(tmp[:])
                return

            for c in candidates:
                if tmp and c < tmp[-1]:  # 保证 tmp 内部有序来达到去重的目的
                    continue
                tmp.append(c)
                dfs(s + c, tmp)
                tmp.pop()

        dfs(0, [])
        return ret
```

</details>


<summary><b>相关问题</b></summary>

- [40. 组合总和 II - 力扣 (LeetCode) ](https://leetcode.cn/problems/combination-sum-ii/)


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


<details><summary><b>LeetCode Hot 100 (32)</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 两数相加 🔥](../../2021/10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 全排列 🔥](LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 和为K的子数组 🔥](../../2025/11/LeetCode_0560_中等_和为K的子数组.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 字母异位词分组 🔥](LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 找到字符串中所有字母异位词 🔥](../../2025/11/LeetCode_0438_中等_找到字符串中所有字母异位词.md)  
> [[中等, LeetCode] 括号生成 🔥](LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, LeetCode] 无重复字符的最长子串 🔥](../02/LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 最长连续序列 🔥](../../2025/11/LeetCode_0128_中等_最长连续序列.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, LeetCode] 组合总和 II 🔥](LeetCode_0040_中等_组合总和II.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 最小覆盖子串 🔥](../../2025/11/LeetCode_0076_困难_最小覆盖子串.md)  
> [[困难, LeetCode] 最长有效括号 🔥](LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, 牛客] 最小覆盖子串 🔥](../02/牛客_0028_困难_最小覆盖子串.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 有效的括号 🔥](../03/LeetCode_0020_简单_有效的括号.md)  
> [[简单, LeetCode] 移动零 🔥](../../2025/11/LeetCode_0283_简单_移动零.md)  
  > 

</details>

<details><summary><b>深度优先搜索 (19)</b></summary>

> [[中等, LeetCode] 括号生成 🔥](LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 路径总和III](../06/LeetCode_0437_中等_路径总和III.md)  
> [[中等, 剑指Offer] 二叉树中和为某一值的路径](../../2021/12/剑指Offer_3400_中等_二叉树中和为某一值的路径.md)  
> [[中等, 剑指Offer] 字符串的排列 (全排列) 🔥](../../2021/12/剑指Offer_3800_中等_字符串的排列(全排列).md)  
> [[中等, 剑指Offer] 打印从1到最大的n位数 (N叉树的遍历)](../../2021/11/剑指Offer_1700_中等_打印从1到最大的n位数(N叉树的遍历).md)  
> [[中等, 剑指Offer] 机器人的运动范围](../../2021/11/剑指Offer_1300_中等_机器人的运动范围.md)  
> [[中等, 剑指Offer] 矩阵中的路径](../../2021/11/剑指Offer_1200_中等_矩阵中的路径.md)  
> [[中等, 牛客] 二叉树中和为某一值的路径(二)](../01/牛客_0008_中等_二叉树中和为某一值的路径(二).md)  
> [[中等, 牛客] 二叉树根节点到叶子节点的所有路径和](../01/牛客_0005_中等_二叉树根节点到叶子节点的所有路径和.md)  
> [[中等, 牛客] 字符串的排列 🔥](../05/牛客_0121_中等_字符串的排列.md)  
> [[中等, 牛客] 实现二叉树先序、中序、后序遍历](../03/牛客_0045_中等_实现二叉树先序、中序、后序遍历.md)  
> [[中等, 牛客] 岛屿数量 🔥](../04/牛客_0109_中等_岛屿数量.md)  
> [[中等, 牛客] 数字字符串转化成IP地址](../01/牛客_0020_中等_数字字符串转化成IP地址.md)  
  > 
> [[困难, 牛客] 多叉树的直径](../04/牛客_0099_困难_多叉树的直径.md)  
  > 
> [[简单, LeetCode] 二叉树的最小深度](../07/LeetCode_0111_简单_二叉树的最小深度.md)  
> [[简单, 剑指Offer] 二叉搜索树的第k大节点](../01/剑指Offer_5400_简单_二叉搜索树的第k大节点.md)  
> [[简单, 剑指Offer] 从尾到头打印链表](../../2021/11/剑指Offer_0600_简单_从尾到头打印链表.md)  
> [[简单, 牛客] 二叉树中和为某一值的路径(一)](../01/牛客_0009_简单_二叉树中和为某一值的路径(一).md)  
  > 

</details>

<details><summary><b>递归 (25)</b></summary>

> [[中等, LeetCode] 全排列 🔥](LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 分割回文串](../../2025/11/LeetCode_0131_中等_分割回文串.md)  
> [[中等, LeetCode] 子集](../../2025/11/LeetCode_0078_中等_子集.md)  
> [[中等, LeetCode] 组合](../../2025/11/LeetCode_0077_中等_组合.md)  
> [[中等, LeetCode] 组合总和 II 🔥](LeetCode_0040_中等_组合总和II.md)  
> [[中等, LeetCode] 组合总和 III](../../2025/11/LeetCode_0216_中等_组合总和III.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](../../2021/12/剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../../2021/11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 剑指Offer] 树的子结构](../../2021/11/剑指Offer_2600_中等_树的子结构.md)  
> [[中等, 剑指Offer] 求1~n的和](../01/剑指Offer_6400_中等_求1~n的和.md)  
> [[中等, 牛客] 加起来和为目标值的组合(二)](../03/牛客_0046_中等_加起来和为目标值的组合(二).md)  
> [[中等, 牛客] 括号生成](../02/牛客_0026_中等_括号生成.md)  
> [[中等, 牛客] 有重复项数字的全排列](../03/牛客_0042_中等_有重复项数字的全排列.md)  
> [[中等, 牛客] 汉诺塔问题 🔥](../03/牛客_0067_中等_汉诺塔问题.md)  
> [[中等, 牛客] 没有重复项数字的全排列](../03/牛客_0043_中等_没有重复项数字的全排列.md)  
> [[中等, 牛客] 集合的所有子集(一)](../02/牛客_0027_中等_集合的所有子集(一).md)  
  > 
> [[困难, LeetCode] 51](../../2025/11/LeetCode_N 皇后_困难_51.md)  
> [[困难, 剑指Offer] 正则表达式匹配](../../2021/11/剑指Offer_1900_困难_正则表达式匹配.md)  
> [[困难, 牛客] N皇后问题](../03/牛客_0039_困难_N皇后问题.md)  
> [[困难, 牛客] 数独](../03/牛客_0047_困难_数独.md)  
  > 
> [[简单, LeetCode] 二叉树的最大深度 🔥](../07/LeetCode_0104_简单_二叉树的最大深度.md)  
> [[简单, 剑指Offer] 二叉树的镜像](../../2021/11/剑指Offer_2700_简单_二叉树的镜像.md)  
> [[简单, 剑指Offer] 从尾到头打印链表](../../2021/11/剑指Offer_0600_简单_从尾到头打印链表.md)  
> [[简单, 剑指Offer] 对称的二叉树](../../2021/11/剑指Offer_2800_简单_对称的二叉树.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
