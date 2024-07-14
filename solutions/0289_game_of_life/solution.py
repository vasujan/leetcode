class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def sum_neighbors(i, j):
            count = 0
            rows = [i]
            cols = [j]
            if i > 0: rows.append(i-1)
            if j > 0: cols.append(j-1)
            if i < m - 1: rows.append(i+1)
            if j < n - 1: cols.append(j+1)

            for ni in rows:
                for nj in cols:
                    # print(ni, nj, board[ni][nj])
                    count += board[ni][nj] % 2
            count -= board[i][j] % 2
            # print(i, j, rows, cols, count)
            return count
            
        for i in range(m):
            for j in range(n):
                neighbors = sum_neighbors(i, j)
                cell = board[i][j] % 2

                if cell == 1 and (neighbors > 3 or neighbors < 2):
                    board[i][j] = 3
                elif cell == 0 and neighbors == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                cell = board[i][j]
                board[i][j] = 3 - cell if cell > 1 else cell
                
