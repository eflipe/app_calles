import ipinfo
import pprint
access_token = "0b334fd91614f7"


def ip_info():
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails()
    print(details.city)
    print(details.city)
    pprint.pprint(details.all)
    

    city_str = details.city
    lat_long = details.loc.split(',')
    lat_str = lat_long[0]
    long_str = lat_long[1]

    return [lat_str, long_str, city_str]
