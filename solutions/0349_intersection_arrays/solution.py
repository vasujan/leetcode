from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = dict()
        for n1 in nums1:
            seen[n1] = 1
        
        for n2 in nums2:
            if n2 in seen:
                seen[n2] = 2
        

        return [k for k,v in seen.items() if v > 1]
        