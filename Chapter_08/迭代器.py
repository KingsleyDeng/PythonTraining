# 定义一个代表斐波那锲数列的迭代器
class Fibs:
    def __init__(self, len):
        self.first = 0
        self.sec = 1
        self.__len = len


# 定义迭代器所需的__next__方法
    def __next__(self):
        # 如果__len属性为0，结束迭代
        if self.__len == 0:
            raise StopIteration
        # 完成数列计算
        self.first, self.sec = self.sec, self.first + self.sec
        # 数列长度减1
        self.__len -= 1
        return self.first



    # 定义__iter__方法，该方法范虎迭代器
    def __iter__(self):
        return self



# 创建Fibs对象
fibs = Fibs(10)
# 获取迭代器的下一个元素
print(next(fibs))
# 使用for循环遍历迭代器
for el in fibs:
    print(el, end=' ')

# 程序可使用内置的iter()
# 函数将列表、元组等转换成迭代器。

# 定义ValueDict类，继承dict类
class ValueDict(dict):
    # 定义构造函数
    def __init__(self, *args, **kwargs):
        # 调用父类构造函数
        super().__init__(*args, **kwargs)



    # 新增getkeys方法
    def getkeys(self, val):
        result = []
        for key, value in self.items():
            if value == val:
                result.append(key)
        return result



my_dict = ValueDict(语文=92, 数学=89, 英语=92)
# 获取92对应的所有key
print(my_dict.getkeys(92))  # 语文 英语
my_dict['编程'] = 92
print(my_dict.getkeys(92))  # 语文 英语 编程