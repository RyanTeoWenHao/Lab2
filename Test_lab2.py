import lab2

def test_find_min_max():
    numbers=[10,23,34,22,43]
    test_arr = 10, 43
    result=lab2.find_min_max(numbers)
    assert (result == test_arr)

