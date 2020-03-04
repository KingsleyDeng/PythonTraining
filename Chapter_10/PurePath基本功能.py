from pathlib import *

# 创建PurePath 实际上使用PureWindowsPath
pp = PurePath('setup.py')
print(type(pp))
# 使用PurePath创建PurePath对象会自动识别操作系统，
# 在UNIX或Mac OS X系统上会返回PurePosixPath对象，
# 在Windows系统上则返回PureWindowsPath对象。
# 也可以使用PurePosixPath或PureWindowsPath类明确指定要创建的对象是什么类型的。
pp = PurePath('ib-top', 'some/path', 'info')
# 看到输出Wiondows风格的路径
print(pp)  # 'ib-top\some\path\info'
pp = PurePath(Path('ib-top'), Path('info'))
# 看到输出Windows风格的路径
print(pp)  # 'ib-top\info'
# 明确指定创建PurePosixPath
pp = PurePosixPath('ib-top', 'some/path', 'info')
# 看到输出UNIX风格的路径
print(pp)  # 'ib-top/some/path/info'