常用 LaTeX 公式
===
<!--START_SECTION:badge-->

![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&color=yellowgreen&style=flat-square)

<!--END_SECTION:badge-->
<!--info
top: false
hidden: false
-->

<!--START_SECTION:toc-->
- [参考](#参考)
- [常用符号](#常用符号)
- [多行公式](#多行公式)
- [括号](#括号)
- [标记](#标记)
<!--END_SECTION:toc-->

## 参考
- [【LaTeX】LaTeX符号大全_Ljnoit-CSDN博客_latex 绝对值符号](https://blog.csdn.net/ljnoit/article/details/104264753)
- 在线 LaTeX 公式编辑器：https://editor.codecogs.com


## 常用符号

$$
    \sum_{a}^{e}
$$


## 多行公式

**示例 1**

**单行**: $\begin{aligned} x &= a + b \\  &= c + d \end{aligned}$

**多行**: 
$$
\begin{align*}
 a &= 1+2 \\ 
   &= 2+1
\end{align*}
$$

**示例 2**

$$
\begin{align}
 a &= 1+1 \\ 
 b &= 2+2
\end{align}
$$

**示例 3**
$$
\left\{
    \begin{align*}
    a &= 1+2 &// 说明1  \\ 
    b &= 2+1 &// 说明2
    \end{align*}
\right.
$$

## 括号

**绝对值**
$$
\left | a \right |
$$

## 标记

**转置**
$$\begin{align*}
& \mathbf{A}^\mathrm{T}                 \\
& \mathbf{A}^\top           &// 推荐     \\
& \mathbf{A}^\mathsf{T}                 \\
& \mathbf{A}^\intercal                  \\
\end{align*}$$
