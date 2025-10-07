from collections import defaultdict
import heapq as h
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, src: int) -> int:

        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append((v,w))

        result = [float('inf')] * (n+1)
        minheap = []
        result[src] = 0 # takes 0 to reach itself
        h.heappush(minheap, (0, src)) # (cost, node) into minheap

        while minheap:
            cost, source = h.heappop(minheap)
            for neighbor, add_cost in adj[source]:
                new_cost = cost + add_cost
                if new_cost < result[neighbor]:
                    result[neighbor] = new_cost
                    h.heappush(minheap, (new_cost, neighbor))

        ans = max(result[1:n+1])
        if ans == float('inf'):
            return -1
        else:
            return ans