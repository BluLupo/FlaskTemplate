#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright Hersel Giannella

from flask import Blueprint, render_template, request

route_home = Blueprint('route_home', __name__)

@route_home.route('/', methods=['GET', 'POST'])
def home():
    test_list = ['apple', 'orange', 'lemon']
    test_dict = [{
        "a": "apple",
        "b": "orange",
        "c": "lemon"
    },
    {
        "d": "strawberry",
        "e": "banana",
        "f": "watermelon"
    }]
    if request.method == 'GET':
        return render_template('home.html',list=test_list,dict=test_dict)
    elif request.method == 'POST':
        form_data = request.form
        hidden_input = form_data['testpost']
        print(hidden_input)
        return render_template('home.html',list=test_list,dict=test_dict)
    else:
        return "Method not Allowed!!!"