VSCode 配置 for Python
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-08-05&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-03%2022%3A42%3A16&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
date: 2025-08-05 13:36:02
top: false
draft: false
hidden: true
level: 0
tags: [python_tool]
-->

> ***Keywords**: python_tool*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [基础](#基础)
    - [Linter](#linter)
    - [Formatter](#formatter)
- [插件](#插件)
    - [Python](#python)
    - [Ruff](#ruff)
    - [](#)
<!--END_SECTION:toc-->

---

## 基础

- **官方**: [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)


### Linter
> [Linting Python in Visual Studio Code](https://code.visualstudio.com/docs/python/linting)

- **作用**: 静态检查工具 - 代码错误, 风格规范, 安全隐患等
- 候选:
    -
- 我使用的: [Ruff - Astral Software](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- 候选:
    - [Pylint | Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)
    - [flake8 | Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)
    - [mypy | Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker)
    - [Ruff | Astral Software](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) **(我使用的)**
    - [Mypy - Matan Gover](https://marketplace.visualstudio.com/items?itemName=matangover.mypy)

### Formatter
> [Formatting Python in VS Code](https://code.visualstudio.com/docs/python/formatting#_choose-a-formatter)

- **作用**: 格式化代码
- **候选**
    - [autopep8 | Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8)
    - [Black Formatter - Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
    - [Ruff - Astral Software](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) **(我使用的)**
        > Ruff 可以代替 Black + isort, 但是在可定制化方面不如 autopep8
    - [yapf - EeyoreLee](https://marketplace.visualstudio.com/items?itemName=eeyore.yapf)
    - [isort - Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
        > 仅优化 import


## 插件

### Python
> [Python - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

**作用**
- 自动补全 (Autocomplete)
- 智能提示 (IntelliSense)
- 自动导入 (Auto-Import)

**附带插件**
- [Pylance - 类型检查](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Python Debugger - 调试](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)


### Ruff
> [Ruff - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

- **作用**: Linter + Formatter
- **Github**: [astral-sh/ruff-vscode: A Visual Studio Code extension with support for the Ruff linter.](https://github.com/astral-sh/ruff-vscode?tab=readme-ov-file)
- **配置**
    - lint: [`lint` Settings | Ruff](https://docs.astral.sh/ruff/settings/#lint)
    - format: [`format` Settings | Ruff](https://docs.astral.sh/ruff/settings/#format)

        ```json
        "[python]": {
            "editor.formatOnSave": true,
            "editor.codeActionsOnSave": {
                "source.fixAll": "always",
                "source.organizeImports": "explicit"
            },
            "editor.defaultFormatter": "charliermarsh.ruff"
        },
        "ruff.nativeServer": "on",
        "ruff.configuration": {
            "line-length": 120,
            "format": {
                // ref: https://docs.astral.sh/ruff/settings/#format
                "docstring-code-format": true,
                "docstring-code-line-length": 100,
                "exclude": [ // file path
                ],
                "indent-style": "space",
                "line-ending": "native",
                "quote-style": "single",
                "skip-magic-trailing-comma": false,
                "preview": false
            },
            "lint": {
                "ignore": [
                    "F401", // imported but unused
                ]
            }
        }
        ```


###