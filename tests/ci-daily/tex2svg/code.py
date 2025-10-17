import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from pprint import pprint

from sympy import im

sys.path.append('/home/huay/workspace/git/my/sspace/scripts/readme')

from utils import GitUtils, MarkdownMath2SvgHelper, MarkdownUtils

# @dataclass
# class FormulaBlock:
#     idx: int
#     line_start_i: int
#     line_end_i: int
#     content: str = ''
#     tex_file_path: str = ''
#     is_svg: bool = False


# def extract_math_blocks(md_path: str | Path, pad: int = 3):
#     def _strip(_l):
#         return re.sub(r'^[ \t>]+', '', _l).rstrip()

#     def _zfill(_i):
#         return str(_i).zfill(pad)

#     md_file = Path(md_path)
#     lines = md_file.read_text(encoding='utf-8').splitlines()

#     base = md_file.stem
#     blocks = []
#     idx = 1

#     in_block = False
#     content_lines = []

#     for i, line in enumerate(lines):
#         line = _strip(line)

#         # m = re.match(r'^\$\$(.+?)\$\$$', line.strip())
#         if line.startswith('$$') and line.rstrip().endswith('$$') and len(line) > 3:
#             # 单行公式: $$ ... $$
#             content = line.strip()[2:-2].strip()
#             filename = f'{base}_{_zfill(idx)}.tex'
#             blocks.append(FormulaBlock(idx, content, filename))
#             idx += 1
#             continue
#         elif not in_block and line.startswith('$$'):
#             # 多行公式: 起始行
#             in_block = True
#             content_lines.append(line.lstrip('$'))
#             continue
#         elif in_block and line.rstrip().endswith('$$'):
#             # 多行公式: 结尾行
#             content_lines.append(line.rstrip('$').strip())
#             content = '\n'.join(content_lines).strip()
#             filename = f'{base}_{_zfill(idx)}.tex'
#             blocks.append(FormulaBlock(idx, content, filename))
#             idx += 1
#             in_block = False
#             content_lines.clear()
#             continue
#         elif in_block:
#             # 多行公式: 内容行
#             content_lines.append(line)
#             continue

#     return blocks


# def file_content_modified(file_path: str | Path) -> bool:
#     """
#     检查某文件内容是否相对于 HEAD 提交有修改
#     :param file_path: 文件路径（相对或绝对）
#     :return: True 表示内容有修改，False 表示没有
#     """
#     file_path = str(file_path)
#     result = subprocess.run(
#         ["git", "diff", "--quiet", "HEAD", "--", file_path],
#         capture_output=True
#     )
#     # 返回码 0 表示无差异，1 表示有差异
#     return result.returncode == 1


def normalize_to_repo_relative(file_path: str) -> str:
    repo_root = subprocess.run(
        ['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True, check=True
    ).stdout.strip()
    repo_root = Path(repo_root)
    return str(Path(file_path).resolve().relative_to(repo_root))


def file_changed_or_new(file_path: str) -> tuple[bool, str | None]:
    """
    检查文件是否相对于 HEAD 有改动（修改/重命名/新增）
    :param file_path: 文件路径（相对仓库根目录）
    :return: (changed, original_name)
             changed=True 表示有改动或新增
             如果是重命名，original_name 返回旧名字，否则为 None
    """
    file_path = normalize_to_repo_relative(file_path)
    # 检查 diff
    result = subprocess.run(['git', 'diff', '--name-status', 'HEAD^'], capture_output=True, text=True, check=True)

    for line in result.stdout.splitlines():
        parts = line.split()
        status = parts[0]

        if status.startswith('R'):  # 重命名
            old, new = parts[1], parts[2]
            if new == file_path:
                return True, old
            if old == file_path:
                return True, old  # 旧名也算改动
        elif status in {'M', 'A'}:  # 修改或新增
            fname = parts[1]
            if fname == file_path:
                return True, None

    # 如果文件不在 HEAD 中，说明是新增文件
    result = subprocess.run(['git', 'ls-files', '--error-unmatch', file_path], capture_output=True, text=True)
    if result.returncode != 0:
        return True, None

    return False, None


def test_get_math_blocks():
    """"""
    cur_dir = Path(__file__).parent
    md_path = cur_dir / 'demo.md'
    
    helper = MarkdownMath2SvgHelper(md_path)
    helper.run()


def test_file_changed():
    md_path = '/home/huay/workspace/git/my/sspace/tests/ci-daily/tex2svg/demo.md'

    ret = GitUtils.file_changed_or_new(md_path)
    print(ret)


def test_run_path():
    from utils import GitUtils

    ret = GitUtils.last_commit_date(Path('/home/huay/workspace/git/my/sspace/README.md'))
    print(ret)


# 示例：读取 md 文件并提取
if __name__ == '__main__':
    # cur_dir = Path(__file__).parent
    # md_file = cur_dir / 'demo.md'
    # print(f'{md_file} modified: {file_changed_or_new(str(md_file))}')

    # blocks = extract_math_blocks(md_file, pad=3)
    # for b in blocks:
    #     print(f'{b.file_name}:\n{b.content}\n{"-" * 30}')
    test_run_path()