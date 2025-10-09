## 二叉搜索树的后序遍历序列
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%8F%89%E6%A0%91/%E6%A0%91&color=blue&style=flat-square)](../../../README.md#二叉树树)
<!--END_SECTION:badge-->
<!--info
tags: [二叉树]
source: 剑指Offer
level: 中等
number: '3300'
name: 二叉搜索树的后序遍历序列
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
输入一个整数数组, 判断该数组是不是某二叉搜索树的后序遍历结果.
```

<details><summary><b>详细描述</b></summary>

```txt
输入一个整数数组, 判断该数组是不是某二叉搜索树的后序遍历结果. 如果是则返回 true, 否则返回 false. 假设输入的数组的任意两个数字都互不相同.

参考以下这颗二叉搜索树:

     5
    / \
   2   6
  / \
 1   3

示例 1:
    输入: [1,6,3,2,5]
    输出: false
示例 2:
    输入: [1,3,2,6,5]
    输出: true

提示:
    数组长度 <= 1000

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 记后序遍历的结果为 `p`, 则 `p` 有如下结论:
    - `p[-1]` 为根节点:
    - `p[:-1]` 可以划分为左右子树两个部分, 分别记为 `pl` 和 `pr`;
- 而该二叉树为二叉搜索树, 又有 `all(x < p[-1] for x in pl)` 和 `all(x > p[-1] for x in pr)`
- 然后递归判断左右子树是否满足以上性质即可;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        def dfs(p):
            if not p: return True  # 记空树为二叉搜索树

            root_val = p[-1]
            pl = []  # 左子树
            for idx, x in enumerate(p):
                if x < root_val:  # 题目规定 p 中元素互不相等
                    pl.append(x)
                else:
                    break

            pr = p[idx: -1]  # 右子树
            flag = all(x > root_val for x in pr)
            return flag and dfs(pl) and dfs(pr)

        return dfs(postorder)
```

</details>

<details><summary><b>Python: 优化</b></summary>

- 可以用索引范围代替 `pl` 和 `pr`, 避免使用额外空间;
- 还有其他判断方法, 这里是严格按照上面的思路来写的;
    > [二叉搜索树的后序遍历序列 (递归分治 / 单调栈, 清晰图解) ](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/)

```python
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        p = postorder

        def dfs(l, r):  # [l, r]
            if l >= r: return True

            root_val = p[r]
            cnt = 0  # 记录小于root的节点数量, 即左子树
            for i in range(l, r):  # 这里踩了个坑, 不能直接用 i 代替 cnt, 因为退出循环时不能保证 i 一定指向第一个大于 root 的元素, 比如右子树为空的情况
                if p[i] > root_val:
                    break
                else:
                    cnt += 1
            flag = all(p[i] > root_val for i in range(l + cnt, r))
            return flag and dfs(l, l + cnt - 1) and dfs(l + cnt, r - 1)

        return dfs(0, len(p) - 1)
```

</details>


<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>二叉树/树</b></summary>

> [[中等, LeetCode] 二叉树的完全性检验 🔥](../../2022/03/LeetCode_0958_中等_二叉树的完全性检验.md)  
> [[中等, LeetCode] 从叶结点开始的最小字符串](../../2022/07/LeetCode_0988_中等_从叶结点开始的最小字符串.md)  
> [[中等, LeetCode] 求根节点到叶节点数字之和](../../2022/07/LeetCode_0129_中等_求根节点到叶节点数字之和.md)  
> [[中等, LeetCode] 路径总和II](../../2022/06/LeetCode_0113_中等_路径总和II.md)  
> [[中等, LeetCode] 路径总和III](../../2022/06/LeetCode_0437_中等_路径总和III.md)  
> [[中等, LeetCode] 验证二叉搜索树](../../2022/03/LeetCode_0098_中等_验证二叉搜索树.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 二叉树中和为某一值的路径](剑指Offer_3400_中等_二叉树中和为某一值的路径.md)  
> [[中等, 剑指Offer] 树的子结构](../11/剑指Offer_2600_中等_树的子结构.md)  
> [[中等, 剑指Offer] 重建二叉树 🔥](../11/剑指Offer_0700_中等_重建二叉树.md)  
> [[中等, 牛客] 二叉搜索树与双向链表](../../2022/03/牛客_0064_中等_二叉搜索树与双向链表.md)  
> [[中等, 牛客] 二叉搜索树的第k个节点](../../2022/03/牛客_0081_中等_二叉搜索树的第k个节点.md)  
> [[中等, 牛客] 二叉树中和为某一值的路径(二)](../../2022/01/牛客_0008_中等_二叉树中和为某一值的路径(二).md)  
> [[中等, 牛客] 二叉树根节点到叶子节点的所有路径和](../../2022/01/牛客_0005_中等_二叉树根节点到叶子节点的所有路径和.md)  
> [[中等, 牛客] 在二叉树中找到两个节点的最近公共祖先](../../2022/04/牛客_0102_中等_在二叉树中找到两个节点的最近公共祖先.md)  
> [[中等, 牛客] 完全二叉树结点数](../../2022/04/牛客_0084_中等_完全二叉树结点数.md)  
> [[中等, 牛客] 找到搜索二叉树中两个错误的节点](../../2022/03/牛客_0058_中等_找到搜索二叉树中两个错误的节点.md)  
> [[中等, 牛客] 把二叉树打印成多行 🔥](../../2022/03/牛客_0080_中等_把二叉树打印成多行.md)  
> [[中等, 牛客] 按之字形顺序打印二叉树](../../2022/01/牛客_0014_中等_按之字形顺序打印二叉树.md)  
> [[中等, 牛客] 求二叉树的层序遍历](../../2022/01/牛客_0015_中等_求二叉树的层序遍历.md)  
> [[中等, 牛客] 重建二叉树](../../2022/01/牛客_0012_中等_重建二叉树.md)  
  > 
> [[困难, 剑指Offer] 序列化二叉树](剑指Offer_3700_困难_序列化二叉树.md)  
> [[困难, 牛客] 二叉树中的最大路径和](../../2022/01/牛客_0006_困难_二叉树中的最大路径和.md)  
> [[困难, 牛客] 序列化二叉树](../../2022/05/牛客_0123_困难_序列化二叉树.md)  
  > 
> [[简单, LeetCode] 二叉树的所有路径](../../2022/07/LeetCode_0257_简单_二叉树的所有路径.md)  
> [[简单, LeetCode] 二叉树的最大深度 🔥](../../2022/07/LeetCode_0104_简单_二叉树的最大深度.md)  
> [[简单, LeetCode] 二叉树的最小深度](../../2022/07/LeetCode_0111_简单_二叉树的最小深度.md)  
> [[简单, LeetCode] 平衡二叉树 🔥](../../2022/09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, LeetCode] 路径总和](../../2022/06/LeetCode_0112_简单_路径总和.md)  
> [[简单, 剑指Offer] 二叉搜索树的最近公共祖先 🔥](../../2022/01/剑指Offer_6801_简单_二叉搜索树的最近公共祖先.md)  
> [[简单, 剑指Offer] 二叉搜索树的第k大节点](../../2022/01/剑指Offer_5400_简单_二叉搜索树的第k大节点.md)  
> [[简单, 剑指Offer] 二叉树的最近公共祖先](../../2022/01/剑指Offer_6802_简单_二叉树的最近公共祖先.md)  
> [[简单, 剑指Offer] 二叉树的镜像](../11/剑指Offer_2700_简单_二叉树的镜像.md)  
> [[简单, 剑指Offer] 判断是否为平衡二叉树](../../2022/01/剑指Offer_5502_简单_判断是否为平衡二叉树.md)  
> [[简单, 剑指Offer] 对称的二叉树](../11/剑指Offer_2800_简单_对称的二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](../11/剑指Offer_3201_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树](../11/剑指Offer_3202_简单_层序遍历二叉树.md)  
> [[简单, 剑指Offer] 层序遍历二叉树 (之字形遍历)](../11/剑指Offer_3203_简单_层序遍历二叉树(之字形遍历).md)  
> [[简单, 剑指Offer] 求二叉树的深度](../../2022/01/剑指Offer_5501_简单_求二叉树的深度.md)  
> [[简单, 牛客] 二叉树中和为某一值的路径(一)](../../2022/01/牛客_0009_简单_二叉树中和为某一值的路径(一).md)  
> [[简单, 牛客] 二叉树的最大深度](../../2022/01/牛客_0013_简单_二叉树的最大深度.md)  
> [[简单, 牛客] 二叉树的镜像](../../2022/03/牛客_0072_简单_二叉树的镜像.md)  
> [[简单, 牛客] 判断t1树中是否有与t2树完全相同的子树](../../2022/04/牛客_0098_简单_判断t1树中是否有与t2树完全相同的子树.md)  
> [[简单, 牛客] 判断是不是平衡二叉树](../../2022/03/牛客_0062_简单_判断是不是平衡二叉树.md)  
> [[简单, 牛客] 合并二叉树](../../2022/05/牛客_0117_简单_合并二叉树.md)  
> [[简单, 牛客] 对称的二叉树](../../2022/01/牛客_0016_简单_对称的二叉树.md)  
> [[简单, 牛客] 将升序数组转化为平衡二叉搜索树](../../2022/01/牛客_0011_简单_将升序数组转化为平衡二叉搜索树.md)  
  > 

</details>
<!--END_SECTION:relate-->
