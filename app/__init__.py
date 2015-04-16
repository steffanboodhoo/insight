from flask import Flask

myapp = Flask(__name__)
from myapp import routes
