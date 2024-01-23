# [Maximum Length of a Concatenated String with Unique Characters - LeetCode](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/?envType=daily-question&envId=2024-01-23)
from typing import Union, Iterable

class Solution:
    def maxLength(self, arr: list[str]) -> int:
        max_length = 0
        
        def is_unique(arr: Iterable) -> bool:
            return len(arr) == len(set(arr))

        def backtrack(iterate_index: int, current_string: str) -> int:
            nonlocal max_length
            if is_unique(current_string):
                max_length = max(max_length, len(current_string))
            else:
                return 0

            for i in range(iterate_index, len(arr)):
                backtrack(i + 1, current_string + arr[i])
        
        backtrack(0, "")
        return max_length


t = ["a", "abc", "d", "de", "def"]
s = Solution().maxLength(t)
print(s)