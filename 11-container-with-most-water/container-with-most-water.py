class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        res = 0
        while l < r:
            water = (r-l) * min(height[l], height[r])
            res = max(res, water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res