from flask import Flask, render_template
from views.item_calle import calle_blueprint


app = Flask(__name__)

app.register_blueprint(calle_blueprint, url_prefix="/")


@app.errorhandler(404)
def not_found_404(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def not_found_500(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=False)
    # app.run(debug=True, host="0.0.0.0", port=5000)
