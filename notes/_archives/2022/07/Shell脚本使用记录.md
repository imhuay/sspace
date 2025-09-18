Shell 脚本备忘
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-07-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-03%2022%3A42%3A16&label_color=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
top: false
draft: true
hidden: true
tags: [linux]
-->

> ***Keywords**: Linux, Shell*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [Tips](#tips)
    - [不使用 sh 命令, 直接运行 shell 脚本的方法](#不使用-sh-命令直接运行-shell-脚本的方法)
<!--END_SECTION:toc-->

---

## Tips

### 不使用 sh 命令, 直接运行 shell 脚本的方法
> [How do I run a shell script without using "sh" or "bash" commands? - Stack Overflow](https://stackoverflow.com/questions/8779951/how-do-i-run-a-shell-script-without-using-sh-or-bash-commands)

1. 在脚本开始添加 `#!/bin/bash`;
2. 执行 `chmod u+x $script_path`;
3. (可选) 添加环境变量, 使脚本全局可用, `export PATH=$PATH:$script_directory`;
    > 如果不行添加, 可以把脚本保存到 `/usr/local/bin`;
