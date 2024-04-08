from AutomationProjectClass.PytestPrac.src.calculator import multiply
import  pytest

def test_mul_positive_number():
    assert multiply(2,5) == 10# original result == expected result

@pytest.mark.sanity
def test_mul_negetive_numbers():
    assert multiply(-2,-3)==6

@pytest.mark.sanity_sprint_15
def test_mul_mixed_numbers():
    assert multiply(2,-3) == -6
