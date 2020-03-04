import json

name = input('请输入姓名：')
age = input('请输入年龄：')
hight = input('请输入身高：')
with open('info.json', 'w') as f:
    s = json.dump(['info', {'姓名': name, '年龄：': age, '身高：': hight}], f)

# 读取json文件使用load方法
with open('info.json', 'r') as f:
    result = json.load(f)
    print(result)