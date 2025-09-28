from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # n = len(isConnected[0])
        # adj = defaultdict(list)

        # for u in range(m):
        #     for v in range(n):
        #         if isConnected[u][v] == 1:
        #             adj[u].append(v)
        #             adj[v].append(u)

        visited = [False] * n

        def explore(city):
            visited[city] = True
            for j in range(n):
                if isConnected[city][j] == 1 and not visited[j]:
                    explore(j)

        count = 0
        for city in range(n):
            if not visited[city]:
                explore(city)
                count += 1

        return count

       