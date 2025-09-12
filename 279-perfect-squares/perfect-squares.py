class Solution:
    def numSquares(self, num: int) -> int:
        memo = [-1] * (num+1)
        def fn(n):
            if n == 0:
                return 0
            if memo[n] != -1:
                return memo[n]
            i = 1
            res = float(inf)
            while i <= sqrt(n):
                res = min(res, 1+fn(n-(i**2)))
                i += 1
            memo[n] = res
            return res

        return fn(num)