# 导入MySQL模块
import mysql.connector

# 第一步：连接数据库
conn = mysql.connector.connect(
    user='root',
    password='DawnDeng1993',
    host='localhost',
    port='3306',
    database='python',
    use_unicode=True)
# 第二步：获取游标
c = conn.cursor()
# 第三步：调用execute()方法执行select语句查询数据
c.execute('select * from user_tb where user_id > %s', (0,))
# 通过游标的description属性获取列信息
for col in (c.description):
    print(col[0], end='\t')
print('\n--------------------------')
# 使用for循环遍历游标中的结果集
for row in c:
    print(row)
    print(row[1] + '-->' + row[2])
# 第四步：关闭游标
c.close()
# 第五步：关闭连接
conn.close()
