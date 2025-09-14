class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        totalsum = 0
        for i in range(n):
            totalsum += nums[i]
        if totalsum % 2 != 0:
            return False
        required = totalsum // 2
        memo = {}
        def fn(idx, cursum):
            if cursum == required:
                return True
            if idx == n:
                return False
            if cursum > required:
                return False
            if (idx, cursum) in memo:
                return memo[(idx, cursum)]
            memo[(idx, cursum)] = fn(idx + 1, cursum + nums[idx]) or fn(idx+1, cursum)
            return memo[(idx, cursum)]

        return fn(0, 0)