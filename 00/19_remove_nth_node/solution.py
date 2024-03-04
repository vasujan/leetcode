from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

    @classmethod
    def fromList(cls, values: list[int]):
        ln = cls(values.pop(), None)
        while values:
            ln = cls(values.pop(), ln)
        return ln
    
    def toList(self):
        result = [self.val]
        while self.next:
            result.append(self.next.val)
            self = self.next
        return result
    
    def __repr__(self):
        next = f"ListNode({self.next.val})" if self.next else "None"
        return f"ListNode(val={self.val}, next={next})"
    
class Solution:
    def reverse_ll(self, head: ListNode) -> ListNode:
        tail = ListNode(head.val, None)
        current_head = head
        while current_head.next:
            current_head = current_head.next
            tail = ListNode(current_head.val, tail)
        return tail
        
    def removeNthFromEnd_r(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = self.reverse_ll(head)
        
        if n == 1:
            tail = tail.next
        else:
            prev_tail = ListNode(None, tail)
            for _ in range(n - 1):
                prev_tail = prev_tail.next

            prev_tail.next = prev_tail.next.next

        return self.reverse_ll(tail) if tail else None
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        iterator = before = pointer = ListNode(None, head)
        
        while iterator.next:
            n -= 1
            iterator = iterator.next
            if n < 0:
                before = before.next

        before.next = before.next.next
        return pointer.next
