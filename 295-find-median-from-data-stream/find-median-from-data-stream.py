import heapq as h
class MedianFinder:
    '''
    # 1. push to maxheap
        # 2. take top of maxheap (largest element) and move to minheap, now it will come to bottom of minheap 
        # if size of minheap > maxheap, remove top of minheap (minimum element) and push to maxheap
        # this will keep balance
    '''

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num: int) -> None:
        # 1. push to maxheap
        # 2. take top of maxheap (largest element) and move to minheap, now it will come to bottom of minheap 
        # if size of minheap > maxheap, remove top of minheap (minimum element) and push to maxheap
        # this will keep balance

        h.heappush(self.maxheap, -num)
        h.heappush(self.minheap, -h.heappop(self.maxheap))

        if len(self.minheap) > len(self.maxheap):
            h.heappush(self.maxheap, -h.heappop(self.minheap))
            

    def findMedian(self) -> float:

        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2
        if self.maxheap and len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()