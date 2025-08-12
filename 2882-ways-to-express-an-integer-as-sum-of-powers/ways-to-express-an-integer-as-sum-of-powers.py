mod = 10**9 + 7

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        self.arr = []
        i = 1
        num = i ** x
        while num <= n:
            self.arr.append(num)
            i += 1
            num = i ** x
        
        memo = [[-1] * (n + 1) for _ in range(len(self.arr) + 1)]
        
        def fn(idx, tsum):
            if tsum == n:
                return 1
            if idx >= len(self.arr) or tsum > n:
                return 0
            if memo[idx][tsum] != -1:
                return memo[idx][tsum]
            
            memo[idx][tsum] = (fn(idx + 1, tsum + self.arr[idx]) + fn(idx + 1, tsum)) % mod
            return memo[idx][tsum]
        
        return fn(0, 0)
