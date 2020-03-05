# 导入访问SQLite的模块
import sqlite3

# 第一步：打开或创建数据库
conn = sqlite3.connect('first.db')
# 第二步：获取游标
c = conn.cursor()
# 第三步：调用execute执行select语句
c.execute('select * from user_tb where _id > ?', (2,))
print('查询返回的记录数：', c.rowcount)
# 通过游标的description属性获取列信息
for col in (c.description):
    print(col[0], end='\t')
print('\n-------------------------')
while True:
    # 获取一条记录，每行数据都是一个元组
    row = c.fetchone()
    # 如果获取的row为None，也就是没有查询到数据，则退出循环
    if not row:
        break
    print(row)
    print(row[1] + '-->' + row[2])
# 第四步：关闭游标
c.close()
# 第五步：关闭数据库连接
conn.close()
