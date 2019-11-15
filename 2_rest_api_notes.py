# jsonplaceholder.com untuk mendapatkan file API fake sebagai latihan
# download dan install postman

# python GET request => API
# urllib

import requests
url = 'http://jsonplaceholder.typicode.com/users'
data = requests.get(url)
# print(data.json()['name'])
# print(data.json()['email'])
# print(type(data.json()))

for i in data.json():
    print(i['name'], i['address'])

