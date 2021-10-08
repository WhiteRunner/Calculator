import os, sys


def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
        basedir = os.path.dirname(basedir)
    return os.path.join(basedir, path)


tmd = base_path('')  # exe解压到的临时目录/工程目录
cwd = os.getcwd()  # 当前文件的所在路径

# 当需要调用打包的外部文件时
# 先把工作路径变成解压路径
# os.chdir(tmd)


# 当需要写出文件到程序所在目录时
# 把工作路径切换回来
# os.chdir(cwd)
