
import sys
from collections import Counter

while True:
    user_str = input('请输入一个字符串：')
    if user_str.lower() == 'exit':
        sys.exit(0)
    user_counter = Counter(user_str)
    # print('字符串中出现最多的3个字符为：', user_counter.most_common(3))
    [print(t[0]) for t in user_counter.most_common(3)]