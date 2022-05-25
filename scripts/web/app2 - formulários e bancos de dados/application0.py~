#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Projeto Aplicação Web

Professor: Álvaro Campos Ferreira
Contato: alvaro.ferreira@idp.edu.br
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    return render_template('index_inicial.html',name=name)


if __name__ == "__main__":
    app.run(debug=True)