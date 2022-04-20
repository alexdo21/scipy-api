import collections
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, convert_xor, implicit_multiplication
from sympy import Symbol


Function = collections.namedtuple("Function", ("expr", "wrt"))


def parse_function(raw_expr: str, wrt: str) -> Function:
    transformations = standard_transformations + (convert_xor, implicit_multiplication)
    raw_expr = raw_expr.replace("{", "").replace("}", "")
    expr = parse_expr(raw_expr, transformations=transformations)
    return Function(expr, Symbol(wrt))

