import re
import sys

while True:
    user_str = input('请输入一个字符串：')
    if user_str.lower() == 'exit':
        sys.exit(0)
    ch_lst = re.findall(r'[a-zA-Z]', user_str)
    for i in range(len(ch_lst)):
        repeat_ch = re.search(ch_lst[i], user_str[i+1:])
        if repeat_ch:
            print('第一次重复出现的英文字母为：', ch_lst[i])
            break