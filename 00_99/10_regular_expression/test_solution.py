from solution import Solution

_test = Solution().isMatch

def test_basic_true():
    s = 'apple'
    p = 'le'
    assert _test(s, p) == True

def test_basic_false():
    s = 'banana'
    p = 'bt'
    assert _test(s, p) == False

def test_any():
    s = 'apples'
    p = 'pl.'
    assert _test(s, p) == True

def test_any_multiple():
    s = 'mango'
    p = '.an.'
    assert _test(s, p) == True

def test_only_multiple():
    s = 'asdf'
    p = '..'
    assert _test(s, p) == True

def test_pattern_overflow():
    s = 'asdf'
    p = 'asdflkjas'
    assert _test(s, p) == False

def test_any_overflow():
    s = 'asd'
    p = '....'
    assert _test(s, p) == False

def test_simple_repeat():
    s = 'aaa'
    p = 'a*'
    assert _test(s, p) == True

def test_all_match():
    s = 'asdfkj'
    p = '.*'
    assert _test(s, p) == True

def test_mid_repeat():
    s = 'asbbbbsa'
    p = 'asb*sa'
    assert _test(s, p) == True

def test_repeat_zero():
    s = 'assa'
    p = 'asb*sa'
    assert _test(s, p) == True

def test_surrounded_all_match():
    s = 'abc234def'
    p = 'abc.*def'
    assert _test(s, p) == True