import pytest
from hypothesis import given
from hypothesis.strategies import integers


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def test_add():
    assert add(10, 20) == 30


def test_multiply():
    assert multiply(10, 20) == 200


@given(integers(), integers())
def test_add_property(a, b):
    assert add(a, b) == a + b


@given(integers(), integers())
def test_multiply_property(a, b):
    assert multiply(a, b) == a * b


if __name__ == "__main__":
    pytest.main([__file__, "-v"])