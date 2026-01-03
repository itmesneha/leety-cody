class Solution:
    def climbStairs(self, n: int) -> int:

        ar = [-1] * (n+1)
        
        def fn(step):
            if step > n:
                return 0
            if step == n:
                return 1

            if ar[step] != -1:
                return ar[step]
            
            ar[step] = fn(step + 1) + fn(step + 2)
            return ar[step]

        return fn(0)