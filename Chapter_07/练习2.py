n = input('请输入一个整数：')
try:
    n = int(n)
    if (n % 2 == 0) and (n >= 2) and (n <= 5):
        print('没意思！')
    elif (n % 2 == 0) and (n >= 6) and (n <= 20):
        print('有趣！')
    elif (n % 2 != 0):
        print('有趣！')
except ValueError:
    print('输入的必须是一个数字！')