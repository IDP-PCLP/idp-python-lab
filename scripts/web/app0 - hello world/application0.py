#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplicação Web

@author: cafe
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá, mundo!"

if __name__ == "__main__":
    app.run(debug=True)