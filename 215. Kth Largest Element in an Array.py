import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for num in nums:
            h.heappush(minheap, num)
            if len(minheap) > k:
                h.heappop(minheap)

        return h.heappop(minheap)
