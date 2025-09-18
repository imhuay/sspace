Linux 解压缩
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-06-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-19%2004%3A11%3A35&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden: false
tags: [linux]
-->

> ***Keywords**: linux*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [`tar` 解压缩](#tar-解压缩)
    - [tar.gz 格式](#targz-格式)
    - [tar.bz2 格式](#tarbz2-格式)
- [`zip/unzip` 解压缩](#zipunzip-解压缩)
<!--END_SECTION:toc-->

---

## `tar` 解压缩

```shell
# 查看档案中的内容
tar -tv -f $filename
```

### tar.gz 格式

```shell
tar -czv -f $xxx.tar.gz file1 file2 dir1 dir2
# -c: 打包
# -z: 使用 gzip 压缩, 文件名一般为 *.tar.gz
# -v: 显示正在处理的文件名
# -f filename: 处理的档案名

tar -xzv -f $xxx.tar.gz
# -x: 解包
```

### tar.bz2 格式

```shell
tar -cjv -f $xxx.tar.bz2 file1 file2 dir1 dir2
## -j: 使用 bzip2 压缩, 文件名一般为 *.tar.bz2

tar -xjv -f $xxx.tar.bz2
# -x: 解包
```

## `zip/unzip` 解压缩

```shell
zip -r -q $xxx.zip file1 file2 dir1 dir2
# -q: quiet, 不显示指令执行过程
# -r: 递归处理

unzip $xxx.zip > /dev/null 2>&1
```