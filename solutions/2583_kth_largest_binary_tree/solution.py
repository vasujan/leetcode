from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def construct_preorder(cls, arr: list):
        # pre-order list to tree
        root = None
        q = []
        root = cls(arr.pop(0))
        q.append(root)
        while q:
            node = q.pop(0)
            if arr:
                node.left = cls(arr.pop(0))
                q.append(node.left)
            if arr:
                node.right = cls(arr.pop(0))
                q.append(node.right)
        return root




class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Compute the level sum for each level using bfs
        if isinstance(root, list):
            root = TreeNode.construct_preorder(root)
        level_sums = []
        q = [(root, 0)]
        while q:
            node, level = q.pop(0)
            # print(
            #     level,
            #     node.val,
            #     node.left.val if node.left else None,
            #     node.right.val if node.right else None
            # )
            if level >= len(level_sums):
                level_sums.append(0)
            level_sums[level] += node.val if node.val else 0
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            # print(level, node.val, level_sums)
            # print(level, node.val, [(x[1], x[0].val) for x in q])
        level_sums.sort(reverse=True)
        if k > len(level_sums):
            return -1
        else:
            return level_sums[k - 1]
