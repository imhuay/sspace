## 全排列II
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
[![](https://img.shields.io/static/v1?label=&message=%E7%83%AD%E9%97%A8&color=blue&style=flat-square)](../../../README.md#热门)
[![](https://img.shields.io/static/v1?label=&message=%E9%80%92%E5%BD%92&color=blue&style=flat-square)](../../../README.md#递归)
<!--END_SECTION:badge-->
<!--info
tags: [递归, 回溯, lc100, 热门]
source: LeetCode
level: 中等
number: '0047'
name: 全排列II
companies: []
-->

> [47. 全排列 II - 力扣 (LeetCode) ](https://leetcode.cn/problems/permutations-ii/)

<summary><b>问题简述</b></summary>

```txt
给定一个可包含重复数字的序列 nums , 按任意顺序 返回所有不重复的全排列.
```

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 递归回溯的关键问题是, 在生成递归树的过程中, 每个节点应该生成哪些分支;
- 相比无重复的全排列, 需要额外考虑一个去重的剪枝过程, 这里提供了写法1 和写法2 两种剪枝方法;
  - 写法 1 是最常见的写法, 解释成本低;
  - 如果画出递归树的生成过程, 那么写法2 更直观的;

<details><summary><b>Python 写法1 (推荐) </b></summary>

- 本写法中核心的去重剪枝有两种写法:
    ```python
    # 写法1 (推荐)
    if i > 0 and nums[i] == nums[i - 1] and not used[i - i]:
        continue

    # 写法2, 区别仅在于 used[i - i]
    if i > 0 and nums[i] == nums[i - 1] and used[i - i]:
        continue
    ```
  写法1 的效率更高, 关于这两种写法的实际含义, 详见: [47. 全排列 II - 「代码随想录」](https://leetcode.cn/problems/permutations-ii/solution/dai-ma-sui-xiang-lu-dai-ni-xue-tou-hui-s-ki1h/)

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()  # 先排序, 剪枝需要
        len_nums = len(nums)
        ret = []
        used = [0] * len_nums

        def dfs(deep, tmp):
            if deep == len_nums:
                ret.append(tmp[:])
                return

            for i in range(len_nums):
                if used[i]: continue
                # 相比无重复的全排列, 多了这一步剪枝过程, 该剪枝过程依赖于 nums 有序
                if i > 0 and nums[i] == nums[i - 1] and not used[i - i]:
                    continue

                used[i] = 1
                tmp.append(nums[i])
                dfs(deep + 1, tmp)
                tmp.pop()
                used[i] = 0

        dfs(0, [])
        return ret
```

</details>

<details><summary><b>Python 写法2 (直观) </b></summary>

- 在递归树的每一层中, 维护一个集合, 记录已经使用过的数字;
- 该方法不需要预先排序;

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # nums.sort()  # 先排序, 剪枝需要
        len_nums = len(nums)
        ret = []
        used = [0] * len_nums

        def dfs(deep, tmp):
            if deep == len_nums:
                ret.append(tmp[:])
                return

            book = set()  # 该变量在递归树的每一层共享, 记录在这一层中已经用过了哪些数字
            for i in range(len_nums):
                if used[i] or nums[i] in book: continue
                book.add(nums[i])

                used[i] = 1
                tmp.append(nums[i])
                dfs(deep + 1, tmp)
                tmp.pop()
                used[i] = 0

        dfs(0, [])
        return ret
```

</details>

<summary><b>相关问题</b></summary>

- [46. 全排列 - 力扣 (LeetCode) ](https://leetcode.cn/problems/permutations/)


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
> [[中等, LeetCode] 组合总和 🔥](LeetCode_0039_中等_组合总和.md)  
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

<details><summary><b>热门 (16)</b></summary>

> [[中等, LeetCode] 买卖股票的最佳时机 II 🔥](../06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 全排列 🔥](LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 重排链表 🔥](../06/LeetCode_0143_中等_重排链表.md)  
> [[中等, 剑指Offer] 把字符串转换成整数 🔥](../01/剑指Offer_6700_中等_把字符串转换成整数.md)  
> [[中等, 牛客] 三数之和 🔥](../03/牛客_0054_中等_三数之和.md)  
> [[中等, 牛客] 把二叉树打印成多行 🔥](../03/牛客_0080_中等_把二叉树打印成多行.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 平衡二叉树 🔥](../09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, 牛客] 两个链表的第一个公共结点 🔥](../03/牛客_0066_简单_两个链表的第一个公共结点.md)  
  > 

</details>

<details><summary><b>递归 (25)</b></summary>

> [[中等, LeetCode] 全排列 🔥](LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 分割回文串](../../2025/11/LeetCode_0131_中等_分割回文串.md)  
> [[中等, LeetCode] 子集](../../2025/11/LeetCode_0078_中等_子集.md)  
> [[中等, LeetCode] 组合](../../2025/11/LeetCode_0077_中等_组合.md)  
> [[中等, LeetCode] 组合总和 II 🔥](LeetCode_0040_中等_组合总和II.md)  
> [[中等, LeetCode] 组合总和 III](../../2025/11/LeetCode_0216_中等_组合总和III.md)  
> [[中等, LeetCode] 组合总和 🔥](LeetCode_0039_中等_组合总和.md)  
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
