import re

user_str, sub_str = input('请输入字符串：'), input('请输入子字符串：')
matches = list(re.finditer(r'(?={})'.format(sub_str), user_str))
if matches:
    print('\n'.join(
        str((match.start(), match.start() + len(sub_str) - 1))
        for match in matches))
else:
    print('(-1, -1)')