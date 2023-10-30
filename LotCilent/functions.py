import os
import sys
import shutil
import threading
import time


class MyThread(threading.Thread):
    """
    多线程优化
    """

    def __init__(self, func, *args):
        super().__init__()

        self.func = func
        self.args = args

        self.daemon = True
        self.start()

    def run(self):
        self.func(*self.args)


class ProgramInit():
    """
    信息类-处理信息
    """
    PROGRAM_NAME = "zb小程序"  # 程序名称
    PROGRAM_VERSION = "3.0.0"  # 程序版本
    PROGRAM_TITLE = f"{PROGRAM_NAME} {PROGRAM_VERSION}"  # 程序窗口标题
    AUTHOR_NAME = "Ianzb"  # 作者名称
    AUTHOR_URL = "https://ianzb.github.io/"  # 作者网址
    PROGRAM_URL = "https://ianzb.github.io/program/"  # 程序网址
    GITHUB_URL = "https://github.com/Ianzb/program/"  # Github网址
    PROGRAM_MAIN_FILE_PATH = sys.argv[0]  # 程序主文件路径
    PROGRAM_PATH = os.path.dirname(sys.argv[0])  # 程序安装路径
    SOURCE_PATH = os.path.join(PROGRAM_PATH, "img")  # 程序资源文件路径
    FILE_NAME = os.path.basename(sys.argv[0])  # 当前程序文件名称
    PROGRAM_PID = os.getpid()  # 程序pid
    USER_PATH = os.path.expanduser("~")  # 系统用户路径
    STARTUP_ARGUMENT = sys.argv[1:]  # 程序启动参数
    REQUEST_HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"}  # 程序默认网络请求头

    REQUIRE_LIB = ["PyQt-Fluent-Widgets",
                   "qt5_tools",
                   "requests",
                   "bs4",
                   "lxml",
                   "pypiwin32",
                   "pandas",
                   "winshell",
                   ]

    def __init__(self):
        pass

    @property
    def DESKTOP_PATH(self) -> str:
        """
        获得桌面路径
        :return: 桌面路径
        """
        import winreg
        return winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"), "Desktop")[0]

    @property
    def isStartup(self) -> bool:
        """
        判断程序是否为开机自启动
        :return: bool
        """
        return "startup" in self.STARTUP_ARGUMENT

    def source(self, name: str) -> str:
        """
        快捷获取程序资源文件路径
        :param name: 文件名
        :return: 文件路径
        """
        return f.pathJoin(self.SOURCE_PATH, name)


program = ProgramInit()


class Functions():
    """
    程序相关函数
    """

    def __init__(self):
        pass

    def pathJoin(self, *data) -> str:
        """
        拼接路径
        :param data: 多个字符串参数
        :return: 拼接后的字符串
        """
        path = ""
        for i in data:
            path = os.path.join(path, i)
        path = path.replace("//", r"\ "[:-1]).replace(r"\\ "[:-1], r"\ "[:-1]).replace("\/", r"\ "[:-1]).replace("/\ "[:-1], r"\ "[:-1]).replace("/", r"\ "[:-1])
        return path


f = Functions()
# 切换运行路径

os.chdir(program.PROGRAM_PATH)

# 设置任务栏
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("zb小程序")

# UI多线程
from PyQt5.Qt import *
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as FIF


class NewThread(QThread):
    """
    多线程模块
    """
    signalStr = pyqtSignal(str)
    signalBool = pyqtSignal(bool)
    signalList = pyqtSignal(list)
    signalDict = pyqtSignal(dict)

    def __init__(self, mode: str, data=None):
        super().__init__()
        self.mode = mode
        self.data = data

    def run(self):
        pass
