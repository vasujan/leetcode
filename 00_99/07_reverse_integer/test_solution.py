from solution import Solution

_test = Solution().reverse

def test_1():
    x = 123
    assert _test(x) == 321

   
def test_2():
    x = -123
    assert _test(x) == -321


def test_above_max():
    x = 8463847412
    assert _test(x) == 0


def test_at_max():
    x = 7463847412
    y = 2 ** 31 - 1
    assert _test(x) == y

def test_at_min():
    x = -8463847412
    y = -(2 ** 31)
    assert _test(x) == y