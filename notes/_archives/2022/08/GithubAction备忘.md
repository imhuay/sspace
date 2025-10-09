Github Action 备忘
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-08-xx&labelColor=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-29%2003%3A21%3A55&labelColor=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden_in_recent: false
tags: [tool]
-->

> ***Keywords**: GithubAction备忘*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [工作流程语法](#工作流程语法)
    - [触发器 - `on`](#触发器---on)
    - [作业 - `jobs`](#作业---jobs)
        - [条件执行 - `jobs.<job_id>.if`](#条件执行---jobsjob_idif)
        - [矩阵策略 - `jobs.<job_id>.strategy.matrix`](#矩阵策略---jobsjob_idstrategymatrix)
        - [复用流程 - `jobs.<job_id>.uses`](#复用流程---jobsjob_iduses)
        - [依赖执行](#依赖执行)
- [其他事项](#其他事项)
    - [添加 Actions secrets](#添加-actions-secrets)
    - [添加工作流状态徽章](#添加工作流状态徽章)
- [GitHub Action 推荐](#github-action-推荐)
<!--END_SECTION:toc-->

---

> 官方文档: [Workflows - GitHub Docs](https://docs.github.com/cn/actions/using-workflows)

## 工作流程语法
> [GitHub Actions 的工作流程语法](https://docs.github.com/cn/actions/using-workflows/workflow-syntax-for-github-actions)

**示例**
```yaml
name: learn-github-actions  # (可选) 将出现在 GitHub 仓库的 Actions 选项卡中的工作流程名称.

# 触发器
on: [push]  # 指定此工作流程的触发器, 更多细节: https://docs.github.com/cn/actions/using-workflows/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore

# 作业
jobs:  # 该工作流的所有作业

  check-bats-version:  # 子作业的名称 (自定义)
    runs-on: ubuntu-latest  # 该作业运行的环境, 更多细节: https://docs.github.com/cn/actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on
    steps:  # 该子作业的所有步骤
      - name: Checkout repository  # 该步骤的名称
        uses: actions/checkout@v3  # 复用 https://github.com/actions/checkout/tree/v3
      - name: Setup nodejs
        uses: actions/setup-node@v3  # 复用 https://github.com/actions/setup-node/tree/v3
        with:  # 附加选项
          node-version: '14'  # 设定 node 的版本
      - name: Install bats  
        run: |
          npm install -g bats  # run 指示作业在运行器上执行命令
          bats -v

  build:  # 子作业
    runs-on: ubuntu-latest
    # 策略矩阵: 通过创建变量来自动构建基于变量组合的多个作业
    strategy:
      matrix:  
        node: [12, 14, 16]
    steps:
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node }}

  setup:  # 子作业
    runs-on: ubuntu-latest
    # 自作业之间默认是并行执行的, 可以通过 needs 来指定依赖, 更多细节: https://docs.github.com/cn/actions/using-jobs/using-jobs-in-a-workflow#defining-prerequisite-jobs
    needs: build  # 依赖 build 作业
    steps:
      - run: ./build_server.sh  # 相对于仓库主目录
```

### 触发器 - `on`
> [`on`](https://docs.github.com/cn/actions/using-workflows/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore)

```yaml
on:
  # 在 push 时被触发
  push:
    branches:
      - '**'  # 任意分支
      - 'releases/**-alpha'
      - '!releases/**'  # 所有 releases/** 都不触发, 除了 releases/**-alpha

  # 使该 workflow 依赖于其他 workflow 触发
  workflow_run:
    workflows: [ "Build" ]  # 当名为 Build 的 workflow 在满足以下条件的分支上执行时, 本 workflow 才会被执行
    types: [ requested ]  # requested/completed
    branches:
      - 'releases/**'
      - '!releases/**-alpha'

  # 使该 workflow 能被其他 workflow 调用
  workflow_call:

  # 使该 workflow 能在 GitHub 上手动触发
  workflow_dispatch:

  # 执行 release 时触发 (GitHub 项目页)
  release:
    types: [ published ]  # published/created/edited/deleted/...

  # 定时触发
  schedule:
    - cron: '0 0 * * *'  # cron 语法, UTC 时间, +08:00 即北京时间
```

> 关于各触发事件的可选项(`types`): [Events that trigger workflows - GitHub Docs](https://docs.github.com/cn/actions/using-workflows/events-that-trigger-workflows#available-events)


### 作业 - `jobs`
> [`jobs`](https://docs.github.com/cn/actions/using-workflows/workflow-syntax-for-github-actions#jobs)

#### 条件执行 - `jobs.<job_id>.if`
> [`jobs.<job_id>.if`](https://docs.github.com/cn/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idif)

```yaml
steps:
- name: Install dependencies on Windows
  if: matrix.os == 'windows-latest'
  run: |
    python -m pip install --upgrade pip
    python -m pip install flake8 pytest coverage
    if (Test-Path -Path 'requirements.txt' -PathType Leaf) {pip install -r requirements.txt}
```

#### 矩阵策略 - `jobs.<job_id>.strategy.matrix`
> [`jobs.<job_id>.strategy.matrix`](https://docs.github.com/cn/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstrategymatrix)

```yaml
strategy:
  fail-fast: false  # 当矩阵中有任何一个作业失败时, 是否停止其他所有作业, 默认为 true, 建议设为 false
  matrix:
    python-version: ["3.7", "3.8", "3.9", "3.10"]
    os: [ubuntu-latest, macos-latest, windows-latest]
```

#### 复用流程 - `jobs.<job_id>.uses`
> [`jobs.<job_id>.uses`](https://docs.github.com/cn/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_iduses)

- 复用的流程来自于其他仓库;
    -
- **不能跟 `run` 同时使用**;
- 两类复用:
    - 其他 workflow 文件
    - 其他 GitHub Actions 仓库
        - 官方仓库: [GitHub Actions](https://github.com/actions)
        - GitHub 市场: https://github.com/marketplace?type=actions

```yaml
steps:
- name: Checkout
  uses: actions/checkout@v3  # 仓库
- name: Build
  uses: ./.github/workflows/build.yml  # 文件
```

#### 依赖执行

- 默认各 workflow, 以及 workflow 内的各 job 都是并发执行的;
- 使用 `on.workflow_run` 触发器添加 workflow 之间的依赖
- 使用 `jobs.<job_id>.needs` 添加 job 之间的依赖

```yml
on:
  workflow_run:
    workflows: [ "Build" ]  # 当名为 Build 的 workflow 完成时
    types: [ completed ]

jobs:
  build:
    # ...
  publish:  # 依赖 build 完成时
    needs: build
```

## 其他事项

### 添加 Actions secrets
> 仓库主页 -> Settings -> Secrets -> Actions -> New repository secret

示例: 在工作流文件中引用
```yaml
steps:
- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    token: ${{ secrets.CODECOV_TOKEN }}
```

### 添加工作流状态徽章
> [Adding a workflow status badge - GitHub Docs](https://docs.github.com/cn/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)

![workflow](https://github.com/imhuay/space/actions/workflows/daily.yml/badge.svg?branch=master)
```txt
![workflow](https://github.com/<user>/<repo>/actions/workflows/$file_name.yml/badge.svg?branch=master)
```

## GitHub Action 推荐

- [yi-Xu-0100/traffic-to-badge: 📊 The GitHub action that using repositories Insights/traffic data to generate badges that include views and clones.](https://github.com/yi-Xu-0100/traffic-to-badge)
    > 生成仓库的访问量
- [athul/waka-readme: Wakatime Weekly Metrics on your Profile Readme.](https://github.com/athul/waka-readme)
    > 添加 Wakatime 信息
- [gautamkrishnar/blog-post-workflow: Show your latest blog posts from any sources or StackOverflow activity or Youtube Videos on your GitHub profile/project readme automatically using the RSS feed](https://github.com/gautamkrishnar/blog-post-workflow)
    > 添加 blog-post
