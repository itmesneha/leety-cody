import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for num in nums:
            heappush(minheap, num)
            if len(minheap) > k:
                heappop(minheap)

        return minheap[0]        
