class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Returns the minimum window substring of `s` that contains all characters of `t`
        (including multiplicities). If no such substring exists, returns an empty string.

        This uses the sliding window technique with two pointers (`l` and `r`) and two
        frequency maps:
        - `t_map` stores the required character counts from `t`
        - `s_map` tracks character counts in the current window of `s`

        The window expands by moving `r` and contracts by moving `l` whenever all required
        characters are satisfied. The smallest valid window found during the process is
        returned.

        Time Complexity:  O(len(s))
        Space Complexity: O(len(t))
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

        # for r, ch in enumerate(s):
        #     if ch in t_map:
        #         s_map[ch] += 1
        #         if s_map[ch] == t_map[ch]:
        #             needed -= 1

        #     while needed == 0 and l <= r:
        #         window = r - l + 1
        #         if window < min_len:
        #             min_len = window
        #             ans = s[l:r+1]
        #         left_char = s[l]
        #         if left_char in t_map:
        #             s_map[left_char] -= 1
        #             if s_map[left_char] < t_map[left_char]:
        #                 needed += 1

        #         l += 1

        # return ans





       

