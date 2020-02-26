#codeing: utf-8
height = int(input("请输入菱形的高度: "))
height = (height +1)//2
for i in range(height):
    half_blank = " " * (int((height*2-1-(i*2+1))/2))
    if i == 0:
        print(half_blank,"*",half_blank,sep='')
    else:
        mid_blank = " " * (i*2-1)
        print(half_blank,"*",mid_blank,"*",half_blank,sep='')
for i in range(height-1,-1,-1):
    half_blank = " " * (int((height*2-1-(i*2+1))/2))
    if i == 0:
        print(half_blank,"*",half_blank,sep='')
    else:
        mid_blank = " " * (i*2-1)
        print(half_blank,"*",mid_blank,"*",half_blank,sep='')