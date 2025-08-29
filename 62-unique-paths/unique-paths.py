class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n + 1)] for _ in range(m+1)]
        def fn(x,y):
            if x == m-1 and y == n-1:
                return 1
            if x > m-1 or y > n-1 or x < 0 or y < 0:
                return 0
            if memo[x][y] != -1:
                return memo[x][y]
            memo[x][y] = fn(x, y+1) + fn(x+1, y)
            return memo[x][y]

        return fn(0,0)