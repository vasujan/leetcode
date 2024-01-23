from solution import Solution

_test = Solution().myAtoi

def test_words():
    assert _test("4193 with words") == 4193

def test_positive():
    assert _test("+123") == 123

def test_negative():
    assert _test("-123") == -123

def test_fail():
    assert _test("asd123") == 0

def test_empty():
    assert _test('    ') == 0

def test_above_max():
    m = 2**31 - 1
    s = str(m + 2)
    assert _test(s) == m 

def test_at_max():
    s = str(2**31 - 1)
    assert _test(s) == 2**31 - 1

def test_below_min():
    m = -2**31 
    s = str(m - 1)
    assert _test(s) == m

def test_at_min():
    m = -2**31
    assert _test(str(m)) == m

def test_multiple_signs():
    assert _test("+-123") == 0

def test_disjointed():
    assert _test("   +0  123") == 0
