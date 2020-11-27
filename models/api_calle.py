import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def geolocator(lat, long):
    locator = Nominatim(user_agent="myGeocoder")
    coordinates = f"{lat}, {long}"
    location = locator.reverse(coordinates)
    road_string = location.raw['address']['road']
    if 'Doctor' in road_string:
        long = len('Doctor')
        return road_string[long:]
    print(road_string)
    return road_string
