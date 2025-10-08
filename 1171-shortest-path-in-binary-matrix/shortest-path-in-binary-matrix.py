from collections import deque
import heapq as h
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid) # rows
        n = len(grid[0]) # cols

        result = [[float('inf') for _ in range(n)] for _ in range(m)] # result vector

        i, j = 0, 0 # source
        if grid[i][j] == 1: # if source = 1
            return -1
        grid[i][j] = 1 # mark as visited
        minheap = []
        h.heappush(minheap, (1, i, j)) # cost,  x , y 
        result[i][j] = 1
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        
        while minheap:
            dist, x, y = h.heappop(minheap)
            # if x == m - 1 and y == n-1:
            #     return dist
            for add_x, add_y in directions:
                new_x = x + add_x
                new_y = y + add_y
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and grid[new_x][new_y] == 0 :
                    grid[new_x][new_y] = 1 # mark as visited
                    if dist + 1 < result[new_x][new_y]:
                        result[new_x][new_y] = dist + 1 # update result
                        h.heappush(minheap, (dist + 1, new_x, new_y)) # insert into minheap

        if result[m-1][n-1] < float('inf'):
            return result[m-1][n-1]
        else:
            return -1