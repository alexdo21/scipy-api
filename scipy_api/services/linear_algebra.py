import numpy as np
from scipy import linalg


def inverse(A: np.ndarray) -> np.ndarray:
    return linalg.inv(A)


def determinant(A: np.ndarray) -> float:
    return linalg.det(A)
