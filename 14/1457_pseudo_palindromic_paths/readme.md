# 1457. Pseudo-Palindromic Paths in a Binary Tree

[Pseudo-Palindromic Paths in a Binary Tree - LeetCode](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/?envType=daily-question&envId=2024-01-24)

## Problem

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Input: root = `[2,3,1,3,1,null,1]`
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path `[2,3,3]`, the green path `[2,1,1]`, and the path `[2,3,1]`. Among these paths only red path and green path are pseudo-palindromic paths since the red path `[2,3,3]` can be rearranged in `[3,2,3]` (palindrome) and the green path `[2,1,1]` can be rearranged in `[1,2,1]` (palindrome).

## Solution


This uses a simple freq map and conducting a depth first check at every leaf node. When the leaf node is encountered, the check is run for whether the path is pseudo-palindromic or not. Return the count upwards recursively, collect in the caller `dfs` and return at root. 

Using `defaultdict` to make it easier to increment and decrement counts for integers to avoid key checks.