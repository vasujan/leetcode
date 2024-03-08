class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_count = [0] * 101
        max_freq = 1
        result = 0

        for num in nums:
            nums_count[num] += 1
            if nums_count[num] == max_freq:
                result += max_freq
            elif nums_count[num] > max_freq:
                max_freq = nums_count[num]
                result = max_freq

        return result