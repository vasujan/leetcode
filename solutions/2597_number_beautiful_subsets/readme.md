# 2597. The Number of Beautiful Subsets

## Problem

You are given an array `nums` of positive integers and a positive integer `k`.

A subset of `nums` is beautiful if it does not contain two integers with an absolute difference equal to `k`.

Return the number of non-empty beautiful subsets of the array `nums`.

A subset of `nums` is an array that can be obtained by deleting some (possibly none) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.

### Example 1

Input: `nums = [2, 4, 6]`, `k = 2`

Output: `4`

Explanation: The beautiful subsets of the array `nums` are: `[2]`, `[4]`, `[6]`, `[2, 6]`. It can be proved that there are only 4 beautiful subsets in the array `[2, 4, 6]`.

### Example 2

Input: `nums = [1]`, `k = 1`

Output: `1`

Explanation: The beautiful subset of the array `nums` is `[1]`. It can be proved that there is only 1 beautiful subset in the array `[1]`.

### Constraints

- `1 <= nums.length <= 20`
- `1 <= nums[i], k <= 1000`

## Solution

### Approach

We will use a backtracking approach to explore all possible subsets of the given array. For each subset, we will check if it is a beautiful subset (i.e., no two elements in the subset have an absolute difference equal to `k`). We will count all such beautiful subsets.

#### Algorithm

1. Define a backtracking function `backtrack` that:
   - Takes the current starting index and the current subset as arguments.
   - Counts the current subset if it is non-empty.
   - Iterates through the array from the current starting index.
   - Checks if adding the current element forms a valid beautiful subset.
   - Recursively calls `backtrack` to explore further elements.
   - Removes the current element to backtrack and explore other possibilities.

2. Initialize the count of beautiful subsets.
3. Call the backtracking function starting with the first element.

#### Complexity Analysis

- **Time complexity**: O(2^n * n)
  - The backtracking algorithm explores all possible subsets, which are `2^n` in total. For each subset, it may need to check all the elements to validate the beautiful subset condition, making the complexity O(2^n * n).

- **Space complexity**: O(n)
  - The space complexity is primarily due to the recursion stack and the current subset being maintained, which both take O(n) space.