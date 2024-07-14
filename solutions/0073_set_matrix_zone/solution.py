class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row_mask = [1 for x in range(len(matrix))]
        col_mask = [1 for x in range(len(matrix[0]))]

        def row_change(row):
            return [r * c for r, c in zip(row, col_mask)]

        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if item == 0: 
                    col_mask[j] = 0
                    row_mask[i] = 0

        for i in range(len(matrix)):
            matrix[i] = [row_mask[i] * item for item in row_change(matrix[i])]



