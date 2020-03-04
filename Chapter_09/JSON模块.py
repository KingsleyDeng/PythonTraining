import json


# 将Python对象转换为JSON字符串（元组会被当成数组）
s = json.dumps(['yeeku', {'favorite': ('coding', None, 'game', 25)}])
print(s)
# 将简单的Python字符串转换为JSON字符串
s2 = json.dumps("\"foo\bar")
print(s2)
# 将简单的Python字符串转为JSON字符串
s3 = json.dumps('\\')
print(s3)
# 将Python的dict对象转换为JSON字符串，并对key排序
s4 = json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
print(s4)
# 将python列表转换为JSON字符串
# 并制定JSON分隔符：在逗号和冒号之后没有空格（默认有空格）
s5 = json.dumps([1, 2, 3, {'x': 5, 'y': 7}], separators=(',', ':'))
print(s5)
# 指定indent为4，意味着转换的JSON字符串有缩进
s6 = json.dumps({'python': 5, 'Kotlin': 7}, sort_keys=True, indent=4)
print(s6)
# 使用JSONEncoder的encode方法将Python对象转换为JSON字符串
s7 = json.JSONEncoder().encode({"names": ("孙悟空", "齐天大圣")})
print(s7)
f = open('a.json', 'w')
# 使用dump()函数将转换得到的JSON字符串输出到文件中
json.dump(['Kotlin', {'Python': 'excellent'}], f)