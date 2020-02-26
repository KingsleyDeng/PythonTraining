def count_str_char(my_str):
    digit_count = 0
    char_count = 0
    blank_count = 0
    other_count = 0
    for ch in my_str:
        if ch.isdigit():
            digit_count += 1
        elif ch.encode('utf-8').isalpha():
            char_count += 1
        elif ch.isspace():
            blank_count += 1
        else:
            other_count += 1
    return digit_count, char_count, blank_count, other_count


while(True):
    my_str = input('请输入一个字符串：')
    if my_str == 'exit':
        import sys
        sys.exit(0)
    digit_count, char_count, blank_count, other_count = count_str_char(my_str)
    print('字母个数：', char_count)
    print('数字个数', digit_count)
    print('空白个数：', blank_count)
    print('其他字符个数：', other_count)