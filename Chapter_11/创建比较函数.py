import sqlite3

# 定义函数 去掉字符串的第一个字符和最后一个字符 比较大小
def my_collate(st1, st2):
    if st1[1:-1] == st2[1:-1]:
        return 0
    elif st1[1:-1] > st2[1:-1]:
        return 1
    else:
        return -1


# 第一步：打开或创建数据库
conn = sqlite3.connect('first.db')
# 调用conn.create_collation()注册自定义比较函数：sub_cmp
conn.create_collation('sub_cmp', my_collate)
# 第二步：获取游标
c = conn.cursor()
# 第三步：在SQL语句中使用sub_cmp自定义比较函数
c.execute('select * from user_tb order by pass collate sub_cmp')
# 采用for循环遍历游标
for row in c:
    print(row)
# 提交事务
conn.commit()
# 第四步：关闭游标
c.close()
# 第五步：关闭数据库连接
conn.close()