def sort_list(sort_lst):
    lst_len = len(sort_lst)
    for i in range(0, lst_len):
        sort_flag = True
        for j in range(0, lst_len - i - 1):
            if sort_lst[j] > sort_lst[j + 1]:
                sort_lst[j], sort_lst[j + 1] = sort_lst[j + 1], sort_lst[j]
                sort_flag = False
        if sort_flag:
            break
    return sort_lst


my_lst = [5, 9, 3, 1, 2, 8, 4, 7, 6]
print(sort_list(my_lst))
