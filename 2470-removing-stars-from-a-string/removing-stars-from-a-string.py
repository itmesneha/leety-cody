class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '*':
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)   

        # i = 0
        # while i < len(s):
        #     if s[i] == '*' and i > 0:
        #         s = s[:i-1] + s[i+1:]
        #         i -= 2
        #     i += 1

        # return s