#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-10-21 13:49:23
Author:
    huayang (imhuay@163.com)
Subject:
    test_qa_section
References:
    None
"""

from __future__ import annotations

import sys
from pathlib import Path

from markdown_it import MarkdownIt

sys.path.append(str(Path(__file__).parent.parent))
from sections.qa_section import QaSection

_test_content = r"""
<!--qa_info
use_section_number: true
-->
## Q&A

<!--START_SECTION:qa_toc-->
<!--END_SECTION:qa_toc-->

<!-- omit in toc -->
### 1. 问题 1
> 在轨迹采样过程收收集奖励信号, 然后在策略优化时与策略模型一起训练;

- ...

<!-- omit in toc -->
#### 1.1. 333问题 1.1
> ...

### 3. 问题 2

#### 4.1. 问题 2.1

"""


def _test():
    """"""
    qa_section = QaSection(Path(), _test_content)

    print(qa_section.get_toc())
    print()
    print(qa_section.new_content)


if __name__ == '__main__':
    """"""
    _test()