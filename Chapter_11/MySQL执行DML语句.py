# 导入访问MySQL的模块
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
# 第三步：调用execute()执行insert语句插入数据
c.execute('insert into user_tb values(null, %s, %s, %s)',
          ('张三', '123456', 'male'))
c.execute('insert into order_tb values(null, %s, %s, %s, %s)',
          ('鼠标', '34.2', '3', 1))
# 提交事务，将数据写入数据库
conn.commit()
# 第四步：关闭游标
c.close()
# 第五步：关闭连接
conn.close()
