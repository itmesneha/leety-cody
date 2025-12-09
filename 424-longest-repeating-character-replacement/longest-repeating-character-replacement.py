class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        check sliding window length - max(counts map values)
        this max will keep changing.
        '''
        counts = defaultdict(int)
        l = 0
        n = len(s)
        ans = 0
        for r in range(n):
            counts[s[r]] += 1
            while (r-l+1 - max(counts.values())) > k:
                counts[s[l]] -= 1
                l += 1
            # now valid window
            ans = max(ans, r-l+1)

        return ans