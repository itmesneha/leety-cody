class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        summ = 0
        i = 0
        j = 0
        n = len(nums)
        for j in range(n):
            summ += nums[j]
            res = max(res, summ)
            if summ < 0:
                i = j
                i += 1
                summ = 0
            
        return res