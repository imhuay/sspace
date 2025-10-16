import subprocess


def get_commit_date(fp):
    # 优先筛选作者=imhuay 且不含 Auto/AUTO
    cmd1 = [
        "git", "log",
        "--author=imhuay", "--invert-grep", "--grep=Auto\\|AUTO",
        "--format=%ad", "--date=iso-strict", "--follow", "--", fp
    ]
    result1 = subprocess.run(cmd1, capture_output=True, text=True)
    lines = result1.stdout.strip().splitlines()
    if lines:
        return lines[0]  # 最近一次符合条件的提交时间

    # 否则取最早一次提交
    cmd2 = [
        "git", "log",
        "--format=%ad", "--date=iso-strict", "--follow", "--", fp
    ]
    result2 = subprocess.run(cmd2, capture_output=True, text=True)
    lines = result2.stdout.strip().splitlines()
    return lines[-1] if lines else None


if __name__ == '__main__':
    """"""
    fp = "algorithms/problems/2025/10/LeetCode_3147_中等_从魔法师身上吸取的最大能量.md"

    ret = get_commit_date(fp)
    print(ret)