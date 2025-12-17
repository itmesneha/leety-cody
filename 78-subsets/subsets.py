class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.n = len(nums)
        def fn(nums, ans, index):
            if index == self.n:
                self.res.append(ans)
                return

            fn(nums, ans + [nums[index]], index + 1)
            fn(nums, ans, index + 1)

        fn(nums, [], 0)
        return self.res