import pytest
from my_app.fibonacci import fibonacci


@pytest.mark.parametrize("test_input,expected",
                         [
                             (-1, "input should be a positive number"),
                             (0, [0]),
                             (1, [0, 1]),
                             (5, [0, 1, 1, 2, 3, 5]),
                             (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
                         ])
def test_fib(test_input, expected):
    print("\n>>>Test with input <{0}>\n>>>Expected <{1}>".format(test_input, expected))
    assert fibonacci(test_input) == expected
    print("Passed")
