from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        while current and current.next:
            current.val = None
            current = current.next
            if current.val is None:
                return True
        return False