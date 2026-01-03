from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        BFS starting from each node not in a visited set.
        '''

        visited = set()

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque()
            visited.add(node)
            q.append(node)

            while q:
                cur = q.popleft()
                for neighbor in adj[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)

        count = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1 

        

        return count




