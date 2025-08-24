class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def feasible(row, col):
            for i in range(row):
                # same column
                if board[i][col] == 'Q':
                    return False
                # diagonal
                if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                    return False
                if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                    return False
            return True

        def fn(row):
            if row == n:
                res.append([''.join(r) for r in board])
                return
            for col in range(n):
                if feasible(row, col):
                    board[row][col] = 'Q'
                    fn(row + 1)
                    board[row][col] = '.'

        fn(0)
        return res

       