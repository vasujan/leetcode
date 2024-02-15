from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isPseudoPalindromic(freq: dict) -> bool:
            n_odds = sum(v % 2 for k, v in freq.items())
            return n_odds <= 1
        
        def dfs(node: TreeNode, freq: dict) -> int:
            if not node:
                return 0
            
            freq[node.val] += 1

            if not node.left and not node.right:
                count = 1 if isPseudoPalindromic(freq) else 0
            else:
                count = dfs(node.left, freq) + dfs(node.right, freq)
            
            freq[node.val] -= 1 # backtracking
            return count
        
        return dfs(root, defaultdict(int))