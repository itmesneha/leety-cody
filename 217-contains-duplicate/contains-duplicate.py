class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        return False

        # ans = False
        # for num in nums:
        #     ans = ans ^ num
        # print(ans)
        # return bool(ans)