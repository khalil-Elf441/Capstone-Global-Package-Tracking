from flask import Flask, request, jsonify, redirect, render_template
from flask.logging import create_logger
import logging

app = Flask(__name__, template_folder='template', static_folder='static')
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/single")
def single():
    return render_template('single.html')


if __name__ == "__main__":
    # load pretrained model as clf
    app.run(host='0.0.0.0', port=5000, debug=True)  # specify port=80