class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        i = 0
        while i < len(nums):
            start = i
            while i < len(nums) and nums[i] == 0:
                i += 1
            end = i
            n = end - start
            count += (n*(n+1)) // 2
            i += 1
        return count