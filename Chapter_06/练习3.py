class Point:
    # 构造函数，接收x，y坐标作为参数
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 计算两个点之间的距离，接收一个Point实例对象作为参数
    def distance(self, other):
        x_distance = (self.x - other.x) ** 2
        y_distance = (self.y - other.y) ** 2
        return (x_distance + y_distance) ** 0.5

    # 判断三个点组成的三角形是锐角、钝角还是直角三角形
    def judge_triangle(self, other, another):
        # 计算三条边的长度
        side1 = self.distance(other)
        side2 = self.distance(another)
        side3 = other.distance(another)
        # 找出最长的边
        max_side = max(side1, side2, side3)
        if max_side == side1:
            # 先判断能否构成三角形
            if (side2 + side3) < side1:
                print('三边长度为%s，%s，%s，最长边为：%s，这不是一个三角形' % (side1, side2, side3, side1))
            else:
                # 计算side2的平方与side3的平方和,并判断其是否大于side1的平方
                if (side2 ** 2 + side3 ** 2) > (side1 ** 2):
                    print('这是一个锐角三角形')
                elif (side2 ** 2 + side3 ** 2) < (side1 ** 2):
                    print('这是一个钝角三角形')
                elif (side2 ** 2 + side3 ** 2) == (side1 ** 2):
                    print('这是一个直角三角形')
        elif max_side == side2:
            # 先判断能否构成三角形
            if (side1 + side3) < side2:
                print('三边长度为%s，%s，%s，最长边为：%s，这不是一个三角形' % (side1, side2, side3, side2))
            else:
                # 计算side2的平方与side3的平方和,并判断其是否大于side1的平方
                if (side1 ** 2 + side3 ** 2) > (side2 ** 2):
                    print('这是一个锐角三角形')
                elif (side1 ** 2 + side3 ** 2) < (side2 ** 2):
                    print('这是一个钝角三角形')
                elif (side1 ** 2 + side3 ** 2) == (side2 ** 2):
                    print('这是一个直角三角形')
        elif max_side == side3:
            # 先判断能否构成三角形
            if (side1 + side2) < side3:
                print('三边长度为%s，%s，%s，最长边为：%s，这不是一个三角形' % (side1, side2, side3, side3))
            else:
                # 计算side2的平方与side3的平方和,并判断其是否大于side1的平方
                if (side1 ** 2 + side2 ** 2) > (side3 ** 2):
                    print('这是一个锐角三角形')
                elif (side1 ** 2 + side2 ** 2) < (side3 ** 2):
                    print('这是一个钝角三角形')
                elif (side1 ** 2 + side2 ** 2) == (side3 ** 2):
                    print('这是一个直角三角形')

    def __repr__(self):
        return 'P(%s，%s)' % (self.x, self.y)


if __name__ == '__main__':
    p1 = Point(0, 0)
    p2 = Point(3, 3)
    p3 = Point(0, 12)
    p4 = Point(5, 5)
    print('%s到%s的距离为：%s' % (p1, p2, p1.distance(p2)))
    print('%s到%s的距离为：%s' % (p1, p3, p1.distance(p3)))
    print('%s到%s的距离为：%s' % (p2, p3, p2.distance(p3)))
    print('{}，{}，{}，组成的三角形是：'.format(p1, p2, p3), end='')
    p1.judge_triangle(p2, p3)