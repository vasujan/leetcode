# 17. Letter Combinations of a Phone Number

[Letter Combinations of a Phone Number - LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)

## Problem

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the numbers could represent. These combinations can be returned in any order.
Mapping:
- `2`: `abc`
- `3`: `def`
- `4`: `ghi`
- `5`: `jkl`
- `6`: `mno`
- `7`: `pqrs`
- `8`: `tuv`
- `9`: `wxyz`

Contraints:
- `0 <= digits.length <= 4`

## Solution

Since this is limited to just 4 numbers, it is simple to create $8^4 = 4096$ combinations.
The tricky part is to implement the loop to do the same. The best way is the functional `reduce` to systematically reduce the given array of numbers, even if an empty string is received.