import numpy as np
from typing import Dict, Tuple

# Diccionario global para almacenar submatrices
submatrix: Dict[str, np.ndarray] = {}


def calculate_matrix_size(matrix: np.ndarray) -> Tuple[int, int]:
    """
    Calcula el tamaño de la matriz dada.

    Args:
        matrix (np.ndarray): Matriz de la cual se calculará el tamaño.

    Returns:
        Tuple[int, int]: Número de filas y columnas de la matriz.
    """
    m, n = matrix.shape
    return m, n


def create_submatrix(matrix: np.ndarray, name_prefix: str) -> Dict[str, np.ndarray]:
    """
    Divide una matriz en submatrices de acuerdo con el algoritmo de Strassen.

    Args:
        matrix (np.ndarray): Matriz a dividir.
        name_prefix (str): Prefijo de los nombres de las submatrices.

    Returns:
        Dict[str, np.ndarray]: Diccionario que contiene las submatrices.
    """
    rows, columns = calculate_matrix_size(matrix)
    mid_row = rows // 2
    mid_col = columns // 2

    submatrix[f'{name_prefix}11'] = matrix[:mid_row, :mid_col]
    submatrix[f'{name_prefix}12'] = matrix[:mid_row, mid_col:]
    submatrix[f'{name_prefix}21'] = matrix[mid_row:, :mid_col]
    submatrix[f'{name_prefix}22'] = matrix[mid_row:, mid_col:]

    return submatrix


def strassen(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Implementa el algoritmo de Strassen para la multiplicación de matrices.

    Args:
        A (np.ndarray): Primera matriz a multiplicar.
        B (np.ndarray): Segunda matriz a multiplicar.

    Returns:
        np.ndarray: Resultado de la multiplicación de las matrices A y B.
    """
    submatrix_a = create_submatrix(A, 'A')
    submatrix_b = create_submatrix(B, 'B')

    A11 = submatrix_a['A11']
    A12 = submatrix_a['A12']
    A21 = submatrix_a['A21']
    A22 = submatrix_a['A22']
    B11 = submatrix_b['B11']
    B12 = submatrix_b['B12']
    B21 = submatrix_b['B21']
    B22 = submatrix_b['B22']

    M1 = np.dot(A11 + A22, B11 + B22)
    M2 = np.dot(A21 + A22, B11)
    M3 = np.dot(A11, B12 - B22)
    M4 = np.dot(A22, B21 - B11)
    M5 = np.dot(A11 + A12, B22)
    M6 = np.dot(A21 - A11, B11 + B12)
    M7 = np.dot(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    C = np.vstack((top, bottom))

    return C


# Matrices de ejemplo
A = np.array([[2, 4, 1, 3],
              [0, 1, 2, 5],
              [7, 8, 9, 0],
              [4, 3, 2, 1]])

B = np.array([[1, 0, 0, 2],
              [0, 1, 2, 3],
              [4, 0, 1, 0],
              [0, 5, 6, 1]])

C = strassen(A, B)
print(C)
