import graphene, json
import pymysql
import secrets 

from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, request

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app) 

# model of user table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)

    # representation of data for testing
    def __repr__(self):
        return "id: {0} | email : {1}".format(self.id, self.email)
    
