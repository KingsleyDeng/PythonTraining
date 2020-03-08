from urllib.request import urlopen

url = 'http://www.crazyit.org'

result = urlopen(url)

data = result.read()

data = data.decode('utf-8')

print(data)
with open('crazyit.html','w+') as f:
    f.write(data)