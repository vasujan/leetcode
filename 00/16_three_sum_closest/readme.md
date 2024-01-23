# 16. 3Sum Closest

[3Sum Closest - LeetCode](https://leetcode.com/problems/3sum-closest/description/)

## Problem

Given an array of integers and a target integer, find three integers such that the sum is closest to the target.

*Return the sum of the three integers*

Constraints:
- Every input would have exactly one solution. (No ties)
- `3 <= nums.length <= 500`

## Solution

3Sum was done with sorted array and two pointers, by significantly reducing the number of checks involved. 

Here, the problem is to find the closest possible sum to the target. We have to keep a variable for closest sum based on the minimum absolute difference from the target. But there is no way to know when we have arrived at the closest, except when it reaches exactly 0 difference. That means all the possible combinations need to be tested, until the difference becomes larger. 