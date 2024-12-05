import Addition
import Multiplication
import Subtraction
import Division
import pytest

# Test Addition
@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 6),
        ([10, 20], 30),
        ([0, 0, 0], 0),
        ([-1, -2, -3], -6),
        ([], 0),  # Empty list should return 0
    ],
)
def test_addition(numbers, expected):
    assert Addition.addition(numbers) == expected

# Test Multiplication
@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 6),
        ([10, 2], 20),
        ([0, 10, 20], 0),
        ([-1, -2, -3], -6),
        ([], 1),  # Empty list should return 1
    ],
)
def test_multiplication(numbers, expected):
    assert Multiplication.multiply(numbers) == expected

# Test Subtraction
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 5, 5),
        (0, 5, -5),
        (-10, -5, -5),
        (5, 0, 5),
    ],
)
def test_subtraction(a, b, expected):
    assert Subtraction.subtract(a, b) == expected

# Test Division
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (-10, 2, -5),
        (10, -2, -5),
        (0, 10, 0),
    ],
)
def test_division(a, b, expected):
    assert Division.divide(a, b) == expected

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Division.divide(10, 0)
