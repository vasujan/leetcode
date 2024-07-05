class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cursor = head
        
        critical_first = None
        critical_last = None
        nodes_min = None
        nodes_max = None
        index = 0

        while cursor.next.next:
            is_critical = (
                (cursor.next.val > cursor.val and cursor.next.val > cursor.next.next.val) or
                (cursor.next.val < cursor.val and cursor.next.val < cursor.next.next.val)
            )

            if is_critical:
                if critical_last is None:
                    critical_first = index
                elif nodes_min is None:
                    nodes_min = index - critical_last
                else:
                    nodes_min = min(nodes_min, index - critical_last)
                critical_last = index
        
            cursor = cursor.next
            index += 1
        
        if critical_last is None or nodes_min is None:
            return [-1, -1]
        else:
            return [nodes_min, critical_last - critical_first]
