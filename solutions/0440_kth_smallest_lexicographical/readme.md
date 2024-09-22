# 440. K-th Smallest in Lexicographical Order

## Problem

Rating: 3/5

You are given two integers `n` and `k`. Return the `k`-th smallest integer in the range `[1, n]` when the integers are sorted in lexicographical order.

The problem you're solving is the "K-th Smallest in Lexicographical Order." A more efficient approach involves using **prefix counting** to navigate the lexicographical tree instead of iterating one by one. Here's an optimized version of the algorithm.

### Example 1

Input: `n = 13, k = 2`  
Output: `10`  
Explanation: The lexicographical order of numbers from 1 to 13 is `[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]`. The 2nd smallest number is `10`.

### Example 2

Input: `n = 1, k = 1`  
Output: `1`

### Constraints

- 1 <= `n` <= 10^9
- 1 <= `k` <= min(`n`, 10^9)

## Solution

### Approach

The problem asks for the k-th smallest number in lexicographical order, which could be computationally expensive if solved by simply sorting all the numbers. Instead, we can take advantage of the structure of the numbers by treating them as prefixes in a lexicographical tree and efficiently navigating through this tree to find the k-th smallest number.

#### Algorithm

1. We use a helper function `count_prefix` that counts how many numbers exist between a given prefix and the next prefix.
2. Start from `current_number = 1`, the smallest possible prefix.
3. If the prefix range contains fewer than `k` numbers, skip the entire range by moving to the next prefix.
4. Otherwise, descend into the tree by multiplying the current prefix by 10 to explore numbers starting with the current prefix.
5. Decrement `k` appropriately based on the numbers skipped.

#### Implementation

```python
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(prefix: int, n: int) -> int:
            """Counts how many numbers exist between prefix and next prefix in lexicographical order."""
            current = prefix
            next_prefix = prefix + 1
            count = 0
            while current <= n:
                count += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return count

        current_number = 1
        # The first number is 1, so we decrement k to find the k-th number.
        k -= 1  

        while k > 0:
            count = count_prefix(current_number, n)
            if count <= k:
                # If the current prefix range doesn't contain the k-th number, move to the next prefix.
                k -= count
                current_number += 1
            else:
                # If the current prefix range contains the k-th number, go deeper into the prefix.
                k -= 1
                current_number *= 10

        return current_number
```

#### Complexity Analysis

##### Time complexity: `O(log n * log n)`

The time complexity is dominated by navigating through the lexicographical tree using prefix counting. Each operation takes `O(log n)`, and there are at most `O(log n)` steps to find the k-th number.

##### Space complexity: `O(1)`

We only use a constant amount of extra space for variables like `current_number` and `k`.

#### Explanation

1. **Prefix Counting**:
   - The function `count_prefix` calculates how many numbers exist in the lexicographical range between `prefix` and `next_prefix`. This helps to quickly determine how many numbers are in a subtree of the lexicographical tree.

2. **Efficient Search**:
   - Instead of moving linearly through all numbers, this approach navigates the lexicographical tree based on prefix counts, either moving to the next prefix (`current_number += 1`) or descending deeper into the current prefix (`current_number *= 10`).
