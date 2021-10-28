# file for testing

import requests

if __name__ == "__main__":
    
    BASE = 'http://127.0.0.1:5000/'

    # looking for all the investments
    response = requests.get(BASE + 'investments')
    print(response.json(), response)

    # searching for the investments related to the city Paris
    response = requests.get(BASE + 'investments/city/Paris')
    print(response.json(), response)

    # searching for investment related to the specific id
    response = requests.get(BASE + 'investments/id/0750671X')
    print(response.json(), response)

    # testing post function on a duplicate id 
    response = requests.post(BASE + 'investments?id=0750671X&lycee=abc&ville=Paris&year=2016')
    print(response.json(), response)

    # testing post function on the new id
    response = requests.post(BASE + 'investments?id=025ABC&lycee=abc&ville=Lyon&year=2021')
    print(response.json(), response)

    # testing the patch function on a valid id, SHOULD WORK !! 
    response = requests.patch(BASE + 'investments/id/0750671X?lycee=abc&ville=Lyon&year=2021')
    print(response.json(), response)

    # testingthe patch function on an invalid id, SHOULD FAIL !!
    response = requests.patch(BASE + 'investments/id/07506?lycee=abc&ville=Lyon&year=2021')
    print(response.json(), response)