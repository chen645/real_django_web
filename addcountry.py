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
data = raw_data[1]

countries_name = list(data['countries']['name'])

countries_id = list(data['countries']['id'])
countries = zip(countries_id,countries_name)

print(type(countries))
for country in countries:
    # print(country)
    temp = Country(name=country[1],country_id=country[0])
    temp.save()
    print(country)

countries = Country.objects.all()
print(countries)
print("done!")