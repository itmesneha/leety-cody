from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        for u,v in edges:
            if isreachable(u,v):
                ans = [u,v]

            adj[u].append(v)
            adj[v].append(u)
        '''
        adj = [[] for _ in range(len(edges) + 1)]

        def isreachable(u,v): # bfs
            q = deque()
            q.append(u)
            visited = set()

            while q:
                cur = q.popleft()
                for neighbor in adj[cur]:
                    if neighbor == v:
                        return True
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)

            return False

        
        for u,v in edges:
            if isreachable(u,v):
                ans = [u,v]

            adj[u].append(v)
            adj[v].append(u)

    
        return ans
