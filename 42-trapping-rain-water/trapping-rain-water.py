class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        n = len(height)
        max_right = [-1] * n
        cur_max = height[0]
        for i in range(n):
            cur_max = max(cur_max, height[i])
            max_left.append(cur_max)
        cur_max = height[n-1]
        for i in range(n-1,-1,-1):
            cur_max = max(cur_max, height[i])
            max_right[i] = cur_max
        # print(max_left)
        # print(max_right)
        res = 0
        for i in range(n):
            res += min(max_left[i], max_right[i]) - height[i]
        return res