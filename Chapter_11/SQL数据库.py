import sqlite3
# Python默认自带了SQLite数据库和SQLite数据库的API模块。
# SQLite只是一个嵌入式的数据库引擎，专门适用于在资源有限的设备上（如手机、PDA等）进行适量数据的存取。
# SQLite数据库只是一个文件，不需要服务器进程。SQLite不需要安装、启动服务器进程。
print(sqlite3.apilevel)
print(sqlite3.paramstyle)

conn = sqlite3.connect('first.db')
c = conn.cursor()
c.execute('''create table user_tb(
_id integer primary key autoincrement,
name text,
pass text,
gender text)
''')

# 执行DDL语句创建数据表
c.execute('''
create table order_tb(
_id integer primary key autoincrement,
item_name text,
item_price real,
item_number real,
user_id inteter,
foreign key(user_id) references user_tb(_id))
''')
# 第四步：关闭游标
c.close()
# 第五步：关闭数据库连接
conn.close()
