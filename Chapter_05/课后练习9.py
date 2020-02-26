import random


def fn(n):
    temp_lst = []
    for i in range(n):
        while (True):
            ch = chr(random.randint(65, 91))
            if ch not in temp_lst:
                temp_lst.append(ch)
                break
    return tuple(temp_lst)


print(fn(10))
