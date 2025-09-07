class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def capture(i, j):
            if i < 0 or i == m or j < 0 or j == n or board[i][j] != 'O':
                return

            board[i][j] = 'T'
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                capture(i + di, j + dj)


        # capture unsurrounded regions convert Os to Ts
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i in [0, m-1] or j in [0, n-1]):
                    capture(i, j)

        # convert remaining Os to Xs & remaining Ts to Os
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'

        

        