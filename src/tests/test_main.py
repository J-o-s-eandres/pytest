import pytest
from src.main import sum, is_greater_than, login


def test_sum():
    assert sum(2,5) ==7
    

def test_is_greater_than():
    assert is_greater_than(10,2)
    

def test_login_pass():
    login_passes = login("Pytest","123456")
    assert login_passes
    
    
def test_login_fail():
    login_fails= login("Pytest","123451")
    assert not login_fails
    


@pytest.mark.parametrize(
    "input_x,input_y, expected",
    [
        (1,1,2),
        (1,3,4),
        (6,4,10),
        (11,11,22),
        (11,10,21),
        (20,20,40),
        (1, 1, 2),
        (2, 3, 5),
        (4, 5, 9),
        (3, 7, 10),
        (5, 5, 10),
        (8, 2, 10),
        (6, 4, 10),
        (9, 1, 10),
        (7, 8, 15),
        (10, 10, 20),
        (3, 4, 7),
        (5, 6, 11),
        (7, 8, 15),
        (9, 10, 19),
        (11, 12, 23),
        (13, 14, 27),
        (15, 16, 31),
        (17, 18, 35),
        (19, 20, 39),
        (21, 22, 43),
        (1,1,2),
        (1,3,4),
        (6,4,10),
        (11,11,22),
        (11,10,21),
        (20,20,40),
        (1, 1, 2),
        (2, 3, 5),
        (4, 5, 9),
        (3, 7, 10),
        (5, 5, 10),
        (8, 2, 10),
        (6, 4, 10),
        (9, 1, 10),
        (7, 8, 15),
        (10, 10, 20),
        (3, 4, 7),
        (5, 6, 11),
        (7, 8, 15),
        (9, 10, 19),
        (11, 12, 23),
        (13, 14, 27),
        (15, 16, 31),
        (17, 18, 35),
        (19, 20, 39),
        (21, 22, 43),
    ]
)
def test_sum_params(input_x,input_y, expected):
    assert sum(input_x, input_y) == expected
    