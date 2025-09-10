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
                    if isConnected[cur][j] and cur != j and not visited[j]:
                        child = j
                        visited[child] = True
                        q.append(child)



        for city in range(n):
            if not visited[city]:
                bfs(city)
                count += 1
        return count