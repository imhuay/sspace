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
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from logging import DEBUG
from pathlib import Path
from typing import ClassVar

import yaml

try:
    from readme._base import Builder
    from readme.utils import MarkdownUtils, ReadmeUtils, TEMP_main_readme_notes_recent_toc, args
except ImportError:
    from _base import Builder

    from utils import MarkdownUtils, ReadmeUtils, TEMP_main_readme_notes_recent_toc, args  # type: ignore


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
    hidden: bool = True
    draft: bool = True
    tag: list[str] | None = None
    level: int | None = 0
    p_title: str | None = None
    date: datetime | None = None

    def __post_init__(self):
        """"""
        if self.tag is None:
            self.tag = ['draft']

        # if _DEBUG and self.tag is not None:
        #     print(self.tag)


@dataclass
class Note:
    path: Path
    sub_notes: list[Note] = field(default_factory=list)
    par_notes: list[Note] = field(default_factory=list)

    _text: str | None = None
    _info: NoteInfo | None = None
    _title: str | None = None
    _first_commit_date: str | None = None
    _last_commit_date: str | None = None
    _paper_title: str | None = None
    _date: str | None = None
    _parent_paths: list[Path] | None = None
    sort_by_first_commit: ClassVar[bool] = True

    def __post_init__(self):
        self.path = self.path.resolve()
        self.update_note_last_modify()

        with self.path.open(encoding='utf8') as f:
            self._text = f.read()

    def update_note_last_modify(self):
        with self.path.open(encoding='utf8') as f:
            new_txt = ReadmeUtils.replace_tag_content(
                'badge', f.read(), ReadmeUtils.get_last_modify_badge_url(self.path)
            )
        with self.path.open('w', encoding='utf8') as f:
            f.write(new_txt)

    def get_toc_line_relative_to(self, parent_path: Path):
        if self.is_top:
            return f'- [`{self.date}` {self.title} 📌]({self.path.relative_to(parent_path)})'
        else:
            return f'- [`{self.date}` {self.title}]({self.path.relative_to(parent_path)})'

    @property
    def toc_line_relative_to_repo(self):
        if self.is_top:
            return f'- [`{self.date}` {self.title} 📌]({self.path_relative_to_repo})'
        else:
            return f'- [`{self.date}` {self.title}]({self.path_relative_to_repo})'

    @property
    def text(self) -> str:
        if self._text:
            return self._text
        else:
            raise ValueError(f'Note text is None: {self.path}')

    @property
    def title(self):
        if self._title is None:
            self._title = self.text.split('\n', maxsplit=1)[0].strip()

            if self._title == '':
                self._title = f'Untitled-{self.path_relative_to_repo}'

            if self.info.draft:
                self._title += ' ⏳'
        return self._title

    @property
    def info(self) -> NoteInfo:
        if self._info is None:
            _info = ReadmeUtils.get_annotation_info_v2(self)
            self._info = NoteInfo(**_info)
        return self._info

    @property
    def first_commit_date(self) -> str:
        if self._first_commit_date is None:
            self._first_commit_date = ReadmeUtils.get_first_commit_date(self.path)
        return self._first_commit_date

    @property
    def last_commit_date(self) -> str:
        if self._last_commit_date is None:
            self._last_commit_date = ReadmeUtils.get_last_commit_date(self.path)
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
    def is_hidden(self):
        if self.info.top:
            return False
        return self.info.hidden

    @property
    def path_relative_to_repo(self):
        return self.path.relative_to(args.fp_repo)

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
    def tag(self) -> list[str]:
        if self.info.tag is None:
            return []
        return self.info.tag

    @property
    def tag_toc_line(self) -> str:
        rel_path = self.path.relative_to(args.fp_notes)
        return f'- [{self.title}]({rel_path})'

    @property
    def paper_title(self):
        if self._paper_title is None:
            paper_title = ReadmeUtils.get_tag_content('paper_title', self.text)
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
        if self.info.draft:
            title = f'{self.paper_title} ⏳'
        else:
            title = self.paper_title
        rel_path = self.path.relative_to(args.fp_notes)
        return f'- [{title}]({rel_path})'

    @property
    def parent_paths(self) -> list[Path]:
        if self._parent_paths is None:
            parent_notes = []
            keywords = ReadmeUtils.get_tag_content('keywords', self.text)
            if keywords:
                links = MarkdownUtils.extract_markdown_links(keywords)
                for lk in links:
                    p_path = (self.path.parent / lk['url']).resolve()
                    parent_notes.append(p_path)
            self._parent_paths = parent_notes
        return self._parent_paths


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
                _info = ReadmeUtils.get_annotation_info(self.txt)
            except:  # noqa
                raise ValueError(self.path)
            self._info = yaml.safe_load(_info)  # type: ignore
        return self._info

    @property
    def toc_id(self):
        return self.info['toc_id']


class NotesBuilder(Builder):
    subjects: list[SubjectInfo]
    fp2date: dict[Path, str]

    notes: list[Note] = []
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

    def _load_all_notes(self):
        """"""
        for dp, _, fns in os.walk(self._fp_notes_archives):
            for fn in fns:
                fp = Path(dp) / fn
                if fp.suffix != '.md':
                    continue
                note = Note(fp)
                self.notes.append(note)
                self.path2note[note.path] = note
                if not note.is_hidden:
                    if note.is_top:
                        self._notes_top.append(note)
                    else:
                        self._notes_recent.append(note)

        self._notes_top.sort(key=lambda x: x.sort_key, reverse=True)
        self._notes_recent.sort(key=lambda x: x.sort_key, reverse=True)

        # update sub_notes and parent_notes
        for note in self.notes:
            # update sub_notes
            if note.parent_paths:
                for p_path in note.parent_paths:
                    if p_path in self.path2note:
                        p_note = self.path2note[p_path]
                        p_note.sub_notes.append(note)
                        note.par_notes.append(p_note)
                    else:
                        raise ValueError(f'Parent note not found: {p_path}')

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

        txt = ReadmeUtils.replace_tag_content('recent', txt, self.recent_toc)

        # contents = {s.toc_id: s.toc for s in self.subjects}
        # txt = txt.format(**contents)
        for s in self.subjects:
            toc_id, toc = s.toc_id, s.toc
            txt = txt.replace(f'{{{toc_id}}}', toc)

        with self._fp_notes_readme_v1.open('w', encoding='utf8') as f:
            f.write(txt)

    @staticmethod
    def _get_sort_sub_toc(notes: list[Note]) -> list[str]:
        """"""
        # sorted_by_level = sorted(notes, key=lambda x: (x.info.level,), reverse=True)

        sort_sub_toc = []
        added = set()

        def _dfs_add(note: Note, n_deep: int):
            if note.path in added:
                return
            added.add(note.path)
            sort_sub_toc.append('  ' * n_deep + note.tag_toc_line)

            # if DEBUG and n_deep > 0:
            #     print(f'{note.path}')

            note.sub_notes.sort(key=lambda x: (x.info.level, x.title), reverse=True)
            for sub_note in note.sub_notes:
                _dfs_add(sub_note, n_deep + 1)

        no_par_notes = [n for n in notes if not n.par_notes]
        no_par_notes.sort(key=lambda x: (x.info.level, x.title), reverse=True)

        for note in no_par_notes:
            _dfs_add(note, 0)

        return sort_sub_toc

    def _get_sub_toc(self):
        """"""
        paper_toc = []
        tag2toc: dict[str, list[str]] = dict()
        tag2notes: dict[str, list[Note]] = defaultdict(list)

        for note in self.notes:
            for tag in note.tag:
                tag2notes[tag].append(note)
            if note.paper_title_toc_line != _EMPTY:
                paper_toc.append(note.paper_title_toc_line)

        for tag, notes in tag2notes.items():
            # if DEBUG and tag == 'nlp_kg':
            #     pass
            tag2toc[tag] = self._get_sort_sub_toc(notes)
        # for notes in tag2notes.values():
        #     notes.sort(key=lambda e: (e.info.level, e.tag_toc_line), reverse=True)
        # for tag, notes in tag2notes.items():
        #     tag2toc[tag] = [e.tag_toc_line for e in notes]

        return tag2toc, paper_toc

    def build_v2(self):
        with self._fp_notes_readme_temp_v2.open(encoding='utf8') as f:
            txt = f.read()
            self._set_recent_limit(txt)
            self._get_available_tags(txt)

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

        # replace template
        txt = ReadmeUtils.replace_tag_content('recent', txt, self.recent_toc)
        for tag, toc in tag2toc.items():
            if tag == 'paper':
                toc_str = '\n'.join(paper_toc)
            else:
                toc_str = '\n'.join(toc)
            txt = txt.replace(f'{{{{{tag}}}}}', toc_str)

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

        shutil.copy2(getattr(self, f'_fp_notes_readme_{version}'), self._fp_notes_readme)

    @property
    def toc_append(self):
        with self._fp_notes_readme.open(encoding='utf8') as f:
            return RE.note_toc.search(f.read()).group(1).strip()  # type: ignore

    @property
    def recent_toc(self):
        return TEMP_main_readme_notes_recent_toc.format(
            toc_top='\n'.join([n.get_toc_line_relative_to(self._fp_notes) for n in self.notes_top]),
            toc_recent='\n'.join([n.get_toc_line_relative_to(self._fp_notes) for n in self.notes_recent]),
        )

    @property
    def recent_toc_append(self):
        return TEMP_main_readme_notes_recent_toc.format(
            toc_top='\n'.join([n.toc_line_relative_to_repo for n in self.notes_top]),
            toc_recent='\n'.join([n.toc_line_relative_to_repo for n in self.notes_recent]),
        )

    @property
    def readme_append(self):
        with self._fp_notes_readme.open(encoding='utf8') as f:
            # content = RE.note_content.search(f.read()).group(1).strip()
            # return content.replace('](', f']({self._fp_notes.name}/')
            txt = f.read()
        txt = ReadmeUtils.get_tag_content('notes', txt)
        return txt.replace('](', f']({self._fp_notes.name}/')  # type: ignore


if __name__ == '__main__':
    """"""
    _DEBUG = True
    note = NotesBuilder()
    note.build()
