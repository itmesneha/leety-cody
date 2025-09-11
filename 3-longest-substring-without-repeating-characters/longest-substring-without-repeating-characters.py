class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = defaultdict(int)
        n = len(s)
        ans = 0
        start_index = 0
        for end_index in range(n):
            # if letter already in map
            if s[end_index] in map and s[end_index] != -1:
                del_index = map[s[end_index]]
                while start_index <= del_index:
                    map[s[start_index]] = -1
                    start_index += 1

            # if letter not in map
            map[s[end_index]] = end_index

            ans = max(ans, end_index - start_index + 1)

        return ans