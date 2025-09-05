from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
        peri = 0
        def bfs(i, j):
            nonlocal peri
            queue = deque()
            queue.append((i, j))
            grid[i][j] = -1
            while queue:
                x, y = queue.popleft()
                for direction in directions:
                    x_, y_ = x + direction[0], y + direction[1]
                    if x_ < 0 or x_ >= rows or y_ < 0 or y_ >= cols or grid[x_][y_] == 0:
                        peri += 1
                        continue
                    if grid[x_][y_] == 1:
                        queue.append((x_, y_))
                        grid[x_][y_] = -1
            


        # def dfs(i, j):
        #     if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
        #         return 1
        #     if grid[i][j] == -1:
        #         return 0
        #     grid[i][j] = -1

        #     return (dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # return dfs(i, j)
                    bfs(i, j)
                    return peri