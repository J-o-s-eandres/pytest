from src.main import sum, is_greater_than


def test_sum():
    assert sum(2,5) ==7
    

def test_is_greater_than():
    assert is_greater_than(10,2)