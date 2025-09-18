Mac 环境配置
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-07-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-19%2004%3A11%3A35&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden: true
tags: []
-->

> ***Keywords**: 环境配置*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [必备软件](#必备软件)
    - [Homebrew (brew)](#homebrew-brew)
- [常用工具](#常用工具)
<!--END_SECTION:toc-->

---

## 必备软件

### Homebrew (brew)
> [Homebrew - 软件包管理工具](https://brew.sh/)

安装后需要手动添加环境变量 (注意安装完成后的提示)
```shell
$ echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/huay/.zprofile
$ eval "$(/opt/homebrew/bin/brew shellenv)"
```

## 常用工具

```shell
$ brew install cmake
$ brew install pkgconfig
```
