class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        ans = 0
        for num in store:
            if (num-1) not in store:
                start = num
                length = 1
                while start + length in store:
                    length += 1
                ans = max(ans, length)
        return ans