def fn(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * fn(n-1)


while(True):
    n = input('请输入一个整数：')
    if n == 'exit':
        import sys
        sys.exit(0)
    if not n.isdigit():
        print('您输入的不是一个数字！')
        continue
    print('%s的阶乘是：%d' % (n, fn(int(n))))