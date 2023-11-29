from lib.time_converter import convert_time, is_valid

def test_period_am():
    assert(convert_time('8:30 am') == '0830')
    assert(convert_time('12:30 am') == '0030')
    
def test_period_pm():
    assert(convert_time('8:30 pm') == '2030')
    assert(convert_time('12:30 pm') == '1230')
    
def test_invalid_time():
    assert(is_valid('8:60 pm') == False)
    assert(is_valid('13:30 pm') == False)
    
