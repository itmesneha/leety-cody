class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        as it is sorted only need to look front
        '''
        n = len(numbers)
        for i in range(n):
            left = i + 1
            right = n-1
            required = target - numbers[i]
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == required:
                    return [i+1, mid+1]
                if required < numbers[mid]:
                    right = mid - 1
                else:
                    left = mid + 1


        