class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        def fn(nums, index, memo):
            if index >= len(nums):
                return 0
            if memo[index] != -1:
                return memo[index]
            not_rob = fn(nums, index + 1, memo)
            rob = nums[index] + fn(nums, index + 2, memo)
            memo[index] = max(rob, not_rob) 
            return memo[index]

        return max(fn(nums[:n-1], 0, [-1] * n), fn(nums[1:], 0, [-1] * n))