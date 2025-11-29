#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2022-09-28 20:19
Author:
    huayang (imhuay@163.com)
Subject:
    algo
"""

from __future__ import annotations

import os
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar

import yaml
from _base import Builder
from utils import MarkdownUtils, NoteUtils, args

if TYPE_CHECKING:
    from notes import Note


@dataclass(unsafe_hash=True)
class Tag:
    name: str
    type: str
    is_hot: bool = False
    add_to_collection: bool = False
    aliases: list[str] = field(default_factory=list, hash=False)
    notes: list[str] = field(default_factory=list, hash=False)
    _problems: list[Problem] = field(default_factory=list, hash=False)

    def add_problem(self, p: Problem):
        self._problems.append(p)

    @property
    def problems(self) -> list[Problem]:
        return sorted(set(self._problems), key=lambda i: i.sort_key)

    def __post_init__(self):
        self.aliases.insert(0, self.name)
        self.aliases = sorted(set(self.aliases), key=self.aliases.index)

    @property
    def title(self):
        return self.name

    @property
    def count(self):
        return len(self.problems)

    @property
    def toc_title(self):
        # return f'{self.title} (`{self.count}`)'
        return self.title

    @property
    def toc_line(self):
        # return f'- [{self.title} ({self.count})](#{MarkdownUtils.slugify(self.toc_title)})'
        return f'- [{self.title} <sup>({self.count})</sup>](#{MarkdownUtils.slugify(self.toc_title)})'

    @property
    def toc(self):
        lns = [f'### {self.toc_title}']
        # if self.notes:
        #     lns.append('- **相关笔记** 🔗')
        #     for n in self.notes:
        #         _p = Path(n)
        #         lns.append(f'    - [{_p.stem}](../notes/_archives/{_p})')
        #     lns.append('')
        lns.append(NoteUtils.get_badge('total', self.count, 'blue'))
        for p in self.problems:
            lns.append(p.toc_line)
        return '\n'.join(lns)

    @property
    def sort_key(self):
        return self.count, self.name


@dataclass()
class TagType:
    name: str
    priority: int
    tags: list[Tag] = field(default_factory=list, hash=False)

    @property
    def toc(self):
        lns = []
        for tag in self.sorted_tags:
            lns.append(tag.toc_line)
        return '\n'.join(lns)

    @property
    def sorted_tags(self):
        return sorted(self.tags, key=lambda i: i.sort_key, reverse=True)


class TagInfo:
    # name2key: dict[str, str] = dict()
    # key2tag: dict[str, Tag] = dict()
    tags: list[Tag] = list()
    alias2tags: dict[str, list[Tag]] = defaultdict(list)
    type2tags: dict[str, TagType] = dict()
    hot_tags: list[Tag] = []

    TYPE_COLLECTION: str = 'collection'

    def __init__(self):
        self._fp_tag_info = args.fp_algorithms_tag_info

        self._load_tag_info()

    def _load_tag_info(self):
        with self._fp_tag_info.open(encoding='utf8') as f:
            _tag_info: list[dict] = yaml.safe_load(f.read())

        for it in _tag_info:
            tag_type: str = it['tag_type']
            priority: int = int(it['priority'])
            self.type2tags[tag_type] = TagType(tag_type, priority)
            tags: dict = it['tags']
            for name, info in tags.items():
                info = info or dict()
                info.setdefault('name', name)
                info.setdefault('type', tag_type)
                tag = Tag(**info)
                self.tags.append(tag)
                self.type2tags[tag_type].tags.append(tag)
                if tag.is_hot:
                    self.hot_tags.append(tag)
                if tag.add_to_collection:
                    self.type2tags[self.TYPE_COLLECTION].tags.append(tag)
                for alias in tag.aliases:
                    self.alias2tags[NoteUtils.norm(alias)].append(tag)

    @property
    def hot_tags_sorted(self):
        return sorted(self.hot_tags, key=lambda i: i.sort_key, reverse=True)

    def get_formal_tags(self, tags: list[str]) -> list[Tag]:
        used = set()
        formal_tags = []
        for t in tags:
            for tag in self.alias2tags[NoteUtils.norm(t)]:
                if tag not in used:
                    used.add(tag)
                    formal_tags.append(tag)
        formal_tags = sorted(formal_tags, key=lambda e: e.name)
        return formal_tags

    def get_formal_tags_str(self, tags: list[str]) -> list[str]:
        return [t.name for t in self.get_formal_tags(tags)]

    def get_toc_lns_from_tags(self, tags: list[str], from_path: Path, skip_self: bool = True) -> list[str]:
        """"""
        lns = []
        for tag in tag_info.get_formal_tags(tags):
            l2p = defaultdict(list)
            for p in tag.problems:
                if skip_self and p.path.resolve() == from_path.resolve():
                    continue
                l2p[p.level].append(p)

            if l2p:
                cnt = tag.count - 1 if skip_self else tag.count
                lns.append(f'\n<details><summary><b>{tag.name} ({cnt})</b></summary>\n')
                l2p = sorted(l2p.items(), key=lambda i: i[0])
                for _, ps in l2p:
                    ps = sorted(ps, key=lambda i: i.relate_title)
                    for p in ps:
                        _p = MarkdownUtils.get_relpath_from_p1_to_p2(from_path, p.path)
                        lns.append(f'> [{p.relate_title}]({_p})  ')
                    lns.append('  > ')
                lns.append('\n</details>')

        return lns

    def get_toc_for_note(self, note: Note):
        """"""
        # lns = ['## 相关问题\n']
        lns = self.get_toc_lns_from_tags(note.algo_tags, note.path, skip_self=False)
        return '\n'.join(lns)


tag_info = TagInfo()


@dataclass(unsafe_hash=True)
class Problem:
    _path: Path

    # property
    _text = ''
    _info = None
    _file_name = ''
    _title = None
    _last_commit_time = None
    _formal_tags = None
    # _pre_p = None
    # _nxt_p = None

    _TAG_BADGE = 'badge'
    _TAG_RELATE_PROBLEM = 'relate_problem'
    _TAG_RELATE_NOTE = 'relate_note'

    def __post_init__(self):
        """"""
        self._path = self._path.resolve()

        with self._path.open(encoding='utf8') as f:
            self._text = f.read()

        self._norm_text()
        self._update_file()

        # 因为最后还要更新 relate 部分, 所以这里不写文件了
        # with self.path.open('w', encoding='utf8') as f:
        #     f.write(self._text)

    def _norm_text(self):
        """文本规范化"""
        new_text = MarkdownUtils.normalize_text(self._text)
        if new_text != self._text:
            self._text = new_text

    def _update_file(self):
        """"""
        if self._text is None:
            return

        txt = self._text

        # try update title
        lns = txt.rstrip().split('\n', maxsplit=1)

        if lns[0].startswith('##'):
            lns[0] = self.head
        else:
            lns.insert(0, self.head)

        lns[-1] = lns[-1].rstrip() + '\n'

        # 对没有 badge tag 做的兜底
        if not NoteUtils.get_section_content(self._TAG_BADGE, txt):
            lns.insert(1, NoteUtils.get_section_begin(self._TAG_BADGE))
            lns.insert(2, NoteUtils.get_section_end(self._TAG_BADGE))

        # 对没有 relate_note 做的兜底 (假设 relate_problem 一定存在)
        if not NoteUtils.section_exists(self._TAG_RELATE_NOTE, txt):
            _lns = lns[-1].split('\n')
            _idx = _lns.index(NoteUtils.get_section_begin(self._TAG_RELATE_PROBLEM))
            _lns.insert(_idx, '')
            _lns.insert(_idx, '')
            _lns.insert(_idx, NoteUtils.get_section_end(self._TAG_RELATE_NOTE))
            _lns.insert(_idx, NoteUtils.get_section_begin(self._TAG_RELATE_NOTE))
            lns[-1] = '\n'.join(_lns)

        # 对没有 relate_problem 做的兜底
        if not NoteUtils.section_exists(self._TAG_RELATE_PROBLEM, txt):
            lns.append('')
            lns.append(NoteUtils.get_section_begin(self._TAG_RELATE_PROBLEM))
            lns.append(NoteUtils.get_section_end(self._TAG_RELATE_PROBLEM))
        else:
            # 对 section_begin 之前没有空行做兜底
            _lns = lns[-1].split('\n')
            _idx = _lns.index(NoteUtils.get_section_begin(self._TAG_RELATE_PROBLEM))
            # 至少两个空行
            if _idx > 1 and (_lns[_idx - 1] != '' or _lns[_idx - 2] != ''):
                _lns.insert(_idx, '')
                if _lns[_idx - 1] != '':
                    _lns.insert(_idx, '')
            lns[-1] = '\n'.join(_lns)

        self._text = NoteUtils.replace_section_content(self._TAG_BADGE, '\n'.join(lns), self.badge_content)

    def set_relate_notes(self, notes: list[Note]):
        """"""
        lns = [
            '---\n',
            '### 算法笔记\n',
        ]

        # 主题相关的笔记
        relate_notes = []
        other_notes = []
        for note in notes:
            formal_tags_of_note = tag_info.get_formal_tags_str(note.algo_tags)
            _p = MarkdownUtils.get_relpath_from_p1_to_p2(self.path, note.path)
            if set(formal_tags_of_note) & set(self.formal_tags):
                relate_notes.append(f'- [{note.title}]({_p})  ')
            else:
                other_notes.append(f'- [{note.title}]({_p})  ')

        relate_notes = sorted(relate_notes)
        other_notes = sorted(other_notes)

        if relate_notes:
            lns.extend(relate_notes)
        else:
            lns.append('> 🌧️ _暂无主题相关的笔记_\n')

        if other_notes:
            lns.append('\n<details><summary><b>其他算法笔记</b></summary>\n')
            lns.extend(other_notes)
            lns.append('\n</details>')

        self._text = NoteUtils.replace_section_content(self._TAG_RELATE_NOTE, self._text, '\n'.join(lns))
        with self.path.open('w', encoding='utf8') as f:
            f.write(self._text)

    def set_relate_problems(self):
        """"""
        lns = [
            '---\n',
            '### 相关问题\n',
        ]
        lns += tag_info.get_toc_lns_from_tags(self.tags, self.path, skip_self=True)

        self._text = NoteUtils.replace_section_content(self._TAG_RELATE_PROBLEM, self._text, '\n'.join(lns))
        with self.path.open('w', encoding='utf8') as f:
            f.write(self._text)

    @property
    def badge_content(self):
        lns = [NoteUtils.get_last_modify_badge_url(self._path)]

        if self.level == '困难':
            color = 'red'
        elif self.level == '中等':
            color = 'yellow'
        else:
            color = 'green'
        lns.append(
            NoteUtils.get_badge(
                '',
                message=self.level,
                color=color,
                url=f'../../../README.md#{MarkdownUtils.slugify(self.level)}',
            )
        )
        lns.append(
            NoteUtils.get_badge(
                '',
                message=self.source,
                color='darkcyan',
                url=f'../../../README.md#{MarkdownUtils.slugify(self.source)}',
            )
        )

        for tag in tag_info.get_formal_tags(self.tags):
            lns.append(
                NoteUtils.get_badge(
                    '',
                    message=tag.name,
                    color='blue',
                    url=f'../../../README.md#{MarkdownUtils.slugify(tag.title)}',
                )
            )
        # used = set()
        # for t in self.tags:
        #     for tag in tag_info.alias2tags[NoteUtils.norm(t)]:
        #         if tag not in used:
        #             used.add(tag)
        #             lns.append(
        #                 NoteUtils.get_badge(
        #                     '',
        #                     message=tag.name,
        #                     color='blue',
        #                     url=f'../../../README.md#{MarkdownUtils.slugify(tag.title)}',
        #                 )
        #             )
        return '\n'.join(lns)

    # @property
    # def message_tags(self):
    #     return ', '.join([tag_info.alias2tag[ReadmeUtils.norm(tag)].name for tag in self.tags])

    @property
    def path(self):
        if self.file_name != self._path.name:
            new_path = self._path.parent / self.file_name
            NoteUtils.git_mv(self._path, new_path)
            self._path = new_path
        return self._path

    @property
    def title(self):
        # if self._title is None:
        #     self._title = '{name} ({src}, {level})'.format(name=self.name,
        #                                                    src=self.source,
        #                                                    level=self.level)
        # return self._title
        return self.name

    @property
    def relate_title(self):
        # tags = ', '.join(self.tags)
        if {'热门', '经典', 'lc100'}.isdisjoint(self.tags):
            return f'[{self.level}, {self.source}] {self.name}'
        else:
            return f'[{self.level}, {self.source}] {self.name} 🔥'

    @property
    def sort_key(self):
        return self.source, self.number

    @property
    def head(self):
        return f'## {self.title}'

    @property
    def toc_line(self):
        return f'- [`{self.path.stem}`]({self.path.relative_to(args.fp_algorithms)})'

    @property
    def last_commit_time(self):
        if self._last_commit_time is None:
            NoteUtils.get_last_commit_date(self.path)
        return self._last_commit_time

    @property
    def file_name(self):
        # if self._file_name is None:
        #     self._file_name = '{src}_{no}_{level}_{name}.md'.format(
        #         src=self.source, no=self.number, level=self.level, name=re.sub(r'\s+', '', self.name)
        #     )
        return self._file_name

    def set_file_name(self, max_no_len: int):
        """"""
        _name = re.sub(r'\s+', '', self.name)
        self._file_name = '{src}_{no}_{level}_{name}.md'.format(
            src=self.source, no=str.zfill(self.number, max_no_len), level=self.level, name=_name
        )

    @property
    def info(self):
        if self._info is None:
            with self._path.open(encoding='utf8') as f:
                txt = f.read()
            try:
                info_str = NoteUtils.get_annotation_info(txt)
                self._info = yaml.safe_load(info_str.strip())  # type: ignore
            except:  # noqa
                raise ValueError(self._path)
        return self._info

    @property
    def formal_tags(self) -> list[str]:
        if self._formal_tags is None:
            self._formal_tags = tag_info.get_formal_tags_str(self.tags)
        return self._formal_tags

    _F_TAGS: ClassVar[str] = 'tags'
    _F_SOURCE: ClassVar[str] = 'source'
    _F_NUMBER: ClassVar[str] = 'number'
    _F_LEVEL: ClassVar[str] = 'level'
    _F_NAME: ClassVar[str] = 'name'
    _F_COMPANIES: ClassVar[str] = 'companies'

    @property
    def tags(self) -> list[str]:
        return self.info[Problem._F_TAGS]

    @property
    def source(self) -> str:
        return self.info[Problem._F_SOURCE]

    @property
    def number(self) -> str:
        return self.info[Problem._F_NUMBER]

    @property
    def level(self) -> str:
        return self.info[Problem._F_LEVEL]

    @property
    def name(self) -> str:
        return self.info[Problem._F_NAME]

    @property
    def companies(self) -> list[str]:
        return self.info[Problem._F_COMPANIES]


class AlgorithmsBuilder(Builder):
    """"""

    problems: list[Problem]

    def __init__(self):
        self._fp_algo = args.fp_algorithms
        self._fp_algo_readme = args.fp_algorithms_readme
        self._fp_problems = args.fp_algorithms_problems

        self.alias2tags = tag_info.alias2tags
        self.type2tags = tag_info.type2tags
        self.title = args.algorithms_readme_title

        self._load_problems()

    def _load_problems(self):
        self.problems = []
        for dp, _, fns in os.walk(self._fp_problems):
            for fn in fns:
                fp = Path(dp) / fn  # each problem.md
                if fp.suffix != '.md':
                    continue
                p = Problem(fp)
                self.problems.append(p)

        for p in self.problems:
            [tag.add_problem(p) for tag in self.alias2tags[NoteUtils.norm(p.source)]]
            [tag.add_problem(p) for tag in self.alias2tags[NoteUtils.norm(p.level)]]
            for name in p.tags:
                [tag.add_problem(p) for tag in self.alias2tags[NoteUtils.norm(name)]]

        src_max_no_len = defaultdict(int)
        for p in self.problems:
            src_max_no_len[p.source] = max(src_max_no_len[p.source], len(p.info.get('number', '')))

        for p in self.problems:
            p.set_file_name(src_max_no_len[p.source])

    @property
    def hot_toc(self):
        lns = []
        for tag in tag_info.hot_tags_sorted:
            lns.append(tag.toc_line)
        return '\n'.join(lns)

    @property
    def problems_toc(self):
        lns = []
        # first_p, last_p = None, None
        for tag_type in sorted(self.type2tags.values(), key=lambda i: i.priority):
            # if first_p is None:
            # first_p = tag_type.sorted_tags[0].problems[0]
            for tag in tag_type.sorted_tags:
                lns.append(tag.toc)
                lns.append('')
                # last_p = tag.problems[-1]

        return '\n'.join(lns)

    @property
    def readme_append(self):
        with self._fp_algo_readme.open(encoding='utf8') as f:
            txt = f.read()
        section = NoteUtils.get_section_content('toc', txt)
        section = section.replace(  # type: ignore
            '## Algorithm Topics', '<details><summary><b>More Algorithm Topics 📚🧩🎲💡🚨</b></summary>', count=1
        )
        section += '\n</details>\n\n---'
        return section.replace('](', f']({self._fp_algo_readme.relative_to(args.fp_repo)}')  # type: ignore

    @property
    def toc_append(self):
        return f'- [{self.title}](#{MarkdownUtils.slugify(self.title)})'

    @property
    def head(self):
        return f'## {self.title}'

    COLL_TOP_LIMIT: int = 3

    def build(self):
        with self._fp_algo_readme.open(encoding='utf8') as f:
            txt = f.read()

        # title
        txt = NoteUtils.replace_section_content('head', txt, self.head)

        # hot
        txt = NoteUtils.replace_section_content('hot', txt, self.hot_toc)

        # tags toc
        for tag_type, info in self.type2tags.items():
            toc = info.toc
            if tag_type == TagInfo.TYPE_COLLECTION:
                lns = toc.split('\n')
                hot_lns = self.hot_toc.split('\n')
                coll_lines = [ln for ln in lns if ln not in hot_lns]
                coll_top3 = '\n'.join(coll_lines[: self.COLL_TOP_LIMIT])
                coll_left = '\n'.join(coll_lines[self.COLL_TOP_LIMIT :])
                txt = NoteUtils.replace_section_content(tag_type, txt, coll_top3)
                txt = NoteUtils.replace_section_content(f'{tag_type}_more', txt, coll_left)
            else:
                txt = NoteUtils.replace_section_content(tag_type, txt, toc)

        # problems toc
        txt = NoteUtils.replace_section_content('problems', txt, self.problems_toc)

        # update problems relate
        for p in self.problems:
            p.set_relate_problems()

        with self._fp_algo_readme.open('w', encoding='utf8') as f:
            f.write(txt)

    def set_relate_notes(self, notes: list[Note]):
        """"""
        for p in self.problems:
            p.set_relate_notes(notes)


if __name__ == '__main__':
    """"""
    algo = AlgorithmsBuilder()
    algo.build()
