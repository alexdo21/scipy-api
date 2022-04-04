import collections
from abc import abstractmethod
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, convert_xor, implicit_multiplication
from sympy import Symbol


class Base:
    @staticmethod
    @abstractmethod
    def symbolic_derivative(*args, **kwargs):
        pass


MonomialFunction = collections.namedtuple("MonomialFunction", ("expr", "wrt"))


def parse_monomial_function(raw_expr: str, wrt: str) -> MonomialFunction:
    transformations = standard_transformations + (convert_xor, implicit_multiplication)
    expr = parse_expr(raw_expr, transformations=transformations)
    return MonomialFunction(expr, Symbol(wrt))

