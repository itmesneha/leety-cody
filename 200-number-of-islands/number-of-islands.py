class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def explore(i, j):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] != '1':
                return
            grid[i][j] = -1
            for di, dj in directions:
                explore(i + di, j + dj)
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': # != -1
                    explore(i, j)
                    count += 1

        return count

    
