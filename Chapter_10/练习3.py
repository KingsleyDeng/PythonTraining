import re
import sys

while True:
    phone_str = input('请输入手机号码：')
    if phone_str.lower() == 'exit':
        sys.exit(0)
    else:
        if re.fullmatch(
                r'^(1[358][0-9]|14[579]|16[6]|17[0135678]|19[89])\d{8}$',
                phone_str):
            print('手机号码有效！')
        else:
            print('手机号码无效！')