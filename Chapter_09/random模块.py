import random


# 生成范围为0.0≤x≤1.0的伪随机浮点数
print(random.random())
# 生成范围为2.5≤x≤10.0的伪随机浮点数
print(random.uniform(2.5, 10.0))
# 生成呈指数分布的伪随机浮点数
print(random.expovariate(1 / 5))
# 生成从0到100的随机偶数
print(random.randrange(0, 101, 2))
# 随机抽取一个元素
print(random.choice(['Python', 'Swift', 'Kotlin']))
book_list = ['Python', 'Swift', 'Kotlin']
# 对列表元素进行随机排列
random.shuffle(book_list)
print(book_list)
# 随机抽取4个独立的元素
print(random.sample([10, 20, 30, 40, 50], k=4))