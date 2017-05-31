from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/')
def logout():
    return "<h1>Hello world</h1>"


app.run(host='0.0.0.0', port=80, debug=False)
