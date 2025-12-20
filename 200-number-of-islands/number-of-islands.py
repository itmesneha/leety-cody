from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        explore via bfs or dfs
        '''
        def explore(x,y): # bfs
            q = deque()
            grid[x][y] = '-1'
            q.append((x,y))
            while q:
                curx, cury = q.popleft()
                for dx, dy in dir:
                    nx = curx + dx
                    ny = cury + dy
                    if nx < 0 or nx == m or ny < 0 or ny == n or grid[nx][ny] != '1':
                        continue
                    grid[nx][ny] = '-1'
                    q.append((nx, ny))

        # def explore(x, y):

        #     if x < 0 or x == m or y < 0 or y == n or grid[x][y] =='0' or grid[x][y] == '-1':
        #         return

        #     for dx, dy in dir:
        #         grid[x][y] = '-1' # mark as visited
        #         explore(x + dx, y + dy)
        #         # grid[x][y] = '1' # no need for this as we want to classify all reachable positions in 1 island 

        dir = [[0,1], [0,-1], [1,0], [-1,0]]
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    explore(i, j)
                    count += 1

        return count
