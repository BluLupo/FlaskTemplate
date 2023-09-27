#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright Hersel Giannella

from flask import Flask
from config import Config
from routes.home import route_home

app = Flask(__name__)

############
## ROUTES ##
############
app.register_blueprint(route_home,url_prefix=Config.URL_PREFIX)

if __name__ == '__main__':
    app.run(debug=Config.APP_DEBUG, host=Config.APP_HOST, port=Config.APP_PORT)