from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        # Count num of subarrs where current sum <= x
        def subarrs(x):
            if x < 0: return x

            res = 0
            l, cur = 0, 0
            for r in range(len(nums)):
                cur += nums[r]
                while cur > x:
                    cur -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res
        
        return subarrs(goal) - subarrs(goal - 1)