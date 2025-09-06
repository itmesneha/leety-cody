class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        if not grid or not grid[0]:
            return []

        m, n = len(grid), len(grid[0])
        pac, atl = set(), set()
        
        def dfs(i, j, visited, prev_height):
            if (i, j) in visited or i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] < prev_height:
                return
            
            visited.add((i, j))
            
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                dfs(i + di, j + dj, visited, grid[i][j])


        for i in range(m):
            dfs(i, 0, pac, grid[i][0])
        for j in range(n):
            dfs(0, j, pac, grid[0][j])

        for i in range(m):
            dfs(i, n-1, atl, grid[i][n-1])
        for j in range(n):
            dfs(m-1, j, atl, grid[m-1][j])

        ans = []
        for val in pac:
            if val in atl:
                ans.append(val)

        return ans
