class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        diagonals = set()
        antidiagonals = set()

        def fn(row):
            if row == n:
                res.append([''.join(r) for r in board])
                return 

            for col in range(n):
                if col in cols or row + col in diagonals or row - col in antidiagonals:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                diagonals.add(row + col)
                antidiagonals.add(row - col)

                fn(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                diagonals.remove(row + col)
                antidiagonals.remove(row - col)

        fn(0)
        return res

