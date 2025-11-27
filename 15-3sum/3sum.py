class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n):
            j = i + 1
            k = n-1
            required = 0 - nums[i]
            while j < k:
                if nums[j] + nums[k] == required:
                    res.add((nums[i], nums[j], nums[k]))
                if nums[j] + nums[k] < required:
                    j += 1
                else:
                    k -= 1
        return list(res)