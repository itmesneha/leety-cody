
#User function Template for python3
from typing import List
from collections import defaultdict
import heapq as h
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
            
        # print(adj)
            
        result = [float('inf')] * (n+1)
        parent = []
        
        for i in range(n+1):
            parent.append(i)
            
        minheap = []
        h.heappush(minheap, (0, 1))
        result[1] = 0
        
        while minheap:
            cost, source = h.heappop(minheap)
            for neighbor, add_cost in adj[source]:
                new_cost = cost + add_cost
                if new_cost < result[neighbor]:
                    result[neighbor] = new_cost
                    parent[neighbor] = source
                    h.heappush(minheap, (new_cost, neighbor))
                    
        # print('result: ', result)
        # print('parent: ', parent)   
        if result[n] == float('inf'):
            return [-1]
            
        path = []
        node = n
        while parent[node] != node:
            path.append(node)
            node = parent[node]
            
        path.append(1)
        path.append(result[n])
        # print(path)
        return path[::-1]
            
        
        
