class Solution:

    #Function to detect cycle using DSU in an undirected graph.
	def detectCycle(self, V, adj):
		#Code here
		parent = [-1] * V
		for i in range(V):
		    parent[i] = i
		    
		rank = [1] * V
		
		def find(i):
		    if parent[i] == i:
		        return i
		    parent[i] = find(parent[i])
		    return parent[i]
		    
        def union(u, v):
            parent_u = find(u)
            parent_v = find(v)
            if parent_u == parent_v:
                return
            elif rank[parent_u] > rank[parent_v]:
                parent[parent_v] = parent_u
            elif rank[parent_u] < rank[parent_v]:
                parent[parent_u] = parent_v
            else:
                parent[parent_u] = parent_v
                rank[parent_v] += 1
		
		
		for u in range(V):
		    for v in adj[u]:
		        if u < v:
		            parent_u = find(u)
		            parent_v = find(v)
		            if parent_u == parent_v:
		                return 1
		            union(u, v)
		            
        return 0
