import requests
# https://home.openweathermap.org/api_keys
# user: ridhoaryo
# pass: do

from datetime import datetime
from dateutil import tz

city = input('Input city name:')
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c7178d52369034abdac08bbc2eded593"
data = requests.get(url)
data = data.json()


sunrise = data['sys']['sunrise']
myzone = tz.gettz('Asia/Jakarta')
waktu = datetime.utcfromtimestamp(int(sunrise))
print(waktu.astimezone(myzone))