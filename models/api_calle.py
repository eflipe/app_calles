import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def geolocator(lat, long):
    locator = Nominatim(user_agent="myGeocoder")
    coordinates = f"{lat}, {long}"
    location = locator.reverse(coordinates)
    road_string = location.raw['address']['road']
    road_string_edit = ('_').join(road_string.split(' ')[:])
    return road_string_edit
