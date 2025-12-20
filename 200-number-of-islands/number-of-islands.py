class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def explore(x, y):
            dir = [[0,1], [0,-1], [1,0], [-1,0]]

            if x < 0 or x == m or y < 0 or y == n or grid[x][y] =='0' or grid[x][y] == '-1':
                return

            for dx, dy in dir:
                grid[x][y] = '-1' # mark as visited
                explore(x + dx, y + dy)
                # grid[x][y] = '1' 

        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    explore(i, j)
                    count += 1

        return count
