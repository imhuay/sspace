`uv` 备忘
===
<!--START_SECTION:badge-->

![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-06%2023%3A10%3A23&color=yellowgreen&style=flat-square)

<!--END_SECTION:badge-->
<!--info
date: 2025-08-05 01:38:20
top: false
draft: true
hidden: false
level: 0
tag: [python_tool]
-->

> ***Keywords**: python_tool*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [背景](#背景)
- [基础命令](#基础命令)
    - [换源](#换源)
    - [依赖管理](#依赖管理)
        - [源代码依赖](#源代码依赖)
<!--END_SECTION:toc-->

---

## 背景

记录 `uv` 的使用

- **官方文档**: [uv](https://docs.astral.sh/uv/)
    - **包管理**: [Managing dependencies | uv](https://docs.astral.sh/uv/concepts/projects/dependencies/#adding-dependencies)
    - **包发布**: [Building distributions | uv](https://docs.astral.sh/uv/concepts/projects/build/)
- **Github**: [astral-sh/uv: An extremely fast Python package and project manager, written in Rust.](https://github.com/astral-sh/uv)


## 基础命令

```bash
# 初始化
uv init 
    --name [name]
    --package               # Set up the project as a Python package
    --bare                  # Only create a `pyproject.toml`
    --python [py_version]   # Specify python version

# Python package 初始化结构
## 在使用 uv 第一次运行后(如 uv add/run/sync/lock), 会自动添加 .venv 和 uv.lock
.
├── .git/
├── .gitignore
├── .python-version
├── .venv/
├── README.md
├── pyproject.toml
├── src
│   └── [name]/
│       └── __init__.py
└── uv.lock
```

- `uv.lock`: `uv` 生成的锁文件, 其核心作用是确保 Python 项目的依赖安装具有确定性和可复现性; 该文件由 `uv` 管理, 不需要手动操作;

### 换源
```toml
# pyproject.toml
[tool.uv]
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple"
```

### 依赖管理
> [Managing dependencies | uv](https://docs.astral.sh/uv/concepts/projects/dependencies/)
```bash
# 添加依赖
uv add [package]

    # Specify a version constraint
    uv add 'requests==2.31.0'

    # Add a git dependency
    uv add git+https://github.com/psf/requests
    
    # Add all dependencies from `requirements.txt`.
    uv add -r requirements.txt

    # 修改依赖版本
    uv add "httpx>0.1.0"

    # 本地版本
    uv add "httpx @ ../httpx"

    # 其他用法
    uv add "jax; sys_platform == 'linux'"
    uv add "numpy; python_version >= '3.11'"
    uv add "tqdm>=4.66.2,<5"

# 移除依赖
uv remove [package]

# 同步环境
## 生成 .venv, 并同步 pyproject.toml 中的依赖
# rm .venv
uv sync
```

#### 源代码依赖
> [Dependency sources | uv](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-sources)

```bash
# Index: add package from a specific index
uv add torch --index pytorch=https://download.pytorch.org/whl/cpu

# Git: add a git dependency source
## Install over HTTP(S).
uv add git+https://github.com/encode/httpx
## Install over SSH.
uv add git+ssh://git@github.com/encode/httpx
## Specific Git references
### tag
uv add git+https://github.com/encode/httpx --tag 0.27.0
### branch
uv add git+https://github.com/encode/httpx --branch main
### commit
uv add git+https://github.com/encode/httpx --rev 326b9431c761e1ef1e00b9f760d1f654c8db48c6
### subdirectory
uv add git+https://github.com/langchain-ai/langchain#subdirectory=libs/langchain

# URL: add a URL source
uv add "https://files.pythonhosted.org/packages/5c/2d/3da5bdf4408b8b2800061c339f240c1802f2e82d55e50bd39c5a881f47f0/httpx-0.27.0.tar.gz"

# Path: add a path source
uv add /example/foo-0.1.0-py3-none-any.whl
## relative path
uv add ./foo-0.1.0-py3-none-any.whl
## directory
uv add ~/projects/bar/
## editable installation
uv add --editable ../projects/bar/

# Workspace
## 详见: https://docs.astral.sh/uv/concepts/projects/workspaces/
```