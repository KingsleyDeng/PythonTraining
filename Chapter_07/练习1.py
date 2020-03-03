n = input("请输入一个整数")
try:
    num = int(n)
    i = 0
    while (True):
        num_str = input("请输入以空格分隔的两个整数")
        try:
            a, b = num_str.split(' ')
            print("%d整除%d的结果为：%d" % (int(a), int(b), int(a) // int(b)))
            i += 1
            if i >= num:
                break
        except ValueError:
            print("必须输入两个以空格隔开的数字，请重新输入！")
            continue
except ValueError:
    print("请输入一个数字")
