## 完全平方数
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#动态规划)
[![](https://img.shields.io/static/v1?label=&message=%E6%9A%B4%E5%8A%9B%E9%80%92%E5%BD%92%E4%B8%8E%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#暴力递归与动态规划)
<!--END_SECTION:badge-->
<!--info
tags: [dfs2dp]
source: LeetCode
level: 中等
number: '0279'
name: 完全平方数
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给你一个整数 n , 返回 和为 n 的完全平方数的最少数量 .

完全平方数 是一个整数, 其值等于另一个整数的平方; 换句话说, 其值等于一个整数自乘的积. 例如, 1、4、9 和 16 都是完全平方数, 而 3 和 11 不是.
```
> [279. 完全平方数 - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/perfect-squares/)

<!--
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->


<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1: 朴素完全背包 (超时) </b></summary>

- 定义 `dfs(i, j)` 表示用 `1~i` 的完全平方数凑出 `j` 需要的最小数量;
- 不能 AC, 仅离线验证了正确性;
    <!-- - 优化一下剪枝应该是能过的 -->


<details><summary><b>Python: 递归</b></summary>

```python
class Solution:
    def numSquares(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if i == 0 and j == 0: return 0  # 显然
            if i == 0: return float('inf')  # 凑不出的情况, 返回不可能, 注意此时 j != 0
            # if i == 1: return j

            ret = j  # 最大值为 j, 因为任意数字最差都可以用 1 组成
            times = 0  # i 使用的次数, 0 次也考虑在内
            while (x := (i ** 2) * times) <= j:
                ret = min(ret, dfs(i - 1, j - x) + times)
                times += 1

            return ret

        N = int(n ** 0.5)  # 可以使用数字的范围
        return dfs(N, n)
```

</details>


<details><summary><b>Python: 动态规划 (从递归修改而来) </b></summary>

```python
class Solution:
    def numSquares(self, n: int) -> int:
        from functools import lru_cache

        N = int(n ** 0.5)
        dp = [[0] * (n + 1) for _ in range(N + 1)]
        dp[0] = [float('inf')] * (n + 1)
        dp[0][0] = 0

        for i in range(1, N + 1):
            for j in range(1, n + 1):
                dp[i][j] = j
                times = 0
                while (x := i * i * times) <= j:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - x] + times)
                    times += 1

        return dp[-1][-1]
```

</details>


<summary><b>思路2: 完全背包 (优化) </b></summary>

- 定义 `dfs(j)` 表示目标和为`j`时需要完全平方数的最少个数;
    > 这里隐含了完全平方数的范围 `i*i <= j`;
- 【递归基】`j == 0` 时, 返回 `0`;
<!-- - 这里的递归含义并不直观, 直接看代码吧; -->

<details><summary><b>Python: 递归</b></summary>

```python
class Solution:
    def numSquares(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(j):
            if j == 0: return 0

            # 这里设置初始化为一个上界
            #   本题中初始化为无穷大、j (全部 1) 、4 (四平方和定理) 都可以;
            #   为了使解法更通用, 故初始化为无穷大
            ret = float('inf')
            i = 1
            while (x := i * i) <= j:
                ret = min(ret, dfs(j - x) + 1)
                i += 1

            return ret

        return dfs(n)
```

</details>

<details><summary><b>Python: 动态规划 (从递归修改而来) </b></summary>

```python
class Solution:
    def numSquares(self, n: int) -> int:

        dp = [i for i in range(n + 1)]
        dp[0] = 0

        for j in range(1, n + 1):
            i = 1
            while (x := i * i) <= n:
                dp[j] = min(dp[j], dp[j - x] + 1)
                i += 1

        return dp[-1]
```

</details>


<details><summary><b>Python: 动态规划 (更快的写法) </b></summary>

- 交换内外层遍历顺序 (本题无影响), 减小 `j` 的遍历范围;
    > 关于遍历 "物品" 和 "容量" 的顺序影响, 见: [零钱兑换 - 代码随想录](https://programmercarl.com/0322.零钱兑换.html)

```python
class Solution:
    def numSquares(self, n: int) -> int:

        dp = [i for i in range(n + 1)]
        dp[0] = 0

        i = 1
        while (x := i * i) <= n:
            for j in range(x, n + 1):
                dp[j] = min(dp[j], dp[j - x] + 1)
            i += 1

        return dp[-1]
```

</details>


<summary><b>其他思路</b></summary>

- 数学 (时间复杂度 $O(\sqrt{n})$): [完全平方数 - 力扣官方题解](https://leetcode-cn.com/problems/perfect-squares/solution/wan-quan-ping-fang-shu-by-leetcode-solut-t99c/)
    > [四平方和定理](https://baike.baidu.com/item/四平方和定理)证明了任意一个正整数都可以被表示为至多四个正整数的平方和;
- BFS: [完全平方数 - 自来火](https://leetcode-cn.com/problems/perfect-squares/solution/python3zui-ji-chu-de-bfstao-lu-dai-ma-gua-he-ru-me/)


<!--START_SECTION:relate_note-->
---

### 算法笔记

- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  

<details><summary><b>其他算法笔记</b></summary>

- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>动态规划 (53)</b></summary>

> [[中等, LeetCode] 一和零](../06/LeetCode_0474_中等_一和零.md)  
> [[中等, LeetCode] 三角形最小路径和](../06/LeetCode_0120_中等_三角形最小路径和.md)  
> [[中等, LeetCode] 不同的二叉搜索树](../03/LeetCode_0096_中等_不同的二叉搜索树.md)  
> [[中等, LeetCode] 乘积最大子数组](../06/LeetCode_0152_中等_乘积最大子数组.md)  
> [[中等, LeetCode] 买卖股票的最佳时机II 🔥](../06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 打家劫舍](../06/LeetCode_0198_中等_打家劫舍.md)  
> [[中等, LeetCode] 打家劫舍II](../06/LeetCode_0213_中等_打家劫舍II.md)  
> [[中等, LeetCode] 整数拆分](../../2021/12/LeetCode_0343_中等_整数拆分.md)  
> [[中等, LeetCode] 施咒的最大总伤害](../../2025/10/LeetCode_3186_中等_施咒的最大总伤害.md)  
> [[中等, LeetCode] 最小路径和](../01/LeetCode_0064_中等_最小路径和.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, LeetCode] 解码方法](LeetCode_0091_中等_解码方法.md)  
> [[中等, LeetCode] 零钱兑换](../06/LeetCode_0322_中等_零钱兑换.md)  
> [[中等, LeetCode] 零钱兑换II](../06/LeetCode_0518_中等_零钱兑换II.md)  
> [[中等, 剑指Offer] n个骰子的点数](../01/剑指Offer_6000_中等_n个骰子的点数.md)  
> [[中等, 剑指Offer] 丑数 🔥](../../2021/12/剑指Offer_4900_中等_丑数.md)  
> [[中等, 剑指Offer] 剪绳子 (整数拆分)](../../2021/11/剑指Offer_1401_中等_剪绳子(整数拆分).md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](../01/剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 剑指Offer] 斐波那契数列-3 (把数字翻译成字符串)](../../2021/12/剑指Offer_4600_中等_斐波那契数列-3(把数字翻译成字符串).md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../../2021/12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 剑指Offer] 礼物的最大价值](../../2021/12/剑指Offer_4700_中等_礼物的最大价值.md)  
> [[中等, 牛客] 01背包 🔥](../05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 丑数](../03/牛客_0079_中等_丑数.md)  
> [[中等, 牛客] 丢棋子问题 (鹰蛋问题) 🔥](../04/牛客_0087_中等_丢棋子问题(鹰蛋问题).md)  
> [[中等, 牛客] 把数字翻译成字符串](../05/牛客_0116_中等_把数字翻译成字符串.md)  
> [[中等, 牛客] 最大正方形](../04/牛客_0108_中等_最大正方形.md)  
> [[中等, 牛客] 最长公共子串](../05/牛客_0127_中等_最长公共子串.md)  
> [[中等, 牛客] 最长公共子序列(二) 🔥](../04/牛客_0092_中等_最长公共子序列(二).md)  
> [[中等, 牛客] 最长回文子串](../01/牛客_0017_中等_最长回文子串.md)  
> [[中等, 牛客] 矩阵的最小路径和](../03/牛客_0059_中等_矩阵的最小路径和.md)  
> [[中等, 牛客] 连续子数组的最大乘积](../04/牛客_0083_中等_连续子数组的最大乘积.md)  
  > 
> [[困难, LeetCode] 买卖股票的最佳时机III](../06/LeetCode_0123_困难_买卖股票的最佳时机III.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../01/LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 正则表达式匹配](../../2021/11/剑指Offer_1900_困难_正则表达式匹配.md)  
> [[困难, 牛客] 最长上升子序列(三)](../04/牛客_0091_困难_最长上升子序列(三).md)  
> [[困难, 牛客] 正则表达式匹配](../05/牛客_0122_困难_正则表达式匹配.md)  
> [[困难, 牛客] 编辑距离(二)](牛客_0035_困难_编辑距离(二).md)  
> [[困难, 牛客] 通配符匹配](../03/牛客_0044_困难_通配符匹配.md)  
  > 
> [[简单, LeetCode] 买卖股票的最佳时机](../06/LeetCode_0121_简单_买卖股票的最佳时机.md)  
> [[简单, LeetCode] 最大子数组和](../01/LeetCode_0053_简单_最大子数组和.md)  
> [[简单, LeetCode] 爬楼梯](../01/LeetCode_0070_简单_爬楼梯.md)  
> [[简单, 剑指Offer] 斐波那契数列](../../2021/11/剑指Offer_1001_简单_斐波那契数列.md)  
> [[简单, 剑指Offer] 跳台阶](../../2021/11/剑指Offer_1002_简单_跳台阶.md)  
> [[简单, 剑指Offer] 连续子数组的最大和](../../2021/12/剑指Offer_4200_简单_连续子数组的最大和.md)  
> [[简单, 华为机试] 放苹果](../05/华为机试_061_简单_放苹果.md)  
> [[简单, 牛客] 兑换零钱(一)](../05/牛客_0126_简单_兑换零钱(一).md)  
> [[简单, 牛客] 斐波那契数列](../03/牛客_0065_简单_斐波那契数列.md)  
> [[简单, 牛客] 求路径](牛客_0034_简单_求路径.md)  
> [[简单, 牛客] 跳台阶](../03/牛客_0068_简单_跳台阶.md)  
> [[简单, 牛客] 连续子数组的最大和](../01/牛客_0019_简单_连续子数组的最大和.md)  
  > 

</details>

<details><summary><b>暴力递归与动态规划 (11)</b></summary>

> [[中等, LeetCode] 一和零](../06/LeetCode_0474_中等_一和零.md)  
> [[中等, LeetCode] 打家劫舍](../06/LeetCode_0198_中等_打家劫舍.md)  
> [[中等, LeetCode] 施咒的最大总伤害](../../2025/10/LeetCode_3186_中等_施咒的最大总伤害.md)  
> [[中等, LeetCode] 解码方法](LeetCode_0091_中等_解码方法.md)  
> [[中等, LeetCode] 零钱兑换](../06/LeetCode_0322_中等_零钱兑换.md)  
> [[中等, 剑指Offer] n个骰子的点数](../01/剑指Offer_6000_中等_n个骰子的点数.md)  
> [[中等, 牛客] 01背包 🔥](../05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 最长公共子串](../05/牛客_0127_中等_最长公共子串.md)  
  > 
> [[困难, 牛客] 编辑距离(二)](牛客_0035_困难_编辑距离(二).md)  
> [[困难, 牛客] 通配符匹配](../03/牛客_0044_困难_通配符匹配.md)  
  > 
> [[简单, LeetCode] 爬楼梯](../01/LeetCode_0070_简单_爬楼梯.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
