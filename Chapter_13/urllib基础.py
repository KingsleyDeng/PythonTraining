from urllib.parse import urlparse

# 解析URL字符串
result = urlparse('http://www.ib-top.com:8080/index.php;yeeku?name=parse_test#parse')

print(result)
# 通过属性名和索引来获取URL的各部分

print('scheme:', result.scheme, result[0])
print('主机和端口：', result.netloc, result[1])
print('主机：', result.hostname)
print('端口：', result.port)
print('资源路径：', result.path, result[2])
print('参数：', result.params, result[3])
print('查询字符串：', result.query, result[4])
print('fragment：', result.fragment, result[5])
print(result.geturl())