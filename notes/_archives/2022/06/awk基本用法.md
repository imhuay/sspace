`awk` 备忘
===
<!--START_SECTION:badge-->

![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-06-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-03%2022%3A42%3A16&label_color=gray&color=thistle&style=flat-square)

<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden: false
tag: [linux]
-->

> ***Keywords**: linux, awk*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [`awk` 批量处理行](#awk-批量处理行)
    - [基本使用](#基本使用)
    - [Reference](#reference)
    - [内建变量](#内建变量)
    - [内建函数](#内建函数)
- [示例](#示例)
    - [正则过滤](#正则过滤)
    - [一行转多行](#一行转多行)
<!--END_SECTION:toc-->

---

## `awk` 批量处理行
- `awk` 不仅仅是一个命令行工具, 而且还是一门种编程语言; 不过在大多数场景下, 命令行的使用方式已经足够了;
- `awk` 主要用于处理格式化的文本文件, 对每一行数据进行相同的操作, 以**重构文件**或**筛选信息**;
- 相比使用 python 处理, `awk` 的启动更快, 成本更低 (Linux环境下, 且熟练掌握后);

### 基本使用
```shell
awk [选项参数] 'script' 文件
```
> script 只能被单引号包含

### Reference
- 【官网】 Top (The GNU Awk User' s Guide)  ( https://www.gnu.org/software/gawk/manual/html_node/Index.html )
- awk 入门教程 - 阮一峰的网络日志  ( http://www.ruanyifeng.com/blog/2018/11/awk.html )
- Linux awk 命令 | 菜鸟教程  ( https://www.runoob.com/linux/linux-comm-awk.html )


### 内建变量
`awk` 内建了一些常用变量,

| 变量 | 描述                                                                             |
| ---- | -------------------------------------------------------------------------------- |
| `$n` | 一行中的第 `n` 个字段, 分隔符由变量 `FS` 定义, `n` 从 1 开始, `n=0` 时表示当前行 |
| `FS` | 字段分隔符(默认是空格和tab)                                                      |
| A3   | B3                                                                               |


### 内建函数

## 示例

### 正则过滤

### 一行转多行
**输入**
```
齐@@1##河@@1##美@@0##食@@0##小@@1##镇@@1
星@@1##月@@1##缘@@1##旅@@0##店@@0
```

**输出**
```
齐	1
河	1
美	0
食	0
小	1
镇	1

星	1
月	1
缘	1
旅	0
店	0

```

**命令**
```shell
awk '{ gsub(/@@/, "\t"); gsub(/##/,"\n",$0); print $0,"\n"; }' tmp.txt
```

**说明**
- `/.../`: 正则 pattern, 正则是 `awk` 的基础, 为了表达其特殊地位, 使用 `/` 符号包围
- `gsub()`函数: 正则替换, 默认有三个参数 `gsub(r,s,t)`, `t` 默认为当前行, 即 `$0`, 相当于 `gsub(r,s) == gsub(r,s,$0)`
- `print`: 输出, 默认输出当前行, 即 `print == print $0`
- `$i`: `$0` 表示当前行, `$1、$2、...` 表示