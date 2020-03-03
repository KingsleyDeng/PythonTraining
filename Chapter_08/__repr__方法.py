class Apple:
    # 实现构造器
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    # 重写__repr__()方法，用于实现Apple对象的自我描述
    def __repr__(self):
        return "Apple[color=" + self.color + \
               ",weight=" + str(self.weight) + "]"


a = Apple('红色', 5.68)
# 打印Apple对象
print(a)  # Apple[color=红色,weight=5.68]