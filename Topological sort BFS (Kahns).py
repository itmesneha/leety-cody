from collections import deque
class Solution:
    
    def topoSort(self, n, edges):
        # Code here
        indegree = [0] * n
        adj = [[] for _ in range(n)]
        for u, v in edges:
            indegree[v] += 1
            adj[u].append(v)
            
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            cur = queue.popleft()
            for child in adj[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
            res.append(cur)
            
        return res
