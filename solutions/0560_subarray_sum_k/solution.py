from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        res = 0
        cur_sum = 0

        for num in nums:
            cur_sum += nums
            res += sums.get(cur_sum - k, 0)
            sums[cur_sum] = sums[cur_sum, 0] + 1
    
        return res
            