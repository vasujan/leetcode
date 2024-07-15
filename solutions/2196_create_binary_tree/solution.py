# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self._count = None
    
    def count(self):
        if self._count:
            return self._count
        count = 0
        if self.left:
            count += 1 + self.left.count()
        if self.right:
            count += 1 + self.right.count()
        self._count = count
        return count


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        store = {}

        for parent, child, left_node in descriptions:
            if child in store:
                child = store[child]
            else: 
                child = TreeNode(child)

            if parent not in store:
                if left_node:
                    store[parent] = TreeNode(parent, child, None)
                else:
                    store[parent] = TreeNode(parent, None, child)
            else:
                if left_node:
                    store[parent].left = child
                else:
                    store[parent].right = child
                
        root_node = TreeNode()
        for t in store.values():
            if t.count() > root_node.count():
                root_node = t
        
        return root_node
