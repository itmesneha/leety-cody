class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0] * 1001
        for people, start, end in trips:
            passengers[start] += people
            passengers[end] -= people
        pre = 0
        for i in range(1001):
            pre += passengers[i]
            if pre > capacity:
                return False

        return True
