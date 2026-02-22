from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

    @classmethod
    def construct_preorder(cls, _arr: list):
        # pre-order list to tree
        arr = deque(_arr)
        root = None
        queue = deque()
        root = cls(arr.popleft())
        queue.append(root)
        while queue:
            node: TreeNode = queue.popleft()
            if arr:
                node.left = cls(arr.popleft())
                queue.append(node.left)
            if arr:
                node.right = cls(arr.popleft())
                queue.append(node.right)
        return root


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # pre-order list to tree
        # if isinstance(root, list):
        #     root = TreeNode.construct_preorder(root)

        layer = deque()
        layer.append(root)
        while layer:
            if len(layer) == 1:
                node: TreeNode = layer.popleft()
                node.val = 0
                if node.left:
                    node.left.val = 0
                    layer.append(node.left)
                if node.right:
                    node.right.val = 0
                    layer.append(node.right)
            else:
                layer_sum = 0
                for node in layer:
                    layer_sum += node.left.val if node.left else 0
                    layer_sum += node.right.val if node.right else 0
                for _ in range(len(layer)):
                    node: TreeNode = layer.popleft()
                    new_val = layer_sum
                    new_val -= node.left.val if node.left else 0
                    new_val -= node.right.val if node.right else 0
                    if node.left:
                        node.left.val = new_val
                        layer.append(node.left)
                    if node.right:
                        node.right.val = new_val
                        layer.append(node.right)
        
        return root
                

                



       
