class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        n = len(nums)
        ans = float('-inf')
        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n-i-1]
            ans = max(ans, prefix, suffix)
            if nums[i] == 0:
                prefix = 1
            if nums[n-i-1] == 0:
                suffix = 1

        return ans