class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        ar = [-1] * (n+1)

        def fn(step):
            if step > n:
                return 0

            if ar[step] != -1:
                return ar[step]

            if step == n:
                return 0

            ar[step] = cost[step] + min(fn(step + 1) , fn(step + 2))

            return ar[step]
        
        return min(fn(0) , fn(1))