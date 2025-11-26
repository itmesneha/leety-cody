class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        prefix array
        suffix array
        ans = prefix[i-1] * suffix[i+1]
        '''
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i]
            suffix[n-i-1] = suffix[n-i] * nums[n-i-1]
            # print('prefix: ', prefix)
            # print('suffix: ',suffix)
        res = [1] * n
        res[0] = suffix[1]
        res[n-1] = prefix[n-2]
        for i in range(1,n-1):
            res[i] = prefix[i-1] * suffix[i+1]
            # print(res)
        return res