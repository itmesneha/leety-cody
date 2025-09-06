from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        inf = (2**31) - 1
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [(0,1), (0,-1), (1,0), (-1, 0)]

        while q:
            i, j = q.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n and grid[ni][nj] == inf:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni, nj))
