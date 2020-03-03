class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


im = Item('鼠标', 28.9)
print(im.__dict__)
# 通过__dict__访问name属性
print(im.__dict__['name'])    # 鼠标
# 通过__dict__访问price属性
print(im.__dict__['price'])    # 28.9
im.__dict__['name'] = '键盘'
im.__dict__['price'] = 32.8
print(im.name)    # 键盘
print(im.price)    # 32.8