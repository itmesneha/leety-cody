import heapq as h
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x,y in points:
            distance = (x**2 + y**2)
            h.heappush(maxheap, [-distance,[x,y]])
            if len(maxheap) > k:
                h.heappop(maxheap)
            # print(maxheap[0])

        res = []
        while maxheap:
            res.append(h.heappop(maxheap)[1])

        return res
