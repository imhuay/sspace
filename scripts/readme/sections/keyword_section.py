#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-10-25 18:22:16
Author:
    huayang (imhuay@163.com)
Subject:
    keyword_section
References:
    None
"""

from __future__ import annotations

from dataclasses import dataclass, field

import yaml
from utils import MarkdownUtils, NoteUtils, _md


@dataclass
class KeywordSectionInfo:
    """"""
    name: str = ''
    extra_url: bool = False
    with_keywords: bool = True


@dataclass
class KeywordSection:
    """"""

    content: str
    head_name: str = ''
    url: str = ''
    info: KeywordSectionInfo = field(default_factory=KeywordSectionInfo)
    # name: str = ''

    def __post_init__(self):
        tokens = _md.parse(self.content)
        is_heading = False
        for t in tokens:
            if t.type == 'html_block' and 'keyword_info' in t.content:
                info_str = NoteUtils.get_annotation('keyword_info', t.content)
                info_str = '\n'.join([ln.lstrip() for ln in info_str.split('\n')]) if info_str else ''
                info = yaml.safe_load(info_str) if info_str else {}
                self.info = KeywordSectionInfo(**info)
                # self.name = self.info.name
                if self.info.extra_url:
                    links = MarkdownUtils.extract_markdown_links(self.content)
                    if links:
                        self.url = links[0]['url']
            if t.type == 'heading_open':
                is_heading = True
            elif t.type == 'heading_close':
                is_heading = False
            elif is_heading and t.type == 'inline':
                self.head_name = t.content

        # if not self.name:
            # self.name = self.head_name

    @property
    def name(self):
        return self.info.name or self.head_name
    
    # @property
    # def url(self):
    #     """"""
    
    @property
    def with_keywords(self):
        return self.info.with_keywords
