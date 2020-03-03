class Points:
    # 定义构造函数，传入x，y值
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 定义__sub__方法，以支持-操作符
    def __sub__(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


if __name__ == '__main__':
    p1 = Points(1, 2)
    p2 = Points(1, 3)
    print('两点之间的距离为：', p1 - p2)