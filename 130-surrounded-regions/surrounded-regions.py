from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Only the 'O's connected to the border are safe.
        Every other 'O' must be flipped to 'X'.
        Multisource BFS - from 'O's at border - if any 'O' reachable from there
        flip to 'S' for (safe)

        At end any 'O' still left, means not reachable from border - flip to 'X'
        and flip back 'S' to '0'
        """

        m = len(board)
        n = len(board[0])
        
        q = deque()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        # add border cells to deque
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i  == 0 or i == m-1 or j == 0 or j == n-1):
                    q.append((i, j))
                    board[i][j] = 'S' 

        while q:
            x,y = q.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx == m or ny < 0 or ny == n or board[nx][ny] != 'O':
                    continue

                board[nx][ny] = 'S' #safe
                q.append((nx,ny))

        # mark remaining 'O's to 'X's
        # and 'S' to 'O'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == 'S':
                    board[i][j] = 'O'