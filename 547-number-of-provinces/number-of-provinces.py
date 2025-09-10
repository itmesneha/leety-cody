class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def bfs(city):
            q = deque()
            visited[city] = True
            q.append(city)
            while q:
                cur = q.popleft()
                for j in range(n):
                    if isConnected[cur][j] and not visited[j]: # and cur != j 
                        child = j
                        visited[child] = True
                        q.append(child)

        def dfs(cur):
            visited[cur] = True
            for j in range(n):
                if isConnected[cur][j] and not visited[j]: # and cur != j 
                    dfs(j)

        for city in range(n):
            if not visited[city]:
                # bfs(city)
                dfs(city)
                count += 1
        return count