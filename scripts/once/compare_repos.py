#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-09-30 20:41:13
Author:
    huayang (imhuay@163.com)
Subject:
    This script compares files between two repository directories without relying on Git internals.

    Why:
        In some cases, the .git/objects directory of an old repository may be corrupted, making Git commands
        such as git diff or git log unusable. However, the source files themselves may still exist. To
        identify modifications in the old repository relative to a newly cloned clean repository, a
        standalone file-level comparison tool is required.

    Functions:
    - Traverse both repository directories while excluding specified directories (e.g., .git, .venv, __pycache__).
    - Detect files that exist in both repositories but differ in content.
    - Detect files that exist only in the old repository or only in the new repository.
    - Print results to facilitate manual inspection and migration of changes.

    Usage:
        Use this script when a Git repository is corrupted and direct Git commands cannot be used, but you
        still need to manually synchronize modifications from the old repository to a new clean repository.
References:
    Copilot
"""

from __future__ import annotations

import filecmp
import os


def collect_files(root, exclude_dirs=None):
    """收集 root 下所有文件路径，排除 exclude_dirs 中的目录"""
    if exclude_dirs is None:
        exclude_dirs = []

    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # 过滤掉需要排除的目录
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        for f in filenames:
            files.append(os.path.relpath(os.path.join(dirpath, f), root))
    return set(files)


def main(old_repo, new_repo, exclude_dirs=None):
    old_files = collect_files(old_repo, exclude_dirs)
    new_files = collect_files(new_repo, exclude_dirs)

    # 两边都存在的文件
    common_files = old_files & new_files
    # 只在旧仓库存在
    only_in_old = old_files - new_files
    # 只在新仓库存在
    only_in_new = new_files - old_files

    diff_files = []
    for f in common_files:
        old_path = os.path.join(old_repo, f)
        new_path = os.path.join(new_repo, f)
        if not filecmp.cmp(old_path, new_path, shallow=False):
            diff_files.append(f)

    print('=== 差异文件 ===')
    for f in diff_files:
        print(f)

    print('\n=== 仅在旧仓库存在 ===')
    for f in only_in_old:
        print(f)

    print('\n=== 仅在新仓库存在 ===')
    for f in only_in_new:
        print(f)


if __name__ == '__main__':
    # 修改为你的路径
    old_repo_path = '/home/huay/workspace/git/my/sspace_git_break/'
    new_repo_path = '/home/huay/workspace/git/my/sspace'
    # 自定义需要排除的目录
    exclude = ['.git', '.venv', '.idea', '__pycache__']

    main(old_repo_path, new_repo_path, exclude_dirs=exclude)
