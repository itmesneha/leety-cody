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
            q.append([cur, None])
            while q:
                city, parent = q.popleft()
                for child in adj[city]:
                    if child == parent:
                        continue
                    
                    if not visited[child]:
                        visited[child] = True
                        q.append([child, cur])

        count = 0
        for city in range(n):
            if not visited[city]:
                explore(city)
                count += 1

        return count

       