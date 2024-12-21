#test 
from flask import Flask
from flask import request
import os
import json
from multiprocessing import Process


app = Flask(__name__)

@app.route("/")
def hello():
    return str(request.headers) + "\n" + str(request.data) 

@app.route("/env")
def env():
    return str(json.dumps(dict(os.environ), indent=2))
