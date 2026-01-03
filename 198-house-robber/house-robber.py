class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        '''

        n = len(nums)
        memo = [-1] * (n+1)
        def fn(i):
            if i >= n:
                return 0

            if memo[i] != -1:
                return memo[i]

            rob = nums[i] + fn(i+2)
            not_rob = fn(i+1)

            memo[i]  = max(rob, not_rob)
            return memo[i]

        return fn(0)