import ipinfo
import pprint
import models.constants as Constants

access_token = Constants.API_IP_TOKEN #Constants.API_IP_TOKEN


def ip_info(ip_address=None):
    handler = ipinfo.getHandler(access_token)
    print(handler)
    print(ip_address)
    details = handler.getDetails(ip_address)
    pprint.pprint(details.all)
    print(details.city)

    city_str = details.city
    lat_long = details.loc.split(',')
    lat_str = lat_long[0]
    long_str = lat_long[1]

    return [lat_str, long_str, city_str]
