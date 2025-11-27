class Solution:
    def isValid(self, s: str) -> bool:
        d = {}
        d = {')':'(', ']':'[', '}':'{'}

        stack = []
        for bracket in s:
            if bracket in d.values():
                stack.append(bracket)
            else:
                if stack:
                    temp = stack.pop()
                    if d[bracket] != temp:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
