import math


class Point:
    # 定义构造函数
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # 重写方法__sub__为-操作符提供支持
    def __sub__(self, other):
        return Point((self.x - other.x),
                     (self.y - other.y),
                     (self.z - other.z))

    # 定义方法dot,计算点积
    def dot(self, other):
        return Point((self.x * other.x),
                     (self.y * other.y),
                     (self.z * other.z))

    # 定义方法cross，计算叉积
    def cross(self, other):
        return Point((self.y * other.z - self.z * other.y),
        (self.z * other.x - self.x * other.z),
        (self.x * other.y - self.y * other.x))

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

    # 定义方法接收b,c,d三个参数，计算当前点、b 、c 组成的面与b 、c 、d 组成的面之间的夹角
    def angle(self, b, c, d):
        X = (b - self).cross(c - b)
        Y = (c - b).cross(d - c)
        return math.acos(X.dot(Y) / (X.absolute() * Y.absolute()))


if __name__ == '__main__':
    points = list()
    print('请依次输入4个点的x y z（中间以空格隔开）')
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Point(*points[0]), Point(*points[1]), Point(*points[2]), Point(*points[3])
    angle = a.angle(b, c, d)
    print("%.2f" % math.degrees(angle))