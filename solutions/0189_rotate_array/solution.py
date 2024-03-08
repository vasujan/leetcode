from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        n = len(nums)

        def reverse_inplace(a, b):
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1

        reverse_inplace(0, n-1)
        reverse_inplace(0, k-1)
        reverse_inplace(k, n-1)
