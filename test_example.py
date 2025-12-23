import pytest

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

def test_fail_example():
    # Этот тест всегда проходит
    assert True

class TestMath:
    def test_multiplication(self):
        assert 2 * 3 == 6

    def test_division(self):
        assert 10 / 2 == 5
