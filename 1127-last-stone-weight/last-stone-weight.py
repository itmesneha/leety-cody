import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for stone in stones:
            h.heappush(maxheap, -stone)

        while len(maxheap) > 1:
            x = h.heappop(maxheap)
            y = h.heappop(maxheap)

            if x != y:
                h.heappush(maxheap, -abs(x-y))

        if maxheap:
            return -1*h.heappop(maxheap)
        else:
            return 0