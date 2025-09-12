class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * (n+1)
        def fn(idx):
            if idx >= n:
                return 0
            if memo[idx] != -1:
                return memo[idx]
            memo[idx] = nums[idx] + min(fn(idx + 1), fn(idx + 2))
            return memo[idx]

        return min(fn(0),fn(1))
