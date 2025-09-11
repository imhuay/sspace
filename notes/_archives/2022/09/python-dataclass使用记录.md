`dataclass` 使用记录
===
<!--START_SECTION:badge-->

![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-09-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-03%2022%3A42%3A16&label_color=gray&color=thistle&style=flat-square)

<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden: false
tag: [python]
-->

> ***Keywords**: python*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [基础](#基础)
- [进阶](#进阶)
<!--END_SECTION:toc-->

---

## 基础
- `dataclass` 是对数据的模板化封装, 类比 C/C++ 中的 `stuct`;
- 基本用法:
    ```python
    from dataclasses import dataclass

    @dataclass
    class Foo:
        a: int
        b: str = 'B'  # 默认值

    f1 = Foo(1)
    f2 = Foo(2, 'b')
    ```
- Python 3.7 开始加入标准库, 3.7 之前需要安装外部依赖;
    ```
    # requirements.txt
    dataclasses; python_version < '3.7'
    ```


## 进阶
> 参考: [Python 最佳实践 (数据类专题) - 肥清哥哥](https://space.bilibili.com/374243420/channel/collectiondetail?sid=422655)

