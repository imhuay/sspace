#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-10-21 14:41:08
Author:
    huayang (imhuay@163.com)
Subject:
    qa_section
References:
    None
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import ClassVar

import yaml
from markdown_it import MarkdownIt
from markdown_it.token import Token
from regex import P
from utils import MarkdownUtils, NoteUtils

_md = MarkdownIt()


subject_level = [
    'Transformer',
    'RLHF',
    'SFT',
    'LLM',
    'Agent',
]


@dataclass
class TocLine:
    """"""

    title: str
    level: int
    section_number: str = ''

    def __post_init__(self):
        if self.section_number:
            self.title = f'{self.section_number} {self.title}'

    @property
    def slug_title(self):
        """"""
        return MarkdownUtils.slugify(self.title)

    @property
    def default_url(self):
        """"""
        return f'#{self.slug_title}'

    def get_toc_line(self, prefix: str | Path = ''):
        indent_prefix = '    ' * self.level
        return f'{indent_prefix}- [{self.title}]({prefix}{self.default_url})'


@dataclass
class QaSectionInfo:
    subject: str = ''
    subject_level: int = 0
    topic: str = ''
    topic_level: int = 0
    with_section_title: bool = True
    use_section_number: bool = True


@dataclass
class QaSection:
    """"""

    content: str
    md_path: Path
    md_toc_title: str = ''
    section_title: str = ''
    toc_lines: list[TocLine] = field(default_factory=list)
    max_section_level: int = 5
    min_section_level: int = 2
    info: QaSectionInfo = field(default_factory=QaSectionInfo)
    _tokens: list[Token] = field(default_factory=list)

    def __post_init__(self):
        """"""
        self._tokens = _md.parse(self.content)
        self._parse_info()
        self._set_section_title()

        if self.info.use_section_number:
            self.content = MarkdownUtils.update_section_number(
                self.content,
                min_section_level=self.min_section_level,
                max_section_level=self.max_section_level,
            )

        self._parse_toc_lines()

    SECTION_KEY: ClassVar[str] = 'qa'
    _TOC_SECTION_KEY: ClassVar[str] = 'qa_toc'
    _INFO_KEY: ClassVar[str] = 'qa_info'

    def _set_section_title(self):
        """"""
        if not self.info.with_section_title:
            return

        is_heading = False
        for t in self._tokens:
            if t.type == 'heading_open':
                self.min_section_level = int(t.tag[1:]) + 1
                is_heading = True
            elif t.type == 'heading_close':
                is_heading = False
            elif is_heading and t.type == 'inline':
                self.section_title = t.content
                break

        assert self.section_title

    def _parse_info(self):
        """"""
        for t in self._tokens:
            if t.type == 'html_block' and self._INFO_KEY in t.content:
                info_str = NoteUtils.get_annotation(self._INFO_KEY, t.content)
                info_str = '\n'.join([ln.lstrip() for ln in info_str.split('\n')]) if info_str else ''
                _info = yaml.safe_load(info_str) if info_str else {}
                self.info = QaSectionInfo(**_info)
                break

    def _parse_toc_lines(self):
        """"""
        lines = self.content.split('\n')
        toc_lines = self.toc_lines
        
        re_line = re.compile(r'^(#+)\s*(\d+(\.\d+)*\.)\s*(.*)$')
        for line in lines:
            m = re_line.match(line)
            if not m:
                continue

            hashes, section_number, _, title = m.groups()
            toc_line = TocLine(title=title, level=len(hashes), section_number=section_number)
            toc_lines.append(toc_line)

    @property
    def toc_title(self):
        """"""
        toc_title = f'**{self.topic.strip("*").strip()}**'
        if self.subject:
            toc_title = f'{self.subject} · ' + toc_title

        if self.qa_count > 0:
            toc_title += f' · `{self.qa_count}`'

        return toc_title.strip()

    @property
    def subject_toc_line(self):
        return f'- [{self.toc_title}](#{MarkdownUtils.slugify(self.toc_title)})'

    def get_toc(self, prefix: str | Path = '', with_subject_title: bool = False, head_level: int = 2):
        """"""
        if prefix:
            assert Path(prefix).suffix == '.md'

        lines = []
        for ln in self.toc_lines:
            lines.append(ln.get_toc_line(prefix))

        lines = MarkdownUtils.remove_min_prefix_spaces(lines)
        toc = '\n'.join(lines)
        if with_subject_title:
            return f'{"#" * head_level} {self.toc_title}<!-- {self.subject_level} -->\n\n{toc}'

        return toc

    @property
    def new_content(self) -> str:
        new_content = NoteUtils.replace_section_content(self._TOC_SECTION_KEY, self.content, self.get_toc())
        return new_content

    @property
    def sort_key(self):
        return (-self.info.subject_level, self.info.subject, -self.info.topic_level)

    @property
    def subject(self) -> str:
        return self.info.subject

    @property
    def top_subject(self) -> str:
        return self.info.subject.split(' · ')[0]

    @property
    def qa_count(self) -> int:
        # 有 🏷️ 标签的行不是具体问题
        return len(self.toc_lines) - sum('🏷️' in ln.title for ln in self.toc_lines)

    @property
    def subject_level(self):
        return self.info.subject_level

    @property
    def topic(self):
        return self.info.topic or self.md_toc_title.replace('**', '')
