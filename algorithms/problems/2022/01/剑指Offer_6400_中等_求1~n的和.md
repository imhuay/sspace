## 求1~n的和
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E9%80%92%E5%BD%92&color=blue&style=flat-square)](../../../README.md#递归)
<!--END_SECTION:badge-->
<!--info
tags: [递归]
source: 剑指Offer
level: 中等
number: '6400'
name: 求1~n的和
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
求 1+2+...+n , 要求不能使用乘除法、for、while、if、else、switch、case等关键字及三目运算符.
```

<details><summary><b>详细描述</b></summary>

```txt
求 1+2+...+n , 要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句 (A?B:C).

示例 1:
    输入: n = 3
    输出: 6
示例 2:
    输入: n = 9
    输出: 45

限制:
    1 <= n <= 10000

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/qiu-12n-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 通过 "短路" 中止递归;
- 在 Python 中 `and` 操作如果最后结果为真, 返回最后一个表达式的值, `or` 操作如果结果为真, 返回第一个结果为真的表达式的值 (写法2);

<details><summary><b>Python: 写法1</b></summary>

```python
class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)  # 当 n <= 1 时, 因为短路导致递归中止
        self.res += n
        return self.res
```

</details>

<details><summary><b>Python: 写法2</b></summary>

```python
class Solution:
    def sumNums(self, n: int) -> int:
        return n > 0 and (n + self.sumNums(n-1))
```

</details>


<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>递归</b></summary>

> [[中等, LeetCode] 全排列 🔥](../10/LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](../10/LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 组合总和 🔥](../10/LeetCode_0039_中等_组合总和.md)  
> [[中等, LeetCode] 组合总和II 🔥](../10/LeetCode_0040_中等_组合总和II.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](../../2021/12/剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../../2021/11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 剑指Offer] 树的子结构](../../2021/11/剑指Offer_2600_中等_树的子结构.md)  
> [[中等, 牛客] 加起来和为目标值的组合(二)](../03/牛客_0046_中等_加起来和为目标值的组合(二).md)  
> [[中等, 牛客] 括号生成](../02/牛客_0026_中等_括号生成.md)  
> [[中等, 牛客] 有重复项数字的全排列](../03/牛客_0042_中等_有重复项数字的全排列.md)  
> [[中等, 牛客] 汉诺塔问题 🔥](../03/牛客_0067_中等_汉诺塔问题.md)  
> [[中等, 牛客] 没有重复项数字的全排列](../03/牛客_0043_中等_没有重复项数字的全排列.md)  
> [[中等, 牛客] 集合的所有子集(一)](../02/牛客_0027_中等_集合的所有子集(一).md)  
  > 
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
<!--END_SECTION:relate-->