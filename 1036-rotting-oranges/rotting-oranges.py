from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        multi source BFS
        at end run through whole matrix to check if any fresh oranges left

        how to deal with time - add it as part of deque
        '''

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        q = deque()

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,0))

        time = 0
        
        while q:
            x,y, time = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx == m or ny < 0 or ny == n or grid[nx][ny] != 1:
                    continue

                grid[nx][ny] = 2
                q.append((nx,ny, time + 1))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return time
