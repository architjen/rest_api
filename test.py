import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.get(BASE + 'investments')
print(response.json())

response = requests.post(BASE + 'investments')
print(response.json())