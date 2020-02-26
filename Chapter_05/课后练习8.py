import random

def fn(n):
    temp_lst = []
    for i in range(n):
        while(True):
            num = random.randint(0, 100)
            if num not in temp_lst:
                temp_lst.append(num)
                break
    return tuple(temp_lst)

print(fn(10))