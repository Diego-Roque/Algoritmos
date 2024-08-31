import pytest
from memoization_wedding import wedding_memoization



def test_exact_budget():
    assert wedding_memoization(100, 3, [[20, 30], [50, 60], [10, 30]]) == 0

def test_insufficient_budget():
    assert wedding_memoization(50, 3, [[60, 70], [50, 60], [30, 40]]) == -1

def test_large_input():
    prices = [[i for i in range(1, 11)] for _ in range(10)]
    assert wedding_memoization(100, 10, prices) == 0

def test_minimal_budget():
    assert wedding_memoization(1, 1, [[1]]) == 0

def test_edge_case_large_numbers():
    assert wedding_memoization(1000, 5, [[200, 400, 600], [200, 400, 600], [200, 400, 600], [200, 400, 600], [200, 400, 600]]) == 0


def test_non_positive_budget():
    assert wedding_memoization(0, 2, [[20, 30], [50, 60]]) == -1

if __name__ == "__main__":
    pytest.main()
