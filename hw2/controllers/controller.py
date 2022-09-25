import json
from flask import abort, make_response, jsonify, request, Response
from db import DB


def hello_handler():
    return Response(response="Hse One Love!", status=200, mimetype="text/plain")


def get_handler(key):

    if key in DB:

        return jsonify([key, DB[key]])

    return abort(404, f"Not found")


def set_handler(body: json):
    DB[body["key"]] = body["value"]
    return make_response("Ok", 200)


def divide_handler(body: json):
    return make_response(str(body["dividend"] / body["divider"]), 200)
