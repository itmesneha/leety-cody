class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        d = defaultdict(int)
        n = len(nums)
        ans = [0] * n
        maxheap = []
        for i in range(n):
            d[nums[i]] += freq[i]
            heappush(maxheap, ( (0-d[nums[i]]) , nums[i]))
            while maxheap and 0-maxheap[0][0] > d[maxheap[0][1]]:
                # stale: freq of top element is more than what is there in dictionary
                heappop(maxheap)
            if maxheap:
                # print('i: ', i, 'taking this value', 'maxheap[0]: ', maxheap[0])
                ans[i] = 0 - maxheap[0][0]

        return ans
