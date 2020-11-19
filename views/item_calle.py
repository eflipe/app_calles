from flask import Blueprint, render_template, request
from models.item_calle import Calle
from models.api_calle import geolocator
from models.api_here import api_here
from models.api_ip import ip_info






calle_blueprint = Blueprint('item_calle', __name__)


@calle_blueprint.route('/', methods=['GET', 'POST']) # index
def index():
    if request.method == 'POST':
        calle_lat = request.form['lat_url']
        calle_long = request.form['long_url']
        print(calle_lat, calle_long)
        geo_calle = geolocator(calle_lat, calle_long)
        print(geo_calle)
        info_calle = Calle(geo_calle)
        print_calle = info_calle.load_calle()
        wiki_calle = info_calle.wiki_calle()

        return render_template("info_calle.html", geo_calle=geo_calle,
                                print_calle=print_calle, wiki_calle=wiki_calle)

    ip_info_api = ip_info()
    context = api_here(ip_info_api[0], ip_info_api[1])
    print(type(context))

    print(context)
    print(context[1])
    print(context[2])

    return render_template("new_calle.html", api_key=context[0],
                           lat_str=ip_info_api[0], long_str=ip_info_api[1],
                           address=context[3], city_str=ip_info_api[2])
    #return render_template("new_calle.html", lat_str=lat_str, long_str=long_str, city_str=city_str)
