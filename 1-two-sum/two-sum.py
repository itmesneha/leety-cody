class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        # if its already in the map return, else insert
        for i, num in enumerate(nums): # index, num
            if target-num in hmap:
                return [hmap[target-num], i]
            else:
                hmap[num] = i
