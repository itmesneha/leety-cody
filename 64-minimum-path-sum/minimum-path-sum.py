class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        def fn(x, y):
            if x == m or y == n or x < 0 or y < 0:
                return float('inf')
            if x == m-1 and y == n-1:
                return grid[x][y]
            if memo[x][y] != -1:
                return memo[x][y]
            memo[x][y] = grid[x][y] + min(fn(x+1, y), fn(x, y+1))
            return memo[x][y]

        return fn(0, 0)