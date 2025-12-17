class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Fix one position at a time by swapping each possible choice into it, recurse, then swap back.
        '''
        self.res = []

        def fn(nums, idx):
            n = len(nums)
            if idx == n:
                self.res.append(nums[:])
                return

            for i in range(idx, n):
                nums[i], nums[idx] = nums[idx], nums[i]
                fn(nums, idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        fn(nums, 0)
        return self.res