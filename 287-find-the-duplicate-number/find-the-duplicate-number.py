class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        use slow & fast to find exact duplicate. then reset slow to start & move both one by one to find duplicate element.
        '''
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0

        while slow != fast: # guaranteed to meet
            slow = nums[slow]
            fast = nums[fast]

        return slow       

        
