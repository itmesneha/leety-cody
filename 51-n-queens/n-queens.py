class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def feasible(row, col):
            for i in range(row):
                for j in range(n):
                    if board[i][j] == 'Q': 
                        if j == col or abs(row-i) == abs(col-j):
                            return False
            return True
            
            # no need to check down as we are coming from up only
            # for i in range(x, n):
            #     for j in range(y, n):
            #         if board[i][j] == 'Q': 
            #             return False
            #         if abs(x-i) == abs(y-j) and board[i][j] == 'Q':
            #             return False


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

        # count = 0
        # res = []
        # board = [['.' for _ in range(n)] for _ in range(n)]
        # def fn(x, y, board, count):
        #     if count == n:
        #         for row in board:
        #             res.append(''.join(row[:]))
        #         return
        #     for i in range(n):
        #         for j in range(n):
        #             if i != x and j != y and abs(i-x) != abs(j-y):
        #                 board[i][j] = 'Q'
        #                 fn(i, j, board, count + 1)
        #                 board[i][j] = '.'

        # fn(0, 0, board, 0)
        # return res
