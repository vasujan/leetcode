from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 2

        while fast < len(nums):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow