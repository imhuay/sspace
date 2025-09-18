requirements.txt 语法备忘
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-09-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-03%2022%3A42%3A16&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden: true
tags: []
-->

> ***Keywords**: python*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [示例](#示例)
<!--END_SECTION:toc-->

---


- 参考: [Python requirements.txt 语法 - ChnMig - 博客园](https://www.cnblogs.com/chnmig/p/12107199.html)
- 标准文档: [PEP 508 – Dependency specification for Python Software Packages | peps.python.org](https://peps.python.org/pep-0508/#environment-markers)


## 示例
```shell
# requirements.txt
ipywidgets
loky>=3.0.0
jaxlib; sys_platform != 'win32'
pywinpty==1.1.6; python_version < '3.7' and sys_platform == 'win32'
```