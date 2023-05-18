from flask import Flask
from flask_cors import CORS
from application import routes

app = Flask(__name__)
CORS(app)