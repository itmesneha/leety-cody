class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.res = []
        nums.sort()
        def fn(idx, subs):
            if idx == len(nums):
                if len(subs) != 0:
                    self.res.append(subs)
                return
            fn(idx + 1, subs)
            if nums[idx] - k not in subs:
                fn(idx + 1, subs + [nums[idx]])
           

        fn(0, [])
        return len(self.res)