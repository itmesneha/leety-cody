class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        ar[step] = cost[step] + min(fn(step + 1) , fn(step + 2))
        return min(start_0 , start_1) - reuse memo across function calls
        '''
        
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
        
        start_0 = fn(0)
        start_1 = fn(1)
        return min(start_0 , start_1)