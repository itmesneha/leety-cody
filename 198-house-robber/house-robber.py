class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def fn(index, money):
            if index >= n:
                return money
            
            if (index, money) in memo:
                return memo[(index, money)]

            not_rob = fn(index + 1, money)

            rob = fn(index + 2, money + nums[index])

            res = max(rob, not_rob) 
            memo[(index, money)] = res
            return res


        return fn(0, 0)