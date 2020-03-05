# 导入访问SQLite的模块
import sqlite3

# 第一步：打开或创建数据库
# 也可以使用特殊名称:memory:，代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# 第二步：打开游标
c = conn.cursor()
# 第三步：调用executemany()方法多次执行同一条SQL语句
c.executemany('update user_tb set name=? where _id=?',
              (('小孙', 2), ('小白', 3), ('小猪', 4), ('小牛', 5), ('小唐', 6)))
# 通过rowcount获取被修改的记录条数
print('修改的记录条数：', c.rowcount)
# 提交查询
conn.commit()
# 第四步：关闭游标
c.close()
# 第五步：关闭数据库连接
conn.close()