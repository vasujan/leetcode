# 18. 4Sum

[4Sum - LeetCode](https://leetcode.com/problems/4sum/)

## Problem

Given an array nums of `n` integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

`0 <= a, b, c, d < n`
`a`, `b`, `c`, and `d` are distinct.
`nums[a] + nums[b] + nums[c] + nums[d] == target`
You may return the answer in any order.

## Solution

This will be similar to 3Sum but a bit more complicated to allow for the additional integer. The integers can be repeated as required provided they have distinct indices. No need to return indices, so the array can be sorted to make it easier. 

1. Sort the array
2. 