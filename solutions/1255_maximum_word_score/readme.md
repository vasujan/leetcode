# 1255. Maximum Score Words Formed by Letters

## Problem

Given an array `nums` of positive integers and a positive integer `k`, a subset of `nums` is considered beautiful if it does not contain two integers with an absolute difference equal to `k`. Return the number of non-empty beautiful subsets of the array `nums`. A subset is any array that can be obtained by deleting some (possibly none) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.

### Example 1:

- Input: `nums = [2, 4, 6]`, `k = 2`
- Output: `4`
- Explanation: The beautiful subsets are: `[2]`, `[4]`, `[6]`, `[2, 6]`.

### Example 2:

- Input: `nums = [1]`, `k = 1`
- Output: `1`
- Explanation: The beautiful subset is `[1]`.

### Constraints:

- `1 <= nums.length <= 20`
- `1 <= nums[i], k <= 1000`

Rating: 5/5

## Solution

### Approach

The approach involves generating all possible subsets of `nums` and checking each subset to determine if it is beautiful. A subset is beautiful if no two elements in the subset have an absolute difference of `k`.

#### Algorithm

1. Use a backtracking method to generate all possible subsets of `nums`.
2. For each subset, check if it is beautiful by ensuring no two elements have an absolute difference of `k`.
3. Count the number of beautiful subsets.

#### Complexity Analysis

- **Time complexity**: The time complexity is $O(2^n \cdot n)$, where $n$ is the length of `nums`. This is because there are $2^n$ subsets, and checking each subset for the beautiful condition takes $O(n)$ time in the worst case.
  
- **Space complexity**: The space complexity is $O(n)$ due to the space required for the recursion stack and storing the current subset during the backtracking process.
