from typing import List

class Solution:
    def twoSum_brute(self, nums: List[int], target: int) -> List[int]:
        a, b = 0, 1

        while a < len(nums) - 1:
            if b == len(nums):
                a += 1
                b = a + 1
            
            if nums[a] + nums[b] == target:
                return [a, b]
            b += 1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {nums[0]: 0}
        for i in range(1, len(nums)):
            ni = nums[i]
            if ni in find:
                return [find[ni], i]
            find[target - ni] = i
        

            

class Test:
    def __init__(self, input, expected_output, func):
        self.input = input
        self.expected_output = expected_output
        self.actual_output = None
        self.func = func
        self.error = None
    
    def throw(self):
        print("Input    ", self.input)
        print("Expected ", self.expected_output)
        print("Actual   ", self.actual_output)

    def test(self):
        self.actual_output = self.func(**self.input)
        if self.actual_output == self.expected_output:
            self.error = True
        else:
            self.throw()
            self.error = False

s = Solution().twoSum
Test({'nums': [2, 7, 11, 15], 'target': 9}, [0, 1], s).test()
Test({'nums': [3, 2, 4], 'target': 6}, [1, 2], s).test()
Test({'nums': [3, 3], 'target': 6}, [0, 1], s).test()
Test({'nums': [2,5,5,11], 'target': 10}, [1, 2], s).test()