import pytest
from decimal import Decimal
from fractions import Fraction

from safe_division import safe_division

def test_divides_integers():
    assert safe_division(10, 2) == 5.0

def test_divides_floats():
    assert safe_division(3.5, 2) == 1.75

def test_division_by_zero_returns_none():
    assert safe_division(5, 0) is None
    assert safe_division(0, 0) is None
    assert safe_division(0.0, 0.0) is None

def test_non_numeric_raises_type_error():
    with pytest.raises(TypeError):
        safe_division("10", 2)
    with pytest.raises(TypeError):
        safe_division(10, "2")
    with pytest.raises(TypeError):
        safe_division(None, 1)

def test_works_with_decimal_and_fraction():
    assert safe_division(Decimal('1.5'), Decimal('0.5')) == 3.0
    assert safe_division(Fraction(3, 2), Fraction(1, 2)) == 3.0

def test_negative_and_large_numbers():
    assert safe_division(-10, 2) == -5.0
    assert safe_division(10, -2) == -5.0
    assert safe_division(10**18, 2) == float(10**18 / 2)
