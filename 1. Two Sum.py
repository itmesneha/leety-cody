class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevmap = dict()

        for i,num in enumerate(nums):
            if target - num in prevmap:
                return(prevmap[target-num], i)
            prevmap[num] = i

        # hashmap = dict()
        # i = 0
        # for num in nums:
        #     hashmap[num] = i
        #     i += 1
        # print(hashmap)
        # indices = []
        # for num in nums:
        #     if (target - num) in hashmap and nums.index(num) != hashmap[target - num]:
        #         return [nums.index(num), hashmap[target - num]]
        #     else:
        #         continue
