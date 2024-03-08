from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = dict()
        for a in arr:
            counts[a] = counts.get(a, 0) + 1
        
        n = len(counts)
        for i in sorted(counts.values()):
            if k <= 0:
                return n
            if k >= i:
                n -= 1
            k -= i
        else:
            return n