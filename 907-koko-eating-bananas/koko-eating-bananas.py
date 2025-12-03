class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        binary search on answer ie k
        max = ceil(total bananas / hours)
        min = 1
        '''
        min_k = 1
        max_k = max(piles)
        n = len(piles)
        while min_k <= max_k:
            k = (min_k + max_k) // 2
            time = 0
            for i in range(n):
                if piles[i] - k <= 0:
                    time += 1
                elif piles[i] % k == 0:
                    time += piles[i] // k
                else:
                    time += (piles[i] // k) + 1
            if time > h:
                min_k = k + 1
            elif time <= h:
                max_k = k - 1
            
        return min_k