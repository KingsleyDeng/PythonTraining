from urllib.request import urlopen
import re

url = 'http://www.crazyit.org'

result = urlopen(url)

data = result.read()

pattern = r'<a\s+href=\"([a-zA-Z0-9\.:\?&=\-;/%]+)\"'
link_list = re.finditer(pattern, data.decode('utf-8'))
for link in link_list:
    print(link.group(1))