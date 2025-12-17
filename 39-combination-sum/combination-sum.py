class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def fn(nums, op, index, target):
            if target < 0:
                return

            if target == 0:
                self.res.append(op[:])
                return 

            if index == len(nums):
                return

            fn(nums, op, index+1, target) # dont take & move
            op.append(nums[index])
            fn(nums, op, index, target - nums[index]) # take it but dont move, can repeat
            op.pop()
            # op.append(nums[index])
            # fn(nums, op, index + 1, target - nums[index]) # take it & move
            # op.pop()

        fn(nums, [], 0, target)
        return self.res