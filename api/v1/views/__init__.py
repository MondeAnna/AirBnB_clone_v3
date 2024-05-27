#!/usr/bin/python3
"""bluesprint api app views"""


from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
