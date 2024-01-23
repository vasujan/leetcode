# 1. Two Sum

[Two Sum - LeetCode](https://leetcode.com/problems/two-sum/)

## Problem

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the `target`. 

- You may assume that each input would have *exactly* one solution and you may nnot use the same element twice. 
- You may return answer in any order

## Solution 

Brute force approach $O(n^2)$

Have two pointers on the array `a` and `b` such that `b > a` and check if `num[a] + num[b] == target`. Keep iterating till `nums` is exhausted.
Total of $\frac{n(n-1)}{2}$ lookups

Memoization $O(n)$

Keep a dictionary `find` with key values as `num[i] = i`. 
Iterate over `nums` and find `target - nums[i]` in the dictionary `find`
Using constant lookups, if the difference was found earlier, the index is already available. 
> This is possible because of the constraint of *exactly* one solution and not reusing same index. 