class Solution:
    def change(self, amount: int, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def fn(idx, cur):
            if cur == amount:
                return 1
            if idx == n:
                return 0
            if cur > amount:
                return 0
            if (idx, cur) in memo:
                return memo[(idx, cur)]
            memo[(idx, cur)] = fn(idx, cur + nums[idx]) + fn(idx + 1, cur)
            return memo[(idx, cur)]
            # +fn(idx + 1, cur + nums[idx])

        return fn(0,0)