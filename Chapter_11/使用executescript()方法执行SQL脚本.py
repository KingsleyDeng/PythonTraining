# 导入访问SQLite的模块
import sqlite3

# 第一步：打开或创建数据库
# 也可以使用特殊名称：memory:，代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# 第二步：获取游标
c = conn.cursor()
# 第三步：调用executescript()方法，执行一段SQL脚本
c.executescript('''
    insert into user_tb values(null, '李四', '3444', 'male');
    insert into user_tb values(null, '王五', '44444', 'male');
    create table item_tb(_id integer primary key autoincrement,
    name,
    price);
    ''')
# 提交事务
conn.commit()
# 第四步：关闭游标
c.close()
# 第五步：关闭数据库连接
conn.close()