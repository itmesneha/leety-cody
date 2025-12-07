class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        greedy approach
        '''
        profit = 0
        n = len(prices)
        left = 0
        for right in range(1, n):
            if prices[right] > prices[left]:
                profit = max(profit, prices[right] - prices[left])

            else:
                left = right

        return profit
