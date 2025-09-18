Python 容器基类的使用
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-08-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-03%2022%3A42%3A16&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden: false
tags: [python]
-->

> ***Keywords**: Python*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [背景](#背景)
- [使用场景](#使用场景)
    - [Type Hints](#type-hints)
    - [判断一个具体类或实例是否具有某一特定的接口](#判断一个具体类或实例是否具有某一特定的接口)
<!--END_SECTION:toc-->

---

## 背景
> [容器的抽象基类 (`collections.abc`) — Python 文档](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections-abstract-base-classes)  

- 容器基类列表: [collections.abc — Python 文档](https://docs.python.org/zh-cn/3/library/collections.abc.html)


## 使用场景

### Type Hints

```python
# def foo(ls: Union[List, Tuple]):
def foo(ls: Sequence):
    ...
```

### 判断一个具体类或实例是否具有某一特定的接口

```python
from typing import *

# 判断能否 len(obj), 即判断是否实现了 __len__
isinstance(obj, Sized)

# 判断能否 obj[index]
isinstance(obj, Sequence)

# 判断某个类是否可以哈希
issubclass(cls, Hashable)
```
