class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        Sort first; at each depth, skip equal values sideways (same tree level) but allow them downward.
        at same tree level, try each choice as the next element of the subset (for loop)
        inside for loop skip dups and add element, go deeper

        dont mix:
            - binary choice recursion (take / not take)
            - for-loop backtracking recursion
        👉 These are mutually exclusive patterns. use one, not both.

        '''
        nums.sort()
        self.res = []

        def fn(nums, op, idx):
            n = len(nums)
            self.res.append(op[:])

            for i in range(idx, n): # in same tree level, explore all subsets, give all subsets of same length
                
                if i > idx and nums[i] == nums[i-1]: # Skip duplicate values only when they appear sideways at same tree level
                    continue

                # # dont take
                # fn(nums, op, idx + 1)

                # take
                op.append(nums[i])
                fn(nums, op, i + 1) # go deeper, bigger subsets
                op.pop() # come back to same tree level and explore further with idx increments


        fn(nums, [], 0)
        return self.res