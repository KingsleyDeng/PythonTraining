temp_str = ('this is test', 'test the str', 'test')
for s in temp_str:
    if (len(s) < 5) or (len(s) > 20):
        raise ValueError('元组的每个元素长度必须在5~20之间')