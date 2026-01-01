from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        shortest path in unweighted graph = BFS

        Imagine all gates flooding the grid at the same time.
        The water that reaches a cell first is from the nearest gate.
        That’s multi-source BFS.

        Add all treasure to q, then keep adding one at each level.
        '''

        q = deque()

        m = len(grid)
        n = len(grid[0])
        inf = (2**31) - 1
        # push all treasure chests into deque first
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while q:
            x,y = q.popleft() # pop treasure chest
            
            # begin exploration
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if nx < 0 or nx == m or ny < 0 or ny == n or grid[nx][ny] != inf:
                    continue
                
                # if grid[nx][ny] == float('inf')
                grid[nx][ny] = grid[x][y] + 1 
                # as we expand outwards from each x,y in q 
                # we can just add 1. initially the value of treasure points is 0, 
                # the first ones we reach from it would be 0 + 1
                q.append((nx,ny))







