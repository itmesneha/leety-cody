class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        memo = [-1] * n
        def fn(idx, memo):
            if idx >= n:
                return 0
            if memo[idx] != -1:
                return memo[idx]
            memo[idx] = nums[idx] + min(fn(idx + 1, memo), fn(idx + 2, memo))
            return memo[idx]
        
        start_0 = fn(0, memo)
        start_1 = fn(1, memo)
        return min(start_1,start_0)
