from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
        next = f"{self.next.val}" if self.next else "None"
        return f"ListNode(val={self.val}, next={next})"

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Variables

        head_0 = ListNode(0, head) # points to actual header. used when returning the results 
        rev = None # reversed k group
        rev_t = rev # tail of reversed
        head_k = head_0 # points to current group
        i = 1 # track for the k groups. Take action on i == 1 and i == k
        while head:
            rev = ListNode(head.val, rev)
            if i == 1: 
                # save the tail for the reversed group
                rev_t = rev
            if i == k:
                # swap the group with reversed group
                head_k.next, rev_t.next = rev, head.next
                # change the headers for next group
                head_k, rev = rev_t, None
                # reset the counter for the group
                i = 0

            i += 1
            head = head.next
        
        return head_0.next

t = ListNode.fromList([1, 2, 4, 6, 8, 10, 12, 15, 16, 19])
s = Solution().reverseKGroup(t, 5)
print(s.toList())