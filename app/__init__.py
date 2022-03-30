from flask import Flask
from config import Config

myobj = Flask(__name__)
myobj.config.from_mapping(
  SECRET_KEY = 'potatoes'
)

from app import routes
