class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        columns = set()
        diagonals = set()
        antidiagonals = set()

        def feasible(row, col):
            if col in columns:
                return False
            if row + col in diagonals:
                return False
            if row - col in antidiagonals:
                return False

            return True

            # for i in range(row):
            #     # same column
            #     if board[i][col] == 'Q':
            #         return False
                
            # i = row - 1
            # j = col - 1
            # while i >= 0 and j >= 0:
            #     if board[i][j] == 'Q':
            #         return False
            #     i -= 1
            #     j -= 1

            # i = row-1
            # j = col + 1
            # while i >= 0 and j < n:
            #     if board[i][j] == 'Q':
            #         return False
            #     i -= 1
            #     j += 1

            # return True

        def fn(row):
            if row == n:
                res.append([''.join(r) for r in board])
                return
            for col in range(n):
                if feasible(row, col):
                    # place & explore
                    board[row][col] = 'Q'
                    columns.add(col)
                    diagonals.add(row + col)
                    antidiagonals.add(row - col)
                    fn(row + 1)

                    # backtrack
                    board[row][col] = '.'
                    columns.remove(col)
                    diagonals.remove(row + col)
                    antidiagonals.remove(row - col)

        fn(0)
        return res

       