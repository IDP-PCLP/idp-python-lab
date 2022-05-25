#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Projeto Aplicação Web

Formulários e Banco de Dados

Professor: Álvaro Campos Ferreira
Contato: alvaro.ferreira@idp.edu.br
'''

from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

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


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        new_user = User(
            username=request.form['username'],
            password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('registrar.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        try:
            data = User.query.filter_by(username=name, password=passw).first()
            if data is not None:
                session['logged_in'] = True
                return redirect(url_for('index'))
            else:
                return 'Erro login - usuário não encontrado'
        except:
            return "Erro Login"

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.secret_key = "123"
    app.run(host='0.0.0.0')