# file for testing
import requests

BASE = 'http://127.0.0.1:5000/'

# looking for all the investments
response = requests.get(BASE + 'investments')
print(response.json())

# searching for the investments related to the city Paris
response = requests.get(BASE + 'investments/city/Paris')
print(response.json())
#print('nothing')

# searching for investment related to the specific id
response = requests.get(BASE + 'investments/id/0750671X')
print(response.json())

# creating a new investment entry in case the id is not found.
response = requests.post(BASE + 'investments?id=0750671X&lycee=abc&ville=Lyon&year=2016')
print(response.json())
