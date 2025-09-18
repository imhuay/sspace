类方法中 `self` 的含义
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-06-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-19%2004%3A11%3A35&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden: false
level: 0
tags: [python]
-->

> ***Keywords**: python*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [本质](#本质)
- [使用场景](#使用场景)
    - [动态修改成员函数](#动态修改成员函数)
- [参考](#参考)
<!--END_SECTION:toc-->

---

## 本质

- 以下面的类和方法为例:
    ```python
    class A:
        def f(self, x):
            print(x)
    ```
- `self` 本质就是 `A` 的一个实例;
    ```python
    # 定义
    a = A()  # 创建 A 的一个实例

    # 调用
    a.f(1)  # 1
    ```
- `a.f(1)` 实际上就是 `A.f(a, 1)` 的语法糖;


## 使用场景

### 动态修改成员函数
- 如果是将新函数赋值给**类**, 那么需要预留第一个位置给 `slef`;
    ```python
    # 定义一个新的 f
    def new_f(self: A, x):
        print(x + 1)

    A.f = new_f  # 将新函数赋值给类
    a.f(x)  # 2
    ```
- 如果是将新函数赋值给**类的实例**, 那么需要就需要去掉第一个位置的参数;
    ```python
    # 定义一个新的 f
    def new_f(x):
        print(x + 1)

    a.f = new_f  # 将新函数赋值给类的实例
    a.f(x)  # 2
    ```


## 参考
- [【python】class里定义的函数是怎么变成方法的? 函数里的self有什么特殊意义么? _哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1pa411e7tQ)
