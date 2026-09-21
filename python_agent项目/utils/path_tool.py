"""
为整个工程提供统一的绝对路径
"""
import os

# 导入操作系统相关的模块，用于处理文件和路径操作


def get_project_root() -> str:
    """
    获取工程所在的根目录
    :return: 字符串根目录
    """
    # 当前文件的绝对路径
    current_file = os.path.abspath(__file__)

    # 获取当前文件所在的目录（即utils目录）的绝对路径
    current_dir = os.path.dirname(current_file)
    # 获取上一级目录。即项目的根目录
    project_root = os.path.dirname(current_dir)

    return project_root


def get_abs_path(relative_path: str) -> str:
    """
    传递相对路径，得到绝对路径
    :param relative_path: 相对领
    :return: 绝对路径
    """

    #调用函数获取项目的根目录
    project_root = get_project_root()

    # 将项目根目录与相对路径拼接，生成完整的绝对路径并返回
    return os.path.join(project_root, relative_path)


if __name__ == '__main__':
    # 测试调用get_abs_path函数，打印config/config.txt的绝对路径
    print(get_abs_path("config/config.txt"))

