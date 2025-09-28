from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        n = len(isConnected[0])
        count = 0
        adj = defaultdict(list)

        for u in range(m):
            for v in range(n):
                if isConnected[u][v] == 1:
                    adj[u].append(v)
                    adj[v].append(u)

        visited = [False] * n

        def explore(cur):
            q = deque()
            visited[cur] = True
            q.append(cur)
            while q:
                city = q.popleft()
                for child in adj[city]:
                    if not visited[child]:
                        visited[child] = True
                        q.append(child)

        count = 0
        for city in range(n):
            if not visited[city]:
                explore(city)
                count += 1

        return count

        # directions = [[0,1],[0,-1],[1,0],[-1,0]]

        # def explore(i, j):
        #     q = deque()
        #     isConnected[i][j] = -1
        #     q.append([i, j])
        #     while q:
        #         x, y = q.popleft()
        #         for d_x, d_y in directions:
        #             n_x, n_y = x + d_x, y + d_y
        #             if n_x >= 0 and n_x < m and n_y >= 0 and n_y < n and isConnected[n_x][n_y] == 1:
        #                 isConnected[n_x][n_y] = -1    
        #                 q.append([n_x, n_y])


        # for i in range(m):
        #     for j in range(n):
        #         if isConnected[i][j] == 1:
        #             explore(i, j)
        #             count += 1

        # return count