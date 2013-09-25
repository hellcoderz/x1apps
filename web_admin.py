from flask import request
from flask import Flask
from flask import render_template
import logging
import json


app = Flask(__name__)
logging.basicConfig(filename='example.log',level=logging.DEBUG)


@app.route("/", methods = ["POST","GET"])
def index():
	return render_template("index.html")

@app.route("/test", methods = ["POST","GET"])
def test():
	return render_template("testing.html")


if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)