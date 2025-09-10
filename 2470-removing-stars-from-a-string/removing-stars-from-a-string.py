class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for _ in s:
            if _ == '*':
                stack.pop()
            else:
                stack.append(_)

        return ''.join(stack)   

        # i = 0
        # while i < len(s):
        #     if s[i] == '*' and i > 0:
        #         s = s[:i-1] + s[i+1:]
        #         i -= 2
        #     i += 1

        # return s