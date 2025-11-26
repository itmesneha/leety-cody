class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board) # rows
        n = len(board[0]) # cols
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list) #[[-1 for _ in range(m//3)] for _ in range(n//3)]

        for i in range(m):
            for j in range(n):
                val = board[i][j]
                if val == '.':
                    continue
                if val in rows[i] or val in cols[j] or val in boxes[(i//3,j//3)]:
                    return False
                rows[i].append(val)
                cols[j].append(val)
                boxes[(i//3, j//3)].append(val)
        return True
