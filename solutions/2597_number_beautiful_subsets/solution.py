from typing import List
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def backtrack(start: int, current: list):
            if current:
                self.count += 1

            for i in range(start, len(nums)):
                can_add = True
                for num in current:
                    if abs(num - nums[i]) == k:
                        can_add = False
                        break
                
                if can_add:
                    current.append(nums[i])
                    backtrack(i + 1, current)
                    current.pop()
                
        self.count = 0
        backtrack(0, [])
        return self.count

def test_beautifulSubsets():
    sol = Solution()
    
    # Test case 1: Small array, k = 1
    assert sol.beautifulSubsets([1, 2, 3], 1) == 4  # [1], [2], [3], [1, 3]

    # Test case 2: Single element
    assert sol.beautifulSubsets([1], 1) == 1  # [1]

    # Test case 3: All elements are the same
    assert sol.beautifulSubsets([1, 1, 1], 1) == 7  # [1], [1], [1], [1, 1], [1, 1], [1, 1], [1, 1, 1]

    # Test case 4: Array with no valid beautiful subsets except single elements
    assert sol.beautifulSubsets([1, 4, 7], 2) == 7  # All subsets are valid

    # Test case 5: Array with exactly k differences
    assert sol.beautifulSubsets([2, 4, 6], 2) == 4  # [2], [4], [6], [2, 6]

    # Test case 6: Large k value
    assert sol.beautifulSubsets([1, 2, 3, 4, 5], 10) == 31  # All subsets are valid

    # Test case 7: Large input array, small k
    assert sol.beautifulSubsets(list(range(1, 21)), 1) == 17710  # Every subset of 20 elements

    # Test case 8: Alternating pattern
    assert sol.beautifulSubsets([1, 3, 1, 3, 1], 2) == 10  # [1], [3], [1, 1], [3, 3], ...

    # Test case 9: Small array, large k
    assert sol.beautifulSubsets([1, 2, 3], 1000) == 7  # All subsets are valid

    # Test case 10: Edge case, empty input
    assert sol.beautifulSubsets([], 1) == 0  # No subsets possible

    print("All test cases passed.")

if __name__ == '__main__':
    test_beautifulSubsets()