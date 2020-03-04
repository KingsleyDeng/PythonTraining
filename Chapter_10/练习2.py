import re
import sys

while True:
    string = input("请输入字符串（只能包含0-9以及,和.）:")
    if string.lower() == 'exit':
        sys.exit(0)
    else:
        if not re.fullmatch(r'[0-9,\.]+', string):
            raise ValueError('您的输入只能包含0-9数字、英文逗号、英文点号')
        str_list = re.findall('[0-9]+', string)
        print(str_list)