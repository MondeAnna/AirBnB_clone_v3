#!/usr/bin/python3
"""load server framework"""


import os
from flask import Flask
from models import storage
from api.v1.views import app_views


HOST = os.getenv("HBNB_API_HOST", "0.0.0.0")
PORT = os.getenv("HBNB_API_PORT", "5000")


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_app(exception):
    """teardown app session"""

    storage.close()


if __name__ == "__main__":
    app.run(HOST, PORT, threaded=True)
