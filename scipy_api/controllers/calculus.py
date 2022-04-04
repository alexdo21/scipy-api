from flask import request, Blueprint
from scipy_api.services import calculus


calculus_blueprint = Blueprint("calculus_blueprint", __name__)


@calculus_blueprint.route("/monomial/symbolic-derivative", methods=["POST"])
def get_monomial_symbolic_derivative():
    data = request.get_json(force=True)
    expr = data["expression"]
    wrt = data["wrt"]
    return {"symbolicDerivative": calculus.Monomial.symbolic_derivative(expr, wrt)}
