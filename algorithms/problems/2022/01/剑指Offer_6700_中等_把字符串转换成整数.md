## 把字符串转换成整数
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%AD%97%E7%AC%A6%E4%B8%B2&color=blue&style=flat-square)](../../../README.md#字符串)
[![](https://img.shields.io/static/v1?label=&message=%E7%83%AD%E9%97%A8&color=blue&style=flat-square)](../../../README.md#热门)
[![](https://img.shields.io/static/v1?label=&message=%E7%BB%8F%E5%85%B8&color=blue&style=flat-square)](../../../README.md#经典)
<!--END_SECTION:badge-->
<!--info
tags: [字符串, 经典, 热门]
source: 剑指Offer
level: 中等
number: '6700'
name: 把字符串转换成整数
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
写一个函数 strToInt(string s), 实现把字符串转换成整数这个功能. 不能使用 atoi 或者其他类似的库函数.
```

<details><summary><b>详细描述</b></summary>

```txt
写一个函数 strToInt(string s), 实现把字符串转换成整数这个功能. 不能使用 atoi 或者其他类似的库函数.

首先, 该函数会根据需要丢弃无用的开头空格字符, 直到寻找到第一个非空格的字符为止.

当我们寻找到的第一个非空字符为正或者负号时, 则将该符号与之后面尽可能多的连续数字组合起来, 作为该整数的正负号; 假如第一个非空字符是数字, 则直接将其与之后连续的数字字符组合起来, 形成整数.

该字符串除了有效的整数部分之后也可能会存在多余的字符, 这些字符可以被忽略, 它们对于函数不应该造成影响.

注意: 假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时, 则你的函数不需要进行转换.

在任何情况下, 若函数不能进行有效的转换时, 请返回 0.

说明:
    假设我们的环境只能存储 32 位大小的有符号整数, 那么其数值范围为 [−231,  231 − 1]. 如果数值超过这个范围, 请返回  INT_MAX (231 − 1) 或 INT_MIN (−231).

示例 1:
    输入: "42"
    输出: 42
示例 2:
    输入: "   -42"
    输出: -42
    解释: 第一个非空白字符为 '-', 它是一个负号.
         我们尽可能将负号与后面所有连续出现的数字组合起来, 最后得到 -42 .
示例 3:
    输入: "4193 with words"
    输出: 4193
    解释: 转换截止于数字 '3', 因为它的下一个字符不为数字.
示例 4:
    输入: "words and 987"
    输出: 0
    解释: 第一个非空字符是 'w', 但它不是数字或正、负号.
        因此无法执行有效的转换.
示例 5:
    输入: "-91283472332"
    输出: -2147483648
    解释: 数字 "-91283472332" 超过 32 位有符号整数范围.
         因此返回 INT_MIN (−231).

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<summary><b>思路</b></summary>

- 把字符串当做数组, 依次遍历每个字符, 根据题目要求执行每一步操作;
- 注意一些细节: 如正负号、char 与 int 的互转、越界判断等, 详见下方代码;
- PS: 不同编程语言中字符串的实现细节;


<details><summary><b>C++</b></summary>

```cpp
class Solution {
public:
    int strToInt(string str) {
        int n = str.length();
        if (n < 1) return 0;

        int ret = 0;
        int p = 0;      // 模拟指针
        int sign = 1;   // 正负
        int s_max = INT_MAX / 10;

        while (isspace(str[p]))
            p++;  // 跳过前置空格

        // c++ 的字符串末尾有一个特殊字符, 因此不需要做越界判断
        // if (p == n) return 0;

        if (str[p] == '-') sign = -1;
        if (str[p] == '-' || str[p] == '+') p++;

        while (str[p] >= '0' && str[p] <= '9') {
            if (ret > s_max || (ret == s_max && str[p] > '7')) {  // 越界判断
                return sign > 0 ? INT_MAX : INT_MIN;
            }
            ret = ret * 10 + (str[p] - '0');  // str[p] - '0' 必须括起来, 否则顺序计算时会溢出
            p++;
        }

        return sign * ret;
    }
};

```

</details>


<details><summary><b>Python</b></summary>

```python
class Solution:
    def strToInt(self, str: str) -> int:

        n = len(str)
        if n < 1: return 0

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        ret = 0  # 保存结果
        sign = 1  # 记录符号
        p = 0  # 模拟指针

        # Python 字符串与 C++ 不同, 时刻需要进行越界判断
        while p < n and str[p] == ' ':
            p += 1

        if p == n:  # 越界判断
            return ret

        if str[p] == '-':
            sign = -1
        if str[p] in ('-', '+'):
            p += 1

        while p < n and '0' <= str[p] <= '9':  # 注意越界判断
            ret = ret * 10 + int(str[p])
            p += 1
            if ret > INT_MAX:  # python 中不存在越界, 因此直接跟 INT_MAX 比较即可
                return INT_MAX if sign == 1 else INT_MIN

        return ret * sign
```

</details>


<details><summary><b>Java</b></summary>

> [把字符串转换成整数 (数字越界处理, 清晰图解) ](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/solution/mian-shi-ti-67-ba-zi-fu-chuan-zhuan-huan-cheng-z-4/)

```java
class Solution {
    public int strToInt(String str) {
        int res = 0, bndry = Integer.MAX_VALUE / 10;
        int i = 0, sign = 1, length = str.length();
        if(length == 0) return 0;
        while(str.charAt(i) == ' ')
            if(++i == length) return 0;
        if(str.charAt(i) == '-') sign = -1;
        if(str.charAt(i) == '-' || str.charAt(i) == '+') i++;
        for(int j = i; j < length; j++) {
            if(str.charAt(j) < '0' || str.charAt(j) > '9') break;
            if(res > bndry || res == bndry && str.charAt(j) > '7')
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            res = res * 10 + (str.charAt(j) - '0');
        }
        return sign * res;
    }
}

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


<details><summary><b>字符串 (16)</b></summary>

> [[中等, LeetCode] 电话号码的字母组合 🔥](../10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, 剑指Offer] 表示数值的字符串](../../2021/11/剑指Offer_2000_中等_表示数值的字符串.md)  
> [[中等, 牛客] 大数乘法](牛客_0010_中等_大数乘法.md)  
> [[中等, 牛客] 大数加法](牛客_0001_中等_大数加法.md)  
> [[中等, 牛客] 把字符串转换成整数(atoi) 🔥](../04/牛客_0100_中等_把字符串转换成整数(atoi).md)  
> [[中等, 牛客] 比较版本号](../04/牛客_0104_中等_比较版本号.md)  
> [[中等, 牛客] 验证IP地址](../05/牛客_0113_中等_验证IP地址.md)  
  > 
> [[困难, 剑指Offer] 正则表达式匹配](../../2021/11/剑指Offer_1900_困难_正则表达式匹配.md)  
  > 
> [[简单, LeetCode] 亲密字符串](../../2021/11/LeetCode_0859_简单_亲密字符串.md)  
> [[简单, LeetCode] 字符串中的单词数](../07/LeetCode_0434_简单_字符串中的单词数.md)  
> [[简单, 剑指Offer] 左旋转字符串](剑指Offer_5802_简单_左旋转字符串.md)  
> [[简单, 剑指Offer] 替换空格](../../2021/11/剑指Offer_0500_简单_替换空格.md)  
> [[简单, 牛客] 压缩字符串(一)](../04/牛客_0101_简单_压缩字符串(一).md)  
> [[简单, 牛客] 反转字符串](../04/牛客_0103_简单_反转字符串.md)  
> [[简单, 牛客] 旋转字符串](../05/牛客_0114_简单_旋转字符串.md)  
> [[简单, 牛客] 最长公共前缀](../03/牛客_0055_简单_最长公共前缀.md)  
  > 

</details>

<details><summary><b>热门 (16)</b></summary>

> [[中等, LeetCode] 买卖股票的最佳时机 II 🔥](../06/LeetCode_0122_中等_买卖股票的最佳时机II.md)  
> [[中等, LeetCode] 全排列 🔥](../10/LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](../10/LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 重排链表 🔥](../06/LeetCode_0143_中等_重排链表.md)  
> [[中等, 牛客] 三数之和 🔥](../03/牛客_0054_中等_三数之和.md)  
> [[中等, 牛客] 把二叉树打印成多行 🔥](../03/牛客_0080_中等_把二叉树打印成多行.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](../10/LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](../10/LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](../10/LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 平衡二叉树 🔥](../09/LeetCode_0110_简单_平衡二叉树.md)  
> [[简单, 牛客] 两个链表的第一个公共结点 🔥](../03/牛客_0066_简单_两个链表的第一个公共结点.md)  
  > 

</details>

<details><summary><b>经典 (37)</b></summary>

> [[中等, LeetCode] 下一个排列 🔥](../10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 二叉树的完全性检验 🔥](../03/LeetCode_0958_中等_二叉树的完全性检验.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, 剑指Offer2] 整数除法 🔥](../09/剑指Offer2_001_中等_整数除法.md)  
> [[中等, 剑指Offer] 丑数 🔥](../../2021/12/剑指Offer_4900_中等_丑数.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](../../2021/12/剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 剑指Offer] 复杂链表的复制 (深拷贝) 🔥](../../2021/12/剑指Offer_3500_中等_复杂链表的复制(深拷贝).md)  
> [[中等, 剑指Offer] 字符串的排列 (全排列) 🔥](../../2021/12/剑指Offer_3800_中等_字符串的排列(全排列).md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../../2021/11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 剑指Offer] 栈的压入、弹出序列 🔥](../../2021/11/剑指Offer_3100_中等_栈的压入、弹出序列.md)  
> [[中等, 剑指Offer] 重建二叉树 🔥](../../2021/11/剑指Offer_0700_中等_重建二叉树.md)  
> [[中等, 剑指Offer] 顺时针打印矩阵 (3种思路4个写法) 🔥](../../2021/11/剑指Offer_2900_中等_顺时针打印矩阵(3种思路4个写法).md)  
> [[中等, 牛客] 01背包 🔥](../05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 丢棋子问题 (鹰蛋问题) 🔥](../04/牛客_0087_中等_丢棋子问题(鹰蛋问题).md)  
> [[中等, 牛客] 字符串的排列 🔥](../05/牛客_0121_中等_字符串的排列.md)  
> [[中等, 牛客] 寻找峰值 🔥](../04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 岛屿数量 🔥](../04/牛客_0109_中等_岛屿数量.md)  
> [[中等, 牛客] 把字符串转换成整数(atoi) 🔥](../04/牛客_0100_中等_把字符串转换成整数(atoi).md)  
> [[中等, 牛客] 数组中只出现一次的两个数字 🔥](../03/牛客_0075_中等_数组中只出现一次的两个数字.md)  
> [[中等, 牛客] 最长公共子序列(二) 🔥](../04/牛客_0092_中等_最长公共子序列(二).md)  
> [[中等, 牛客] 栈和排序 🔥](../05/牛客_0115_中等_栈和排序.md)  
> [[中等, 牛客] 汉诺塔问题 🔥](../03/牛客_0067_中等_汉诺塔问题.md)  
  > 
> [[困难, LeetCode] 编辑距离 🔥](../06/LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 数组中的逆序对 🔥](剑指Offer_5100_困难_数组中的逆序对.md)  
> [[困难, 牛客] 接雨水问题 🔥](../05/牛客_0128_困难_接雨水问题.md)  
> [[困难, 牛客] 设计LFU缓存结构 🔥](../04/牛客_0094_困难_设计LFU缓存结构.md)  
> [[困难, 牛客] 设计LRU缓存结构 🔥](../04/牛客_0093_困难_设计LRU缓存结构.md)  
  > 
> [[简单, LeetCode] 二叉树的最大深度 🔥](../07/LeetCode_0104_简单_二叉树的最大深度.md)  
> [[简单, LeetCode] 反转链表 🔥](../10/LeetCode_0206_简单_反转链表.md)  
> [[简单, 剑指Offer] 二叉搜索树的最近公共祖先 🔥](剑指Offer_6801_简单_二叉搜索树的最近公共祖先.md)  
> [[简单, 剑指Offer] 反转链表 🔥](../../2021/11/剑指Offer_2400_简单_反转链表.md)  
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](../../2021/12/剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
> [[简单, 剑指Offer] 最小的k个数 (partition操作) 🔥](../../2021/12/剑指Offer_4000_简单_最小的k个数(partition操作).md)  
> [[简单, 牛客] 二进制中1的个数 🔥](../05/牛客_0120_简单_二进制中1的个数.md)  
> [[简单, 牛客] 单链表的排序 🔥](../03/牛客_0070_简单_单链表的排序.md)  
> [[简单, 牛客] 求平方根 🔥](../02/牛客_0032_简单_求平方根.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
