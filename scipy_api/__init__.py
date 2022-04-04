from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Welcome to scipy_api"

from scipy_api.controllers.linear_algebra import linear_algebra_blueprint
app.register_blueprint(linear_algebra_blueprint, url_prefix="/linalg")

from scipy_api.controllers.calculus import calculus_blueprint
app.register_blueprint(calculus_blueprint, url_prefix="/calculus")
