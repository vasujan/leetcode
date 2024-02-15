class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return -1
        nums_s = sorted(nums)
        cumsum_nums = nums_s[:1]
        for n in nums_s[1:]:
            cumsum_nums.append(cumsum_nums[-1] + n)
        
        for i in range(1, len(nums)):
            if nums_s[-i] < cumsum_nums[-i-1]:
                return cumsum_nums[-i]
            else:
                continue
        else:
            return -1
