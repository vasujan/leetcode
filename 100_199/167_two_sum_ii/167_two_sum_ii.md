# 167. Two Sum II

[Two Sum II - Input Array Is Sorted - LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

## Problem

Given 1D array of integers `numbers` that is already **sorted** in ascending order, find two numbers such that they add up to a specific `target` number. 

`numbers[id_1] + numbers[id_2] == target`

Indices start from 1 and they are unequal
`1 <= id_1 < id_2 <= len(numbers)`

Input: `numbers: list[int]`, `target: int` 
Output: `[id_1, id_2]` which are two indices of the two sum.

Tests:
- There is exactly one solution.
- May not use the same element twice.

Constraints:
- Solution must only use constant space
- Inputs are sorted in non-descending order
- `2 <= numbers.length <= 3 * 104`
- `-1000 <= numbers[i] <= 1000`
- `-1000 <= target <= 1000`

## Solution

Two pointer (0, 1) $O(n^2)$

- Reset at `j == n`. Reset by `i += 1` and `j = i + 1`
- Exit at `sum == target`
- Early exit by checking if 
    - `target - num[i] < num[i]`
    - if not match and `num[i] == num[j]` to avoid repeated checks. Possible because of single solution and `j > i`

Two pointer (0, n-1) $O(n)$

- 


## Thoughts

constraints
numbers are sorted in non-descending order
there is only one solution
id_1 < id_2

have to use ordering to exit early and avoid O(n^2) lookups
can implement two pointers at both ends to check if the numbers add up to target
integers can be negative which creates the issue as distant indices can give 0 

time exceeded at [0, 0, ...., 2, 3, ...., 9, 9] for target = 5
using unique and guaranteed solution, increment the two indices by 1 in case target is not matched and `num[i] == num[j]` 