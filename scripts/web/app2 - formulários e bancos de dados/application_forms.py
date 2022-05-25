#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Projeto Aplicação Web

Professor: Álvaro Campos Ferreira
Contato: alvaro.ferreira@idp.edu.br
'''

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

nomes = []
passwords = []

@app.route("/")
def index():
    name = request.args.get("name")
    return render_template('index.html',name=name)

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/recursos")
def recursos():
    return render_template('recursos.html')

@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome=request.form['username']
        password=request.form['password']
        nomes.append(nome)
        passwords.append(password)
        pd.DataFrame({'nome':nomes,'password':passwords}).to_excel('usuarios.xlsx')
        return render_template('index.html',name=nome)
    return render_template('registrar.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)