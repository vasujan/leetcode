# 2. Add Two Numbers

[Add Two Numbers - LeetCode](https://leetcode.com/problems/add-two-numbers/)

## Problemm

Given two non-empty linked lists representing two non-negative integers. The digits are stored in the reverse order, and each of their node contains a single digit. 

Add two numbers and return the sum as a linked list.
You may assume that the two numbers do not contain any leading zeros, except the number 0 itself.

123 represented as (3) -> (2) -> (1)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next
```

Constraints:
- The number of nodes in each linked list is in the range `[1, 100]`
- Guaranteed that the list represents the number that does not have a leading zero

## Solution

Iterate over both linked list till both have `.next` or the carry is non-zero.
Add the `node.next.val` to the sum if it exists. 
Add the unit digit from the sum to the result Node.
Divide the sum by 10 or in other terms shift the digits to the right by 1 for base 10.

