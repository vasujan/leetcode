# 3. Longest Substring Without Repeating Characters

[Longest Substring Without Repeating Characters - LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

## Problem

Given the string `s`, find the length of the longest substring without repeating characters.


## Solution

The solution doesn't demand the lonogest substring indices but only the length. So, the solution can be simpler by keeping the track of the maximum substring length. 

The naive solution is to maintain a moving queue of characters and check if next character is in queue. If it is, delete the queue till the character including it. 

Better solution is using a pointer and hashmap, and iteration.
We maintain the hashmap `seen` for the characters and the last known occurence for it. 
The pointer `start` retains the start point for the current substring. If the same character is encountered again `seec.get(c, -1) >= start`, we reset the `start` pointer to `seen[c] + 1` i.e. after the character. 
Regardless, increment the result if `i - start + 1` is more than it. Store the current index `i` for the character `c`