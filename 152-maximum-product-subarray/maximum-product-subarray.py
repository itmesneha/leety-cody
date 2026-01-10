class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Negative numbers flip max ↔ min, so scan from both ends and reset at zero.
        Inside each zero-free segment:
            If there’s an even number of negatives → whole segment is best
            If odd → drop either the leftmost or rightmost negative
        '''
        prefix = 1
        suffix = 1
        ans = float('-inf')
        n = len(nums)
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[n-i-1]

            ans = max(ans, prefix, suffix)

        return ans
