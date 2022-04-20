from scipy_api.services.utils import parse_function
from sympy import integrate as integrate_indef, printing, lambdify
from scipy import integrate as integrate_def


def symbolic_derivative(expr: str, wrt: str):
    function = parse_function(expr, wrt)
    derivative = function.expr.diff(function.wrt)
    return printing.latex(derivative)


def solve_derivative(expr: str, wrt: str, at_value: str):
    function = parse_function(expr, wrt)
    derivative = function.expr.diff(function.wrt)
    return printing.latex(derivative.evalf(subs={function.wrt: at_value}))


def symbolic_integral(expr: str, wrt: str):
    function = parse_function(expr, wrt)
    integral = integrate_indef(function.expr, function.wrt)
    return printing.latex(integral)


def solve_integral(expr: str, wrt: str, fr: str, to: str):
    expr, wrt = parse_function(expr, wrt)
    f = lambdify(wrt, expr)
    integral, _ = integrate_def.quad(f, float(fr), float(to))
    return printing.latex(integral)
