class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def fn(i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] <= 0:
                return 0
            gold = grid[i][j]
            grid[i][j] = -1
            max_gold = max(fn(i + 1, j, grid), fn(i-1, j, grid), fn(i, j+1, grid), fn(i, j - 1, grid))
            grid[i][j] = gold
            return gold + max_gold

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] >0:
                    res = max(res, fn(i, j, grid))

        return res

        
