import requests
'''
{'status': 400, 'title': "Illegal input for parameter 'at'",
'cause': "Actual parameter value: 'Buenos Aires'",
'action': 'Expecting string formatted like 43.42387,15.490238',
'correlationId': '3a778093-52e4-4722-9534-690ee9210e47',
'requestId': 'REQ-312f15d4-4049-4a12-85f8-db0563417d55'}
'''

# 'at': '{},{}'.format(latitude,longitude),
# at=[-34.6131, -58.3772]
def api_here(latitude, longitude):
    URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"
    location = "Buenos Aires"
    at='{},{}'.format(latitude,longitude)
    api_key = 'DTefltZHcbSfUzgnavsqWrZbsPZgEJ3EFHyz-EDcqBc' # Acquire from developer.here.com
    PARAMS = {'apikey':api_key,'at':at}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()

    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']
    address = data['items'][0]['address']['label']
    street = data['items'][0]['address']['street']
    district = data['items'][0]['address']['district']

    print(latitude)
    print(longitude)
    print(address)
    print(street)
    print(district)
    return [api_key, latitude, longitude, address]
