#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplicação Web

@author: cafe
"""

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(debug=True)