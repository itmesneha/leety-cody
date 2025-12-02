class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        two functions:
        nearest smallest left
        nearest smallest right

        for each bar we need nsl & nsr coz uptil that the bar's
        area can be extended.

        ans = max(ans, (nsr - nsl - 1) * height)
        '''
        n = len(heights)
        def nsl(heights):
            nsl = [] 
            stack = []
            for i in range(n):
                while stack and stack[-1][0] >= heights[i]:
                    stack.pop()
                if stack:
                    nsl.append(stack[-1][1])
                else:
                    nsl.append(-1)
                stack.append((heights[i], i))

            return nsl

        def nsr(heights):
            nsr = [] 
            stack = []
            for i in range(n-1, -1, -1):
                while stack and stack[-1][0] >= heights[i] :
                    stack.pop()
                if stack:
                    nsr.append(stack[-1][1])
                else:
                    nsr.append(n)
                stack.append((heights[i], i))

            return nsr[::-1]
        ans = 0
        nsl = nsl(heights)
        nsr = nsr(heights)
        # print(nsl)
        # print(nsr)
        for i in range(n):
            cur_area =  (nsr[i] - nsl[i] - 1) * heights[i]
            # print(cur_area)
            ans = max(ans,cur_area)

        return ans