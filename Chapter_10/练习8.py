from datetime import datetime as dt

time_str1 = input('请输入带时区的时间戳字符串：')
time_str2 = input('请再输入一个带时区的时间戳字符串：')
fmt = '%a %d %b %Y %H:%M:%S %z'
diff_time = int(abs((dt.strptime(time_str1, fmt) - dt.strptime(time_str2, fmt)).total_seconds()))
print('两个时间戳之间相差%d秒' % diff_time)