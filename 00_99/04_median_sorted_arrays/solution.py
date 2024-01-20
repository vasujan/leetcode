from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        mid = (n1 + n2 + 1) // 2
        two = (n1 + n2 + 1) %  2

        cursor = 0
        median = 0.0

        while n1 + n2 >= mid:
            
            if (n1 and n2 and nums1[-n1] < nums2[-n2]) or n2 == 0:
                cursor = 1
                n1 -= 1
            else:
                cursor = 2
                n2 -= 1

            if n1 + n2 < mid + two:
                if cursor == 1:
                    median += nums1[-n1-1]
                elif cursor == 2:
                    median += nums2[-n2-1]

        return median / (1 + two)
                
        
Solution().findMedianSortedArrays([1, 2], [3, 5])

        
