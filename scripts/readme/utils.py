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
import shutil
import subprocess
import urllib.parse
from dataclasses import dataclass, fields
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, List, Literal, Tuple

import emoji
import regex
import yaml
from markdown.extensions import toc
from markdown_it import MarkdownIt

from huaytools.utils import get_logger, is_wsl

if TYPE_CHECKING:
    from .notes import Note

DEBUG = False
if is_wsl():
    DEBUG = True

logger = get_logger()
_md = MarkdownIt('commonmark')


@dataclass
class MathBlock:
    idx: int
    md_path: Path
    line_prefix: str
    already_img_block: bool
    tmp_save_dir: Path
    line_start_i: int
    line_end_i: int
    pre_line: str = ''
    nxt_line: str = ''
    content: str | None = None
    tex_file_path: Path | None = None
    svg_file_path: Path | None = None
    need_regen: bool = False

    _pad_size: ClassVar[int] = 3
    IMG_BLOCK_TEMP = "{line_prefix}<div align='center'><a href='{tex_file_path}'><img src='{svg_file_path}'/></a></div>"

    def __post_init__(self):
        """"""
        if not self.already_img_block:
            self.need_regen = True
        else:
            assert self.tex_file_path and self.svg_file_path
            if self._need_regeneration(self.tex_file_path, self.svg_file_path):
                self.need_regen = True

        if self.tex_file_path is not None and self.tex_file_path.exists():
            assert self.content is None
            self.content = self.tex_file_path.read_text(encoding='utf8')
            shutil.move(self.tex_file_path, self._tex_save_path)
        self.tex_file_path = self._tex_save_path

        if self.svg_file_path is not None:
            shutil.move(self.svg_file_path, self._svg_save_path)
        self.svg_file_path = self._svg_save_path

    def _zfill(self, _i):
        return 'f_' + str(_i).zfill(self._pad_size)

    @staticmethod
    def _need_regeneration(tex_file_path: str | Path, svg_file_path: str | Path):
        """"""
        last_tex = GitUtils.last_commit_date(tex_file_path)
        last_svg = GitUtils.last_commit_date(svg_file_path)

        try:
            # 比较时间戳, tex 晚于 svg, 则需要更新
            dt_tex = datetime.fromisoformat(last_tex)  # type: ignore
            dt_svg = datetime.fromisoformat(last_svg)  # type: ignore
            return dt_tex > dt_svg
        except:  # noqa: E722
            return True

    def _need_add_empty_line(self) -> bool:
        """是否需要添加空行"""
        if self.prefix_has_quote():
            nxt_prefix, nxt_left = MarkdownMath2SvgHelper.split_prefix_and_left(self.nxt_line)
            if '>' in nxt_prefix and nxt_left.strip():
                return True
        else:
            if self.nxt_line.strip():
                return True
        return False

    def prefix_has_quote(self):
        return '>' in self.line_prefix

    # @property
    # def already_img_block(self) -> bool:
    #     return self.tex_file_path is not None and self.tex_file_path.exists()

    @property
    def img_line(self) -> str:
        # prefix = self.line_prefix
        # if self._need_indent():
        #     prefix += '    '
        line = self.IMG_BLOCK_TEMP.format(
            line_prefix=self.line_prefix,
            tex_file_path=self.tex_href,
            svg_file_path=self.svg_href,
        )
        # 添加注释行
        # assert self.content
        # math_flat = ' '.join([ln.strip() for ln in self.content.split('\n')])
        # line += f'\n{self.line_prefix}<!-- $${math_flat}$$ -->'
        if self._need_add_empty_line():
            if self.prefix_has_quote():
                line += '\n>'
            else:
                line += '\n'
        # if self._nxt_is_code or self.is_pre_empty_and_nxt_not_emplt:
        #     line += '\n'
        # if self.is_pre_not_quote_and_nxt_not_emplt:
        #     line += '\n>'
        return line

    @property
    def tex_name(self):
        return f'{self._zfill(self.idx)}.js.tex'

    @property
    def svg_name(self):
        return f'{self._zfill(self.idx)}.js.svg'

    @property
    def _tex_save_path(self):
        return self.tmp_save_dir / self.tex_name

    @property
    def _svg_save_path(self):
        return self.tmp_save_dir / self.svg_name

    @property
    def _href_prefix(self) -> Path:
        return Path(MarkdownMath2SvgHelper.save_dir_name) / self.md_path.stem

    @property
    def tex_href(self) -> str:
        return str(self._href_prefix / self.tex_name)

    @property
    def svg_href(self):
        return str(self._href_prefix / self.svg_name)

    # @property
    # def _nxt_is_code(self):
    #     return self.nxt_line and self.nxt_line.lstrip().startswith('```')

    # @property
    # def _nxt_is_comment(self):
    #     return self.nxt_line and self.nxt_line.lstrip().startswith('<!--')

    # @property
    # def _pre_is_code(self):
    #     return self.pre_line and self.pre_line.lstrip().startswith('```')

    # @property
    # def _pre_is_comment(self):
    #     return self.pre_line and self.pre_line.lstrip().startswith('<!--')

    # def save_to_svg(self):
    #     assert self.tex_file_path is not None
    #     assert self.content is not None

    #     with open(self.tex_file_path, 'w', encoding='utf8') as fw:
    #         fw.write(self.content)

    # @property
    # def is_pre_not_quote_and_nxt_not_emplt(self) -> bool:
    #     """一种特殊情况:
    #     ...
    #     > <img_block>
    #     > ...
    #     """
    #     # 如果前缀中有 >, 且上一行没有 >, 且下一行不是空白 >
    #     if self.prefix_has_quote:
    #         if self.pre_line and not self.pre_line.lstrip().startswith('>'):
    #             if self.nxt_line:
    #                 _, nxt_left = MarkdownMath2SvgHelper.split_prefix_and_left(self.nxt_line)
    #                 if nxt_left:
    #                     return True
    #     return False

    # @property
    # def is_pre_empty_and_nxt_not_emplt(self) -> bool:
    #     if self.line_prefix == '':
    #         if not self.pre_line.strip():
    #             if self.nxt_line.strip():
    #                 return True
    #     return False

    # def _need_indent(self) -> bool:
    #     """"""
    #     if self.is_pre_not_quote_and_nxt_not_emplt:
    #         return False
    #     if self.is_pre_empty_and_nxt_not_emplt:
    #         return False

    #     def _check_line(ln: str):
    #         _is_code_block = ln.lstrip().startswith('```')
    #         _is_comment = ln.lstrip().startswith('<!--')
    #         if _is_code_block or _is_comment:
    #             return False

    #         _ln_prefix, _ln_left = MarkdownMath2SvgHelper.split_prefix_and_left(ln)

    #         if not _ln_left:
    #             return False

    #         _is_img_blk, _, _ = MarkdownMath2SvgHelper.is_img_block(_ln_left)
    #         _leading_spaces = MarkdownMath2SvgHelper.count_leading_spaces(ln)
    #         if prefix_has_quote:
    #             if len(prefix) == len(_ln_prefix) and (not _is_img_blk):
    #                 return True
    #         else:
    #             if ln.strip() and (not _is_img_blk) and cur_leading_spaces == _leading_spaces:
    #                 return True
    #         return False

    #     prefix = self.line_prefix
    #     nxt_line = self.nxt_line
    #     pre_line = self.pre_line

    #     prefix_has_quote = '>' in prefix
    #     cur_leading_spaces = len(prefix)
    #     if nxt_line:
    #         if _check_line(nxt_line):
    #             return True

    #     if pre_line:
    #         if _check_line(pre_line):
    #             return True

    #     return False


class MarkdownMath2SvgHelper:
    """"""

    # 正则：匹配 <div align='center'><a href='xxx'><img src='yyy'/></a></div>
    IMG_BLOCK_PATTERN = re.compile(
        r"""^\s*<div\s+align=['"]center['"]>\s*
            <a\s+href=['"](?P<tex>[^'"]+)['"]>\s*
            <img\s+src=['"](?P<svg>[^'"]+)['"]\s*/?>\s*
            </a>\s*</div>\s*$""",
        re.VERBOSE,
    )

    # IMG_BLOCK_TEMP = "{line_prefix}<div align='center'><a href='{tex_file_path}'><img src='{svg_file_path}'/></a></div>"

    text: str
    math_blocks: list[MathBlock]
    save_dir_name: ClassVar[str] = '_formulas'

    def __init__(
        self,
        md_path: Path | str,
        md_content: str | None = None,
        tex2svg_script_path: str | Path | None = None,
        save_mode: bool = True,
    ) -> None:
        self.md_path = Path(md_path).resolve()
        if md_content is not None:
            self.text = md_content
        else:
            self.text = self.md_path.read_text(encoding='utf8')

        self.save_mode = save_mode

        self._md_dir = self.md_path.parent

        self._tmp_save_dir = self._get_save_dir(self.md_path, is_tmp=True)
        self._final_save_dir = self._get_save_dir(self.md_path)
        # print(self._tmp_save_dir)
        # self._svg_save_dir = self._md_dir / self.save_dir_name / f'{self.md_path.stem}_svgs'
        self.changed, old_name = GitUtils.file_changed_or_new(self.md_path)
        self.old_path = Path(old_name) if old_name is not None else None
        # if DEBUG:
        #     print(f'{self.changed = }, {self.old_name = }')

        if tex2svg_script_path is None:
            tex2svg_script_path = Path(__file__).parent.parent / 'tex2svg.js'
        self.tex2svg_script = tex2svg_script_path

    def _get_save_dir(self, md_path: Path, is_tmp: bool = False) -> Path:
        """"""
        dir_name = md_path.stem
        if is_tmp:
            dir_name += '_tmp'
        save_dir = self._md_dir / self.save_dir_name / f'{dir_name}'
        save_dir.mkdir(exist_ok=True, parents=True)
        return save_dir

    def run(self):
        """"""
        # self._rename_save_dir()
        self._get_all_math_blocks()
        self._save_to_tex_and_svg()
        self._replace_math_to_svg()

        if self._final_save_dir.exists():
            shutil.rmtree(self._final_save_dir)
            shutil.move(self._tmp_save_dir, self._final_save_dir)
            if not any(self._final_save_dir.iterdir()):
                shutil.rmtree(self._final_save_dir)

        if self.old_path is not None and self.old_path:
            old_save_dir = self._get_save_dir(self.old_path)
            if old_save_dir.exists() and not old_save_dir.samefile(self._final_save_dir):
                shutil.rmtree(old_save_dir)

    def _save_to_tex_and_svg(self):
        """"""
        for blk in self.math_blocks:
            if not blk.already_img_block:
                assert blk.tex_file_path is not None
                with open(blk.tex_file_path, 'w', encoding='utf8') as fw:
                    assert blk.content is not None
                    fw.write(blk.content)

            if blk.need_regen:
                os.system(f'node {self.tex2svg_script} {blk.tex_file_path} {blk.svg_file_path}')

    def _replace_math_to_svg(self):
        """"""
        lines = self.text.split('\n')
        blocks = sorted(self.math_blocks, key=lambda b: b.line_start_i, reverse=True)

        for blk in blocks:
            # 生成替换 HTML
            # html = self.IMG_BLOCK_TEMP.format(
            #     line_prefix=blk.line_prefix,
            #     tex_file_path=blk.tex_href,
            #     svg_file_path=blk.svg_href,
            # )
            # 替换对应行
            assert blk.line_end_i != -1
            lines[blk.line_start_i : blk.line_end_i + 1] = [blk.img_line]

        self.text = '\n'.join(lines)

        if self.save_mode:
            with self.md_path.open('w', encoding='utf8') as fw:
                fw.write(self.text)

    def _rename_save_dir(self):
        """"""
        if self.old_path is not None:
            old_save_dir = self._md_dir / self.save_dir_name / f'{self.old_path.stem}_svgs'
            if old_save_dir.exists():
                shutil.move(old_save_dir, self._tmp_save_dir)

    # @staticmethod
    # def count_leading_spaces(line: str) -> int:
    #     return len(line) - len(line.lstrip(' '))

    @staticmethod
    def split_prefix_and_left(_l: str) -> Tuple[str, str]:
        """
        拆分一行，返回 (前缀, 剩余内容)
        前缀包括开头的空格、制表符、引用符号 '>'
        """
        m = re.match(r'^([ \t>]*)', _l)
        prefix = m.group(1) if m else ''
        left = _l[len(prefix) :].rstrip()
        return prefix, left

    @staticmethod
    def is_img_block(_l: str) -> Tuple[bool, str, str]:
        """
        判断一行是否是 img block。
        返回 (is_img_block, tex_file_path, svg_file_path)
        如果不是 img block，则 tex_file_path 和 svg_file_path 返回空字符串。
        """
        false_ret = False, '', ''
        if 'js.tex' not in _l:
            return false_ret

        m = MarkdownMath2SvgHelper.IMG_BLOCK_PATTERN.match(_l.strip())
        if m:
            return True, m.group('tex'), m.group('svg')
        return false_ret

    # @staticmethod
    # def _need_indent(lines: list[str], i: int) -> bool:
    #     """"""

    #     def _check_line(ln: str):
    #         _is_code_block = ln.lstrip().startswith('```')
    #         _is_comment = ln.lstrip().startswith('<!--')
    #         if _is_code_block or _is_comment:
    #             return False

    #         _ln_prefix, _ln_left = MarkdownMath2SvgHelper.split_prefix_and_left(ln)
    #         _is_img_blk, _, _ = MarkdownMath2SvgHelper.is_img_block(_ln_left)
    #         _leading_spaces = MarkdownMath2SvgHelper.count_leading_spaces(ln)
    #         if prefix_has_quote:
    #             if len(prefix) == len(_ln_prefix) and (not _is_img_blk):
    #                 return True
    #         else:
    #             if ln.strip() and (not _is_img_blk) and cur_leading_spaces == _leading_spaces:
    #                 return True
    #         return False

    #     line = lines[i]
    #     prefix, _ = MarkdownMath2SvgHelper.split_prefix_and_left(line)
    #     prefix_has_quote = '>' in prefix
    #     cur_leading_spaces = MarkdownMath2SvgHelper.count_leading_spaces(line)
    #     if i + 1 < len(lines):
    #         nxt_line = lines[i + 1]
    #         if _check_line(nxt_line):
    #             return True

    #     if i > 0:
    #         pre_line = lines[i - 1]
    #         if _check_line(pre_line):
    #             return True

    #     return False

    def _get_all_math_blocks(self):
        """"""
        lines = self.text.split('\n')

        blocks = []
        idx = 1

        in_block = False
        content_lines = []
        block = None
        for i, raw_line in enumerate(lines):
            if raw_line.startswith('<!--'):
                continue

            prefix, line = self.split_prefix_and_left(raw_line)
            prefix_norm = prefix.replace('>', ' ')
            pre_line = lines[i - 1] if i > 0 else ''
            nxt_line = lines[i + 1] if i < len(lines) - 1 else ''

            is_img_block, tex_file_path, svg_file_path = self.is_img_block(line)
            if is_img_block:
                # img 块
                tex_file_path = self._md_dir / tex_file_path
                svg_file_path = self._md_dir / svg_file_path
                # print(tex_file_path, svg_file_path)
                blocks.append(
                    MathBlock(
                        idx=idx,
                        md_path=self.md_path,
                        line_start_i=i,
                        line_end_i=i,
                        pre_line=pre_line,
                        nxt_line=nxt_line,
                        line_prefix=prefix,
                        tex_file_path=tex_file_path,  # type: ignore
                        svg_file_path=svg_file_path,  # type: ignore
                        tmp_save_dir=self._tmp_save_dir,
                        already_img_block=is_img_block,
                    )
                )
                idx += 1
                continue
            elif line.startswith('$$') and line.rstrip().endswith('$$') and len(line) > 3:
                # 单行公式: $$ ... $$
                blocks.append(
                    MathBlock(
                        idx=idx,
                        md_path=self.md_path,
                        line_start_i=i,
                        line_end_i=i,
                        pre_line=pre_line,
                        nxt_line=nxt_line,
                        line_prefix=prefix,
                        tmp_save_dir=self._tmp_save_dir,
                        already_img_block=is_img_block,
                        content=line.strip()[2:-2].strip(),
                    )
                )
                idx += 1
                continue
            elif not in_block and line.startswith('$$'):
                # 多行公式: 起始行
                in_block = True
                assert block is None
                block = MathBlock(
                    idx=idx,
                    md_path=self.md_path,
                    line_start_i=i,
                    line_end_i=-1,
                    pre_line=pre_line,
                    line_prefix=prefix,
                    tmp_save_dir=self._tmp_save_dir,
                    already_img_block=is_img_block,
                )
                content_lines.append(prefix_norm + line.lstrip('$').rstrip())
                continue
            elif in_block and line.rstrip().endswith('$$'):
                # 多行公式: 结尾行
                content_lines.append(prefix_norm + line.rstrip('$').rstrip())
                assert block is not None
                content_lines = MarkdownUtils.remove_min_prefix_spaces(content_lines)
                block.content = '\n'.join(content_lines).strip()
                block.line_end_i = i
                block.nxt_line = nxt_line
                blocks.append(block)
                block = None
                idx += 1
                in_block = False
                content_lines.clear()
                continue
            elif in_block:
                # 多行公式: 内容行
                content_lines.append(prefix_norm + line.rstrip())
                continue

        self.math_blocks = blocks


class GitUtils:
    """"""

    @staticmethod
    def last_commit_date(fp: str | Path) -> str | None:
        """
        获取文件的最后一次提交时间 (ISO 格式)，如果文件没有提交过则返回 None
        """
        cmd = ['git', 'log', '-1', '--format=%ad', '--date=iso-strict', '--follow', '--', fp]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip() or None

    @staticmethod
    def normalize_to_repo_relative(file_path: str | Path) -> str:
        repo_root = subprocess.run(
            ['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True, check=True
        ).stdout.strip()
        repo_root = Path(repo_root)
        return str(Path(file_path).resolve().relative_to(repo_root))

    @staticmethod
    def file_changed_or_new(file_path: str | Path) -> tuple[bool, str | None]:
        """
        检查文件是否相对于 HEAD 有改动（修改/重命名/新增）
        :param file_path: 文件路径（相对仓库根目录）
        :return: (changed, original_name)
                changed=True 表示有改动或新增
                如果是重命名，original_name 返回旧名字，否则为 None
        """
        _file_path = GitUtils.normalize_to_repo_relative(file_path)
        # 检查 diff
        result = subprocess.run(
            ['git', 'diff', '--name-status', 'HEAD^', 'HEAD'],
            capture_output=True,
            text=True,
            check=True,
        )

        for line in result.stdout.splitlines():
            parts = line.split()
            status = parts[0]

            if status.startswith('R'):  # 重命名
                old, new = parts[1], parts[2]
                if new == _file_path:
                    return True, old
                if old == _file_path:
                    return True, old  # 旧名也算改动
            elif status in {'M', 'A'}:  # 修改或新增
                fname = parts[1]
                if fname == _file_path:
                    return True, None

        # 如果文件不在 HEAD 中，说明是新增文件
        result = subprocess.run(['git', 'ls-files', '--error-unmatch', _file_path], capture_output=True, text=True)
        if result.returncode != 0:
            return True, None

        return False, None


    # @property
    # def slugify_name(self):
    #     return MarkdownUtils.slugify(self.head_name)


class MarkdownUtils:
    """"""

    @staticmethod
    def get_count_sup(cnt: int, *, color: str = 'Gray', style: Literal['math', 'html'] = 'html'):
        """"""
        if style == 'math':
            return rf'$\color{{{color}}}^{{{cnt}}}$'
        else:
            return f'<sup style="color:{color}">{cnt}</sup>'  # 在 GitHub 上, 颜色会失效

    @staticmethod
    def remove_min_prefix_spaces(lines: List[str]) -> List[str]:
        # 过滤掉空行, 避免 min 出错
        non_empty = [line for line in lines if line.strip() != '']
        if not non_empty:
            return lines

        # 计算每行前缀空格数
        def count_leading_spaces(s: str) -> int:
            return len(s) - len(s.lstrip(' '))

        min_spaces = min(count_leading_spaces(line) for line in non_empty)

        # 去掉最小前缀空格
        return [line[min_spaces:] if len(line) >= min_spaces else '' for line in lines]

    @staticmethod
    def update_section_number(
        txt: str,
        *,
        max_section_level: int = 4,
        min_section_level: int = 2,
    ):
        """"""
        L, H = min_section_level, max_section_level
        re_line = re.compile(r'^(#+)\s*(\d+(\.\d+)*\.)?\s*(.*)$')
        section_counts = [0] * H

        lines = txt.split('\n')
        for i, line in enumerate(lines):
            m = re_line.match(line)
            if not m:
                continue

            hashes, _, _, title = m.groups()
            level = len(hashes)

            # 不在编号范围 → 不编号, 且清除已有编号
            if level < L or level > H:
                lines[i] = f'{hashes} {title.strip()}'
                continue

            # 更新当前级别的计数器, 并重置更低级别的计数器
            section_counts[level - 1] += 1
            for j in range(level, H):
                section_counts[j] = 0

            # 构建章节编号字符串
            section_number = '.'.join(str(section_counts[k]) for k in range(level) if section_counts[k] > 0) + '.'

            # 更新标题行
            lines[i] = f'{hashes} {section_number} {title.strip()}'

        return '\n'.join(lines)

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
            # 1: 只应用到单行, 0: 单行或多行
            skip_block = [
                ('```', '```', 0),  # 代码块
                ('$$', '$$', 0),  # 多行公式
                # (r'\[', r'\]'),  # 多行公式
                ('<!--', '-->', 0),  # HTML 注释
                ('<div', '/div>', 1),  # 主要是图片块
            ]

        # skip_block = [(it, it) if isinstance(it, str) else it for it in skip_block]

        lines = text.split('\n')
        in_block = False
        cur_block = None
        line_block = False
        for i in range(len(lines)):
            line = lines[i]

            # 单行块
            for b_start, b_end, _ in skip_block:
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

            # 多行块
            if cur_block is None:
                for b_start, b_end, only_single_line in skip_block:
                    if only_single_line:
                        continue
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

    RE_BRACKET = re.compile(r'\(\s*(.*?)\s*\)')

    @staticmethod
    def add_space_in_bracket(txt):
        return MarkdownUtils.RE_BRACKET.sub(r'( \1 )', txt)

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
        # 优先筛选作者=imhuay 且不含 Auto/AUTO
        cmd1 = [
            'git',
            'log',
            '--author=imhuay',
            '--invert-grep',
            '--grep=Auto\\|AUTO',
            '--format=%ad',
            '--date=iso-strict',
            '--follow',
            '--',
            fp,
        ]
        result1 = subprocess.run(cmd1, capture_output=True, text=True)
        lines = result1.stdout.strip().splitlines()
        if lines:
            # return lines[0]  # 最近一次符合条件的提交时间
            return NoteUtils.get_date_str(lines[0], fmt)

        # 否则取最早一次提交
        cmd2 = ['git', 'log', '--format=%ad', '--date=iso-strict', '--follow', '--', fp]
        result2 = subprocess.run(cmd2, capture_output=True, text=True)
        lines = result2.stdout.strip().splitlines()
        # return lines[-1] if lines else None
        date_str = lines[-1] if lines else ''
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
    def replace_section_content(section_key, txt, new_content, count=1) -> str:
        """"""
        re_pattern = NoteUtils._get_section_re_pattern(section_key)
        repl = f'{NoteUtils.get_section_begin(section_key)}\n{new_content}\n{NoteUtils.get_section_end(section_key)}'
        return re_pattern.sub(lambda m: repl, txt, count=count)

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

    # @staticmethod
    # def get_keyword_section(txt: str) -> KeywordSection:
    #     """从 Markdown 标题中提取纯文本内容，去除标题标记和内联格式"""
    #     # 使用 Markdown-It 解析器
    #     section = KeywordSection(txt)
    #     return section


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

    fp_qa_collection = fp_notes_archives / '2025/10/QA_合集.md'

    notes_top_limit = None

    @staticmethod
    def get_temp_badge_todo_logo(count: int, height: int, color: str = 'important', href: str = '#') -> str:
        """color candidate: orange, E05D44"""
        return f'<a href="{href}"><img src="https://custom-icon-badges.demolab.com/static/v1?label=&message={count}&labelColor={color}&color={color}&style=flat-square&logoSource=feather&logo=edit&logoColor=white" height="{height}"/></a>'

    @staticmethod
    def get_img_badge(
        message: str,
        *,
        label: str = '',
        height: int = 25,
        color: str = 'important',
        labelColor: str = 'important',
        style: str = 'flat-square',
        logoSource: str = 'feather',
        logo: str = '',
        logoColor: str = 'white',
        href: str = '#',
    ) -> str:
        """生成一个带链接的自定义徽章 (badge) HTML 片段"""
        # 基础参数
        args = {
            'label': label,
            'message': message,
            'color': color,
            'labelColor': labelColor,
            'style': style,
        }

        # 如果指定了 logoSource 和 logo, 就加上
        if logoSource and logo:
            args['logoSource'] = logoSource
            args['logo'] = logo
            args['logoColor'] = logoColor

        # 拼接 query string
        query = urllib.parse.urlencode(args)

        # 构造最终 HTML
        return (
            f'<a href="{href}">'
            f'<img src="https://custom-icon-badges.demolab.com/static/v1?{query}" '
            f'height="{height}"/></a>'
        )

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
