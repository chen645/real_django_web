#addcity.py

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()
import pandas as pd
import time
from mysite.models import Post,Country,City

url = "https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html"

raw_data = pd.read_html(url)
time.sleep(3)   #complete test just don't need
data = raw_data[0]

cities = list()
for i in range(len(data)):
    temp = tuple(data["cities"].iloc[i])
    cities.append(temp)
# print(cities)

for city in cities:
    #根據country_id內容 找到country表格內的紀錄
    #把此紀錄放到下面指令的country參數
    # print(city[1],city[2],city[3])
    # print(city[2])
    try:
        country=Country.objects.get(country_id=city[2])
        # print(country.country_id)
        temp = City(name= city[1], country=country,population=city[3])
        temp.save()
    except:
        pass

cities = City.objects.all()
print(cities)
print("done!")
