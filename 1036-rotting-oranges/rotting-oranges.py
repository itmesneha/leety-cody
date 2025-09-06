from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while q:
            i, j, time = q.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    q.append((ni, nj, time + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return time