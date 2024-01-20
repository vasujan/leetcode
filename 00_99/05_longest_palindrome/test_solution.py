from solution import Solution

_test = Solution().longestPalindrome

def test_blank():
    i = ''
    assert _test(i) == ''

def test_single():
    i = 'a'
    assert _test(i) == 'a'

def test_double():
    i = 'aa'
    assert _test(i) == 'aa'

def test_double_different():
    i = 'ab'
    assert _test(i) == 'a'

def test_triple():
    i = 'aaa'
    assert _test(i) == 'aaa'

def test_triple_palindrome():
    i = 'aba'
    assert _test(i) == 'aba'

def test_nested():
    i = 'abcba'
    assert _test(i) == 'abcba'

def test_nested_double():
    i = 'abccba'
    assert _test(i) == 'abccba'

def test_two_palindromes():
    i = 'aba00cbc'
    assert _test(i) == 'aba'

