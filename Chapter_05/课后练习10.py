def fn(n):
    # 先输出n行n列的矩阵
    for i in range(n):
        for j in range(n):
            print(i * n + j + 1, end=' ')
        print()
    # 再输出转置矩阵
    for i in range(n):
        for j in range(n):
            print(j * n + i + 1, end=' ')
        print()
fn(3)