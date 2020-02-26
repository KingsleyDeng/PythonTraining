#codeing: utf-8
height = int(input("请输入腰三角形的高度: "))
for i in range(height):
    star = "*" * (i*2+1)
    half_blank = " " * (int((height*2-1-(i*2+1))/2))
    print(half_blank,star,half_blank)