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