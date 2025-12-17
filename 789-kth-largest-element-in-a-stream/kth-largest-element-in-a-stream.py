import heapq as h
class KthLargest:
    '''
    max heap of size k
    '''
    def __init__(self, k: int, nums: List[int]):
        self.k  = k
        self.nums = nums
        self.minheap = []
        for num in nums:
            h.heappush(self.minheap, num)
            if len(self.minheap) > self.k:
                h.heappop(self.minheap)
        

    def add(self, val: int) -> int:
        h.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            h.heappop(self.minheap)

        return self.minheap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)