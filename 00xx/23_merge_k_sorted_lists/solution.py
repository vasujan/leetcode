from typing import Optional, List

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
        next = f"ListNode({self.next.val})" if self.next else "None"
        return f"ListNode(val={self.val}, next={next})"


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res: ListNode = ListNode()
        r = res

        cache: dict[int, list[ListNode]] = {}

        for l in lists:
            if not l:
                continue
            if l.val in cache:
                cache[l.val].append(l)
            else:
                cache[l.val] = [l]
        
        i = min(cache)
        
        while cache:
            if i not in cache:
                i += 1
                continue
            
            for li in cache.pop(i):
                r.next, r = li, li
                while li.next and li.next.val == i:
                    li = li.next 
                    r.next, r = li, li
                if not li.next:
                    continue
                ln = li.next
                if ln.val in cache:
                    cache[ln.val].append(ln)
                else:
                    cache[ln.val] = [ln]
            else:
                i += 1

        return res.next

test = [
    list(range(1, 100, 4)),
    list(range(11, 98, 7)),
    list(range(21, 111, 10))
]
# print(test)
test = [ListNode.fromList(l) for l in test]

res = ListNode.toList(Solution().mergeKLists(test))
# print(test)
print(res)

