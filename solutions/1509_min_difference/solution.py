from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
       
        def differences(arr, index, n):
            sign = 1 if n >= 0 else -1
            for i in range(0, n + sign, sign):
                yield sign * (arr[index + i] - arr[index])
        
        sorted_nums = sorted(nums)
        left, right = 0, len(sorted_nums) - 1
        left_diffs = list(differences(sorted_nums, left, 3))
        right_diffs = list(differences(sorted_nums, right, -3))
        print(sorted_nums, left_diffs, right_diffs)

        diffs = []
        changes = 3
        for i in range(changes + 1):
            ld = left_diffs[i]
            rd = right_diffs[changes - i]
            print(ld, rd)
            diffs.append(ld + rd)

        return sorted_nums[-1] - sorted_nums[0] - max(diffs)
        
test = [1,5,0,10,14]
print(Solution().minDifference(test))

# import random
# r = []
# for i in range(1000):
#     r.append(random.randint(1, 10**9))
# print(r)