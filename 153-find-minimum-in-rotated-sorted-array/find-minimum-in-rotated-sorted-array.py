class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        draw a graph, compare with right
        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        left = 0
        right = n-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1 
            else:
                right = mid # to not miss any
        return nums[left]