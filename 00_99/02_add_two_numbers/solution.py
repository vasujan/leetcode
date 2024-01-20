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
    def addTwoNumbers_brute(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_listNode(ln: ListNode):
            rn: ListNode = ListNode(ln.val, None)
            while ln.next:
                rn = ListNode(ln.next.val, rn)
            return rn
        
        # ln_1 = reverse_listNode(l1)
        # ln_2 = reverse_listNode(l2)
        ln_1 = l1
        ln_2 = l2

        s = ln_1.val + ln_2.val
        result: ListNode = ListNode(s % 10, None)
        s //= 10

        while ln_1.next or ln_2.next:
            v_1 = v_2 = 0
            if ln_1.next:
                ln_1 = ln_1.next
                v_1 = ln_1.val
            if ln_2.next:
                ln_2 = ln_2.next
                v_2 = ln_2.val
            s += v_1 + v_2 

            result: ListNode = ListNode(s % 10, result)
            s //= 10

        return reverse_listNode(result)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d_sum = l1.val + l2.val
        r: ListNode = ListNode(d_sum % 10, None)
        r0 = r
        d_sum //= 10

        while l1.next or l2.next:
            if l1.next:
                l1 = l1.next
                d_sum += l1.val
            if l2.next:
                l2 = l2.next
                d_sum += l2.val
            rn = ListNode(d_sum % 10, None)
            r.next, r = rn, rn
            d_sum //= 10
        
        return r0
            

    


