#!/usr/bin/python3
"""api v1 index"""


from flask import jsonify


from api.v1.views import app_views
from models import storage


@app_views.route("/status", methods["GET"], strict_slashes=False)
def status_route():
    """JSON Serialiasble Object with site status"""

    return jsonify({"status": "OK"})

@app_views.route("/stats", methods["GET"], strict_slashes=False)
def stats_route():
    """JSON Serialiasble Object with site stats"""

    return jsonify({
        "amnesty": storage.count(Amensty),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User),
    })
