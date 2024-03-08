from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = None
        major_count = 0

        for num in nums:
            if major_count == 0:
                major = num
                major_count += 1
            elif num == major:
                major_count += 1
            else:
                major_count -= 1
            
        return major