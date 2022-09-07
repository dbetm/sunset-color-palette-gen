import pytest

from src.sum import sum


# multiple cases to test the sum(int, int) function
@pytest.mark.parametrize("a,b", [(1, 1), (2, 3), (5, 8)])
def test_sum_a_b(a, b):
    assert (a + b) == sum(a, b)