
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        max_score = 0
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0

        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                score += 1       
                left += 1
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

            max_score = max(max_score, score)
        
        return max_score

def test():
    test_cases = [
        [[100], 50],
        [[200, 100], 150],
        [[100, 200, 300, 400], 200],
        [[26,78,43,36,6,87,70,91,45,68], 12],
        [[], 85]
    ]

    s = Solution()
    for test_case in test_cases:
        r = s.bagOfTokensScore(*test_case)
        print(*test_case)
        print(r)
