#!/usr/bin/python3
"""api v1 index"""


from api.v1.views import app_views
from flask import jsonify


@app_views("/status", methods["GET"], strict_slashes=False)
def status_route():
    """JSON Serialiasble Object with site status"""

    return jsonify({"status": "OK"})
