from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask_ngrok import run_with_ngrok

import stripe

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
 
app = Flask(__name__)

run_with_ngrok(app)

#website_url = 'v.gfg:5000'
#app.config['SERVER_NAME'] = website_url 
    
app.config.from_object(Config)
app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51Kn4m1SImNF9Ed8Pe0bAy6FQHxhLfobwOpt8veyyeWUSoWhBlJsnaTmrFAT8sK21gifQXOboAcLSutoYuidq4NSm00Cl5gwKa3'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51Kn4m1SImNF9Ed8Pe8havwEl5hG6oW34o6ZxJvuLUdrqiXuoIpnv1tbJdjIp791lQyWH4xvGKslTnqdmocY5qo5v00ciqQUK3W'

app.config["MONGO_URI"] = "mongodb://localhost:27017/project"
mongo = PyMongo(app)

stripe.api_key = app.config['STRIPE_SECRET_KEY']

db = MongoEngine()
db.init_app(app)

from application import routes

if __name__ == "__main__": 
    website_url = 'www.furergofly:5000'
    app.config['SERVER_NAME'] = website_url 
    app.run() 