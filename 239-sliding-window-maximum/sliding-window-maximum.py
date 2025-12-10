import heapq as h

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        using deque
        '''
        queue = deque()
        n = len(nums)
        l,r = 0,0
        ans = []
        while r < n:
            # print(f'queue: {queue}')x
            while queue and nums[r] > nums[queue[0]]:
                queue.popleft()

            if queue and l > queue[0]:
                queue.popleft()

            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()

            queue.append(r)
            
            if r >= k-1:
                ans.append(nums[queue[0]])
                l += 1
            # print(f'ans: {ans}')
            r += 1
            
        return ans


        # using heap
        # max_heap = []
        # ans = []
        # n = len(nums)
        # l = 0
        # r = k-1
        # for i in range(l, r+1):
        #     h.heappush(max_heap, [-nums[i], i])
        # ans.append(-1 * max_heap[0][0])
        # l += 1
        # r += 1
        # while r < n:
        #     h.heappush(max_heap, [-nums[r], r])
        #     # if max number no longer in window
        #     while max_heap[0][1] < l : 
        #         h.heappop(max_heap)
        #     ans.append(-1 * max_heap[0][0])
        #     l += 1
        #     r += 1
        # return ans

