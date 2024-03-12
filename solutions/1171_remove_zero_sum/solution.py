# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeZeroSumSublists(self, head):
        dummy = ListNode(None, head)
        cur_sum = 0
        prefix_sums = {cur_sum: dummy}
        current = head

        while current:
            cur_sum += current.val

            if cur_sum in prefix_sums:
                prefix_node = prefix_sums[cur_sum]
                to_delete = prefix_node.next
                temp_sum = cur_sum 
                
                # delete till current
                while to_delete != current:
                    temp_sum += to_delete.val
                    del prefix_sums[temp_sum]
                    to_delete = to_delete.next
                
                prefix_node.next = current.next
            
            else:
                prefix_sums[cur_sum] = current

            current = current.next

        return dummy.next