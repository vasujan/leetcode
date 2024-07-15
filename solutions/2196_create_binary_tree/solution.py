# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        store = {}

        for parent, child, left_node in descriptions:
            if parent not in store:
                store[parent] = TreeNode(parent)
            if child not in store:
                store[child] = TreeNode(child)

            if left_node:
                store[parent].left = store[child]
            else:
                store[parent].right = store[child]


        root = None
        children = [item[1] for item in descriptions]
        for key in store:
            if key not in children:
                root = store[key]
                break

        return roo
