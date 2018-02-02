from model.Model import app
from classes.UserClass import UserClass
from flask import render_template, request
import csv
import io
import random



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        
        f = request.files['file']
        print ('teste')
        if not f:
            return "No file"
        uc = UserClass()
        uc.adicionar_usuario(f)
        return 'Tem file'
    else:
        return 'get'

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        uc = UserClass()
        uc.login('mariana.albano@outlook.com',660416)

    else:
        return render_template("login.html")

    return "teste"


@app.route("/home")
def home():
    pass
    

if __name__ == '__main__':
    app.run(debug=True)