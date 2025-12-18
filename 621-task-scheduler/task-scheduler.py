import heapq as h
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        n+1 block + max heap
        '''
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # print(freq)

        time = 0
        maxheap = []

        for element in freq:
            if element > 0:
                h.heappush(maxheap, -element)

        while maxheap:
            temp = []
            for i in range(1, n+2):
                if maxheap:
                    f = -1 * h.heappop(maxheap)
                    f -= 1
                    temp.append(f)

            for f in temp:
                if f > 0:
                    h.heappush(maxheap, -f)

            if not maxheap: # empty
                time += len(temp)
            else:
                time += n+1

        return time