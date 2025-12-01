class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # monotonic stack
        n = len(temperatures)
        res = []
        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                res.append(stack[-1] - i)
            else:
                res.append(0)
            stack.append(i)
        res = res[::-1]
        # res.append(0)
        print(res)
        return res