from flask import Flask
from dotenv import load_dotenv
from views.item_calle import calle_blueprint

load_dotenv()
app = Flask(__name__)

app.register_blueprint(calle_blueprint, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, host="0.0.0.0", port=5000)
