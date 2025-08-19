class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxindex = 0
        n = len(nums)
        for i in range(n):
            if i > maxindex:
                return False
            maxindex = max(maxindex, i + nums[i])
            if maxindex >= n:
                return True
        return True