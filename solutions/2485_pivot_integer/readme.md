# 2485. Find the Pivot Integer

## Problem

Rating: 1/5

## Solution

### Approach

There is no need to compute the sum of numbers from the right.  
We can use the property of consequetive integers:

$$
\sum_{i=1}^{n}{i} = \frac{n(n + 1)}{2}, 
\quad \text{where } i \in \mathbb{Z}
$$

#### Algorithm

1. Calculate $N = \sum_{i=1}^{n}{i} = \frac{n(n+1)}{2}$
2. Keep a running sum of the numbers: $s$
    - Check if: $s + i = N - i$, If true return $i$.
4. If not found, return `-1`

#### Implementation

#### Complexity Analysis

- Time complexity

- Space complexity