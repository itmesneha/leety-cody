class Solution:
    
    def topoSort(self, n, edges):
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            
        visited = [False] * n
        stack = []
        
        def dfs(i):
            visited[i] = True
            for child in adj[i]:
                if not visited[child]:
                    dfs(child)
            stack.append(i)
            
            
        for i in range(n):
            if not visited[i]:
                dfs(i)
                
        return stack[::-1]
