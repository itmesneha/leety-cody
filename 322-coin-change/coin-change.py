class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        When you see:
            minimum number of items
            unlimited usage
            target amount

        Think: DP on amount, not on index
        Time Complexity: for amount = 11 there will be [11, 10, 9, 8,...] each is split 3 ways here
        and fn(amount) is calculated only once. so O(amount x coins)
        '''
        dp = {}
        def fn(rem): # rem = remaining amount
            if rem == 0:
                return 0

            if rem < 0:
                return float('inf') # it does not work 

            if rem in dp:
                return dp[rem]

            ans = float('inf') # start with maximum ans (number of coins needed to make rem)
            for coin in coins: # try every coin
                ans = min(ans, 1 + fn(rem - coin))

            dp[rem] = ans # at the end of trying all coins & combos assign best (min) to dp
            return dp[rem]

        ans = fn(amount)
        if ans != float('inf'):
            return ans
        else:
            return -1

