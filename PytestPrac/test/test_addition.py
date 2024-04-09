from AutomationProjectClass.PytestPrac.src.calculator import add
import pytest

#all positive test cases
'''def test_add_positive_number():
    assert add(2,5) == 7# original result == expected result

@pytest.mark.sanity
def test_add_negetive_numbers():
    assert add(-2,-3)==-5

@pytest.mark.xfail
def test_add_mixed_numbers():
    assert add(2,-3) == 1'''

test_data = [
    (2,3,5),
    (0,0,0),
    (1,-1,0),
    (-5,10,5),
    (3,4,8),
    (-5,5,-1)
]
@pytest.mark.parametrize("x,y,expected",test_data)
def test_addition(x,y,expected):
    result = add(x,y)
    if result == expected:
        pytest.mark.positive
    else:
        pytest.mark.negative

    assert result == expected










