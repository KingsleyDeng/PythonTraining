# 导入SQLite
import sqlite3


# 定义函数 准备注册为SQL语句中的自定义函数
def reverse_ext(st):
    # 对字符串翻转 前后添加方括号
    return '[' + st[::-1] + ']'


conn = sqlite3.connect('first.db')

conn.create_function('enc', 1, reverse_ext)
c = conn.cursor()
c.execute('insert into user_tb values(null, enc(?), ?, ?)',
          ('李连杰', '123456', 'male'))

conn.commit()
c.close()
conn.close()
