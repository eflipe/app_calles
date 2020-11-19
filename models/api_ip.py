import ipinfo
import pprint
import models.constants as Constants

access_token = Constants.API_IP_TOKEN


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
