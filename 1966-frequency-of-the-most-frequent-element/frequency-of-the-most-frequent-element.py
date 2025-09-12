class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        currsum = 0
        nums.sort()
        freq = 1
        for r in range(n):
            currsum += nums[r]
            if (nums[r] * (r-l+1)) - currsum > k:
                currsum -= nums[l]
                l += 1
            freq = max(freq, r - l + 1)

        return freq