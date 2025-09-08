from collections import deque
class Solution:
	def isCycle(self, n, edges):
	    adj = [[] for _ in range(n)]
	    for u,v in edges:
	        adj[u].append(v)
	        adj[v].append(u)
	        
	    visited = [False] * n
	    
	    def bfs(node, parent):
	        q = deque()
	        q.append((node, parent))
	        visited[node] = True
	        while q:
	            cur, parent = q.popleft()
	            for child in adj[cur]:
	                if child == parent:
	                    continue
	                if visited[child]:
	                    return True
	                q.append((child, cur))
	                visited[child] = True
	    
	    for i in range(n):
	        if not visited[i] and bfs(i, -1):
	            return True
	    return False
