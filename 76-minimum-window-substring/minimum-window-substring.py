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

        for r, ch in enumerate(s):
            if ch in t_map:
                s_map[ch] += 1
                if s_map[ch] == t_map[ch]:
                    needed -= 1

            while needed == 0 and l <= r:
                window = r - l + 1
                if window < min_len:
                    min_len = window
                    ans = s[l:r+1]
                left_char = s[l]
                if left_char in t_map:
                    s_map[left_char] -= 1
                    if s_map[left_char] < t_map[left_char]:
                        needed += 1

                l += 1

        return ans





        # for r in range(len(s)):
        #     if s[r] in t_map:
        #         s_map[s[r]] += 1
        #         if s_map[s[r]] == t_map[s[r]]:
        #             needed -= 1
        #     while needed == 0:
        #         if r - l + 1 < min_len:
        #             min_len = r - l + 1
        #             ans = s[l:r+1]
        #         # contract
        #         if s[l] in t_map:
        #             s_map[s[l]] -= 1
        #         if s_map[s[l]] < t_map[s[l]]:
        #             needed += 1
        #         l += 1

        # return ans

