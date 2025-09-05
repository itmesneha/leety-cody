class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(i, j):
            queue = []
            queue.append([i, j])
            grid[i][j] = '$'
            while queue:
                x, y = queue.pop(0)
                for direction in directions:
                    x_, y_ = x + direction[0], y + direction[1]
                    if x_ < 0 or x_ >= m or y_ < 0 or y_ >= n or grid[x_][y_] != '1':
                        continue
                    else:
                        queue.append([x_, y_])
                        grid[x_][y_] = '$'

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    # dfs(i, j)
                    count += 1

        return count

  # def dfs(i, j):
        #     if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
        #         return # stop

        #     grid[i][j] = '$'

        #     dfs(i+1, j)
        #     dfs(i-1, j)
        #     dfs(i, j+1)
        #     dfs(i, j-1)

        