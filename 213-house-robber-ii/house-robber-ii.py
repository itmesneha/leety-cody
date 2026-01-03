class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Break the circle into two linear problems and take the max.
        ie max( nums[:n-1], nums[1:] )
        rob = nums[i] + fn(i+2)
            not_rob = fn(i+1)
        memo[i]  = max(rob, not_rob)
        '''
        n = len(nums)
        
        if n == 1:
            return nums[0]

      
        memo = [-1] * (n+1)

        def fn(i, nums, memo):
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]

            rob = nums[i] + fn(i+2, nums, memo)
            not_rob = fn(i+1, nums, memo)

            memo[i]  = max(rob, not_rob)
            return memo[i]

        return max(fn(0, nums[:n-1], [-1] * (n+1)), fn(0, nums[1: ], [-1] * (n+1)))