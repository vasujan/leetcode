# 20. Valid Parentheses

[Valid Parentheses - LeetCode](https://leetcode.com/problems/valid-parentheses/description/)

## Problem

Given a string with just bracket characters `()`, `{}`, `[]` determine if every bracket is properly closed or not.

Validity:
- Open brackets must be closed by same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a correponding open bracket of the same type.

## Solution

Approaching this using a stack and a lookup for brackets. On encountering the closing brackets, it will check the stack if the correct opening bracket is on top. If it isn't this is a `False`. Go on till stack is exhausted. If the string is exhausted, return `True` or continue iterating in the same manner.

## Edge Cases

- Only the opening bracket was provided in the string, or the closing bracket was missing.
- Closing bracket is the first in the string.