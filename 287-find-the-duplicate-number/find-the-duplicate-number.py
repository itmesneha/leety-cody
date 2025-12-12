class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        array = [0] * (n+1)
        for num in nums:
            if array[num] == 1:
                return num
            else:
                array[num] = 1

        
