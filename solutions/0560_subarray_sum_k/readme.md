# 560. Subarray Sum Equals K

[Subarray Sum Equals K - LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/description/)

## Problem

Rating: 2/5

## Solution

### Naive Brute-force Approach

#### Algorithm

#### Implementation

```python
def subarraySum(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1

    return count
```

#### Complexity Analysis

- Time complexity O(n2)O(n^2)

- Space complexity O(1)O(1)


### Optimized Hash-lookup Approach

#### Algorithm

#### Implementation

```python
def subarraySum(nums, k):
    sum_counts = {0: 1}  # Initialize with 0 sum having a count of 1
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num
        if curr_sum - k in sum_counts:
            count += sum_counts[curr_sum - k]
        sum_counts[curr_sum] = sum_counts.get(curr_sum, 0) + 1

    return count
```

#### Complexity Analysis

- Time complexity O(n)O(n)

- Space complexity O(n)O(n)  
In the worst case the `prefix_sum` can be of the same length as the input `nums`.
