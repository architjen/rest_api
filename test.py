# file for testing
import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.get(BASE + 'investments')
print(response.json())

response = requests.get(BASE + 'investments/city/Paris')
print(response.json())
#print('nothing')

response = requests.get(BASE + 'investments/id/0750671X')
print(response.json())
