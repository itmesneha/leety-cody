3.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = defaultdict(int)
        n = len(s)
        ans = 0
        start_index = 0
        for end_index in range(n):
            # if letter already in map
            if s[end_index] in map and s[end_index] != -1:
                del_index = map[s[end_index]]+ 1
                for i in range(start_index, del_index):
                    map[s[i]] = -1
                map[s[end_index]] = end_index
                if start_index <= del_index:
                    start_index = del_index

            # if letter not in map
            else:
                map[s[end_index]] = end_index
            ans = max(ans, end_index - start_index + 1)


        return ans