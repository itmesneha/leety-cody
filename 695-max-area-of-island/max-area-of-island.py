class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid)
        n = len(grid[0])
        ans = 0
        def bfs(pos):
            area = 1
            i, j = pos
            q = deque()
            q.append((i, j))
            grid[i][j] = -1
            while q:
                x, y = q.popleft()
                for direction in directions:
                    x_, y_ = x + direction[0], y + direction[1]
                    print(x_, y_)
                    if x_ < 0 or x_ >= m or y_ < 0 or y_ >= n or grid[x_][y_] != 1:
                        continue
                    
                    area += 1
                    grid[x_][y_] = -1
                    q.append((x_, y_))

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, bfs((i, j)))

        return ans

    