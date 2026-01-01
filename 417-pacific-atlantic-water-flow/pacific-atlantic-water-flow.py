from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        correct approach - 
        take bfs start points as full top & left row for pacific
        full bottom & right row for atlantic
        find which cells reachable for 2 oceans then intersect them
        
        wrong approach - 
        upper rightmost + lower leftmost - start points for BFS - cannot do this 
        because cells can flow to both oceans, possibly via different paths
        can only move if height(new cell) >= heigh(current cell)
        '''

        m = len(heights)
        n = len(heights[0])

        p_q = deque() # pacific queue
        a_q = deque() # atlantic queue

        pacific = []
        atlantic = []
        visited_pacific = set()
        visited_atlantic = set()

        # q.append((0,n-1))
        # q.append((m-1,0))

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    p_q.append((i,j))
                    visited_pacific.add((i,j))

                if j == n-1 or i == m-1:
                    a_q.append((i,j))
                    visited_atlantic.add((i,j))


        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while p_q:
            x,y = p_q.popleft()
            pacific.append((x,y))

            for dx,dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx == m or ny < 0 or ny == n or (nx,ny) in visited_pacific:
                    continue
                if heights[nx][ny] >= heights[x][y]:
                    visited_pacific.add((nx,ny))
                    p_q.append((nx,ny))

        while a_q:
            x,y = a_q.popleft()
            atlantic.append((x,y))

            for dx,dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx == m or ny < 0 or ny == n or (nx,ny) in visited_atlantic:
                    continue
                if heights[nx][ny] >= heights[x][y]:
                    visited_atlantic.add((nx,ny))
                    a_q.append((nx,ny))

        # intersection of pacific & atlantic
        ans = []
        for i,j in pacific:
            if (i,j) in atlantic:
                ans.append((i,j))

        return ans