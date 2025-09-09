
class Solution:
    def isCycle(self, n, edges):
        adj = [[] for _ in range(n) ]
        for u,v in edges:
            adj[u].append(v)
        visited = [False] * n
        inRecursion = [False] * n
        def isCycle(i):
            visited[i] = True
            inRecursion[i] = True
            for child in adj[i]:
                if not visited[child] and isCycle(child):
                    return True
                elif inRecursion[child]: # visited[child] == True
                    return True
            inRecursion[i] = False
            return False
                    
        for i in range(n):
            if not visited[i] and isCycle(i):
                return True
        return False
            
