from collections import defaultdict
import heapq as h
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adj = defaultdict(list)
        for source, dest, weight in edges:
            adj[source].append((dest, weight))
            
        # print(adj)
            
        result = [float('inf')] * V
        result[src] = 0
        q = []
        h.heappush(q, (0, src))
        while q:
            cost, source = h.heappop(q)
            for neighbor, add_cost in adj[source]:
                new_cost = cost + add_cost
                if new_cost < result[neighbor]:
                    result[neighbor] = new_cost
                    h.heappush(q, (new_cost, neighbor))
                    
        return result
        
        
