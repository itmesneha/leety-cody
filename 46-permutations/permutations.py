class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def fn(cur, used):
            if len(cur) == n:
                res.append(cur)
                return
            for i in range(n):
                if i in used:
                    continue
                # used.add(nums[i])
                fn(cur + [nums[i]], used + [i])
                # used.remove(nums[i])

        fn([], [])
        return res