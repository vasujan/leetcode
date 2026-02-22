from typing import Deque, LiteralString, TypeVar, Callable, List, Any, Tuple, Optional
from collections import deque
import math

T = TypeVar("T")
R = TypeVar("R")


class TreeNode:
    def __init__(self, val: T = None, left=None, right=None):
        self.val: T = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    def __repr__(self) -> str:
        return f"TreeNode(val={self.val})"

    @staticmethod
    def verify_correct_length(n) -> bool:
        """
        Verify if the length corresponds to a complete binary tree.
        A complete binary tree has 2^h - 1 nodes for some height h.
        """
        if n <= 0:
            return False
        # Check if n is 2^h - 1 for some integer h
        h = math.log2(n + 1)
        return h.is_integer()

    @classmethod
    def create_layerorder(cls, values: List[T]) -> Optional["TreeNode"]:
        if not values:
            return None
        values: Deque = deque(values)
        root = cls(values.popleft())
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if values:
                node.left = cls(values.popleft())
                queue.append(node.left)
            if values:
                node.right = cls(values.popleft())
                queue.append(node.right)
        return root

    @classmethod
    def create_preorder(cls, values: List[T]) -> "TreeNode":
        """
        Create a balanced binary tree from a pre-order traversal.
        Root is always at the start of the subarray.

        Args:
            values: List of values in pre-order traversal

        Returns:
            Root node of the constructed tree
        """
        if not values:
            return None
        n = len(values)
        if not cls.verify_correct_length(n):
            print(
                f"Warning: Input length {n} does not correspond to a complete binary tree."
            )
            raise ValueError("Input length must correspond to a complete binary tree")

        def dfs(left: int, right: int) -> Optional["TreeNode"]:
            if left > right:
                return None
            root = cls(values[left])
            if left == right:
                return root

            # Calculate the split point for left and right subtrees
            # For a range of size k, left subtree gets (k-1)/2 nodes
            mid = left + 1 + (right - left) // 2
            root.left = dfs(left + 1, mid - 1)
            root.right = dfs(mid, right)
            return root

        return dfs(0, n - 1)

    @classmethod
    def create_postorder(cls, values: List[T]) -> "TreeNode":
        """
        Create a balanced binary tree from a post-order traversal.
        Root is always at the end of the subarray.

        Args:
            values: List of values in post-order traversal

        Returns:
            Root node of the constructed tree
        """
        if not values:
            return None
        n = len(values)
        if not cls.verify_correct_length(n):
            print(
                f"Warning: Input length {n} does not correspond to a complete binary tree."
            )
            raise ValueError("Input length must correspond to a complete binary tree")

        def dfs(left: int, right: int) -> Optional["TreeNode"]:
            if left > right:
                return None
            root = cls(values[right])
            if left == right:
                return root

            # Calculate the split point for left and right subtrees
            # For a range of size k, left subtree gets (k-1)/2 nodes
            mid = left + (right - left - 1) // 2
            root.left = dfs(left, mid)
            root.right = dfs(mid + 1, right - 1)
            return root

        return dfs(0, n - 1)

    @classmethod
    def create_inorder(cls, values: List[T]) -> Optional["TreeNode"]:
        """
        Create a balanced binary tree from an in-order traversal.
        Assumes the input list represents a sorted in-order traversal.

        Args:
            values: List of values in in-order traversal

        Returns:
            Root node of the constructed tree or None if invalid input
        """
        if not values:
            return None
        n = len(values)
        if not cls.verify_correct_length(n):
            print(
                f"Warning: Input length {n} does not correspond to a complete binary tree."
            )
            # Continue anyway, as we can still create a valid binary tree

        def dfs(left: int, right: int) -> Optional["TreeNode"]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = cls(values[mid])
            # Recursively construct left and right subtrees
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, n - 1)

    def dump_preorder(self) -> List[T]:
        return list(self.traverse_preorder(lambda n: n.val))

    def dump_inorder(self) -> List[T]:
        return list(self.traverse_inorder(lambda n: n.val))

    def dump_postorder(self) -> List[T]:
        return list(self.traverse_postorder(lambda n: n.val))

    def draw_tree(self) -> str: ...

    def traverse_preorder(self, func: Callable[..., R]) -> R:
        stack: List[TreeNode] = [self]
        # result: List[Any] = []
        while stack:
            node: TreeNode = stack.pop()
            # result.append(func(node))
            yield func(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        # return result

    def traverse_inorder(self, func: Callable[..., R]) -> R:
        stack: List[TreeNode] = []
        # result: List[Any] = []
        node: TreeNode = self
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            # result.append(func(node))
            yield func(node)
            node = node.right
        # return result

    def traverse_postorder(self, func: Callable[..., R]) -> R:
        stack: List[Tuple[TreeNode, bool]] = [(self, False)]
        # result: List[Any] = []
        while stack:
            node, visited = stack[-1]
            if visited:
                # result.append(func(node))
                yield func(node)
                stack.pop()
            else:
                stack[-1] = (node, True)
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        # return result

    @staticmethod
    def dfs_preorder(node: "TreeNode", func: Callable) -> List[Any]:
        result: List[Any] = []

        def preorder(node: TreeNode):
            if not node:
                return
            result.append(func(node))
            preorder(node.left)
            preorder(node.right)

        return result

    @staticmethod
    def dfs_inorder(node: "TreeNode", func: Callable) -> List[Any]:
        result: List[Any] = []

        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            result.append(func(node))
            inorder(node.right)

        return result

    @staticmethod
    def dfs_postorder(node: "TreeNode", func: Callable) -> List[Any]:
        result: List[Any] = []

        def postorder(node: TreeNode):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(func(node))

        return result


def print_tree(node: TreeNode, last=True, header=""):
    if not node:
        return

    blank = "   "
    pipe = "│  "
    tee = "├──"
    elbow = "└──"

    # Print the current node with appropriate prefix
    print(header + (elbow if last else tee) + str(node.val))

    if node.left:
        is_last = node.right is None
        print_tree(node.left, last=is_last, header=header + (blank if last else pipe))
    if node.right:
        print_tree(node.right, last=True, header=header + (blank if last else pipe))


def _draw_tree(root: TreeNode) -> LiteralString:
    """
    Draw a binary tree in ASCII.

    Args:
        root: TreeNode, the root of the binary tree

    Returns:
        str: ASCII representation of the tree
    """
    if not root:
        return "Empty tree"

    def get_height(node):
        if not node:
            return 0
        return max(get_height(node.left), get_height(node.right)) + 1

    def get_width(node):
        if not node:
            return 0
        return max(get_width(node.left), len(str(node.val)), get_width(node.right))

    height = get_height(root)
    width = get_width(root)

    # Initialize the matrix
    matrix = [
        [" " for _ in range((2**height - 1) * (width + 1))]
        for _ in range(height * 2 - 1)
    ]

    def print_node(node: TreeNode, row, left, right):
        if not node:
            return

        middle = (left + right) // 2
        val_str = str(node.val)
        start_pos = middle - len(val_str) // 2

        # Print the value
        for i, char in enumerate(val_str):
            matrix[row][start_pos + i] = char

        # Print left branch
        if node.left:
            for i in range(1, row + 2):
                matrix[row + i][(left + middle) // 2] = "/"
            print_node(node.left, row + 2, left, middle - 1)

        # Print right branch
        if node.right:
            for i in range(1, row + 2):
                matrix[row + i][(middle + right + 2) // 2] = "\\"
            print_node(node.right, row + 2, middle + 1, right)

    print_node(root, 0, 0, len(matrix[0]))

    # Convert matrix to string
    result = []
    for row in matrix:
        # Remove trailing spaces
        while row and row[-1] == " ":
            row.pop()
        if row:
            result.append("".join(row))

    return "\n".join(result)


if __name__ == "__main__":
    # sample_tree = list(range(15))
    # root = TreeNode.create_preorder(sample_tree)
    # is_correct = TreeNode.verify_correct_length(sample_tree)
    # print(is_correct)

    # queue = deque([(root)])
    # while queue:
    #     for _ in range(len(queue)):
    #         node = queue.popleft()
    #         print(node.val, end=" ")
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    #     print()

    # def print_val(node: TreeNode):
    #     return node.val

    # def assign_parents(node: TreeNode):
    #     if node.left:
    #         node.left.parent = node
    #     if node.right:
    #         node.right.parent = node

    # for _ in root.traverse_preorder(assign_parents):
    #     pass

    # for val in root.traverse_inorder(print_val):
    #     print(val, )

    sample_tree = list(range(15))

    # def print_tree(root):
    #     queue = deque([(root)])
    #     while queue:
    #         for _ in range(len(queue)):
    #             node = queue.popleft()
    #             print(node.val, end=" ")
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         print()

    print(sample_tree)
    print("Inorder")
    print_tree(TreeNode.create_inorder(sample_tree))
    print(sample_tree)
    print("Preorder")
    print_tree(TreeNode.create_preorder(sample_tree))
    print(sample_tree)
    print("Postorder")
    print_tree(TreeNode.create_postorder(sample_tree))
    print(sample_tree)
    print("Layerorder")
    print_tree(TreeNode.create_layerorder(sample_tree))
