from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        output = []
        # code here
        q = deque()
        q.append(0)
        visited = [False for _ in range(len(adj))]
        while q:
            u = q.popleft()
            output.append(u)
            for v in adj[u]:
                if visited[v] == False:
                    visited[u] = True
                    q.append(v)
                    
        return output
