# 214. Shortest Palindrome

## Problem

Rating: 4/5

You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.

## Solution

### Approach

The approach is to find the longest palindromic substring in the given string `s`. This substring can be used to create a palindrome.


#### Algorithm

To solve this problem, we can use the following approach:

1. Reverse the input string s to get rev_s.
2. Check if s is already a palindrome by comparing it with rev_s. If it is, return s.
3. Otherwise, find the longest prefix of rev_s that is also a suffix of s.
4. Append the remaining characters of rev_s to the beginning of s to form the shortest palindrome.

#### Implementation

```python
def shortest_palindrome(s: str) -> str:
    """
    Returns the shortest palindrome possible by adding characters in front of the input string.
    
    :param s: The input string.
    :return: The shortest palindrome.
    """
    rev_s = s[::-1]  # Reverse the input string
    for i in range(len(s) + 1):
        if s.startswith(rev_s[i:]):  # Check if s starts with the remaining characters of rev_s
            return rev_s[:i] + s  # Append the remaining characters of rev_s to the beginning of s
```

#### Complexity Analysis

##### Time complexity

The time complexity of this solution is O(n), where n is the length of the input string s.

Here's why:

Reversing the string s using slicing (s[::-1]) takes O(n) time.
The for loop iterates over the range of len(s) + 1, which is also O(n).
Inside the loop, the startswith method is called, which takes O(n) time in the worst case (when the string matches).
The string concatenation (rev_s[:i] + s) takes O(n) time.
Since these operations are performed sequentially, the overall time complexity is O(n) + O(n) + O(n) = O(3n), which simplifies to O(n).

##### Space complexity

The space complexity of this solution is O(n), where n is the length of the input string s.

The space complexity is dominated by the creation of the reversed string rev_s, which takes O(n) space. The space used by the loop variables and the temporary strings created during the string concatenation is O(1), so it does not affect the overall space complexity.