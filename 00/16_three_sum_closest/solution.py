from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(target - s) < abs(target - closest_sum):
                    closest_sum = s
                
                if s == target:
                    return s
                elif s < target:
                    l += 1
                elif s > target: 
                    r -= 1    

        return closest_sum

import random 
print([random.randint(-1000, 1000) for _ in range(250)])