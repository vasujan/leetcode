from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cursor = head
        while cursor.next:
            if cursor.next.val != 0:
                cursor.val += cursor.next.val
                cursor.next = cursor.next.next
            elif cursor.next.val == 0 and cursor.next.next:
                cursor = cursor.next
            else:
                cursor.next = None
        
        return head
        

