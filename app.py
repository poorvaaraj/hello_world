# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:43:41 2021

@author: poorva
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"