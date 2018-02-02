from model.Model import app
from flask import render_template, request
import csv
import io
from werkzeug.datastructures import FileStorage

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        
        f = request.files['file']
        print (f)
        if not f:
            return "No file"
    
        print ('aqui')
        with open(f, 'rb') as fp:
            reader = FileStorage(fp)
            for linha in reader:
                print (linha)
        return 'Tem file'
    else:
        return 'get'

if __name__ == '__main__':
    app.run(debug=True)