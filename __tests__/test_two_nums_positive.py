from ..two_nums_positive import check_positives

def test_positives():
    assert(check_positives(2, 4, -3) == True)
    assert(check_positives(-4, 6, 8) == True)
    assert(check_positives(-4, 6, 0) == False)
    assert(check_positives(4, 6, 10) == False)