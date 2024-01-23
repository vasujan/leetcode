from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = []

        row_min = 0
        row_max = rows - 1
        col_min = -1
        col_max = cols - 1

        # initial conditions
        i, j = 0, -1
        di, dj = 0, 1

        for _ in range(rows * cols):
            i += di
            j += dj
            result.append(matrix[i][j])

            if row_min == row_max:
                # j += dj
                continue
            if col_min == col_max:
                # i += di
                continue
            
            if i == row_min and j == col_max:
                di, dj = 1, 0
                col_min += 1
            elif j == col_max and i == row_max:
                di, dj = 0, -1
                row_min += 1
            elif i == row_max and j == col_min:
                di, dj = -1, 0
                col_max -= 1
            elif j == col_min and i == row_min:
                di, dj = 0, 1
                row_max -= 1
            

        return result
    
class Test:
    def __init__(self, input, expected_output, func):
        self.input = input
        self.expected_output = expected_output
        self.actual_output = None
        self.func = func
        self.error = None
    
    def throw(self):
        print("Expected ", self.expected_output)
        print("Actual   ", self.actual_output)

    def test(self):
        self.actual_output = self.func(self.input)
        if self.actual_output == self.expected_output:
            self.error = True
        else:
            self.throw()
            self.error = False


s = Solution().spiralOrder
t0 = Test([[1]], [1], s)
t0.test()
t1 = Test([[1, 2, 3]], [1, 2, 3], s)
t1.test()
t2 = Test([[1], [2], [3]], [1, 2, 3], s)
t1.test()
t3 = Test([[1, 2, 3], [6, 5, 4]], [1, 2, 3, 4, 5, 6], s)
t3.test()
t4 = Test([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5], s)
t4.test()
t5 = Test([
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
], [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10], s)
t5.test()
t6 = Test([
    [1, 2, 3, 4, 0, 0], 
    [5, 6, 7, 8, 0, 0], 
    [9, 10, 11, 12, 0, 0], 
    [13, 14, 15, 16, 0, 0]
], [1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 16, 15, 14, 13, 9, 5, 6, 7, 8, 0, 0, 12, 11, 10], s)
t6.test()


print("all good")