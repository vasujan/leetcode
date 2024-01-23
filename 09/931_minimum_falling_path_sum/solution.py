from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        def add_to_path(i, j):
            nonlocal matrix
            if j == 0:
                m = min(matrix[i-1][0], matrix[i-1][1])
            elif j == n - 1:
                m = min(matrix[i-1][-1], matrix[i-1][-2])
            else:
                m = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])

            matrix[i][j] += m


        for i in range(1, m):
            for j in range(n):
                add_to_path(i, j)
            
        return min(matrix[-1])
    
