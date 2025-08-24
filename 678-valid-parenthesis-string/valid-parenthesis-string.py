class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        stacky = []
        asterisks = []
        for i in range(n):
            if s[i] == '(':
                stacky.append(i)
            elif s[i] == ')':
                if stacky:
                    stacky.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
            else:
                asterisks.append(i)

        while stacky and asterisks:
            if stacky[-1] < asterisks[-1]:
                stacky.pop()
                asterisks.pop()
            else:
                return False

        return not stacky

        # n = len(s)
        # memo = [[None for _ in range(n + 1)] for _ in range(n + 1)]
        # def fn(idx, open):
        #     if open < 0:
        #         return False
        #     if idx == n:
        #         return open == 0
        #     if memo[idx][open] is not None:
        #         return memo[idx][open]

        #     if s[idx] == '(':
        #         ans = fn(idx + 1, open + 1)
        #     elif s[idx] == ')':
        #         ans = fn(idx + 1, open - 1)
        #     else:
        #         ans = fn(idx + 1, open + 1) or fn(idx + 1, open - 1) or fn(idx + 1, open)
                
        #     memo[idx][open] = ans
        #     return ans
        
        # return fn(0, 0)