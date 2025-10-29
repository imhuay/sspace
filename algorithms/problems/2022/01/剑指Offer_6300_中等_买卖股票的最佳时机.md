## 买卖股票的最佳时机
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=darkcyan&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E6%A8%A1%E6%8B%9F&color=blue&style=flat-square)](../../../README.md#模拟)
<!--END_SECTION:badge-->
<!--info
tags: [模拟]
source: 剑指Offer
level: 中等
number: '6300'
name: 买卖股票的最佳时机
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
把某股票的价格按照时间顺序存储在数组中, 求买卖一次的最大利润.
示例: 输入: [7,1,5,3,6,4], 输出: 5 (在价格 1 时买入, 价格 6 时卖出)
```

<details><summary><b>详细描述</b></summary>

```txt
假设把某股票的价格按照时间先后顺序存储在数组中, 请问买卖该股票一次可能获得的最大利润是多少?

示例 1:
    输入: [7,1,5,3,6,4]
    输出: 5
    解释: 在第 2 天 (股票价格 = 1) 的时候买入, 在第 5 天 (股票价格 = 6) 的时候卖出, 最大利润 = 6-1 = 5 .
        注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格.
示例 2:
    输入: [7,6,4,3,1]
    输出: 0
    解释: 在这种情况下, 没有交易完成, 所以最大利润为 0.


限制:
    0 <= 数组长度 <= 10^5
    0 <= 股票价格 <= 10^5

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<summary><b>思路</b></summary>

```txt
1. 遍历 prices, 以 min_p 记录当前的最小值 (非全局最小值);
2. 用当前价格 p 减去 min_p, 得到当天卖出的利润;
3. 使用 ret 记录遍历过程中的最大利润.
```


<details><summary><b>Python</b></summary>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """"""
        ret = 0
        min_p = 10001
        for p in prices:
            min_p = min(p, min_p)
            ret = max(ret, p - min_p)

        return ret
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


<details><summary><b>模拟 (15)</b></summary>

> [[中等, LeetCode] 分割数组](../06/LeetCode_0915_中等_分割数组.md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 牛客] 大数乘法](牛客_0010_中等_大数乘法.md)  
> [[中等, 牛客] 大数加法](牛客_0001_中等_大数加法.md)  
> [[中等, 牛客] 最长回文子串](牛客_0017_中等_最长回文子串.md)  
> [[中等, 牛客] 螺旋矩阵](../03/牛客_0038_中等_螺旋矩阵.md)  
  > 
> [[困难, LeetCode] 将数据流变为多个不相交区间](../../2021/10/LeetCode_0352_困难_将数据流变为多个不相交区间.md)  
  > 
> [[简单, LeetCode] 亲密字符串](../../2021/11/LeetCode_0859_简单_亲密字符串.md)  
> [[简单, 剑指Offer] 扑克牌中的顺子](剑指Offer_6100_简单_扑克牌中的顺子.md)  
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](../../2021/12/剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
> [[简单, 牛客] 买卖股票的最好时机(一)](牛客_0007_简单_买卖股票的最好时机(一).md)  
> [[简单, 牛客] 反转数字](../03/牛客_0057_简单_反转数字.md)  
> [[简单, 牛客] 字符串变形](../04/牛客_0089_简单_字符串变形.md)  
> [[简单, 牛客] 扑克牌顺子](../03/牛客_0063_简单_扑克牌顺子.md)  
> [[简单, 牛客] 数组中出现次数超过一半的数字](../03/牛客_0073_简单_数组中出现次数超过一半的数字.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
