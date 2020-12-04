from flask import Blueprint, render_template, request, flash
from models.item_calle import Calle
from models.api_calle import geolocator
from models.api_here import api_here
from models.api_ip import ip_info
from models.search_calle import calle_txt
from flask import jsonify
import urllib.request
import json


url = 'http://api.hostip.info/get_json.php'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
info = json.loads(urllib.request.urlopen(req).read())
#ip_address = info['ip']

calle_blueprint = Blueprint('item_calle', __name__)


#flask run -h 192.168.0.85
@calle_blueprint.route('/', methods=['GET', 'POST'])  # index
def index():
    print(request.headers)

    headers_list = request.headers.getlist("X-Forwarded-For")
    print(request.headers)
    ip_address = headers_list[0] if headers_list else request.remote_addr
    print(ip_address)

    ip_address = "201.212.251.103"

    ip_info_api = ip_info(ip_address)

    if request.method == 'POST':
        calle_lat = request.form['lat_url_1']
        calle_long = request.form['long_url_2']
        print(calle_lat, calle_long)
        context = api_here(calle_lat, calle_long)
        print(type(context))

        print(context)
        print(context[1])
        print(context[2])
        print(context[4])

        geo_calle = geolocator(calle_lat, calle_long)
        print(geo_calle)
        info_calle = Calle(geo_calle)
        if context[4] == "Ciudad de Buenos Aires":
            print_calle = calle_txt(geo_calle)
            if not print_calle:
                print("No encontrado")
                print_calle = info_calle.load_calle()
        else:
            print_calle = info_calle.load_calle()

        wiki_calle = info_calle.wiki_calle()

        return render_template("info_calle.html", geo_calle=geo_calle,
                                 print_calle=print_calle, wiki_calle=wiki_calle,
                                 api_key=context[0], address=context[3],
                                 lat_str=calle_lat, long_str=calle_long)

    return render_template("new_calle.html",
                           lat_str=ip_info_api[0], long_str=ip_info_api[1],
                           city_str=ip_info_api[2])
    # return render_template("new_calle.html", lat_str=lat_str, long_str=long_str, city_str=city_str)


@calle_blueprint.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


@calle_blueprint.route("/busqueda_calle", methods=["GET", "POST"])
def busqueda_calle():
    if request.method == 'POST':
        busqueda_calle = request.form['busqueda_calle']
        error = None

        if not busqueda_calle:
            busqueda_calle = 'Por favor, introducir el nombre de la calle'
            return render_template("info_calle.html",
                                    geo_calle=busqueda_calle)

        if error is None:
            info_calle = Calle(busqueda_calle)
            print_calle = calle_txt(busqueda_calle)

            if not print_calle:
                print("No encontrado")
                print_calle = info_calle.load_calle()

            wiki_calle = info_calle.wiki_calle()

            return render_template("info_calle.html",
                                    geo_calle=busqueda_calle.title(),
                                    print_calle=print_calle,
                                    wiki_calle=wiki_calle)
        # flash(error)

    return render_template('busqueda_calle.html')


# @calle_blueprint.errorhandler(404)
# def not_found(e):
#     return render_template('404.html'), 404
