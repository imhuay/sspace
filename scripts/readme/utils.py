#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2022-10-03 23:53
Author:
    huayang (imhuay@163.com)
Subject:
    utils
"""

from __future__ import annotations

import os
import re
import subprocess
from dataclasses import dataclass, fields
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING

import yaml
from markdown.extensions import toc
from markdown_it import MarkdownIt

from huaytools.utils import get_logger

if TYPE_CHECKING:
    from .notes import Note

logger = get_logger()


class MarkdownUtils:
    @staticmethod
    def slugify(head):
        return toc.slugify_unicode(head, '-')  # noqa

    @staticmethod
    def extract_markdown_links(text) -> list[dict]:
        """
        从文本中提取所有 Markdown 格式的链接 [text](url)
        返回包含字典的列表
        """
        # 正则表达式模式：匹配 [文本](链接)
        # pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        pattern = r'\[(.*?)\]\((.*?)\)'

        matches = re.findall(pattern, text)

        result = []
        for link_text, link_url in matches:
            result.append(
                {'text': link_text.strip(), 'url': link_url.strip(), 'full': f'[{link_text}]({link_url})'}
            )

        return result

    @staticmethod
    def get_head_title(head: str) -> str:
        """从 Markdown 标题中提取纯文本内容，去除标题标记和内联格式"""
        # 使用 Markdown-It 解析器
        md = MarkdownIt()
        tokens = md.parse(head)
        for t in tokens:
            if t.type == 'inline':
                return t.content
        return ''


class ReadmeUtils:
    BJS = timezone(
        timedelta(hours=8),
        name='Asia/Beijing',
    )

    @staticmethod
    def norm(txt: str):
        return txt.lower()

    GIT_ADD_TEMP = 'git add "{fp}"'

    @staticmethod
    def git_add(fp: Path):
        """不再使用，通过 git add -u 代替"""
        command = ReadmeUtils.GIT_ADD_TEMP.format(fp=fp.resolve())
        code = os.system(command)
        ReadmeUtils._log_command(code, command)

    GIT_MV_TEMP = 'git mv "{old_fp}" "{new_fp}"'

    @staticmethod
    def git_mv(old_fp: Path, new_fp: Path):
        ReadmeUtils.git_add(old_fp)
        command = ReadmeUtils.GIT_MV_TEMP.format(old_fp=old_fp.resolve(), new_fp=new_fp.resolve())
        code = os.system(command)
        ReadmeUtils._log_command(code, command)

    @staticmethod
    def _log_command(code, command):
        if code == 0:
            logger.info(command)
        else:
            logger.error(command)

    # @staticmethod
    # def _get_file_commit_date(fp, first_commit=True, return_datetime=False) -> str | datetime:
    #     tail_or_head = 'tail' if first_commit else 'head'
    #     code, date_str = subprocess.getstatusoutput(
    #         f'git log --follow --format=%ad --date=iso-strict "{fp}" | {tail_or_head} -1')
    #     if code != 0:
    #         raise ValueError(f'{ReadmeUtils._get_file_commit_date.__name__}: {fp}')
    #     if return_datetime:
    #         return datetime.fromisoformat(date_str)
    #     return date_str

    # @staticmethod
    # def get_file_first_commit_date(fp, return_datetime=False) -> str | datetime:
    #     return ReadmeUtils._get_file_commit_date(fp, first_commit=True, return_datetime=return_datetime)

    # TEMP_GIT_LOG_FOLLOW = r'git log --invert-grep --grep="Auto\|AUTO\|auto" --format=%ad --date=iso-strict --follow "{fp}"'  # noqa
    TEMP_GIT_LOG_FOLLOW = (
        r'git log --author=imhuay --invert-grep --grep="Auto\|AUTO"'
        r' --format=%ad --date=iso-strict --follow "{fp}"'
    )

    @staticmethod
    def get_first_commit_date(fp, fmt='%Y-%m-%d %H:%M:%S') -> str:
        _, date_str = subprocess.getstatusoutput(f'{ReadmeUtils.TEMP_GIT_LOG_FOLLOW.format(fp=fp)} | tail -1')
        return ReadmeUtils.get_date_str(date_str, fmt)

    @staticmethod
    def get_last_commit_date(fp, fmt='%Y-%m-%d %H:%M:%S') -> str:
        _, date_str = subprocess.getstatusoutput(f'{ReadmeUtils.TEMP_GIT_LOG_FOLLOW.format(fp=fp)} | head -1')
        return ReadmeUtils.get_date_str(date_str, fmt)

    @staticmethod
    def get_date_str(iso_date_str: str, fmt):
        if not iso_date_str:
            dt = datetime.now(ReadmeUtils.BJS)
        else:
            dt = datetime.fromisoformat(iso_date_str)
            dt.astimezone(ReadmeUtils.BJS)
        return dt.strftime(fmt)

    # @staticmethod
    # def get_file_last_commit_date(fp, return_datetime=False) -> str | datetime:
    #     return ReadmeUtils._get_file_commit_date(fp, first_commit=False, return_datetime=return_datetime)

    # RE_WAKATIME = re.compile(r'<!--START_SECTION:waka-->[\s\S]+<!--END_SECTION:waka-->')

    # @staticmethod
    # def extract_wakatime(txt) -> str:
    #     return ReadmeUtils.RE_WAKATIME.search(txt).group()

    SECTION_START = '<!--START_SECTION:{tag}-->'
    SECTION_END = '<!--END_SECTION:{tag}-->'
    SECTION_ANNOTATION = r'<!--{tag}\n(.*?)\n-->'
    TEMP_LAST_MODIFY_BADGE = '![last modify](https://img.shields.io/static/v1?label=last%20modify&message={datetime}&color=yellowgreen&style=flat-square)'  # noqa
    TEMP_BADGE_URL = 'https://img.shields.io/static/v1?{}'

    @staticmethod
    def get_tag_begin(tag):
        return ReadmeUtils.SECTION_START.format(tag=tag)

    @staticmethod
    def get_tag_end(tag):
        return ReadmeUtils.SECTION_END.format(tag=tag)

    @staticmethod
    def replace_tag_content(tag, txt, content) -> str:
        """"""
        re_pattern = ReadmeUtils._get_section_re_pattern(tag)
        repl = f'{ReadmeUtils.get_tag_begin(tag)}\n\n{content}\n\n{ReadmeUtils.get_tag_end(tag)}'
        return re_pattern.sub(repl, txt, count=1)

    @staticmethod
    def get_last_modify_badge_url(fp: Path, color: str = 'thistle') -> str:
        return ReadmeUtils.get_badge(
            label='last modify',
            message=ReadmeUtils.get_last_commit_date(fp),
            color=color,
            style='flat-square',
        )

    @staticmethod
    def get_create_date_badge_url(date: datetime | None, fp: Path, color: str = 'lightsteelblue') -> str:
        if date is None:
            date_s = '-'.join(fp.relative_to(args.fp_notes_archives).parts[:2]) + '-xx'
        else:
            date_s = date.strftime('%Y-%m-%d')
        return ReadmeUtils.get_badge(
            label='create date',
            message=date_s,
            color=color,
            style='flat-square',
        )

    @staticmethod
    def get_badge(label, message, color, label_color='gray', style='flat-square', url=None, **options):
        from urllib.parse import quote

        parameters = {
            'label': quote(str(label)),
            'message': quote(str(message)),
            'label_color': label_color,
            'color': color,
            'style': style,
        }
        parameters.update(options)
        # parameters = {k: quote(str(v)) for k, v in parameters.items()}
        badge_url = ReadmeUtils.TEMP_BADGE_URL.format('&'.join([f'{k}={v}' for k, v in parameters.items()]))
        if url is None:
            return f'![{label}]({badge_url})'
        else:
            return f'[![{label}]({badge_url})]({url})'

    @staticmethod
    def get_tag_content(tag, txt) -> str | None:
        """
        <!--START_SECTION:{tag}-->
        <content>
        <!--END_SECTION:{tag}-->
        """
        re_pattern = ReadmeUtils._get_section_re_pattern(tag)
        m = re_pattern.search(txt)
        if not m:
            return None
        return m.group(1).strip()

    @staticmethod
    def findall_tag_content(tag, txt) -> list[str]:
        """
        <!--START_SECTION:{tag}-->
        <content>
        <!--END_SECTION:{tag}-->
        """
        re_pattern = ReadmeUtils._get_section_re_pattern(tag)
        return [m.group(1).strip() for m in re_pattern.finditer(txt) if m]

    @staticmethod
    def _get_section_re_pattern(tag):
        return re.compile(
            rf'{ReadmeUtils.get_tag_begin(tag)}(.*?){ReadmeUtils.get_tag_end(tag)}',
            flags=re.DOTALL,
        )

    @staticmethod
    def get_annotation(tag, txt) -> str | None:
        """
        <!--<tag>
        <info>
        -->
        """
        re_pattern = re.compile(ReadmeUtils.SECTION_ANNOTATION.format(tag=tag), flags=re.DOTALL)
        m = re_pattern.search(txt)
        if m:
            return m.group(1).strip()
        return None

    @staticmethod
    def get_annotation_info(txt) -> str | None:
        """"""
        return ReadmeUtils.get_annotation('info', txt)

    @staticmethod
    def get_annotation_info_v2(note: Note) -> dict:
        """"""
        info_str = ReadmeUtils.get_annotation_info(note.text)
        if info_str is None:
            # raise ValueError(f'Note info not found: {note.path}')
            return dict()
        info = yaml.safe_load(info_str)
        return info


@dataclass
class ReadmeTag:
    index: str | None = None
    recent: str | None = None
    algorithms: str | None = None
    notes: str | None = None
    waka: str | None = None

    def __post_init__(self):
        for f in fields(self):
            setattr(self, f.name, f.name)


readme_tag = ReadmeTag()


class args:  # noqa
    """"""

    _fp_cur_file = Path(__file__)
    # repo
    fp_repo = Path(_fp_cur_file.parent / '../..').resolve()
    fp_repo_readme = fp_repo / 'README.md'

    # algorithms
    fp_algorithms = Path(fp_repo / 'algorithms')
    fp_algorithms_readme = fp_algorithms / 'README.md'
    fp_algorithms_problems = fp_algorithms / 'problems'
    fp_algorithms_tag_info = fp_algorithms / 'tag_info.yml'
    algorithms_readme_title = 'Algorithm Codings'

    # notes
    fp_notes = Path(fp_repo / 'notes')
    fp_notes_archives = fp_notes / '_archives'
    fp_notes_readme_temp = fp_notes / 'README_template.md'
    fp_notes_readme = fp_notes / 'README.md'

    fp_notes_readme_dev = fp_notes / 'README_dev.md'
    fp_notes_readme_v1 = fp_notes / 'README_v1.md'
    fp_notes_readme_temp_v1 = fp_notes / 'README_template_v1.md'
    fp_notes_readme_v2 = fp_notes / 'README_v2.md'
    fp_notes_readme_temp_v2 = fp_notes / 'README_template_v2.md'
    fp_tags = fp_notes / '_tags.json'
    notes_top_limit = None


TEMP_main_readme_notes_recent_toc = """{toc_top}
{toc_recent}
"""

TEMP_main_readme_algorithms_concat = """## {title}

{toc}
"""

TEMP_algorithm_toc_td_category = '<td width="1000" valign="top">\n\n{sub_toc}\n\n</td>'
TEMP_algorithm_toc_table = """<table>  <!-- invalid: frame="void", style="width: 100%; border: none; background: none" -->
<tr>
<td colspan="2" valign="top" width="1000">

{toc_hot}

</td>
<td colspan="2" rowspan="3" valign="top" width="1000">

{toc_subject}

</td>
</tr>
<tr></tr>
<tr>
<td colspan="2" valign="top">

{toc_level}

</td>
</tr>
<tr></tr>
<tr>  <!-- loop TMP_TOC_TD_CATEGORY -->

{toc_category}

</tr>
</table>"""

TEMP_algorithm_readme = """# {title}

{toc}

---

{sub_toc}"""
