from solution import Solution

solution = Solution().lengthOfLongestSubstring

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def test_ex1():
    input = "abcabcbb"
    output = 3
    assert output == solution(input)

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

def test_ex2():
    input = "bbbbb"
    output = 1
    assert output == solution(input)


# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def test_ex3():
    input = "pwwk"
    output = 2
    assert output == solution(input)


def test_1():
    input = "aabcc"
    output = 3
    assert output == solution(input)

def test_empty():
    input = ""
    output = 0
    assert output == solution(input)

def test_space():
    input = " "
    output = 1
    assert output == solution(input)

def test_single():
    input = "a"
    output = 1
    assert output == solution(input)

def test_long():
    input = "1234567890abcdefghijklmnopqrstuvwxyz"
    assert len(input) == solution(input)

def test_mid():
    input = "drdx"
    output = 3
    assert output == solution(input)