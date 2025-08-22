class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalearnings = sum(gas)
        totalexpenditure = sum(cost)
        if totalexpenditure > totalearnings:
            return -1
        n = len(gas)
        total = 0
        res = 0
        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
            # else:
            #     return res
        return res


        # cur = 0
        # n = len(gas)
        # for start in range(n):
        #     cur = 0
        #     valid = True
        #     for step in range(n): # running loop for number of gas stations
        #         idx = (start + step) % n
        #         cur += gas[idx] - cost[idx]
        #         if cur < 0:
        #             valid = False
        #             break # gas became too low
        #     if valid:
        #         return start
        # return -1