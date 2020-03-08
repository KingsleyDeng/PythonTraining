import mysql.connector

print(mysql.connector.apilevel)
print(mysql.connector.paramstyle)

# 连接数据库
conn = mysql.connector.connect(
    user='root',
    password='DawnDeng1993',
    host='localhost',
    port='3306',
    database='python',
    use_unicode=True
)

# 获取游标
c = conn.cursor()
# 执行DDL语句
c.execute('''
    create table user_tb(user_id int primary key auto_increment,
    name varchar(255),
    pass varchar(255),
    gender varchar(255))
    ''')
c.execute('''
    create table order_tb(order_id integer primary key auto_increment,
    item_name varchar(255),
    item_price double,
    item_number double,
    user_id int,
    foreign key(user_id) references user_tb(user_id))
    ''')
c.close()
conn.close()