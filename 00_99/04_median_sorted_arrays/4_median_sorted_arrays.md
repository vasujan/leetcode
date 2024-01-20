# 4. Median of Two Sorted Arrays

[Median of Two Sorted Arrays - LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Problem

Given two *sorted* arrays, return the median of the two sorted arrays.

## Solution

We have to use a single pointer to iterate over two sorted arrays. Since, we only need to compute the median, we need to fetch the values at indices: 

`(m + n - 1) // 2` and `(m + n) // 2`

The second one only in case where `m + n` is even.

So this translates to :
```python
if (m + n) % 2 == 0:
    median = arr[(m + n - 1) // 2] + arr[(m + n) // 2]
else:
    arr[(m + n) // 2]
```

The main problem is choosing which array to increment. This can be decided based on which incoming character is smaller. In a way we are sorting the leading characters of the two arrays. 