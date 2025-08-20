class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        self.memo = [-1 for _ in range(n + 1)]
        def fn(idx):
            if idx >= n-1:
                return 0
            if self.memo[idx] != -1:
                return self.memo[idx]
            ans = float('inf')
            for i in range(1, nums[idx] + 1):
                if idx + i < n:
                    ans = min(ans , 1 + fn(idx + i))
            self.memo[idx] = ans 
            return self.memo[idx]

        return fn(0)
        