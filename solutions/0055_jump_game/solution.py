from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        for i in reversed(range(len(nums))):
            if i + nums[i] >= target:
                target = i
            
        return target == 0