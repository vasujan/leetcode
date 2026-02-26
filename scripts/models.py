from typing import Self

import attrs


@attrs.define
class ListNode[T]:
    val: T
    next: Self | None = None

    @classmethod
    def from_list(cls, values: list[T]) -> Self | None:
        if not values:
            return None
        ln = cls(values[0], None)
        current = ln
        for value in values[1:]:
            current.next = cls(value, None)
            current = current.next
        return ln

    def to_list(self) -> list[T]:
        result = [self.val]
        current = self
        while current.next:
            current = current.next
            result.append(current.val)
        return result

    def __repr__(self):
        next_repr = f"ListNode({self.next.val})" if self.next else "None"
        return f"ListNode(val={self.val}, next={next_repr})"


@attrs.define
class TreeNode[T]:
    val: T
    left: Self | None = None
    right: Self | None = None

    @classmethod
    def from_list(cls, values: list[T]) -> Self | None:
        if not values:
            return None
        root = cls(values[0], None, None)
        queue = [root]
        index = 1
        while queue and index < len(values):
            current = queue.pop(0)
            if index < len(values) and values[index] is not None:
                current.left = cls(values[index], None, None)
                queue.append(current.left)
            index += 1
            if index < len(values) and values[index] is not None:
                current.right = cls(values[index], None, None)
                queue.append(current.right)
            index += 1
        return root

    def to_list(self) -> list[T | None]:
        result = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.val)
                queue.append(current.left) if current.left else result.append(None)
                queue.append(current.right) if current.right else result.append(None)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    def __repr__(self):
        left_repr = f"TreeNode({self.left.val})" if self.left else "None"
        right_repr = f"TreeNode({self.right.val})" if self.right else "None"
        return f"TreeNode(val={self.val}, left={left_repr}, right={right_repr})"
