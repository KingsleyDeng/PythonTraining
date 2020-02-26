# codeing: utf-8
height = int(input("请输入菱形的高度: "))
height = (height + 1) // 2
for i in range(height):
    star = "*" * (i * 2 + 1)
    half_blank = " " * (int((height * 2 - 1 - (i * 2 + 1)) / 2))
    print(half_blank, star, half_blank)
for i in range(height - 1, -1, -1):
    star = "*" * (i * 2 + 1)
    half_blank = " " * (int((height * 2 - 1 - (i * 2 + 1)) / 2))
    print(half_blank, star, half_blank)
