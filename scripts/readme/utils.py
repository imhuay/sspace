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

import difflib
import os
import re
import subprocess
from dataclasses import dataclass, fields
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING, List, Tuple

import emoji
import regex
import yaml
from markdown.extensions import toc
from markdown_it import MarkdownIt

from huaytools.utils import get_logger

if TYPE_CHECKING:
    from .notes import Note

logger = get_logger()
_md = MarkdownIt('commonmark')


@dataclass
class KeywordSection:
    """"""

    content: str
    name: str = ''
    head_name: str = ''
    url: str = ''

    def __post_init__(self):
        tokens = _md.parse(self.content)
        is_heading = False
        for t in tokens:
            if t.type == 'html_block' and 'keyword_info' in t.content:
                info_str = NoteUtils.get_annotation('keyword_info', t.content)
                info_str = '\n'.join([ln.lstrip() for ln in info_str.split('\n')]) if info_str else ''
                info = yaml.safe_load(info_str) if info_str else {}
                self.name = info.get('name', '')
                if info.get('extra_url', False):
                    links = MarkdownUtils.extract_markdown_links(self.content)
                    if links:
                        self.url = links[0]['url']
            if t.type == 'heading_open':
                is_heading = True
            elif t.type == 'heading_close':
                is_heading = False
            elif is_heading and t.type == 'inline':
                self.head_name = t.content

        if not self.name:
            self.name = self.head_name

    @property
    def slugify_name(self):
        return MarkdownUtils.slugify(self.head_name)


class MarkdownUtils:
    """"""

    @staticmethod
    def get_relpath_from_p1_to_p2(p1: Path, p2: Path) -> Path:
        """"""
        if p1.is_file():
            p1 = p1.parent
        return Path(os.path.relpath(p2, start=p1))

    @staticmethod
    def slugify(value, mode='github', separator='-'):
        if mode == 'github':
            return MarkdownUtils.slugify_github(value)
        return toc.slugify_unicode(value, separator)  # 无法处理部分由多个 Unicode 码点组成 emoji
        # 以下方法也不能处理
        # value = emoji.replace_emoji(value, '')  # 移除 emoji
        # value = re.sub(r'[^\w\s-]', '', value).strip().lower()
        # return re.sub(r'[{}\s]+'.format(separator), separator, value)

    @staticmethod
    def slugify_github(raw: str) -> str:
        """
        精确复现 GitHub 的 slugify 策略：
            1. mdInlineToPlainText：去除图片和 HTML inline，拼接文本
            2. 用 Unicode 正则去除所有非字母/数字/下划线/连字符/空格的字符
            3. 全部转小写（与 toLowerCase 等价）
            4. 将空格替换为连字符
        """

        def _md_inline_to_plain_text(text: str) -> str:
            """
            将 Markdown inline 结构转换为纯文本：
            - 使用 markdown-it-py 的 parseInline 方法
            - 跳过 image 和 html_inline 类型的 token
            - 其余 token.content 串接输出
            """
            env = {}
            # parseInline 返回 [blockToken], blockToken.children 存放 inline token
            inline_tokens = _md.parseInline(text, env)[0].children or []
            result = []
            for token in inline_tokens:
                if token.type in ('image', 'html_inline'):
                    continue
                result.append(token.content)
            return ''.join(result)

        # 1. 提取纯文本
        text = _md_inline_to_plain_text(raw)
        # 2. 移除指定标点
        #    [^\p{L}\p{M}\p{Nd}\p{Nl}\p{Pc}\- ] 匹配所有非字母/标记/数字/下划线/连字符/空格字符
        text = regex.sub(r'[^\p{L}\p{M}\p{Nd}\p{Nl}\p{Pc}\- ]+', '', text)
        # 3. 小写
        text = text.lower()
        # 4. 空格转连字符
        return text.replace(' ', '-')

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
            result.append({'text': link_text.strip(), 'url': link_url.strip(), 'full': f'[{link_text}]({link_url})'})

        return result

    @staticmethod
    def normalize_text(text: str, skip_block: list | None = None) -> str:
        """文本规范化

        要求:
            1. 行尾空格处理
                如果一行全是空格, 则全部移除
                如果行尾只有一个空格, 移除
                如果有两个以上空格, 保留 2 个
            2. 中文标点处理: ，。！？；：“”‘’（）
                如果在行内, 将 "中文标点+可能得空格" 替换为 "英文标点 + 一个空格"
                如果在行尾, 将 "中文标点+可能得空格" 替换为 "英文标点"
        """
        punc_map = {
            '，': ',',
            '。': '.',
            '！': '!',
            '？': '?',
            '；': ';',
            '：': ':',
        }
        quo_punc_map = {
            ('“', '”'): ('"', '"'),
            ('‘', '’'): ("'", "'"),
            ('（', '）'): ('(', ')'),
        }

        if skip_block is None:
            skip_block = [
                '```',  # 代码块
                '$$',  # 行间公式
                (r'\[', r'\]'),  # 行间公式
                ('<!--', '-->'),  # HTML 注释
            ]

        skip_block = [(it, it) if isinstance(it, str) else it for it in skip_block]

        lines = text.split('\n')
        in_block = False
        cur_block = None
        line_block = False
        for i in range(len(lines)):
            line = lines[i]

            for b_start, b_end in skip_block:
                if (
                    line.lstrip().startswith(b_start)
                    and line.rstrip().endswith(b_end)
                    and len(line.strip()) > len(b_start) + len(b_end)
                ):
                    line_block = True
                    break

            if line_block:
                line_block = False
                continue

            if cur_block is None:
                for b_start, b_end in skip_block:
                    if line.lstrip().startswith(b_start):
                        in_block = True
                        cur_block = (b_start, b_end)
                        break
            else:
                b_start, b_end = cur_block
                if line.lstrip().endswith(b_end):
                    in_block = False
                    cur_block = None

            if in_block:
                continue

            if line.strip() == '':
                lines[i] = ''
                continue

            # 1. 中文标点处理
            for cn_punc, en_punc in punc_map.items():
                line = re.sub(rf'\s*{cn_punc}\s*', f'{en_punc} ', line)
            # 处理成对的中文引号和括号
            for (cn_left, cn_right), (en_left, en_right) in quo_punc_map.items():
                line = re.sub(rf'\s*{cn_left}\s*(.*?)\s*{cn_right}\s*', f' {en_left}\\1{en_right} ', line)
            for _, en_right in quo_punc_map.values():
                for seg_punc in punc_map.values():
                    line = re.sub(rf'{re.escape(en_right)}\s*{re.escape(seg_punc)}', f'{en_right}{seg_punc}', line)

            # 2. 空格处理
            if line.endswith('  '):
                line = line.rstrip() + '  '

            # 3. 为 ##, ### 开头的行添加分割线
            # if re.match(r'^(#{2,3})\s*', line):
            #     has_hr = False
            #     j = i - 1
            #     while j > 0:
            #         if lines[j].startswith('---'):
            #             has_hr = True
            #             break
            #         elif lines[j].strip() != '':
            #             break
            #         j -= 1
            #     if not has_hr:
            #         line = '---\n\n' + line

            lines[i] = line

        text = '\n'.join(lines)

        return text

    @staticmethod
    def print_diffs_with_context(a: str, b: str, l_context=0, r_context=10):
        # 使用 SequenceMatcher 找出差异块
        matcher = difflib.SequenceMatcher(None, a, b)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag != 'equal':
                # 从原文和新文中截取差异前后 context 个字符
                a_start = max(i1 - l_context, 0)
                a_end = min(i2 + r_context, len(a))
                b_start = max(j1 - l_context, 0)
                b_end = min(j2 + r_context, len(b))

                old_seg = a[a_start:a_end]
                new_seg = b[b_start:b_end]

                print(f'=== 差异类型: {tag} ===')
                print(f'旧内容: {repr(old_seg)}')
                print('旧内容 Unicode:', ' '.join(f'U+{ord(ch):04X}' for ch in old_seg))
                print(f'新内容: {repr(new_seg)}')
                print('新内容 Unicode:', ' '.join(f'U+{ord(ch):04X}' for ch in new_seg))
                print()

    @staticmethod
    def add_spaces_around_parentheses(text: str) -> str:
        # 1) Protect Markdown links (both [alt](url) and ![alt](url))
        link_pat = regex.compile(r'!?\[[^\]]*\]\([^)]*\)')
        placeholders = []

        def protect(m):
            placeholders.append(m.group(0))
            return f'@@LINK_{len(placeholders) - 1}@@'

        protected = link_pat.sub(protect, text)

        # 2) Recursive parentheses pattern: matches nested (...) structures
        paren_pat = regex.compile(r'\((?:[^()]+|(?R))*\)')

        def repl(m):
            # Extract inner content
            inner = m.group(0)[1:-1].strip()
            # Recursively format any nested parentheses inside inner first
            inner_processed = paren_pat.sub(repl, inner)
            # Wrap with spaces
            return f'( {inner_processed} )'

        processed = paren_pat.sub(repl, protected)

        # 3) Restore links
        def restore(m):
            return placeholders[int(m.group(1))]

        return regex.sub(r'@@LINK_(\d+)@@', restore, processed)

    @staticmethod
    def _normalize_text_spaces(text: str) -> str:
        """Normalize spaces in plain text (not code), preserving leading spaces."""
        # 保留行首空格
        leading = len(text) - len(text.lstrip(' '))
        prefix = ' ' * leading
        remainder = text[leading:]

        # 检查结尾空格
        trailing_spaces = len(remainder) - len(remainder.rstrip(' '))
        keep_two = trailing_spaces >= 2

        core = remainder.rstrip(' ')
        core = re.sub(r' +', ' ', core)

        if keep_two:
            core += '  '
        return prefix + core

    @staticmethod
    def normalize_markdown_spaces(md_text: str) -> str:
        """Normalize spaces in Markdown, skipping fenced and inline code regions,
        and preserving leading spaces.

        - Lines within fenced code blocks (``` ... ```) are left unchanged.
        - Inline code spans delimited by backticks are preserved unchanged.
        - Other text lines are normalized by replacing consecutive spaces with one,
          while preserving two trailing spaces when originally two or more.
        - Leading spaces are always preserved.
        """
        md = MarkdownIt()
        tokens = md.parse(md_text)

        out_lines: List[str] = []

        for tok in tokens:
            if tok.type in ('fence', 'code_block', 'code_inline'):
                # 保持原样
                if tok.type == 'fence':
                    # 还原完整围栏
                    out_lines.append(f'{tok.markup}{tok.info}\n{tok.content}{tok.markup}')
                else:
                    out_lines.append(tok.content)
            elif tok.type == 'inline':
                parts = []
                for child in tok.children or []:
                    if child.type == 'text':
                        parts.append(MarkdownUtils._normalize_text_spaces(child.content))
                    else:
                        parts.append(child.content)
                out_lines.append(''.join(parts))
            elif tok.type == 'text':
                out_lines.append(MarkdownUtils._normalize_text_spaces(tok.content))
            else:
                # 其它 token（段落、标题等）
                if tok.content:
                    out_lines.append(tok.content)
                else:
                    out_lines.append(tok.markup)

        return '\n'.join(out_lines)


class NoteUtils:
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
        command = NoteUtils.GIT_ADD_TEMP.format(fp=fp.resolve())
        code = os.system(command)
        NoteUtils._log_command(code, command)

    GIT_MV_TEMP = 'git mv "{old_fp}" "{new_fp}"'

    @staticmethod
    def git_mv(old_fp: Path, new_fp: Path):
        NoteUtils.git_add(old_fp)
        command = NoteUtils.GIT_MV_TEMP.format(old_fp=old_fp.resolve(), new_fp=new_fp.resolve())
        code = os.system(command)
        NoteUtils._log_command(code, command)

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
        _, date_str = subprocess.getstatusoutput(f'{NoteUtils.TEMP_GIT_LOG_FOLLOW.format(fp=fp)} | tail -1')
        return NoteUtils.get_date_str(date_str, fmt)

    @staticmethod
    def get_last_commit_date(fp, fmt='%Y-%m-%d %H:%M:%S') -> str:
        _, date_str = subprocess.getstatusoutput(f'{NoteUtils.TEMP_GIT_LOG_FOLLOW.format(fp=fp)} | head -1')
        return NoteUtils.get_date_str(date_str, fmt)

    @staticmethod
    def get_date_str(iso_date_str: str, fmt):
        if not iso_date_str:
            dt = datetime.now(NoteUtils.BJS)
        else:
            dt = datetime.fromisoformat(iso_date_str)
            dt.astimezone(NoteUtils.BJS)
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
    SECTION_ANNOTATION = r'<!--{tag}\s*\n(.*?)\n\s*-->'
    TEMP_LAST_MODIFY_BADGE = '![last modify](https://img.shields.io/static/v1?label=last%20modify&message={datetime}&color=yellowgreen&style=flat-square)'  # noqa
    TEMP_BADGE_URL = 'https://img.shields.io/static/v1?{}'

    @staticmethod
    def section_exists(tag, txt) -> bool:
        return NoteUtils.get_section_begin(tag) in txt

    @staticmethod
    def get_section_begin(tag):
        return NoteUtils.SECTION_START.format(tag=tag)

    @staticmethod
    def get_section_end(tag):
        return NoteUtils.SECTION_END.format(tag=tag)

    @staticmethod
    def replace_tag_content(tag, txt, content, count=1) -> str:
        """"""
        re_pattern = NoteUtils._get_section_re_pattern(tag)
        repl = f'{NoteUtils.get_section_begin(tag)}\n{content}\n{NoteUtils.get_section_end(tag)}'
        return re_pattern.sub(repl, txt, count=count)

    @staticmethod
    def get_last_modify_badge_url(fp: Path, color: str = 'thistle') -> str:
        return NoteUtils.get_badge(
            label='last modify',
            message=NoteUtils.get_last_commit_date(fp),
            color=color,
            style='flat-square',
        )

    @staticmethod
    def get_create_date_badge_url(date: datetime | None, fp: Path, color: str = 'lightsteelblue') -> str:
        if date is None:
            date_s = '-'.join(fp.relative_to(args.fp_notes_archives).parts[:2]) + '-xx'
        else:
            date_s = date.strftime('%Y-%m-%d')
        return NoteUtils.get_badge(
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
            'labelColor': label_color,
            'color': color,
            'style': style,
        }
        if not label:
            parameters.pop('labelColor')

        parameters.update(options)
        # parameters = {k: quote(str(v)) for k, v in parameters.items()}
        badge_url = NoteUtils.TEMP_BADGE_URL.format('&'.join([f'{k}={v}' for k, v in parameters.items()]))
        if url is None:
            return f'![{label}]({badge_url})'
        else:
            return f'[![{label}]({badge_url})]({url})'

    @staticmethod
    def get_section_content(name, txt) -> str | None:
        """
        <!--START_SECTION:{name}-->
        <content>
        <!--END_SECTION:{name}-->
        """
        re_pattern = NoteUtils._get_section_re_pattern(name)
        m = re_pattern.search(txt)
        if not m:
            return None
        return m.group(1).strip()

    @staticmethod
    def findall_section(name, txt) -> list[str]:
        """
        <!--START_SECTION:{name}-->
        <content>
        <!--END_SECTION:{name}-->
        """
        re_pattern = NoteUtils._get_section_re_pattern(name)
        return [m.group(1).strip() for m in re_pattern.finditer(txt) if m]

    @staticmethod
    def _get_section_re_pattern(tag):
        return re.compile(
            rf'{NoteUtils.get_section_begin(tag)}(.*?){NoteUtils.get_section_end(tag)}',
            flags=re.DOTALL,
        )

    @staticmethod
    def get_annotation(name, txt) -> str | None:
        """
        <!--<name>
        <info>
        -->
        """
        re_pattern = re.compile(NoteUtils.SECTION_ANNOTATION.format(tag=name), flags=re.DOTALL)
        m = re_pattern.search(txt)
        if m:
            return m.group(1).strip()
        return None

    @staticmethod
    def get_annotation_info(txt) -> str | None:
        """"""
        return NoteUtils.get_annotation('info', txt)

    @staticmethod
    def get_annotation_info_v2(note: Note) -> dict:
        """"""
        info_str = NoteUtils.get_annotation_info(note.text)
        if info_str is None:
            # raise ValueError(f'Note info not found: {note.path}')
            return dict()
        info = yaml.safe_load(info_str)
        return info

    @staticmethod
    def get_keyword_section(txt: str) -> KeywordSection:
        """从 Markdown 标题中提取纯文本内容，去除标题标记和内联格式"""
        # 使用 Markdown-It 解析器
        section = KeywordSection(txt)
        return section


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

    # template
    temp_badge_todo_logo_check = '<img src="https://custom-icon-badges.demolab.com/static/v1?label=&message={num_todo}&labelColor=E05D44&color=E05D44&style=flat-square&logoSource=feather&logo=check-square&logoColor=white" height="17"/>'
    temp_badge_todo_logo_edit = '<img src="https://custom-icon-badges.demolab.com/static/v1?label=&message={num_todo}&labelColor=E05D44&color=E05D44&style=flat-square&logoSource=feather&logo=edit&logoColor=white" height="17"/>'
    temp_badge_todo_logo_edit_h = '<img src="https://custom-icon-badges.demolab.com/static/v1?label=&message={num_todo}&labelColor=E05D44&color=E05D44&style=flat-square&logoSource=feather&logo=edit&logoColor=white" height="{height}"/>'

    @staticmethod
    def get_temp_badge_todo_logo(count: int, height: int, color: str = 'E05D44', href: str = '#') -> str:
        """"""
        return f'<a href="{href}"><img src="https://custom-icon-badges.demolab.com/static/v1?label=&message={count}&labelColor={color}&color={color}&style=flat-square&logoSource=feather&logo=edit&logoColor=white" height="{height}"/></a>'
        


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
