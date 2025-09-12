class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        cur = 0
        nums.sort()
        # calculating prefix sum
        for i in range(n):
            prefix_sum[i] = cur + nums[i]
            cur = prefix_sum[i]

        def binarysearch(target_index):
            l = 0
            r = target_index
            best_mid = (l+r) // 2
            while l <= r:
                mid = (l+r) // 2
                count = target_index - mid + 1
                windowsum = count * nums[target_index]
                ogsum = prefix_sum[target_index] - prefix_sum[mid] + nums[mid]
                ops = windowsum - ogsum
                if ops > k:
                    l = mid + 1
                else:
                    best_mid = mid
                    r = mid - 1
            return target_index - best_mid + 1

        ans = 1
        for target_index in range(n):
            freq = binarysearch(target_index)
            ans = max(ans, freq)

        return ans
