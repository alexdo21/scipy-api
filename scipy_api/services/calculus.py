from scipy_api.services.utils import Base
from scipy_api.services.utils import parse_monomial_function


class Monomial(Base):
    @staticmethod
    def symbolic_derivative(expr: str, wrt: str):
        monomial = parse_monomial_function(expr, wrt)
        derivative = str(monomial.expr.diff(monomial.wrt)).replace("**", "^").replace("*", "")
        return derivative
