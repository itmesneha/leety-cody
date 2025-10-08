import heapq as h
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        result = [[float('inf')] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        minheap = []
        i = 0
        j = 0
        h.heappush(minheap, (0, i, j, heights[i][j])) # cost, x, y , old heights value
        heights[i][j] = -1 # mark as visited
        result[i][j] = 0 # cost to source = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]] # up, down, left, right
        while minheap:
            d, x, y, val = h.heappop(minheap) # pop top 
            visited[x][y] = True
            for add_x, add_y in directions: # for each direction
                # find new coordinates
                new_x = x + add_x
                new_y = y + add_y
                # check within boundaries new coordinates
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n: 
                    # find abs difference
                    new_cost = max(d, abs(heights[new_x][new_y] - val))
                    if new_cost < result[new_x][new_y]: # if cost is less
                        result[new_x][new_y] = new_cost # update result
                        # add to heap
                        h.heappush(minheap, (new_cost, new_x, new_y, heights[new_x][new_y])) 


        if result[m-1][n-1] != float('inf'):
            return result[m-1][n-1]
        else:
            return -1