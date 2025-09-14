class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def fn(cur, used):
            if len(cur) == n:
                res.append(cur)
                return
            for i in range(n):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                fn(cur + [nums[i]], used)
                used.remove(nums[i])

        fn([], set())
        return res