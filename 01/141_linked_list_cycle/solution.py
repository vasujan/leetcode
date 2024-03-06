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

    # Slow and fast pointer
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
