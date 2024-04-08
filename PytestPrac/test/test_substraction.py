from AutomationProjectClass.PytestPrac.src.calculator import substract
import pytest

def test_sub_positive_number():
    assert substract(2,5) == -3# original result == expected result

@pytest.mark.sanity_sprint_15
def test_sub_negetive_numbers():
    assert substract(-2,-3)==1

@pytest.mark.skipif(reason="i don;t want runing test for now, it's not required")
def test_sub_mixed_numbers():
    assert substract(2,-3) == 5

@pytest.mark.skip
def test_sub_mixed_numbers2():
    assert substract(-2,3) == -5