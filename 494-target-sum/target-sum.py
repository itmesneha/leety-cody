class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def fn(idx, cur):
            if idx == n:
                if cur == target:
                    return 1
                else:
                    return 0
            if (idx, cur) in memo:
                return memo[(idx, cur)]
            memo[(idx, cur)] = fn(idx + 1, cur + nums[idx]) + fn(idx + 1, cur - nums[idx])
            return memo[(idx, cur)]
        return fn(0, 0)