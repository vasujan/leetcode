# 930. Binary Subarrays With Sum

[Binary Subarrays With Sum - LeetCode](https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=daily-question&envId=2024-03-12)

## Problem

Rating: 4/5

## Solution

### Sliding Window Approach

There are few things to consider here:
- We need to return the counts of the subarrays, so it doesn't need to be greedy.
We can use the goal as constraints to move the left and right pointer.
- Instead of computing directly for `n` which is harder, we can compute for `<=n` minus `<=(n-1)` 
which means the same thing mathematically. This includes the edge case for `goal == 0`

#### Algorithm

#### Implementation

#### Complexity Analysis

- Time complexity $O(n)$

- Space complexity $O(1)$