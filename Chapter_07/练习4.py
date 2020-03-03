try:
    x1, y1, x2, y2, x3, y3 = input('请依次输入6个坐标点以空格隔开').split(' ')
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    x3 = float(x3)
    y3 = float(y3)
    if x1 == 0 and x2 == 0 and x3 == 0:
        print('三个点在一条直线上')
    elif 0 in (x1, x2, x3):
        raise Exception('三个点不在同一直线上')
    elif y1 / x1 == y2 / x2 and y1 / x1 == y3 / x3:
        print('三个点在同一直线上')
    else:
        raise Exception('三个点不在同一直线上')
except ValueError:
    print('输入的坐标必须为数字！')