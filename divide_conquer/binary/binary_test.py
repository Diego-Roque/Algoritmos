import pytest
import numpy as np
from binary import binary_multiply

def test_square_matrices():
    A = np.array([[1, 0, 1],
                  [0, 1, 0],
                  [1, 1, 0]])

    B = np.array([[0, 1, 1],
                  [1, 0, 0],
                  [0, 0, 1]])

    expected_result = (np.dot(A, B) > 0).astype(int)

    result = binary_multiply(A, B)
    np.testing.assert_array_equal(result, expected_result)

def test_two():
    A = np.array([[1, 0],
                [0, 1]])

    B = np.array([[1, 0],
                [0, 1]])

    expected_result = (np.dot(A, B) > 0).astype(int)

    result = binary_multiply(A, B)
    np.testing.assert_array_equal(result, expected_result)


def test_larger_square_matrices():
    A = np.array([[1, 0, 1, 0],
                  [0, 1, 0, 1],
                  [1, 1, 0, 0],
                  [0, 0, 1, 1]])

    B = np.array([[0, 1, 1, 0],
                  [1, 0, 0, 1],
                  [0, 1, 1, 1],
                  [1, 0, 0, 1]])


    expected_result = (np.dot(A, B) > 0).astype(int)

    result = binary_multiply(A, B)
    np.testing.assert_array_equal(result, expected_result)

def test_identity_matrix():
    A = np.identity(3, dtype=int)
    B = np.identity(3, dtype=int)


    expected_result = (np.dot(A, B) > 0).astype(int)

    result = binary_multiply(A, B)
    np.testing.assert_array_equal(result, expected_result)

def test_non_square_matrix():
    A = np.array([[1, 0, 1],
                  [0, 1, 0]])

    B = np.array([[0, 1, 1],
                  [1, 0, 0],
                  [0, 0, 1]])

    result = binary_multiply(A, B)
    assert result == False

def test_all_zero_matrix():
    A = np.zeros((3, 3), dtype=int)
    B = np.zeros((3, 3), dtype=int)

    # Usando operaciones de NumPy para obtener el resultado esperado automáticamente
    expected_result = (np.dot(A, B) > 0).astype(int)

    result = binary_multiply(A, B)
    np.testing.assert_array_equal(result, expected_result)

def test_mixed_elements_matrix():
    A = np.array([[1, 0, 1],
                  [1, 1, 0],
                  [0, 1, 1]])

    B = np.array([[1, 1, 0],
                  [0, 1, 1],
                  [1, 0, 1]])

    expected_result = (np.dot(A, B) > 0).astype(int)

    result = binary_multiply(A, B)
    np.testing.assert_array_equal(result, expected_result)

if __name__ == "__main__":
    pytest.main()
