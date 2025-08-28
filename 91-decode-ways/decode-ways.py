class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [-1 for _ in range(n+2)]
        def fn(i):
            if i >= n:
                return 1
            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]
            ans = fn(i+1)
            if i+1 < n and 10 <= int(s[i:i+2]) <= 26:
                ans += fn(i+2)
            dp[i] = ans
            return ans

        return fn(0)