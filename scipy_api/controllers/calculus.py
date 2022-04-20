from flask import request, Blueprint
from scipy_api.services import calculus


calculus_blueprint = Blueprint("calculus_blueprint", __name__)


@calculus_blueprint.route("/symbolic-derivative", methods=["POST"])
def get_monomial_symbolic_derivative():
    data = request.get_json(force=True)
    expr, wrt = data["expression"], data["wrt"]
    return {"symbolicDerivative": calculus.symbolic_derivative(expr, wrt)}


@calculus_blueprint.route("/solve-derivative", methods=["POST"])
def get_monomial_solve_derivative():
    data = request.get_json(force=True)
    expr, wrt, at_value = data["expression"], data["wrt"], data["atValue"]
    return {"derivativeResult": calculus.solve_derivative(expr, wrt, at_value)}


@calculus_blueprint.route("/symbolic-integral", methods=["POST"])
def get_monomial_symbolic_integral():
    data = request.get_json(force=True)
    expr, wrt = data["expression"], data["wrt"]
    return {"symbolicIntegral": calculus.symbolic_integral(expr, wrt)}


@calculus_blueprint.route("/solve-integral", methods=["POST"])
def get_monomial_solve_integral():
    data = request.get_json(force=True)
    expr, wrt, fr, to = data["expression"], data["wrt"], data["from"], data["to"]
    return {"integralResult": calculus.solve_integral(expr, wrt, fr, to)}


