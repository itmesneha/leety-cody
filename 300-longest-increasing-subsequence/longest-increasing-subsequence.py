class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def bs_fn(arr, num):
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] < num:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        bs_array = []
        for num in nums:
            idx = bs_fn(bs_array, num)
            if idx > len(bs_array) - 1:
                bs_array.append(num)
            else:
                bs_array[idx] = num
        return len(bs_array)