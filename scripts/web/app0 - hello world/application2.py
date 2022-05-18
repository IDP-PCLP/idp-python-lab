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

@app.route("/estudantes")
def estudantes():
    estudantes = [{"nome":"Xerxes","curso":"Eco"},
                  {"nome":"Calvin","curso":"Jor"}]
    pagina = ""
    for estudante in estudantes:
        texto = f"Estudante {estudante['nome']} do curso {estudante['curso']}"
        pagina = pagina + "\n <p> " + texto + " </p>"
    return pagina

if __name__ == "__main__":
    app.run(debug=True)