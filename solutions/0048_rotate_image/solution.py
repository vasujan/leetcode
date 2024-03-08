from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        def rotate(matrix, i, j):
            temp = matrix[i][j]
            for _ in range(4):
                ni, nj = j, n - i - 1
                matrix[ni][nj], temp = temp, matrix[ni][nj]
                i, j = ni, nj
        
        i = j = 0
        while i < n // 2:
            rotate(matrix, i, j)
            j += 1
            if j == (n - i - 1):
                i += 1
                j = i

m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
r = Solution().rotate(m)
print(m)