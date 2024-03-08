from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out_array = []
        left_i = 0
        right_i = len(nums) - 1

        while left_i <= right_i:
            left_s = nums[left_i] ** 2
            right_s = nums[right_i] ** 2

            if left_s > right_s:
                out_array.append(left_s)
                left_i += 1
            else:
                out_array.append(right_s)
                right_i -= 1
        
        out_array.reverse()
        return out_array
        