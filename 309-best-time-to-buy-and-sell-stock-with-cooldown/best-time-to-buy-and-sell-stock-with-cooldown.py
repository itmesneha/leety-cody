class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [[-1 for _ in range(2)] for _ in range(n+1)]
        def fn(day, buy):
            if day >= n:
                return 0
            profit = 0
            if memo[day][buy] != -1:
                return memo[day][buy]
            if buy:
                take = fn(day + 1, False) - prices[day]
                not_take = fn(day + 1, True)
                profit = max(profit, take, not_take)
            else:
                sell = fn(day + 2, True) + prices[day]
                not_sell = fn(day + 1, False)
                profit = max(profit, sell, not_sell)
                
            memo[day][buy] = profit
            return profit

        return fn(0, True)