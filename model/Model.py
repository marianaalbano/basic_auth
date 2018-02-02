#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_mongoengine import MongoEngine



from datetime import datetime


app = Flask(__name__,static_folder='../static', template_folder='../templates')
app.config['MONGODB_SETTINGS'] = {"db":"auth_simple"}
db = MongoEngine(app)


class Usuarios(db.Document):
    nome = db.StringField()
    sobrenome = db.StringField()
    email = db.StringField()
    senha = db.StringField()
    data_login = db.IntField()