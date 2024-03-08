from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        left = 1
        for i in range(n):
            res.append(left)
            left *= nums[i]

        right = 1
        for i in reversed(range(n)):
            res[i] *= right
            right *= nums[i]

        return res
        