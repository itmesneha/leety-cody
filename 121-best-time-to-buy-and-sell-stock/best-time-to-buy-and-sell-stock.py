class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        if i buy a stock on one day, need to find minimum value on right side of it.
        '''
        profit = 0
        n = len(prices)
        max_from_right = []
        cur_max = float('-inf')
        for i in range(n-1, -1, -1):
            if prices[i] > cur_max:
                cur_max = prices[i]

            max_from_right.append(cur_max)

        max_from_right = max_from_right[::-1]
        print('max_from_right: ', max_from_right)
        for i in range(n):
            profit = max(profit, max_from_right[i] - prices[i])

        return profit
