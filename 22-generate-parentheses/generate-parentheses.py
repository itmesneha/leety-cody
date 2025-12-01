class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(open_left, close_left, output):
            if close_left < open_left:
                return
            if close_left == 0:
                res.append(output)
                return
            if open_left > 0:
                helper(open_left - 1, close_left, output + '(')
            if close_left > 0 and close_left >= open_left:
                helper(open_left, close_left - 1, output + ')')

        helper(n, n, '')
        return res
            