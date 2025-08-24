`git` 备忘
===
<!--START_SECTION:badge-->

![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-06-xx&label_color=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-08-08%2020%3A00%3A40&label_color=gray&color=thistle&style=flat-square)

<!--END_SECTION:badge-->
<!--info
top: false
draft: true
hidden: true
level: 1
tag: [git]
-->

> ***Keywords**: git*

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [常见错误](#常见错误)
- [基本命令](#基本命令)
    - [删除分支](#删除分支)
    - [推送](#推送)
    - [拉取](#拉取)
    - [强制覆盖本地](#强制覆盖本地)
    - [撤回上次 commit](#撤回上次-commit)
    - [删除已提交文件/文件夹](#删除已提交文件文件夹)
    - [恢复已删除的文件](#恢复已删除的文件)
    - [`fork` 后同步源仓库](#fork-后同步源仓库)
- [`ssh-keygen` 基本用法](#ssh-keygen-基本用法)
- [修改 commit 的 author 信息](#修改-commit-的-author-信息)
- [常用统计](#常用统计)
    - [统计 commit 次数](#统计-commit-次数)
<!--END_SECTION:toc-->

---
> 官方文档：https://git-scm.com/book/zh

## 常见错误

## 基本命令
```shell
# 初始化，新建本地仓库时使用
git init

# 暂存
git add <path>  # 暂存具体文件/文件夹
git add .   # 暂存新文件和被修改的文件，不包括删除的文件
git add -u  # --update，暂存已追踪的文件，即被修改的文件和被删除的文件
git add -A  # --all，全部暂存

# 提交
git commit -m <'提交信息'>
```

### 删除分支
```
# 删除本地分支（需 merge）
git branch -d [分支名]

# 删除本地分支（不需要 merge）
git branch -D [分支名]

# 删除远程分支
git push origin --delete [分支名]
```

### 推送
```sh
# 推送本地分支到远程分支
$ git push <远程主机名/别名> <本地分支名:远程分支名>
# 如果本地分支名与远程分支名相同，则可以省略冒号
$ git push <远程主机名/别名> <本地分支名>

# 将本地的 master 分支推送到 origin 主机的 master 分支
$ git push origin master:master
$ git push origin master  # 同上

# 强制推送
$ git push --force origin master

# 删除远程的 test 分支
git push origin --delete test
```

### 拉取
- `git pull` 是 `git fetch` 和 `git merge FETCH_HEAD` 的简写；

**常用**
```sh
# 完整格式
git pull <远程主机名/别名> <远程分支名:本地分支名>

# 更新
$ git pull
$ git pull origin  # 同上，远程主机默认的别名是 origin

# 将远程主机 origin 的 master 分支拉取过来，与本地的 brantest 分支合并
$ git pull origin master:brantest

# 如果远程分支是与当前分支合并，则冒号后面的部分可以省略
git pull origin master
```

### 强制覆盖本地
使用本命令后，每次拉取，都会生成一次 commit，**慎用**
```sh
git pull --force --strategy recursive -Xtheirs --allow-unrelated-histories
```

### 撤回上次 commit
```
git reset --soft HEAD~1 
-- 撤回最近一次的commit（撤销commit，不撤销git add）

git reset --mixed HEAD~1 
-- 撤回最近一次的commit（撤销commit，撤销git add）

git reset --hard HEAD~1 
-- 撤回最近一次的commit（撤销commit，撤销git add，还原改动的代码）
```

### 删除已提交文件/文件夹
```
# 删除暂存区或分支上的文件，但是工作区还需要这个文件，后续会添加到 .gitignore
# 文件变为未跟踪的状态
git rm --cache <filepath>
git rm -r --cache <dirpath>


# 删除暂存区或分支上的文件，工作区也不需要这个文件
git rm <filepath>
git rm -r <dirpath>


# 不显示移除的文件，当文件夹中文件太多时使用
git rm -r -q --cache <dirpath>
```

### 恢复已删除的文件

**方法 1**：记得文件名
```shell
# 查看删除文件的 commit_id
git log -- [file]

# 恢复文件
git checkout commit_id [file]
```

### `fork` 后同步源仓库

**`rebase` 方案**
- 适用于双方冲突较少的情况;
```bash
# 添加上游仓库远程
git remote add upstream 原仓库的URL

# 获取上游仓库最新更改
git fetch upstream

# rebase
git rebase -i upstream/master

# 解决冲突

# push: 由于历史记录已更改，需要强制推送
git push -f
```

**`merge` 方案**
- 适用于双方冲突较少的情况, 只需要解决一次冲突, 但会在历史记录中创建一个合并提交;
```bash
# 添加上游仓库远程
git remote add upstream 原仓库的URL

# 获取上游仓库最新更改
git fetch upstream

# merge
git merge upstream/master

# 解决冲突

# push
git add .
git commit -m "Sync upstream"
git push
```


## `ssh-keygen` 基本用法
- ssh key 是远程仓库识别用户身份的依据；
- 如果是通过 ssh 与远程仓库交互，第一次在本机执行 git 时需要先生成 ssh key，然后将**公钥**添加到远程仓库中；
    ```shell
    # 生成 ssh key
    ssh-keygen -t rsa
    # 或
    ssh-keygen -t rsa -C "邮箱地址"

    # 之后需要确认三次
    ## 第一次确认密钥的存储位置（默认是 ~/.ssh/id_rsa），可以 Enter 跳过
    ## 后两次确认密钥口令，默认留空，可以 Enter 跳过

    # 最后查看生成的密钥，添加到远程仓库
    cat ~/.ssh/id_rsa.pub
    ```

## 修改 commit 的 author 信息
> 如何修改git commit的author信息 - 咸咸海风 - 博客园 | https://www.cnblogs.com/651434092qq/p/11015901.html


## 常用统计

### 统计 commit 次数

**总次数**
```sh
$ git log | grep '^commit ' | awk '{print $1}' | uniq -c | awk '{print $1}'
# 10
```

**每个人提交的次数，并排序**
> [git查看commit提交次数和代码量-CSDN博客](https://blog.csdn.net/cyf15238622067/article/details/82980782)
```sh
git log | grep "^Author: " | awk '{print $2}' | sort | uniq -c | sort -k1,1nr
# 10 aa
# 8 bb
```
