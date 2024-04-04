class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        length = 0

        numset = set(nums)

        for number in nums:
            #check if its the start of a sequence
            if number-1 not in numset:
                length = 0
                while number+length in numset:
                    length = length + 1
            longest = max(longest, length)
            
        return longest
