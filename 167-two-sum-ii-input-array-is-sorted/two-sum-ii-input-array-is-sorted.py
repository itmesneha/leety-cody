class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        2 pointers
        if left + right < sum:
            left += 1
        else:
            right -= 1
        '''
        n = len(numbers)
        left = 0
        right = n-1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1