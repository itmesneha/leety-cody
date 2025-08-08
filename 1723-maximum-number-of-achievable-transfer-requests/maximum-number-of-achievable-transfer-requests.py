class Solution:
    def solve(self, idx, count, resultant, requests):
        # base case
        if idx >= len(requests):
            flag = True
            for val in resultant:
                if val != 0:
                    flag = False
                    break
            if flag == True:
                self.result = max(self.result, count)
            return

        # process request
        from_building = requests[idx][0]
        to_building = requests[idx][1]

        resultant[from_building] -= 1
        resultant[to_building] += 1

        self.solve(idx + 1, count + 1, resultant, requests)

        # dont process request
        # undo step
        resultant[from_building] += 1
        resultant[to_building] -= 1

        self.solve(idx + 1, count, resultant, requests)


    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.result = float('-inf')
        resultant = [0] * n
        self.solve(0, 0, resultant, requests)
        return self.result