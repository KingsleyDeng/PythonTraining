def sort_list(sort_list):
    temp_list = []
    for i in range(len(sort_list)):
        min_var = min(sort_list)
        sort_list.remove(min_var)
        temp_list.append(min_var)
    return temp_list


my_list = [3,42,43,12,5,3,65]
print(sort_list(my_list))