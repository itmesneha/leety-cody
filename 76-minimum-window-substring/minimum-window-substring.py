class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        '''
        t_map = Counter(t)
        s_map = defaultdict(int)
        min_len = float('inf')
        l = 0
        ans = ''
        needed = len(t_map)
        for r in range(len(s)):
            if s[r] in t_map:
                s_map[s[r]] += 1
                if s_map[s[r]] == t_map[s[r]]:
                    needed -= 1
            while needed == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = s[l:r+1]
                # contract
                if s[l] in t_map:
                    s_map[s[l]] -= 1
                if s_map[s[l]] < t_map[s[l]]:
                    needed += 1
                l += 1

        return ans

