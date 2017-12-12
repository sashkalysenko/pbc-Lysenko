import pytest
from pbc.tools.fibonacci import fibonacci

test_data = [
                (-1, "input should be a positive number"),
                (0, [0]),
                (1, [0, 1]),
                (5, [0, 1, 1, 2, 3, 5]),
                (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
            ]


@pytest.mark.parametrize("test_input,expected", test_data)
@pytest.mark.fib
def test_fib(test_input, expected):
    assert fibonacci(test_input) == expected
