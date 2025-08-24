`split` 分割文件
===
<!--START_SECTION:badge-->

![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-06-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-03%2022%3A42%3A16&label_color=gray&color=thistle&style=flat-square)

<!--END_SECTION:badge-->
<!--info
top: false
hidden: true
-->

> ***Keywords**: Linux*

<!--START_SECTION:toc-->
- [`split` 分割文件](#split-分割文件-1)
<!--END_SECTION:toc-->

---

## `split` 分割文件
```shell

## 将文件 file.txt 分割成 5 个小文件，生成新文件以 new_file_ 为前缀，后缀默认为 aa ab ac ad ae
## 将文件 file.txt 分割成 5 个小文件，不切割行
split -n l/5 file.txt new_file_
split -n 5 file.txt new_file_  ## 注意：直接使用 -n 会切割行

## 同上，-a 选项调整后缀为 1 个字母，即 a b c d e
split -n l/5 -a 1 file new_file_

## 对文件 file.txt 按行数分割，生成新文件以 new_file_ 为前缀，后缀为 a b c ... 等
split -l 100 file new_file_  -a 1  ## 每个文件 100 行

```