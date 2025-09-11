## 划分2N个点
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&label_color=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&label_color=gray&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=Collection&label_color=gray&color=green&style=flat-square)](../../../README.md#collection)
[![](https://img.shields.io/static/v1?label=&message=%E6%95%B0%E5%AD%A6&label_color=gray&color=blue&style=flat-square)](../../../README.md#数学)
<!--END_SECTION:badge-->
<!--info
tags: [数学]
source: Collection
level: 中等
number: '20220126'
name: 划分2N个点
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
平面上有 2N 个点，是否存在一条直线将这 2N 个点一分为二（各 N 个点）
```

<!-- 
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->


<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<details><summary><b>思路</b></summary>

> [是否一点存在直线能把平面上给定的2n个点分成两部分，每部分n个点？ - 知乎](https://www.zhihu.com/question/25071189)

```txt
- 考虑将这 2N 个点两两相连得到 m 条直线（可能存在重叠），其斜率分别为 k_1, .., k_m；
- 因为 m 是有限的，则必然存在与这 m 条直线斜率不同的直线，
- 取这条直线的垂线，则这条垂线与这 m 条直线都不垂直；
- 把这条直线从这 2N 个点的一侧平移到另一侧，得到 2N 个交点，
- 则显然存在一条平行于平移方向的直线将这 2N 个交点分成两部分，而这条直线也将这 2N 个点划分成了数量相等的两部分。
```

</details>

<!--START_SECTION:relate-->
---

### 相关主题

<details><summary><b>数学</b></summary>

> [[中等, LeetCode] 整数拆分](../../2021/12/LeetCode_0343_中等_整数拆分.md)  
> [[中等, 剑指Offer] 剪绳子](../../2021/11/剑指Offer_1402_中等_剪绳子.md)  
> [[中等, 剑指Offer] 剪绳子（整数拆分）](../../2021/11/剑指Offer_1401_中等_剪绳子（整数拆分）.md)  
> [[中等, 牛客] 阶乘末尾0的数量](../05/牛客_0129_中等_阶乘末尾0的数量.md)  
  > 
> [[简单, LeetCode] 排列硬币](../../2021/10/LeetCode_0441_简单_排列硬币.md)  
> [[简单, 牛客] 三个数的最大乘积](../04/牛客_0106_简单_三个数的最大乘积.md)  
> [[简单, 牛客] 回文数字](../03/牛客_0056_简单_回文数字.md)  
> [[简单, 牛客] 进制转换](../04/牛客_0112_简单_进制转换.md)  
  > 

</details>
<!--END_SECTION:relate-->