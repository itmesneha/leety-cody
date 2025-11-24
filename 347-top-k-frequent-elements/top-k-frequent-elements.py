import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums) # num : freq
        max_heap = []
        for num in mp:
            h.heappush(max_heap,(-mp[num], num))
        ans = []
        for i in range(k):
            ele = h.heappop(max_heap)
            ans.append(ele[1])
        return ans
