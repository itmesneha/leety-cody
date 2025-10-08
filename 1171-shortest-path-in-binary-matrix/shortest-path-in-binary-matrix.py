from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid) # rows
        n = len(grid[0]) # cols
        i, j = 0, 0
        q = deque()
        if grid[i][j] == 1:
            return -1
        grid[i][j] = 1
        q.append((i, j, 1)) # x , y , level ( distance or steps taken )
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        count = 0
        while q:
            x, y, dist = q.popleft()
            if x == m - 1 and y == n-1:
                return dist
            for add_x, add_y in directions:
                new_x = x + add_x
                new_y = y + add_y
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and grid[new_x][new_y] == 0 :
                    grid[new_x][new_y] = 1 # mark as visited
                    q.append((new_x, new_y, dist + 1)) # insert into queue

        return -1