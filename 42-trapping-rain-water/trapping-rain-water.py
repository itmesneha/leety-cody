class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        n = len(height)
        max_right = [-1] * n
        cur_max_left = height[0]
        cur_max_right = height[n-1]
        for i in range(n):
            cur_max_left = max(cur_max_left, height[i])
            max_left.append(cur_max_left)
            cur_max_right = max(cur_max_right, height[n-i-1])
            max_right[n-i-1] = cur_max_right

        # cur_max = height[n-1]
        # for i in range(n-1,-1,-1):
        #     cur_max = max(cur_max, height[i])
        #     max_right[i] = cur_max
        # print(max_left)
        # print(max_right)
        res = 0
        for i in range(n):
            res += min(max_left[i], max_right[i]) - height[i]
        return res