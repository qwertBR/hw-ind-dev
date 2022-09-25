"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template

# Local modules
from config import connex_app

# Get the application instance
connex_app = connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yaml")


if __name__ == "__main__":
    connex_app.run(debug=True, port=1234)
