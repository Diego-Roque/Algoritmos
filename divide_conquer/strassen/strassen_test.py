import pytest
import numpy as np
from strassen import calculate_matrix_size, create_submatrix, strassen

def test_calculate_matrix_size():
    matrix = np.array([[1, 2], [3, 4]])
    rows, cols = calculate_matrix_size(matrix)
    assert rows == 2
    assert cols == 2

def test_create_submatrix():
    matrix = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16]])
    submatrix = create_submatrix(matrix, 'A')
    np.testing.assert_array_equal(submatrix['A11'], np.array([[1, 2], [5, 6]]))
    np.testing.assert_array_equal(submatrix['A12'], np.array([[3, 4], [7, 8]]))
    np.testing.assert_array_equal(submatrix['A21'], np.array([[9, 10], [13, 14]]))
    np.testing.assert_array_equal(submatrix['A22'], np.array([[11, 12], [15, 16]]))

def test_strassen():
    A = np.array([[2, 4, 1, 3],
                  [0, 1, 2, 5],
                  [7, 8, 9, 0],
                  [4, 3, 2, 1]])

    B = np.array([[1, 0, 0, 2],
                  [0, 1, 2, 3],
                  [4, 0, 1, 0],
                  [0, 5, 6, 1]])

    expected_result = np.dot(A, B)
    result = strassen(A, B)
    np.testing.assert_array_equal(result, expected_result)


def test_strassen_2x2():
    A = np.array([[1, 2],
                  [3, 4]])

    B = np.array([[5, 6],
                  [7, 8]])

    expected_result = np.dot(A, B)
    result = strassen(A, B)
    np.testing.assert_array_equal(result, expected_result)



def test_strassen_4x4():
    A = np.array([[4, 3, 2, 1],
                  [1, 0, 0, 1],
                  [1, 2, 3, 4],
                  [2, 3, 4, 5]])

    B = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

    expected_result = np.dot(A, B)
    result = strassen(A, B)
    np.testing.assert_array_equal(result, expected_result)


def test_strassen_8x8():
    A = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [1, 3, 5, 7, 9, 11, 13, 15],
                  [15, 13, 11, 9, 7, 5, 3, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1],
                  [2, 4, 6, 8, 10, 12, 14, 16]])

    B = np.array([[16, 15, 14, 13, 12, 11, 10, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [1, 3, 5, 7, 9, 11, 13, 15]])

    expected_result = np.dot(A, B)
    result = strassen(A, B)
    np.testing.assert_array_equal(result, expected_result)


def test_strassen_2x2_negative():
    A = np.array([[-1, -2],
                  [-3, -4]])

    B = np.array([[-5, -6],
                  [-7, -8]])

    expected_result = np.dot(A, B)
    result = strassen(A, B)
    np.testing.assert_array_equal(result, expected_result)


def test_strassen_4x4_mixed():
    A = np.array([[1, -2, 3, -4],
                  [-5, 6, -7, 8],
                  [9, -10, 11, -12],
                  [-13, 14, -15, 16]])

    B = np.array([[16, -15, 14, -13],
                  [-12, 11, -10, 9],
                  [8, -7, 6, -5],
                  [-4, 3, -2, 1]])

    expected_result = np.dot(A, B)
    result = strassen(A, B)
    np.testing.assert_array_equal(result, expected_result)


def test_strassen_16x16_random():
    np.random.seed(0)  # Para hacer la prueba reproducible
    A = np.random.randint(-10, 10, size=(16, 16))
    B = np.random.randint(-10, 10, size=(16, 16))

    expected_result = np.dot(A, B)
    result = strassen(A, B)
    np.testing.assert_array_equal(result, expected_result)


if __name__ == "__main__":
    pytest.main()
