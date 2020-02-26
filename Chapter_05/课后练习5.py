def fn(n):
    result = 0
    for i in range(n + 1):
        result += pow(i, 3)
    return result


while (True):
    n = input('请输入一个整数:')
    if n == 'exit':
        import sys

        sys.exit(0)
    if not n.isdigit():
        print('您输入的不是一个数字!')
        continue
    print('1~n的立方和为：', fn(int(n)))
