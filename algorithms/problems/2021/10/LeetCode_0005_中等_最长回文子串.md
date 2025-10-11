## 最长回文子串
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=green&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92&color=blue&style=flat-square)](../../../README.md#动态规划)
[![](https://img.shields.io/static/v1?label=&message=%E5%8F%8C%E6%8C%87%E9%92%88&color=blue&style=flat-square)](../../../README.md#双指针)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
<!--END_SECTION:badge-->
<!--info
tags: [dp, 双指针, lc100]
source: LeetCode
level: 中等
number: '0005'
name: 最长回文子串
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
给你一个字符串 s, 找到 s 中最长的回文子串.
```
> [5. 最长回文子串 - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/longest-palindromic-substring/)

<details><summary><b>详细描述</b></summary>

```txt
给你一个字符串 s, 找到 s 中最长的回文子串.

示例 1:
    输入: s = "babad"
    输出: "bab"
    解释: "aba" 同样是符合题意的答案.
示例 2:
    输入: s = "cbbd"
    输出: "bb"
示例 3:
    输入: s = "a"
    输出: "a"
示例 4:
    输入: s = "ac"
    输出: "a"

提示:
    1 <= s.length <= 1000
    s 仅由数字和英文字母 (大写和/或小写) 组成

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<summary><b>思路1: 动态规划</b></summary>

- 状态定义: `dp[i][j] := 子串 s[i:j] 是否为回文串`;
- 状态转移方程: `dp[i][j] := dp[i+1][j-1] == True 且 s[i] == s[j]`;
- 初始状态
    - 单个字符: `dp[i][j] := True` 当 `i == j`
    - 两个连续相同字符: `dp[i][j] := True` 当 `j == i + 1 && s[i] == s[j]`
- 动态规划并不是最适合的解, 这里仅提供一个思路;
- 如果要使用动态规划解本题, 如何循环是关键, 因为回文串的特点, 从 "双指针" 的角度来看, 需要从中心往两侧遍历, 这跟大多数的 dp 问题略有不同;

<details><summary><b>C++</b></summary>

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();

        vector<vector<int>> dp(n, vector<int>(n, 0));
        int max_len = 1;    // 保存最长回文子串长度
        int start = 0;      // 保存最长回文子串起点

        // 初始状态1: 子串长度为 1 时, 显然是回文子串
        for (int i = 0; i < n; i++)
            dp[i][i] = 1;

        //for (int j = 1; j < n; j++)         // 子串结束位置
        //    for (int i = 0; i < j; i++) {   // 子串起始位置
        // 上述循环方式也是可以的, 但在 "最长回文子序列" 一题中会有问题
        // 下面的循环方式在两个问题中都正确, 这个遍历思路比较像 "中心扩散法"
        for (int j = 1; j < n; j++)             // 子串结束位置
            for (int i = j - 1; i >= 0; i--) {  // 子串开始位置
                if (j == i + 1)  // 初始状态2: 子串长度为 2 时, 只有当两个字母相同时才是回文子串
                    dp[i][j] = (s[i] == s[j]);
                else  // 状态转移方程: 当上一个状态是回文串, 且此时两个位置的字母也相同时, 当前状态才是回文串
                    dp[i][j] = (dp[i + 1][j - 1] && s[i] == s[j]);

                // 保存最长回文子串
                if (dp[i][j] && max_len < (j - i + 1)) {
                    max_len = j - i + 1;
                    start = i;
                }
            }

        return s.substr(start, max_len);
    }
};
```

</details>

<details><summary><b>Python</b></summary>

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        start = 0
        length = 1
        for j in range(1, n):  # 子串的结束位置
            for i in range(j - 1, -1, -1):  # 子串的开始位置
                if i == j - 1:
                    dp[i][j] = 1 if s[i] == s[j] else 0
                else:
                    dp[i][j] = 1 if dp[i + 1][j - 1] and s[i] == s[j] else 0

                if dp[i][j]:
                    if j - i + 1 > length:
                        length = j - i + 1
                        start = i

        return s[start: start + length]
```

</details>

<summary><b>思路2: 模拟-中心扩散 (推荐) </b></summary>

- 按照回文的定义, 遍历每个字符作为中点, 向两边扩散;
- 注意奇数和偶数两种情况;

<details><summary><b>Python: 写法 1 (推荐, 不容易写错)</b></summary>

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.ret = ''
        n = len(s)

        def process(l, r):
            tmp = ''
            # 从 s[l:r] 开始向两侧扩散
            while l >= 0 and r < n and s[l] == s[r]:
                tmp = s[l: r + 1]
                l, r = l - 1, r + 1

            if len(tmp) > len(self.ret):
                self.ret = tmp

        for i in range(n):  # 注意 i 的范围
            process(i, i)  # 奇数情况
            process(i, i + 1)  # 偶数情况

        return self.ret
```

</details>

<details><summary><b>Python: 写法 2</b></summary>

- 相比写法 1, 写法 2 少用了一个变量, 但是很容易写错;

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.ret = s[0]
        n = len(s)

        def process(l, r):
            # 注意这里比较的时 s[l - 1] 和 s[r + 1]
            while l - 1 >= 0 and r + 1 < n and s[l - 1] == s[r + 1]:
                l, r = l - 1, r + 1

            if r - l + 1 > len(self.ret):
                self.ret = s[l: r + 1]

        for i in range(n - 1):
            process(i, i)  # 奇数情况
            if s[i] == s[i + 1]:  # 偶数情况,
                # 因为 process 中比较的是 s[l - 1] 和 s[r + 1], 所以要额外加一个判断条件
                process(i, i + 1)

        return self.ret
```

</details>


<!--START_SECTION:relate_problem-->
---

### 相关主题

<details><summary><b>动态规划</b></summary>

> [[中等, LeetCode] 一和零](../../2022/06/LeetCode_0474_中等_一和零.md)  
> [[中等, LeetCode] 三角形最小路径和](../../2022/06/LeetCode_0120_中等_三角形最小路径和.md)  
> [[中等, LeetCode] 不同的二叉搜索树](../../2022/03/LeetCode_0096_中等_不同的二叉搜索树.md)  
> [[中等, LeetCode] 乘积最大子数组](../../2022/06/LeetCode_0152_中等_乘积最大子数组.md)  
> [[中等, LeetCode] 买卖股票的最佳时机II 🔥](../../2022/06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 完全平方数](../../2022/02/LeetCode_0279_中等_完全平方数.md)  
> [[中等, LeetCode] 打家劫舍](../../2022/06/LeetCode_0198_中等_打家劫舍.md)  
> [[中等, LeetCode] 打家劫舍II](../../2022/06/LeetCode_0213_中等_打家劫舍II.md)  
> [[中等, LeetCode] 整数拆分](../12/LeetCode_0343_中等_整数拆分.md)  
> [[中等, LeetCode] 最小路径和](../../2022/01/LeetCode_0064_中等_最小路径和.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../../2022/06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, LeetCode] 解码方法](../../2022/02/LeetCode_0091_中等_解码方法.md)  
> [[中等, LeetCode] 零钱兑换](../../2022/06/LeetCode_0322_中等_零钱兑换.md)  
> [[中等, LeetCode] 零钱兑换II](../../2022/06/LeetCode_0518_中等_零钱兑换II.md)  
> [[中等, 剑指Offer] n个骰子的点数](../../2022/01/剑指Offer_6000_中等_n个骰子的点数.md)  
> [[中等, 剑指Offer] 丑数 🔥](../12/剑指Offer_4900_中等_丑数.md)  
> [[中等, 剑指Offer] 剪绳子 (整数拆分)](../11/剑指Offer_1401_中等_剪绳子(整数拆分).md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](../../2022/01/剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 剑指Offer] 斐波那契数列-3 (把数字翻译成字符串)](../12/剑指Offer_4600_中等_斐波那契数列-3(把数字翻译成字符串).md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 剑指Offer] 礼物的最大价值](../12/剑指Offer_4700_中等_礼物的最大价值.md)  
> [[中等, 牛客] 01背包 🔥](../../2022/05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 丑数](../../2022/03/牛客_0079_中等_丑数.md)  
> [[中等, 牛客] 丢棋子问题 (鹰蛋问题) 🔥](../../2022/04/牛客_0087_中等_丢棋子问题(鹰蛋问题).md)  
> [[中等, 牛客] 把数字翻译成字符串](../../2022/05/牛客_0116_中等_把数字翻译成字符串.md)  
> [[中等, 牛客] 最大正方形](../../2022/04/牛客_0108_中等_最大正方形.md)  
> [[中等, 牛客] 最长公共子串](../../2022/05/牛客_0127_中等_最长公共子串.md)  
> [[中等, 牛客] 最长公共子序列(二) 🔥](../../2022/04/牛客_0092_中等_最长公共子序列(二).md)  
> [[中等, 牛客] 最长回文子串](../../2022/01/牛客_0017_中等_最长回文子串.md)  
> [[中等, 牛客] 矩阵的最小路径和](../../2022/03/牛客_0059_中等_矩阵的最小路径和.md)  
> [[中等, 牛客] 连续子数组的最大乘积](../../2022/04/牛客_0083_中等_连续子数组的最大乘积.md)  
  > 
> [[困难, LeetCode] 买卖股票的最佳时机III](../../2022/06/LeetCode_0123_困难_买卖股票的最佳时机III.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../../2022/10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../../2022/01/LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, LeetCode] 编辑距离 🔥](../../2022/06/LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 正则表达式匹配](../11/剑指Offer_1900_困难_正则表达式匹配.md)  
> [[困难, 牛客] 最长上升子序列(三)](../../2022/04/牛客_0091_困难_最长上升子序列(三).md)  
> [[困难, 牛客] 正则表达式匹配](../../2022/05/牛客_0122_困难_正则表达式匹配.md)  
> [[困难, 牛客] 编辑距离(二)](../../2022/02/牛客_0035_困难_编辑距离(二).md)  
> [[困难, 牛客] 通配符匹配](../../2022/03/牛客_0044_困难_通配符匹配.md)  
  > 
> [[简单, LeetCode] 买卖股票的最佳时机](../../2022/06/LeetCode_0121_简单_买卖股票的最佳时机.md)  
> [[简单, LeetCode] 最大子数组和](../../2022/01/LeetCode_0053_简单_最大子数组和.md)  
> [[简单, LeetCode] 爬楼梯](../../2022/01/LeetCode_0070_简单_爬楼梯.md)  
> [[简单, 剑指Offer] 斐波那契数列](../11/剑指Offer_1001_简单_斐波那契数列.md)  
> [[简单, 剑指Offer] 跳台阶](../11/剑指Offer_1002_简单_跳台阶.md)  
> [[简单, 剑指Offer] 连续子数组的最大和](../12/剑指Offer_4200_简单_连续子数组的最大和.md)  
> [[简单, 华为机试] 放苹果](../../2022/05/华为机试_061_简单_放苹果.md)  
> [[简单, 牛客] 兑换零钱(一)](../../2022/05/牛客_0126_简单_兑换零钱(一).md)  
> [[简单, 牛客] 斐波那契数列](../../2022/03/牛客_0065_简单_斐波那契数列.md)  
> [[简单, 牛客] 求路径](../../2022/02/牛客_0034_简单_求路径.md)  
> [[简单, 牛客] 跳台阶](../../2022/03/牛客_0068_简单_跳台阶.md)  
> [[简单, 牛客] 连续子数组的最大和](../../2022/01/牛客_0019_简单_连续子数组的最大和.md)  
  > 

</details>
<details><summary><b>双指针</b></summary>

> [[中等, LeetCode] 三数之和 🔥](LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../../2022/10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../../2022/01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 最接近的三数之和](LeetCode_0016_中等_最接近的三数之和.md)  
> [[中等, LeetCode] 有效三角形的个数](LeetCode_0611_中等_有效三角形的个数.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 牛客] 三数之和 🔥](../../2022/03/牛客_0054_中等_三数之和.md)  
> [[中等, 牛客] 删除链表的倒数第n个节点](../../2022/03/牛客_0053_中等_删除链表的倒数第n个节点.md)  
> [[中等, 牛客] 合并两个有序的数组](../../2022/01/牛客_0022_中等_合并两个有序的数组.md)  
  > 
> [[困难, LeetCode] 接雨水 🔥](LeetCode_0042_困难_接雨水.md)  
> [[困难, 牛客] 接雨水问题 🔥](../../2022/05/牛客_0128_困难_接雨水问题.md)  
  > 
> [[简单, LeetCode] 两数之和II-输入有序数组](../../2022/07/LeetCode_0167_简单_两数之和II-输入有序数组.md)  
> [[简单, LeetCode] 链表的中间结点](../../2022/06/LeetCode_0876_简单_链表的中间结点.md)  
> [[简单, 剑指Offer] 两个链表的第一个公共节点](../../2022/01/剑指Offer_5200_简单_两个链表的第一个公共节点.md)  
> [[简单, 剑指Offer] 和为s的两个数字](../../2022/01/剑指Offer_5701_简单_和为s的两个数字.md)  
> [[简单, 剑指Offer] 和为s的连续正数序列](../../2022/01/剑指Offer_5702_简单_和为s的连续正数序列.md)  
> [[简单, 剑指Offer] 翻转单词顺序](../../2022/01/剑指Offer_5801_简单_翻转单词顺序.md)  
> [[简单, 剑指Offer] 调整数组顺序使奇数位于偶数前面](../11/剑指Offer_2100_简单_调整数组顺序使奇数位于偶数前面.md)  
> [[简单, 剑指Offer] 链表中倒数第k个节点](../11/剑指Offer_2200_简单_链表中倒数第k个节点.md)  
> [[简单, 牛客] 判断链表中是否有环](../../2022/01/牛客_0004_简单_判断链表中是否有环.md)  
> [[简单, 牛客] 反转字符串](../../2022/04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 链表中倒数最后k个结点](../../2022/03/牛客_0069_简单_链表中倒数最后k个结点.md)  
> [[简单, 牛客] 链表中环的入口结点](../../2022/01/牛客_0003_简单_链表中环的入口结点.md)  
  > 

</details>
<details><summary><b>LeetCode Hot 100</b></summary>

> [[中等, LeetCode] 三数之和 🔥](LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../../2022/10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 两数相加 🔥](LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 全排列 🔥](../../2022/10/LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](../../2022/10/LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../../2022/01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../../2022/10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 字母异位词分组 🔥](../../2022/10/LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 括号生成 🔥](../../2022/10/LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](../../2022/10/LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, LeetCode] 无重复字符的最长子串 🔥](../../2022/02/LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](../../2022/10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, LeetCode] 组合总和 🔥](../../2022/10/LeetCode_0039_中等_组合总和.md)  
> [[中等, LeetCode] 组合总和II 🔥](../../2022/10/LeetCode_0040_中等_组合总和II.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../../2022/02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](../../2022/10/LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../../2022/02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 接雨水 🔥](LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../../2022/10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../../2022/01/LeetCode_0010_困难_正则表达式匹配.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](LeetCode_0001_简单_两数之和.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 有效的括号 🔥](../../2022/03/LeetCode_0020_简单_有效的括号.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
