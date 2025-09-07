from collections import deque
class Solution:
	def isCycle(self, n, edges):
	    adj = [[] for _ in range(n)]
	    for u,v in edges:
	        adj[u].append(v)
	        adj[v].append(u)
	        
	    visited = [False] * n
	    
	    def dfs(u, parent):
	        visited[u] = True
	        for v in adj[u]:
	            if v == parent:
	                continue
	            
	            if visited[v]:
	                return True
	  
	            if dfs(v, u):
	                return True
	                    
	        return False
	    
	    # parse all individual nodes
	    
	    for u in range(n):
	        if not visited[u] and dfs(u, -1):
	            return True
	    return False
	        
	    
		
# 		q = deque()
# 		q.append(0)
# 		visited = [False] * n
# 		visited[0] = True
# 		while q:
# 		    u = q.popleft()
# 		    for v in adj[u]:
# 		        if u == v:
# 		            return True
