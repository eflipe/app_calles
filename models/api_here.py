import requests
import models.constants as Constants


# 'at': '{},{}'.format(latitude,longitude),
# at=[-34.6131, -58.3772]
def api_here(latitude, longitude):

    URL = Constants.URL_HERE
    api_key = Constants.API_KEY_HERE # Acquire from developer.here.com

    location = "Buenos Aires"
    at='{},{}'.format(latitude,longitude)
    PARAMS = {'apikey':api_key,'at':at}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()

    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']
    address = data['items'][0]['address']['label']
    street = data['items'][0]['address']['street']
    district = data['items'][0]['address']['district']

    # print(latitude)
    # print(longitude)
    # print(address)
    # print(street)
    # print(district)
    return [api_key, latitude, longitude, address]
