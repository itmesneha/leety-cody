class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        use a monotonic stack (strictly increasing values downwards here)
        for every value in temperatures, check if stack is non empty
        then pop out all values that are <= current temperature value

        then if stack is non empty the top element will be the closest greater
        element.
        then push current temperature into stack.

        in stack we are storing indices as we need that to calculate days.
        '''

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