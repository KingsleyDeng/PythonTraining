import os
import time

# 获取绝对路径
print(os.path.abspath("a_test.txt"))  # 当前路径下的a_test.txt
# 获取共同前缀名
print(os.path.commonprefix(['/user/lib', '/usr/local/lib']))  # /usr/l
# 获取共同路径
print(os.path.commonpath(['/usr/lib', '/usr/local/lib']))  # \usr
# 获取目录
print(os.path.dirname('abc/xyz/README.txt'))  # abc/xyz
# 判断指定目录是否存在
print(os.path.exists('abc/xyz/README.txt'))  # False
# 获取最近一次访问时间
print(time.ctime(os.path.getatime('os_path_test.py')))
# 获取最后一次修改时间
print(time.ctime(os.path.getmtime('os_path_test.py')))
# 获取创建时间
print(time.ctime(os.path.getctime('os_path_test.py')))
# 获取文件大小
print(os.path.getsize('os_path_test.py'))
# 判断是否为文件
print(os.path.isfile('os_path_test.py'))  # True
# 判断是否为目录
print(os.path.isdir('os_path_test.py'))  # False
# 判断是否为同一个文件
print(os.path.samefile('os_path_test.py', './os_path_test.py'))  # True