# 导入SQLite的模块
import sqlite3

# 第一步
conn = sqlite3.connect('first.db')
# 第二步：获取游标
c = conn.cursor()
# 第三步：执行insert语句插入数据
c.execute('insert into user_tb values(null, ?, ?, ?)', ('张三', '123456', 'male'))
c.execute('insert into order_tb values(null, ?, ?, ?, ?)',
          ('鼠标', '34.2', '3', 1))
# 提交DML语句
conn.commit()
# 关闭游标
c.close()
# 关闭数据库连接
conn.close()
