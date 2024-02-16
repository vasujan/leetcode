from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # without modifying the input array and using constant extra space
        count = dict()
        for n in nums:
            if n in count:
                return n
            else:
                count[n] = 1
