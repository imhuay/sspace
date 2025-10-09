Node.js 环境搭建
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-12-xx&labelColor=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
top: false
hidden_in_recent: false
-->

<!-- TOC -->
- [安装 Node.js](#安装-nodejs)
    - [通过 nvm 安装 (推荐)](#通过-nvm-安装-推荐)
        - [为项目配置默认 node](#为项目配置默认-node)
        - [其他版本管理器](#其他版本管理器)
    - [从源码安装](#从源码安装)
- [`npm` 配置](#npm-配置)
    - [配置国内源](#配置国内源)
    - [配置 `npm` 安装目录 (可选)](#配置-npm-安装目录-可选)
    - [安装 `n` 管理器 (可选)](#安装-n-管理器-可选)
<!-- TOC -->

## 安装 Node.js

### 通过 nvm 安装 (推荐)
> 推荐, 使用 nvm 安装的 Node.js 和 npm, 不需要使用 sudo 命令来安装新包.
>> - [在 WSL 2 上设置 Node.js | Microsoft Learn](https://learn.microsoft.com/zh-cn/windows/dev-environment/javascript/nodejs-on-wsl#install-nvm-nodejs-and-npm)  
>> - [nvm-sh/nvm - GitHub](https://github.com/nvm-sh/nvm)

```sh
# 安装 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash

# 卸载 nvm
# rm -rf $NVM_DIR
# 并删除 ~/.bashrc 中相关变量

# 验证 nvm (若失败需重启终端)
nvm -h

# 配置国内源原 (可选)
# vim ~/.bashrc
export NVM_NODEJS_ORG_MIRROR=https://npm.taobao.org/mirrors/node
export NVM_IOJS_ORG_MIRROR=https://npm.taobao.org/mirrors/iojs

# 安装当前版本
nvm install node
# 安装最新的 LTS 版
nvm install --lts
# 安装 14.x lst
nvm install 14 --lst

# 查看已安装的 node 版本
nvm ls

# 选择需要的版本 (只在当前 shell 生效)
nvm use 14

# 设置默认 node (新 shell 也生效)
nvm alias default lts/*
```

#### 为项目配置默认 node
> [.nvmrc - nvm-sh/nvm](https://github.com/nvm-sh/nvm#nvmrc)

- 配置 `.nvmrc`
    ```sh
    mkdir -p ~/tmp/node_project
    cd ~/tmp/node_project
    echo "14" > .nvmrc
    nvm use  # 手动调用
    ```
- 进入文件夹时自动调用 `nvm use`
    > https://github.com/nvm-sh/nvm#deeper-shell-integration


#### 其他版本管理器
> [替代版本管理器 | Microsoft Learn](https://learn.microsoft.com/zh-cn/windows/dev-environment/javascript/nodejs-on-wsl#alternative-version-managers)
>> 这里提到的 [`n` 管理器](#安装-n-管理器-可选)比较特殊, 它需要先安装 node 和 npm 后才可以使用;  
>> 其他管理器都是类似 nvm 的用法;

- [Schniz/fnm: 🚀 Fast and simple Node.js version manager, built in Rust](https://github.com/Schniz/fnm#using-a-script)
- [volta-cli/volta: Volta: JS Toolchains as Code. ⚡](https://github.com/volta-cli/volta#installing-volta)
- [jasongin/nvs: Node Version Switcher - A cross-platform tool for switching between versions and forks of Node.js](https://github.com/jasongin/nvs)

### 从源码安装
> https://github.com/nodesource/distributions/blob/master/README.md#installation-instructions
>> 不推荐, 需要 `sudo`

```sh
# 安装 nodejs (18.x)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# 卸载
# sudo apt-get remove -y nodejs
```

## `npm` 配置

### 配置国内源
> [设置npm源的几种方式 - SNYang - 博客园](https://www.cnblogs.com/steven-yang/p/12317646.html)
```sh
npm config set registry https://registry.npm.taobao.org/
```

### 配置 `npm` 安装目录 (可选)
> 如果从源码安装, 可以避免使用 `sudo` 来安装包  
> 如果从 nvm 安装, 会提示冲突

```sh
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'  # 生成 ~/.npmrc 文件

# 添加环境变量
export PATH=~/.npm-global/bin:$PATH
```

### 安装 `n` 管理器 (可选)
> 基于 npm 的版本管理器
>> [n - npm](https://www.npmjs.com/package/n)

```sh
# 安装 n 模块
npm install -g n

# 配置安装目录, 避免 sudo (默认安装在 /usr/local/n)
mkdir -p $HOME/.n
# vim ~/.bashrc
export N_PREFIX=$HOME/.n
export PATH=$N_PREFIX/bin:$PATH
```
