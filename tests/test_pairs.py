import pytest
from my_app.print_pairs import pairs


@pytest.mark.parametrize("test_input,expected",
                         [
                             ((5, -5), []),
                             ((3, 7, 7, 3), [(3, 7)]),
                             ((10, 0), [(0, 10)]),
                             ((-50, 4, 3, -2, 7, 6, 20, 12, 34, 60), [(-50, 60), (4, 6), (-2, 12), (3, 7)])
                         ])
def test_pairs(test_input, expected):
    print("\n>>>Test with input <{0}>\n>>>Expected <{1}>".format(test_input, expected))
    assert pairs(*test_input) == expected
    print("Passed")