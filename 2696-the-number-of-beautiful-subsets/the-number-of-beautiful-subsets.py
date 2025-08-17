class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        def fn(idx, subs):
            if idx == len(nums):
                if len(subs) != 0:
                    return 1
                else:
                    return 0
            reject = fn(idx + 1, subs)
            take = 0
            if nums[idx] - k not in subs:
                take = fn(idx + 1, subs + [nums[idx]])
            return take + reject

        return fn(0, [])