import numpy as np
from typing import Union


def matrix_int_type(matrix: np.ndarray) -> np.ndarray:
    """
    Convierte una matriz dada al tipo de datos entero (int).

    Args:
        matrix (np.ndarray): La matriz que se desea convertir.

    Returns:
        np.ndarray: La matriz convertida al tipo entero.
        Si ocurre un error durante la conversión, se devuelve la matriz original.
    """
    try:
        int_matrix = matrix.astype(int)
        return int_matrix
    except Exception as e:
        print(f"Error converting matrix to int: {e}")
        return matrix


def zero_matrix(n: int) -> np.ndarray:
    """
    Crea una matriz cuadrada de ceros de tamaño n x n con tipo de datos entero.

    Args:
        n (int): El tamaño de la matriz (número de filas y columnas).

    Returns:
        np.ndarray: Una matriz de ceros de tamaño n x n con dtype=int.
    """
    zeromatrix = np.zeros((n, n), dtype=int)
    return zeromatrix


def verify_size(matrix: np.ndarray) -> bool:
    """
    Verifica si la matriz es cuadrada (tiene el mismo número de filas y columnas).

    Args:
        matrix (np.ndarray): La matriz que se desea verificar.

    Returns:
        bool: True si la matriz es cuadrada, False en caso contrario.
    """
    num_rows, num_cols = matrix.shape
    same_size = (num_rows == num_cols)
    return same_size


def binary_multiply(A: np.ndarray, B: np.ndarray) -> Union[np.ndarray, bool]:
    """
    Realiza la multiplicación de dos matrices booleanas (con valores 0 y 1).

    Las matrices se convierten a tipo entero si no lo son, y se verifica
    que sean cuadradas y del mismo tamaño antes de realizar la multiplicación.

    Args:
        A (np.ndarray): Primera matriz a multiplicar.
        B (np.ndarray): Segunda matriz a multiplicar.

    Returns:
        Union[np.ndarray, bool]: La matriz resultante de la multiplicación booleana.
        Si las matrices no son cuadradas o no tienen el mismo tamaño, retorna False.
    """
    A = matrix_int_type(A)
    B = matrix_int_type(B)
    size_a = verify_size(A)
    size_b = verify_size(B)

    if size_a and size_b and A.shape == B.shape:
        num_rows = A.shape[0]
        num_cols = A.shape[1]
        zeromatrix = zero_matrix(num_rows)

        for i in range(num_rows):
            for j in range(num_cols):
                for k in range(num_cols):
                    zeromatrix[i, j] |= A[i, k] & B[k, j]
        print(zeromatrix)
        return zeromatrix
    else:
        return False



