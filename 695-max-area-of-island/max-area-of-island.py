from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [[0,1], [1,0],[0,-1], [-1,0]]

        m = len(grid)
        n = len(grid[0])
        count = 0

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            grid[x][y] = -1
            area = 1

            while q:
                curx, cury = q.popleft()
                for dx, dy in dir:
                    nx = curx + dx
                    ny = cury + dy
                    if nx < 0 or nx == m or ny < 0 or ny == n or grid[nx][ny] != 1:
                        continue

                    grid[nx][ny] = -1
                    area += 1
                    q.append((nx, ny))

            return area

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))

        return res