from flask import Blueprint, render_template, request
from models.item_calle import Calle
from models.api_calle import geolocator
from models.api_here import api_here
from models.api_ip import ip_info
from flask import jsonify
import urllib.request
import json

url = 'http://api.hostip.info/get_json.php'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
info = json.loads(urllib.request.urlopen(req).read())
ip_address = info['ip']
print(ip_address)

calle_blueprint = Blueprint('item_calle', __name__)

#flask run -h 192.168.0.85
@calle_blueprint.route('/', methods=['GET', 'POST'])  # index
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
    # ip_address = request.remote_addr
    # print(type(ip_address))
    # print(str(ip_address))
    # print(type(ip_address))
    ip_info_api = ip_info(ip_address)
    context = api_here(ip_info_api[0], ip_info_api[1])
    print(type(context))

    print(context)
    print(context[1])
    print(context[2])

    return render_template("new_calle.html", api_key=context[0],
                           lat_str=ip_info_api[0], long_str=ip_info_api[1],
                           address=context[3], city_str=ip_info_api[2])
    #return render_template("new_calle.html", lat_str=lat_str, long_str=long_str, city_str=city_str)


@calle_blueprint.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
