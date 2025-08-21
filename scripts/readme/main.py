#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2022-08-22 20:14
Author:
    huayang (imhuay@163.com)
Subject:
    build_readme
"""

# try:
#     sys.path.insert(0, f'{Path(__file__).parent.parent / "src"}')
#     from huaytools.utils import get_logger
# except:  # noqa
#     exit(1)

from build import BuildReadme

from huaytools.utils import get_logger, is_wsl

logger = get_logger()

if __name__ == '__main__':
    """"""
    br = BuildReadme()
    br.build()
    if not is_wsl():
        br.git_push()
    logger.info('Update Success!')
