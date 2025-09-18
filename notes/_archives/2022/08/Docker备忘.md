Docker 备忘
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-08-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-29%2003%3A21%3A55&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
top: false
draft: false
hidden: false
tags: [tool]
-->

> ***Keywords**: Docker*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [常用命令](#常用命令)
    - [启动容器](#启动容器)
- [配置镜像加速](#配置镜像加速)
- [参考](#参考)
<!--END_SECTION:toc-->

---

## 常用命令

### 启动容器
```shell
$ docker run -it $name /bin/bash
## -it: 等价于 -i -t, 表示以交互方式运行并附加到当前终端
## $name: 容器名
## /bin/bash: 容器启动后, 执行该命令, 表示在容器内开启一个 bash
```


## 配置镜像加速
- 在客户端设置中找到 `Docker Engine`, 或者打开 `~/.docker/daemon.json`;
- 在最上层添加 `registry-mirrors` 配置:
    ```json
    {
        "builder": {
            "gc": {
            "defaultKeepStorage": "20GB",
            "enabled": true
            }
        },
        "experimental": false,
        "features": {
            "buildkit": true
        },
        "registry-mirrors": [
            "https://hub-mirror.c.163.com",
            "https://mirror.baidubce.com"
        ]
    }
    ```
- [阿里云镜像加速](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)


## 参考
- [Docker 官方文档](https://docs.docker.com/)