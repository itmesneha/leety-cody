class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.memo = [[-1 for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        def fn(idx, nums, target):
            if target == 0:
                return 1
            if idx >= len(nums) or target < 0:
                return 0
            if self.memo[idx][target] != -1:
                return self.memo[idx][target]
            self.memo[idx][target] = fn(0, nums, target - nums[idx]) + fn(idx + 1, nums, target)
            return self.memo[idx][target]
        return fn(0, nums, target)