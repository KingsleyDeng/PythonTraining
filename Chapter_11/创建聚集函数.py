import sqlite3


# 定义类 准备注册为SQL中的自定义聚集函数
class MinLen:
    def __init__(self):
        self.min_len = None

    def step(self, value):
        # 如果self.min_len还未赋值 则直接将当前value赋给self.min_len
        if self.min_len is None:
            self.min_len = value
            return
        # 找到一个长度更短的value 则value代替self.min_len
        if len(self.min_len) > len(value):
            self.min_len = value

    def finalize(self):
        return self.min_len


# 第一步：打开或创建数据库
conn = sqlite3.connect('first.db')
# 调用create_aggregate注册自定义聚集函数：min_len
conn.create_aggregate('min_len', 1, MinLen)
# 第二步：获取游标
c = conn.cursor()

# 第三步：使用自定义聚集函数
c.execute('select min_len(pass) from user_tb')
print(c.fetchone()[0])
# 提交事务
conn.commit()
# 关闭游标
c.close()
# 关闭连接
conn.close()
