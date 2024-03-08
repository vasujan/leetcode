from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: [] for i in range(9)}
        column = {i: [] for i in range(9)}
        boxes = {i: [] for i in range(9)}
        for i in range(9):
            for j in range(9):
                c = (i - i % 3) + (j // 3)
                b = board[i][j]
                if b == ".": continue

                if b in boxes[c] or b in rows[i] or b in column[j]:
                    return False
                boxes[c].append(b)
                rows[i].append(b)
                column[j].append(b)
        return True
                   