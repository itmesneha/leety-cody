class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        sliding window
        '''
        counts = defaultdict(int)
        l = 0
        n = len(s)
        ans = 0
        for r in range(n):
            counts[s[r]] += 1
            # contract the window
            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l += 1
            # now you should have valid window
            ans = max(ans, r - l + 1)

        return ans