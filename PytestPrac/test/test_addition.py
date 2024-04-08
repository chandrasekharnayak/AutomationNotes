from AutomationProjectClass.PytestPrac.src.calculator import add
import pytest

#all positive test cases
def test_add_positive_number():
    assert add(2,5) == 7# original result == expected result

@pytest.mark.sanity
def test_add_negetive_numbers():
    assert add(-2,-3)==-5

@pytest.mark.xfail
def test_add_mixed_numbers():
    assert add(2,-3) == 1
