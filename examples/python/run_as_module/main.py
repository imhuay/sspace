
from .utils import foo

if __name__ == '__main__':
    """
    直接运行报错:
        ImportError: attempted relative import with no known parent package
    以模块运行:
        # 在至少一层父目录中
        python -m [parent].main
    """
    foo()