class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        pre = [0] * (n+1)
        cur = 0
        nums.sort()
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]

        freq = 1
        while r < n:
            windowsum = (r - l + 1) * nums[r]
            ogsum = pre[r+1] - pre[l] 

            if windowsum - ogsum <= k:
                freq = max(freq, r - l + 1)
                r += 1
            else:
                l += 1

        return freq
