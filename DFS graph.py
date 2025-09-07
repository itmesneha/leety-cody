class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    
    def dfs(self, adj):
        # code here
        n = len(adj)
        visited = [False for _ in range(n)]
        output = []
        def solve(u):
            if visited[u] == True:
                return
            visited[u] = True
            output.append(u)
            for v in adj[u]:
                solve(v)
                
        solve(0)
        return output
        
