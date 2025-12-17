class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        Sort, skip duplicates sideways, and once you take a number, you must move forward.
        '''
        self.res = []
        nums.sort()
        def fn(index, target, op):
            if target == 0:
                self.res.append(op[:])
                return

            if target < 0 or index == len(nums):
                return

            for i in range(index, len(nums)): # sideways

                if i > index and nums[i] == nums[i-1]:
                    continue

                op.append(nums[i])
                fn(i + 1, target - nums[i], op) # go deeper
                op.pop()

        fn(0, target, [])
        return self.res
