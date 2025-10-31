#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2022-10-05 13:15
Author:
    huayang (imhuay@163.com)
Subject:
    notes
"""

from __future__ import annotations

import json
import os
import re
import shutil
from ast import keyword
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from logging import DEBUG
from pathlib import Path
from typing import ClassVar, Literal

import yaml
from _base import Builder
from sections.keyword_section import KeywordSection
from sections.qa_section import QaSection
from utils import MarkdownUtils, NoteUtils, TEMP_main_readme_notes_recent_toc, args

# TMP_subject_toc = '''### {title}
#
# {toc}
# '''

_DEBUG = False
_EMPTY = ''


@dataclass(unsafe_hash=True)
class SubjectId:
    id: str
    name: str


class RE:
    # note_info = re.compile(r'<!--info(.*?)-->', flags=re.DOTALL)
    note_name = re.compile(r'(\d{3})-(.*?).md')
    note_toc = re.compile(r'<!-- TOC -->(.*?)<!-- TOC -->', flags=re.DOTALL)
    note_content = re.compile(r'<!-- CONTENT -->(.*?)<!-- CONTENT -->', flags=re.DOTALL)


# def _load_note_info(fp, txt):
#     m = RE.note_info.search(txt)
#     if not m:
#         raise ValueError(fp)
#     return yaml.safe_load(m.group(1).strip())


@dataclass
class NoteInfo:
    top: bool = False
    draft: bool = False
    thorough: bool = False
    hidden_in_recent: bool = False
    section_number: bool = False
    apply_tex2svg: bool = True
    out_of_date: bool = False
    tags: list[str] = field(default_factory=list)
    algo_tags: list[str] = field(default_factory=list)
    level: int = 0
    date: datetime | None = None
    toc_title: str | None = None
    # toc_hidden: bool = False
    omit_in_tag_toc: bool = False

    def __post_init__(self):
        """"""
        if not self.tags:
            self.tags = ['draft']

        # if _DEBUG and self.tag is not None:
        #     print(self.tag)


@dataclass
class Note:
    path: Path
    text: str = ''
    _sub_notes: list[Note] = field(default_factory=list)
    _par_notes: list[Note] = field(default_factory=list)
    _tags: set[str] = field(default_factory=set)
    _qa_section: QaSection | None = None

    _info: NoteInfo | None = None
    _title: str | None = None
    _first_commit_date: str | None = None
    _last_commit_date: str | None = None
    _paper_title: str | None = None
    _date: str | None = None
    _parent_paths: list[Path] | None = None
    _keywords: list[KeywordSection] | None = None
    _updated: bool = False
    # _num_todo: int | None = None

    # ClassVar
    sort_by_first_commit: ClassVar[bool] = True
    max_section_level: ClassVar[int] = 6

    def __post_init__(self):
        self.path = self.path.resolve()

        with self.path.open(encoding='utf8') as f:
            self.text = f.read()

        self._tags.update(self.info.tags)

        self._tex2svg()
        self._norm_text()
        self._update_title(self.get_title_suffix_v2(add_tip_prefix=False, style='math'))
        self._update_badge()

        if self.qa_section is not None:
            self.text = NoteUtils.replace_section_content(
                QaSection.SECTION_KEY,
                self.text,
                self.qa_section.new_content,
            )
        elif self.info.section_number:
            # 如果存在 qa_section, 就不应用全局 section_number 了
            self._update_section_number()
            self._update_content_toc()

        if self._updated:
            self.write_text()

    def write_text(self):
        """"""
        self.path.write_text(self.text, encoding='utf8')

    def _norm_text(self):
        """文本规范化"""
        new_text = MarkdownUtils.normalize_text(self.text)
        if new_text != self.text:
            self.text = new_text
            self._updated = True

    SUFFIX_FLAG: str = '<!-- suffix -->'
    RE_SUFFIX_BLOCK = re.compile(rf'{SUFFIX_FLAG}(.*?){SUFFIX_FLAG}')

    def _remove_title_suffix(self, title: str) -> str:
        """"""
        return self.RE_SUFFIX_BLOCK.sub('', title).rstrip()

    def _update_title(self, title_suffix: str):
        """"""
        title, context = self.text.split('\n', maxsplit=1)

        # title_suffix = self.get_title_suffix_v2(qa_count=qa_count)
        if not title_suffix and self.SUFFIX_FLAG in title:
            new_title = self._remove_title_suffix(title)
        elif title_suffix:
            new_title = title
            if self.SUFFIX_FLAG not in new_title:
                new_title += f' {self.SUFFIX_FLAG} {self.SUFFIX_FLAG}'
            new_title = self.RE_SUFFIX_BLOCK.sub(
                lambda m: f'{self.SUFFIX_FLAG} {title_suffix} {self.SUFFIX_FLAG}',
                new_title,
            )
        else:
            new_title = title

        if new_title != title:
            self.text = new_title + '\n' + context
            self._updated = True

    def update_title(self, add_href: bool):
        """"""
        title_suffix = self.get_title_suffix_v2(add_href=add_href, add_tip_prefix=False, style='math')
        self._update_title(title_suffix)
        # self.write_text()

    def _update_badge(self):
        """"""
        badges = [
            NoteUtils.get_create_date_badge_url(self.info.date, self.path),
            NoteUtils.get_last_modify_badge_url(self.path),
        ]
        badge_tag = 'badge'
        new_badge = '\n'.join(badges)
        old_badge = NoteUtils.get_section_content(badge_tag, self.text)
        if new_badge != old_badge:
            self.text = NoteUtils.replace_section_content('badge', self.text, new_badge)
            self._updated = True

    def _tex2svg(self):
        if self.apply_tex2svg:
            from utils import MarkdownMath2SvgHelper

            helper = MarkdownMath2SvgHelper(self.path, self.text, save_mode=False)
            helper.run()
            if self.text != helper.text:
                self.text = helper.text
                self._updated = True

    def _update_section_number(self):
        """为标题添加章节编号
        如果原来已经存在, 则更新章节编号

        效果:
            ## 一级标题 => ## 1. 一级标题
            ### 二级标题 => ### 1.1. 二级标题
            #### 三级标题 => ### 1.1.1. 二级标题
        """
        D = self.max_section_level
        lines = self.text.split('\n')
        section_counts = [0] * D

        for i in range(len(lines)):
            line = lines[i]
            m = re.match(r'^(#{2,' + str(D) + r'})\s*(\d+(\.\d+)*\.)?\s*(.*)$', line)
            if not m:
                continue

            hashes, _, _, title = m.groups()
            level = len(hashes)

            # 更新当前级别的计数器, 并重置更低级别的计数器
            section_counts[level - 1] += 1
            for j in range(level, D):
                section_counts[j] = 0

            # 构建章节编号字符串
            section_number = '.'.join(str(section_counts[k]) for k in range(level) if section_counts[k] > 0) + '.'

            # 更新标题行
            lines[i] = f'{hashes} {section_number} {title.strip()}'

        new_text = '\n'.join(lines)
        if new_text != self.text:
            self.text = new_text
            self._updated = True

    def _update_content_toc(self):
        """更新 Markdown 内容 TOC"""
        D = self.max_section_level
        lines = self.text.split('\n')
        toc_lines = []

        for i in range(len(lines)):
            line = lines[i]
            m = re.match(r'^(#{2,' + str(D) + r'})\s*(.*)$', line)
            if not m:
                continue

            hashes, title = m.groups()
            level = len(hashes)

            indent = '    ' * (level - 2)
            anchor = MarkdownUtils.slugify(title)
            toc_line = f'{indent}- [{title.strip()}](#{anchor})'
            toc_lines.append(toc_line)

        new_toc_content = '\n'.join(toc_lines)
        toc_content = NoteUtils.get_section_content('toc', self.text)
        if new_toc_content != toc_content:
            # MarkdownUtils.print_diffs_with_context(new_toc_content, toc_content or '')
            self.text = NoteUtils.replace_section_content('toc', self.text, new_toc_content)
            self._updated = True

    def add_sub_note(self, note: Note):
        self._sub_notes.append(note)
        self._tags.update(note._tags)

    def add_par_note(self, note: Note):
        self._par_notes.append(note)
        self._tags.update(note._tags)

    def sort_sub_notes(self):
        self._sub_notes.sort(key=lambda x: (x.info.level, x.title), reverse=True)

    def _get_toc_keyword_block(self, _k: KeywordSection):
        """"""
        if _k.url:
            _k_note_path = (self.path.parent / _k.url).resolve()
            url = _k_note_path.relative_to(args.fp_notes)
            base_keyword = f'[{_k.name}]({url})'
            _k_note = path2note[_k_note_path]
            if _k_note.toc_title_suffix:
                base_keyword += f'</i>{_k_note.toc_title_suffix}<i>'
            if _k_note.keywords and _k.with_keywords:
                base_keyword += ' • ' + _k_note.keywords_suffix
            return base_keyword
        elif _k.head_name:
            return f'[{_k.name}]({self.path_relative_to_note}#{MarkdownUtils.slugify(_k.head_name)})'
        else:
            return _k.name

    @property
    def keywords_suffix(self):
        return ' • '.join([self._get_toc_keyword_block(k) for k in self.keywords if k.name])

    def get_tag_toc_line(self, deep: int) -> str:
        global path2note
        assert path2note

        # rel_path = self.path.relative_to(args.fp_notes)
        # title = self.title if self.info.toc_title is None else self.info.toc_title
        # title = self.tag_toc_title
        # title = re.sub(r'\(\s*(.*?)\s*\)', r'( \1 )', self.tag_toc_title)  # 扩号内侧加空格
        title = MarkdownUtils.add_space_in_bracket(self.tag_toc_title)
        # title = f'{title} {self.toc_title_suffix}'
        toc_line = f'- [{title}]({self.path_relative_to_note}) {self.toc_title_suffix}'

        # keywords = ' '.join([f'• {_get_toc_line(k)}' for k in self.keywords if k.name])
        keywords = ' • '.join([self._get_toc_keyword_block(k) for k in self.keywords if k.name])
        if keywords:
            toc_line += '\n' + '  ' * deep + f'> <i>{keywords}</i><br>'

        return toc_line

    def get_recent_toc_line_relative_to(self, parent_path: Path):
        """更新 README recent 模块内的 TOC"""
        title = MarkdownUtils.add_space_in_bracket(self.title)  # 扩号内侧加空格
        rel_path = self.path.relative_to(parent_path)
        title_suffix = self.get_title_suffix_v2(href=rel_path)
        toc_line = f'- [`{self.date}` {title}]({rel_path}) {title_suffix}'
        if self.is_top:
            toc_line += self._get_title_span(self.TIP_TOP, self.EMOJI_TOP)
        return toc_line
        # if self.is_top:
        #     return f'- [`{self.date}` {self.title}]({self.path.relative_to(parent_path)}) 📌'
        # else:
        #     return f'- [`{self.date}` {self.title}]({self.path.relative_to(parent_path)}) {self.toc_title_suffix}'

    # @property
    # def toc_line_for_recent_relative_to_repo(self):
    #     """README recent 模块内的 TOC 行 (路径相对于 repo 根目录)"""
    #     if self.is_top:
    #         return f'- [`{self.date}` {self.title} 📌]({self.path_relative_to_repo})'
    #     else:
    #         return f'- [`{self.date}` {self.title}]({self.path_relative_to_repo})'

    @property
    def keywords(self) -> list[KeywordSection]:
        """文章内部的 keywords 列表, 用于生成 TOC 行时附加到引用中

        示例:
            找出文中所有 keyword 块
                ...
                <!--START_SECTION:keyword-->
                ## keyword1
                <!--END_SECTION:keyword-->
                ...
                <!--START_SECTION:keyword-->
                ## keyword2
                <!--END_SECTION:keyword-->

            生成 toc line 时, 附加 keywords:
                - [title](path)\n  > _keyword1, keyword2_
        """
        if self._keywords is None:
            keyword_sections = NoteUtils.findall_section('keyword', self.text)
            self._keywords = [KeywordSection(k) for k in keyword_sections]
        return self._keywords

    # @property
    # def text(self) -> str:
    #     return self.text

    @property
    def title(self):
        if self._title is None:
            title = self.text.split('\n', maxsplit=1)[0].strip()

            if title == '':
                # self._title = f'{self.path.stem}({self.path_relative_to_repo})'
                title = self.path.stem

            if self.SUFFIX_FLAG in title:
                title = self._remove_title_suffix(title)

            self._title = title
        return self._title

    @property
    def info(self) -> NoteInfo:
        if self._info is None:
            _info = NoteUtils.get_annotation_info_v2(self)
            self._info = NoteInfo(**_info)
        return self._info

    @property
    def first_commit_date(self) -> str:
        if self._first_commit_date is None:
            self._first_commit_date = NoteUtils.get_first_commit_date(self.path)
        return self._first_commit_date

    @property
    def last_commit_date(self) -> str:
        if self._last_commit_date is None:
            self._last_commit_date = NoteUtils.get_last_commit_date(self.path)
        return self._last_commit_date

    @property
    def date(self):
        if self._date is None:
            if self.info.date is not None:
                # print(f'{self.info.date=}, {type(self.info.date)=}')
                self._date = self.info.date.strftime('%Y-%m-%d')
            else:
                self._date = self._commit_datetime_for_sort[:10]
        return self._date

    @property
    def is_top(self):
        return self.info.top

    @property
    def is_draft(self):
        return self.info.draft

    @property
    def is_thorough(self):
        return self.info.thorough

    @property
    def is_hidden_in_recent(self):
        if self.info.top:
            return False
        return self.info.hidden_in_recent

    @property
    def is_algo_note(self):
        return self.info.algo_tags or any(tag.startswith('algo') for tag in self._tags)

    @property
    def apply_tex2svg(self):
        return self.info.apply_tex2svg

    @property
    def path_relative_to_repo(self):
        return self.path.relative_to(args.fp_repo)

    @property
    def path_relative_to_note(self):
        return self.path.relative_to(args.fp_notes)

    @property
    def sort_key(self):
        # if self.title is None:
        #     raise ValueError(self.path)
        # return self.last_commit_date, self.title
        return self._commit_datetime_for_sort, self.title

    @property
    def _commit_datetime_for_sort(self):
        return self.first_commit_date if self.sort_by_first_commit else self.last_commit_date

    @property
    def paper_title(self):
        if self._paper_title is None:
            paper_title = NoteUtils.get_section_content('paper_title', self.text)
            if paper_title is None:
                self._paper_title = _EMPTY
            else:
                # > [[synonym.2012.KDD.01] A framework for robust discovery of entity synonyms | 基于统计方法的通用同义词挖掘框架](https://dl.acm.org/doi/10.1145/2339530.2339743) || [PDF](./[synonym.2012.KDD.01]%20A%20Framework%20for%20Robust%20Discovery%20of%20Entity%20Synonyms.pdf)
                m = re.search(r'\[(\[(.*?)\] (.*?))\]', paper_title)
                if not m:
                    self._paper_title = _EMPTY
                else:
                    self._paper_title = m.group(1).strip()
        return self._paper_title

    @property
    def paper_title_toc_line(self) -> str:
        if self.paper_title == _EMPTY:
            return _EMPTY
        if self.is_draft:
            title = f'{self.paper_title} ⏳'
        else:
            title = self.paper_title
        rel_path = self.path.relative_to(args.fp_notes)
        return f'- [{title}]({rel_path})'

    @property
    def parent_paths(self) -> list[Path]:
        if self._parent_paths is None:
            parent_notes = []
            keywords = NoteUtils.get_section_content('keywords', self.text)
            if keywords:
                links = MarkdownUtils.extract_markdown_links(keywords)
                for lk in links:
                    p_path = (self.path.parent / lk['url']).resolve()
                    parent_notes.append(p_path)
            self._parent_paths = parent_notes
        return self._parent_paths

    @property
    def omit_in_tag_toc(self):
        return self.info.omit_in_tag_toc

    @property
    def sub_notes(self):
        return self._sub_notes

    @property
    def par_notes(self):
        return self._par_notes

    @property
    def tags(self) -> set[str]:
        if 'draft' in self._tags and len(self._tags) > 1:
            self._tags.remove('draft')
        return self._tags

    @property
    def algo_tags(self) -> list[str]:
        return sorted(set(self.info.algo_tags))

    @property
    def tag_toc_title(self) -> str:
        """用于生成在 tag 标签下 TOC 行时的标题"""
        return self.info.toc_title if self.info.toc_title else self.title

    def get_title_suffix(self, todo_size: int = 16, href: str = '#') -> str:
        suffix = ''

        if self.is_thorough:
            suffix += f'{self.EMOJI_THOROUGH}'

        if self.is_draft or self.num_todo > 0:
            suffix += f'{self.EMOJI_TODO}'

        if self.num_todo > 0:
            suffix += args.get_temp_badge_todo_logo(self.num_todo, height=todo_size, href=href)

        return suffix

    _is_qa_coll: bool = False

    @property
    def is_qa_coll(self) -> bool:
        return self._is_qa_coll

    def set_is_qa_coll(self, v: bool):
        self._is_qa_coll = v

    TIP_QA = '面试问题整理'
    EMOJI_QA = '📋'

    TIP_TODO = 'TODO'
    EMOJI_TODO = '✒️'

    TIP_THOROUGH = '特别关注'
    EMOJI_THOROUGH = '🧣'

    TIP_TOP = '置顶'
    EMOJI_TOP = '📌'

    TIP_OUTDATED = 'Out-of-Date'
    EMOJI_OUTDATED = '💾'  # 📦

    @staticmethod
    def _get_title_span(title: str, content: str):
        """"""
        return f'<span title="{title}">{content}</span>'

    @property
    def qa_section_title(self):
        """"""
        if self.qa_section is not None:
            return self.qa_section.section_title
        return ''

    def get_title_suffix_v2(
        self,
        *,
        add_href: bool = True,
        href: str | Path = '',
        add_tip_prefix: bool = True,
        style: Literal['math', 'html'] = 'html',
    ) -> str:
        suffix = ''

        if self.is_thorough:
            suffix += self._get_title_span(self.TIP_THOROUGH, self.EMOJI_THOROUGH)

        if self.is_draft or self.num_todo > 0:
            # badge_src = 'https://img.shields.io/static/v1?label=&message=TODO&color=critical&style=flat-square'
            # suffix = img_temp.format(src=badge_src)
            tip_todo = f'{self.TIP_TODO}({self.num_todo})' if self.num_todo > 0 else self.TIP_TODO
            if self.num_todo > 0:
                suffix += f'[{self.EMOJI_TODO}]({href}#todo "{tip_todo}")' + MarkdownUtils.get_count_sup(
                    self.num_todo, style=style
                )
            else:
                suffix += self._get_title_span(tip_todo, self.EMOJI_TODO)

        if not self.qa_section_title:
            add_href = False

        if self.qa_count > 0:
            if self.qa_section is not None and add_tip_prefix:
                # tip_topic = self.tag_toc_title
                # tip_topic = f'{self.qa_section.subject} · {self.qa_section.topic} · '
                tip_topic = f'{self.qa_section.topic} · '
            else:
                tip_topic = ''
            tip_qa = f'{tip_topic}{self.TIP_QA}({self.qa_count})'
            if add_href:
                if self.is_qa_coll or not self.qa_section_title:
                    _a = f'[{self.EMOJI_QA}]({href} "{tip_qa}")'
                else:
                    _a = f'[{self.EMOJI_QA}]({href}#{MarkdownUtils.slugify(self.qa_section_title)} "{tip_qa}")'
                suffix += f'{_a}' + MarkdownUtils.get_count_sup(self.qa_count, color='Brown', style=style)
            else:
                # GitHub 上 "EMOJI$..$" emoji与公式紧挨时会解析失败
                _span = self._get_title_span(tip_qa, self.EMOJI_QA)
                suffix += _span + MarkdownUtils.get_count_sup(self.qa_count, color='Brown', style=style)

        # if self.num_todo > 0:
        #     # badge_src = f'https://img.shields.io/static/v1?label=✓&message={self.num_todo}&labelColor=critical&color=gray&style=flat-square'
        #     # suffix += args.temp_badge_todo_logo_edit_h.format(num_todo=self.num_todo, height=todo_size)
        #     suffix += args.get_temp_badge_todo_logo(self.num_todo, height=todo_size, href=href)

        if self.out_of_date:
            suffix += self._get_title_span(self.TIP_OUTDATED, self.EMOJI_OUTDATED)

        return suffix

    _toc_title_suffix: str = ''

    def update_toc_title_suffix(self, *, href: str | Path | None = None):
        """"""
        if href is None:
            href = self.path_relative_to_note
        self._toc_title_suffix = self.get_title_suffix_v2(href=href)

    @property
    def toc_title_suffix(self) -> str:
        """toc 标题后缀"""
        if not self._toc_title_suffix:
            self._toc_title_suffix = self.get_title_suffix_v2(href=self.path_relative_to_note)
        return self._toc_title_suffix

    TODO_FLAG = '> ##### TODO'

    @property
    def num_todo(self) -> int:
        """返回全文有几个 TODO"""
        return self.text.lower().count(self.TODO_FLAG.lower())

    @property
    def progress_marker(self) -> str:
        """返回极简进度标记: 一个emoji + N个□"""
        if self.num_todo > 0:
            per = 10 + max(0, 3 - self.num_todo) * 10
            return f'⏳{per}%'
        else:
            return ''

    @property
    def qa_section(self) -> QaSection | None:
        """"""
        if self._qa_section is None:
            c = NoteUtils.get_section_content(QaSection.SECTION_KEY, self.text)
            if c is not None:
                self._qa_section = QaSection(content=c, md_path=self.path, md_toc_title=self.tag_toc_title)
        return self._qa_section

    _qa_count: int = 0

    def set_qa_count(self, v: int):
        assert v > 0
        self._qa_count = v

    @property
    def qa_count(self) -> int:
        """"""
        if self._qa_count == 0:
            if self.qa_section is not None:
                self._qa_count = self.qa_section.qa_count
                assert self._qa_count > 0
        return self._qa_count

    QA_BADGE_COLOR: str = ''
    QA_BADGE_TEMP = '<a href="{href}"><img src="https://custom-icon-badges.demolab.com/static/v1?label=QA&message={count}&labelColor={color}&color={color}&style=flat-square&logoSource=feather&logo=edit&logoColor=white" height="{height}"/></a>'

    @property
    def out_of_date(self):
        """"""
        return self.info.out_of_date


@dataclass
class SubjectInfo:
    path: Path
    # subject_ids: ClassVar[dict[str, SubjectId]]

    _prefix = None
    _name = None
    _txt = None
    _toc = None
    _info = None

    @property
    def head(self):
        h_lv = '###' if self.name != 'WIKI' else '##'
        return f'{h_lv} [{self.name}]({self.path.name})'

    @property
    def prefix(self):
        if self._prefix is None:
            self._prefix = self.path.stem.split('-')[0]
        return self._prefix

    @property
    def name(self):
        if self._name is None:
            self._name = self.path.stem.split('-')[1]
        return self._name

    @property
    def subject_id(self) -> str:
        return self.prefix[0]

    @property
    def subject_number(self) -> str:
        return self.prefix[1:]

    @property
    def txt(self):
        if self._txt is None:
            with self.path.open(encoding='utf8') as f:
                self._txt = f.read().strip()
        return self._txt

    @property
    def toc(self) -> str:
        if self._toc is None:
            m = RE.note_toc.search(self.txt)
            if not m:
                raise ValueError(self.path)
            toc = m.group(1).strip()
            # toc = toc.replace('(#', f'({self.path.name}#')
            lns = toc.split('\n')
            for i in range(len(lns)):
                lns[i] = lns[i].replace('(#', f'({self.path.name}#', 1)
            toc = '\n'.join(lns)
            self._toc = toc
        return self._toc

    @property
    def info(self) -> dict:
        if self._info is None:
            try:
                _info = NoteUtils.get_annotation_info(self.txt)
            except:  # noqa
                raise ValueError(self.path)
            self._info = yaml.safe_load(_info)  # type: ignore
        return self._info

    @property
    def toc_id(self):
        return self.info['toc_id']

path2note: dict[Path, Note] = dict()

class NotesBuilder(Builder):
    subjects: list[SubjectInfo]
    fp2date: dict[Path, str]

    notes: list[Note] = []
    algo_notes: list[Note] = []
    path2note: dict[Path, Note] = dict()
    _notes_top: list[Note] = []
    _notes_recent: list[Note] = []
    _recent_limit: int = 15

    def __init__(self):
        """"""
        self._fp_notes = args.fp_notes
        self._fp_notes_archives = args.fp_notes_archives

        self._fp_notes_readme_v1 = args.fp_notes_readme_v1
        self._fp_notes_readme_temp_v1 = args.fp_notes_readme_temp_v1
        self._fp_notes_readme_v2 = args.fp_notes_readme_v2
        self._fp_notes_readme_temp_v2 = args.fp_notes_readme_temp_v2
        self._fp_tags = args.fp_tags

        self._top_limit = args.notes_top_limit
        self._fp_notes_readme_temp = args.fp_notes_readme_temp
        self._fp_notes_readme = args.fp_notes_readme

        self._load_note_indexes()  # deprecated
        self._load_all_notes()

    @property
    def notes_top(self):
        return self._notes_top[: self._top_limit]

    @property
    def notes_recent(self):
        # recent_limit = len(self.toc_append.split('\n'))
        return self._notes_recent[: self._recent_limit - len(self.notes_top)]

    _qa_sections: list[QaSection] = []

    def _load_all_notes(self):
        """"""
        global path2note
        path2note = self.path2note
        qa_note = None
        for dp, _, fns in os.walk(self._fp_notes_archives):
            for fn in fns:
                fp = Path(dp) / fn
                if fp.suffix != '.md' or fp.name.startswith('tmp') or fp.name.startswith('-'):
                    continue
                note = Note(fp)
                self.notes.append(note)
                self.path2note[note.path] = note
                if note.is_top:
                    self._notes_top.append(note)
                elif not note.is_hidden_in_recent:
                    # 加到 top 就不要再放到 recent 了
                    self._notes_recent.append(note)
                if note.is_algo_note:
                    self.algo_notes.append(note)
                if note.qa_section is not None:
                    self._qa_sections.append(note.qa_section)
                if note.path.samefile(args.fp_qa_collection):
                    qa_note = note
                    qa_note.set_is_qa_coll(True)

        self._notes_top.sort(key=lambda x: x.sort_key, reverse=True)
        self._notes_recent.sort(key=lambda x: x.sort_key, reverse=True)

        # update sub_notes and parent_notes
        for note in self.notes:
            # update sub_notes
            if note.parent_paths:
                for p_path in note.parent_paths:
                    if p_path in self.path2note:
                        p_note = self.path2note[p_path]
                        # p_note.sub_notes.append(note)
                        p_note.add_sub_note(note)
                        # note.par_notes.append(p_note)
                        note.add_par_note(p_note)
                    else:
                        raise ValueError(f'Parent note not found: {p_path}')

        assert qa_note is not None
        self._update_qa_coll(qa_note)

    def _load_note_indexes(self):
        """deprecated"""
        self.subjects = []
        for path in self._fp_notes.iterdir():
            if not RE.note_name.match(path.name):
                continue
            _subject = SubjectInfo(path)
            self.subjects.append(_subject)

    def _set_recent_limit(self, temp: str):
        """"""
        toc = RE.note_toc.search(temp).group(1).strip()  # type: ignore
        self._recent_limit = len(toc.split('\n'))

    def _get_available_tags(self, temp_txt, pattern=r'\{\{(.*?)\}\}'):
        """"""
        with self._fp_tags.open('w', encoding='utf8') as fw:
            tags = sorted(re.findall(pattern, temp_txt))
            json.dump(tags, fw, indent=4, ensure_ascii=False)

        return tags

    def build_v1(self):
        with self._fp_notes_readme_temp_v1.open(encoding='utf8') as f:
            txt = f.read()
            self._set_recent_limit(txt)

        txt = NoteUtils.replace_section_content('recent', txt, self.recent_toc)

        # contents = {s.toc_id: s.toc for s in self.subjects}
        # txt = txt.format(**contents)
        for s in self.subjects:
            toc_id, toc = s.toc_id, s.toc
            txt = txt.replace(f'{{{toc_id}}}', toc)

        with self._fp_notes_readme_v1.open('w', encoding='utf8') as f:
            f.write(txt)

    @staticmethod
    def _get_sort_sub_toc(notes: list[Note], tag: str) -> list[str]:
        """"""
        # sorted_by_level = sorted(notes, key=lambda x: (x.info.level,), reverse=True)

        sort_sub_toc = []
        added = set()

        def _dfs_add(note: Note, deep: int):
            # if note.info.toc_hidden:
            if note.omit_in_tag_toc:
                return
            if note.path in added:
                return
            added.add(note.path)
            toc_line = '  ' * deep + note.get_tag_toc_line(deep + 1)
            sort_sub_toc.append(toc_line)

            # if DEBUG and n_deep > 0:
            #     print(f'{note.path}')

            # note._sub_notes.sort(key=lambda x: (x.info.level, x.title), reverse=True)
            note.sort_sub_notes()
            for sub_note in note.sub_notes:
                # 如果子文档已经在父文档中出现过 (作为引用), 且名称也相同, 则跳过
                rel_path_str = str(sub_note.path.relative_to(args.fp_notes))
                if sub_note.omit_in_tag_toc or (rel_path_str in toc_line and sub_note.tag_toc_title in toc_line):
                    continue
                _dfs_add(sub_note, deep + 1)

        if tag == 'draft':
            notes_without_parent = notes[:]
        else:
            # 所有没有父节点的笔记
            notes_without_parent = [n for n in notes if not n.par_notes]
        notes_without_parent.sort(key=lambda x: (x.info.level, x.title), reverse=True)

        for note in notes_without_parent:
            _dfs_add(note, 0)

        return sort_sub_toc

    def _get_sub_toc(self):
        """"""
        paper_toc: list[str] = []
        tag2toc: dict[str, list[str]] = dict()
        tag2notes: dict[str, list[Note]] = defaultdict(list)

        for note in self.notes:
            for tag in note.tags:
                tag2notes[tag].append(note)
            if note.paper_title_toc_line != _EMPTY:
                paper_toc.append(note.paper_title_toc_line)

        for tag, notes in tag2notes.items():
            # if DEBUG and tag == 'draft':
            #     for n in notes:
            #         if 'LoRA' in n.title:
            #             print(n.path)
            tag2toc[tag] = self._get_sort_sub_toc(notes, tag)
        # for notes in tag2notes.values():
        #     notes.sort(key=lambda e: (e.info.level, e.tag_toc_line), reverse=True)
        # for tag, notes in tag2notes.items():
        #     tag2toc[tag] = [e.tag_toc_line for e in notes]

        paper_toc = sorted(paper_toc)
        return tag2toc, paper_toc

    total_qa_count: int = 0

    def _update_qa_coll(self, note: Note):
        """"""
        # 更新 qa_coll note 相关的标题
        self.total_qa_count = sum(s.qa_count for s in self._qa_sections)
        note.set_qa_count(self.total_qa_count)
        note.update_toc_title_suffix()
        note.update_title(add_href=False)
        # 更新 qa_coll note
        self._update_qa_coll_content(note)

        # Update content
        note.write_text()

    def _update_qa_section_subject_level(self):
        """"""
        qa_sections = self._qa_sections
        subject2level = defaultdict(int)

        for s in qa_sections:
            subject2level[s.top_subject] = max(subject2level[s.top_subject], s.subject_level)

        for s in qa_sections:
            s.info.subject_level = subject2level[s.top_subject]

    def _update_qa_coll_content(self, note: Note):
        """"""
        # txt = md_path.read_text(encoding='utf8')
        md_path = note.path
        # txt = note.text

        self._update_qa_section_subject_level()

        ss = sorted(self._qa_sections, key=lambda s: s.sort_key)
        # md_path = Path('/home/huay/workspace/git/my/sspace/notes/_archives/2025/10/QA_合集.md')

        toc_lines = []
        sub_toc_blocks = []

        for s in ss:
            prefix = MarkdownUtils.get_relpath_from_p1_to_p2(md_path, s.md_path)
            toc_blk = s.get_toc(prefix, with_subject_title=True)
            sub_toc_blocks.append(toc_blk)
            toc_lines.append(s.subject_toc_line)

        toc = '\n'.join(toc_lines)
        sub_tocs = '\n\n'.join(sub_toc_blocks)

        note.text = NoteUtils.replace_section_content('toc', note.text, toc)
        note.text = NoteUtils.replace_section_content('sub_tocs', note.text, sub_tocs)

        # md_path.write_text(note.text, encoding='utf8')
        # note.write_text()

    def build_v2(self):
        with self._fp_notes_readme_temp_v2.open(encoding='utf8') as f:
            txt = f.read()
            self._set_recent_limit(txt)
            available_tags = self._get_available_tags(txt)

        # generate tag toc
        # paper_toc = []
        # tag2toc = dict()
        # tag2notes: dict[str, list[Note]] = defaultdict(list)
        # for note in self.notes:
        #     for tag in note.tag:
        #         tag2notes[tag].append(note)
        #     if note.paper_title_toc_line != _EMPTY:
        #         paper_toc.append(note.paper_title_toc_line)
        # for v in tag2notes.values():
        #     v.sort(key=lambda e: (e.info.level, e.tag_toc_line), reverse=True)
        # for k, v in tag2notes.items():
        #     tag2toc[k] = [e.tag_toc_line for e in v]
        tag2toc, paper_toc = self._get_sub_toc()
        # if DEBUG:
        #     for n in tag2toc['draft']:
        #         if 'LoRA' in n:
        #             print(n)

        # replace template
        txt = NoteUtils.replace_section_content('recent', txt, self.recent_toc)
        draft = []
        for tag, toc in tag2toc.items():
            if tag not in available_tags or tag == 'draft':
                # if DEBUG:
                #     print(f'No tag placeholder found: {tag}: {toc}')
                draft.extend(toc)
                continue

            if tag == 'paper':
                toc_str = '\n'.join(paper_toc)
            else:
                toc_str = '\n'.join(toc)

            txt = txt.replace(f'{{{{{tag}}}}}', toc_str)

        txt = txt.replace('{{draft}}', '\n'.join(sorted(draft)))
        txt = re.sub(r'\{\{.*?\}\}', '', txt)

        for s in self.subjects:
            toc_id, toc = s.toc_id, s.toc
            txt = txt.replace(f'{{{toc_id}}}', toc)

        with self._fp_notes_readme_v2.open('w', encoding='utf8') as f:
            f.write(txt)

    def build(self, version='v2'):
        """"""
        self.build_v1()
        self.build_v2()

        # self._update_qa_coll(Path(args.fp_qa_collection))

        shutil.copy2(getattr(self, f'_fp_notes_readme_{version}'), self._fp_notes_readme)

    def set_relate_problems_for_algo_note(self):
        """"""
        from algorithms import tag_info

        for note in self.algo_notes:
            toc = tag_info.get_toc_for_note(note)

            with note.path.open('r', encoding='utf8') as f:
                txt = f.read()

            txt = NoteUtils.replace_section_content('related_problems', txt, toc)

            with note.path.open('w', encoding='utf8') as f:
                f.write(txt)

    @property
    def toc_append(self):
        with self._fp_notes_readme.open(encoding='utf8') as f:
            return RE.note_toc.search(f.read()).group(1).strip()  # type: ignore

    @property
    def recent_toc(self):
        return TEMP_main_readme_notes_recent_toc.format(
            toc_top='\n'.join([n.get_recent_toc_line_relative_to(self._fp_notes) for n in self.notes_top]),
            toc_recent='\n'.join([n.get_recent_toc_line_relative_to(self._fp_notes) for n in self.notes_recent]),
        )

    @property
    def recent_toc_append(self):
        return TEMP_main_readme_notes_recent_toc.format(
            # toc_top='\n'.join([n.toc_line_for_recent_relative_to_repo for n in self.notes_top]),
            # toc_recent='\n'.join([n.toc_line_for_recent_relative_to_repo for n in self.notes_recent]),
            toc_top='\n'.join([n.get_recent_toc_line_relative_to(args.fp_repo) for n in self.notes_top]),
            toc_recent='\n'.join([n.get_recent_toc_line_relative_to(args.fp_repo) for n in self.notes_recent]),
        )

    @property
    def readme_append(self):
        with self._fp_notes_readme.open(encoding='utf8') as f:
            # content = RE.note_content.search(f.read()).group(1).strip()
            # return content.replace('](', f']({self._fp_notes.name}/')
            txt = f.read()
        txt = NoteUtils.get_section_content('notes', txt)
        return txt.replace('](', f']({self._fp_notes.name}/')  # type: ignore


if __name__ == '__main__':
    """"""
    _DEBUG = True
    note = NotesBuilder()
    note.build()
