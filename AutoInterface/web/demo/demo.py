import requests
import json

data = {
    'username':'mosheng',
    'password':'123456'
}
url = 'http://127.0.0.1:8000/login/'

res = requests.post(url,data)

print(res.json())
4-2
