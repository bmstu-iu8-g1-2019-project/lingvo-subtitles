from flask import Flask
from flask_httpauth import HTTPBasicAuth

from pymongo import MongoClient

app = Flask(__name__)
auth = HTTPBasicAuth()

db = MongoClient().lingvo

from . import views
