class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #defaultdict will setup a dictionary with default value as empty set
        rows = collections.defaultdict(set) # r 
        cols = collections.defaultdict(set) # c
        box = collections.defaultdict(set) # key = (r // 3, c // 3)

        # hashset = defaultdict(set)
        # print('hashset: ', hashset)

        # for i in range(3):
        #     hashset[i].add(i)
        #     hashset[i].add(i)
        #     hashset[i].add(i + 2)

        print('hashset: ', hashset)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in box[(r // 3 , c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                box[(r // 3 , c // 3)].add(board[r][c])
                print('rows: ', rows)
                print('cols: ', cols)
                print('boxes: ', box)
        return True
