from solution import Solution

_test = Solution().convert

def test_3():
    """    Input:
    P   A   H   N
    A P L S I I G
    Y   I   R
    """

    s = "PAYPALISHIRING"
    numRows = 3
    o = "PAHNAPLSIIGYIR"
    assert _test(s, numRows) == o

def test_4():

    s = "PAYPALISHIRING"
    numRows = 4
    o = "PINALSIGYAHRPI"
    assert _test(s, numRows) == o

def test_5():

    s = "PAYPALISHIRINGTODAY"
    numRows = 5
    o = "PHDASIOAYIRTYPLIGAN"
    assert _test(s, numRows) == o

def test_1():
    s = "A"
    numRows = 1
    o = "A"
    assert _test(s, numRows) == o

def test_2():
    s = "AB"
    numRows = 1
    o = "AB"
    assert _test(s, numRows) == o