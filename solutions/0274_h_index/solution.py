from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hIndex = 0

        for i in range(len(citations)):
            if i + 1 <= citations[i]:
                hIndex = i + 1
            else:
                return hIndex
        
        return hIndex
        