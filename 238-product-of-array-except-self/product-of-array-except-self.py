class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        prefix array
        suffix array
        ans = prefix[i-1] * suffix[i+1]
        '''
        n = len(nums)
        prefix = [1] * n
        suffix = 1
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i]
        res = [1] * n
        res[n-1] = prefix[n-2]
        suffix = nums[n-1]
        for i in range(n-2, 0, -1):
            res[i] = prefix[i-1] * suffix
            suffix *= nums[i]
            # print(res)
        res[0] = suffix
        return res