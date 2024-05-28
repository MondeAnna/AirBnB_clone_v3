#!/usr/bin/python3
"""load server framework"""


import os


from flask import make_response
from flask import jsonify
from flask import Flask


from api.v1.views import app_views
from models import storage


HOST = os.getenv("HBNB_API_HOST", "0.0.0.0")
PORT = os.getenv("HBNB_API_PORT", "5000")


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_app(exception):
    """teardown app session"""

    storage.close()


@app.errorhandler(404)
def not_found():
    """404 page not found error"""

    response = jsonify({"error": "Not found"})
    return make_response(response, 404


if __name__ == "__main__":
    app.run(HOST, PORT, threaded=True)
