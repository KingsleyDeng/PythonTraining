import requests
import time

url = 'https://a.hecdn.net/download/dev/china-city-list.csv'
strhtml = requests.get(url)
data = strhtml.text
data1 = data.split("\n")
for i in range(3):
    data1.remove(data1[0])
for item in data1:
    url = 'https://free-api.heweather.net/s6/weather/forecast?location=' + item[
                                                                           0:11] + '&key=aea17cd9b2fd4f509f35456fd9cbd01e'
    strhtml = requests.get(url)
    time.sleep(1)
    dic = strhtml.json()
for item in dic["HeWeather6"][0]["daily_forecast"]:
    print(item["tmp"]["max"])
