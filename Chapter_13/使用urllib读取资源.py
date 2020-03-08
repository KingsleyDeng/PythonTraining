from urllib.request import urlopen

# 打开URL对应资源
result = urlopen('http://www.ib-top.com')
# 按字节读取数据
data = result.read(326)
# 将字节数据恢复成字符串
print(data.decode('utf-8'))

# 用context manager来管理打开的URL资源
with urlopen('http://www.ib-top.com') as f:
    # 按字节读取数据
    data = f.read(326)
    # 将字节数据恢复成字符串
    print(data.decode('utf-8'))
# 在使用urlopen时，可以通过data属性向被请求的URL发送数据。
