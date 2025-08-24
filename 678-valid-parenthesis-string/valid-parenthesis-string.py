class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        self.memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        def fn(idx, open):
            if open < 0:
                return False
            if idx >= len(s):
                return open == 0
            if self.memo[idx][open] != -1:
                return self.memo[idx][open]
            if s[idx] == '(':
                self.memo[idx][open] = fn(idx + 1, open + 1)
                return self.memo[idx][open]
            elif s[idx] == ')':
                self.memo[idx][open] = fn(idx + 1, open - 1)
                return self.memo[idx][open]
            else:
                self.memo[idx][open] = fn(idx + 1, open + 1) or fn(idx + 1, open - 1) or fn(idx + 1, open)
                return self.memo[idx][open]
        
        return fn(0, 0)