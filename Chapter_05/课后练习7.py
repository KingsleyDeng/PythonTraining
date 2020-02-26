def list_uniq(lst):
    temp_lst = set(lst)
    return list(temp_lst)


my_lst = [1, 2, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
print(list_uniq(my_lst))