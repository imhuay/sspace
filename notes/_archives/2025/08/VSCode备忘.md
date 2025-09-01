VSCode 备忘
===
<!--START_SECTION:badge-->

![create date](https://img.shields.io/static/v1?label=create%20date&message=2025-08-08&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-29%2003%3A21%3A55&label_color=gray&color=thistle&style=flat-square)

<!--END_SECTION:badge-->
<!--info
date: 2025-08-08 16:26:03
top: false
draft: false
hidden: false
level: 0
tag: [tool]
-->

> ***Keywords**: VSCode备忘*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [Python 配置](#python-配置)
- [插件](#插件)
    - [AI 代码补全(内联)](#ai-代码补全内联)
<!--END_SECTION:toc-->

---

## Python 配置
> [VSCode配置 for Python](VSCode配置-Python.md)

## 插件

### AI 代码补全(内联)

- Cline 不支持或者我没发现
    - Roo Code 不支持或者我没发现 (基于 Cline)
- Continue 支持
    - 测试了 基于 DeepSeek 的效果; 
    - 首先 DeepSeek 默认不会开启内联补全, 需要手动配置 `%USERPROFILE%\.continue\config.yaml` (Win);
    - API 模式下的自动补全效果很差, 速度慢, 单次补全内容少且不完整, 跟 Copilot 差距很大; 可能本地部署会好一些, 但没尝试;
    ```yaml
    name: Local Assistant
    version: 1.0.0
    schema: v1
    models:
    - name: DeepSeek Coder
        provider: deepseek
        model: deepseek-coder
        apiKey: sk-***
        # 需要补充以下内容
        roles:
        - autocomplete  # 核心是添加这行使 DeepSeek 支持自动补全; 默认只支持以下 4 种场景;
        - chat
        - edit
        - apply
        - rerank
    context:
    - provider: code
    - provider: docs
    - provider: diff
    - provider: terminal
    - provider: problems
    - provider: folder
    - provider: codebase
    ``` 
