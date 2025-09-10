from collections import deque
class Solution:
    def isCycle(self, n, edges):
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for u,v in edges:
            adj[u].append(v)
            indegree[v] += 1
            
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                
        nodecount = 0
        while q:
            cur = q.popleft()
            for child in adj[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
            nodecount += 1
            
        return nodecount != n
