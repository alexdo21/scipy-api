from flask import request, Blueprint
from scipy_api.services import linear_algebra


linear_algebra_blueprint = Blueprint("linear_algebra_blueprint", __name__)


@linear_algebra_blueprint.route("/inverse", methods=["POST"])
def get_inverse():
    data = request.get_json(force=True)
    matrix = data["matrix"]
    return {"inverseMatrix": linear_algebra.inverse(matrix).tolist()}


@linear_algebra_blueprint.route("/determinant", methods=["POST"])
def get_determinant():
    data = request.get_json(force=True)
    matrix = data["matrix"]
    return {"determinant": linear_algebra.determinant(matrix)}
