class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = defaultdict(int)
        have = defaultdict(int)
        if len(t) > len(s):
            return ''
        for _ in t:
            required[_] += 1
        n = len(s)
        start = 0
        end = 0
        ans_indexes = [-1,-1]
        minlength = float('inf')
        have_count = 0
        required_count = len(required)
        for end in range(n):
            if s[end] in required:
                have[s[end]] += 1
                if have[s[end]] == required[s[end]]:
                    have_count += 1
                while have_count == required_count:
                    if end - start + 1 < minlength:
                        ans_indexes = [start, end]
                        minlength = end - start + 1
                    if s[start] in required:
                        have[s[start]] -= 1
                        if have[s[start]] < required[s[start]]:
                            have_count -= 1
                    start += 1
        if minlength == float('inf'):
            return ''
        else:
            return s[ans_indexes[0] : ans_indexes[1] + 1] 