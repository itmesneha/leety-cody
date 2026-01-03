from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        for u,v in edges:
            if u in visited and v in visited:
                isreachable(u,v)

            adj[u].append(v)
            adj[v].append(u)


        while doing BFS if already in visited
        '''

        nodes = set()
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
            if u in nodes and v in nodes and isreachable(u,v):
                ans = [u,v]

            nodes.add(u)
            nodes.add(v)
            adj[u].append(v)
            adj[v].append(u)

    
        return ans
