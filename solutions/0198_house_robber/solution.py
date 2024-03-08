
class Solution:
    def rob(self, nums: list[int]) -> int:
        m = (len(nums) // 2) + 2
        n = (len(nums) // 3) + 2
        max_r = 0

        dp = [[-1] * n for i in range(m)]
        dp[0][0] = 0
        for i in range(m):
            for j in range(n):
                if -2 + i*2 + j*3 < len(nums):
                    if i > 0 and j > 0:
                        m = max(dp[i-1][j], dp[i][j-1])
                    elif i > 0:
                        m = dp[i-1][0]
                    elif j > 0:
                        m = dp[0][j-1]
                    else:
                        dp[i][j] = 0
                        continue
                    m += nums[-2 + i*2 + j*3]
                    dp[i][j] = m
                    max_r = max(max_r, m)
        # return dp
        return max_r
    

h = [2,7,9,3,1]
d = Solution().rob(h)
import numpy as np
print(h)
print(np.array(d))